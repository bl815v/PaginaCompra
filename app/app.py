from flask import Flask, jsonify, render_template, request, session

from logic.Usuario import Usuario
from logic.Envio import Envio
from logic.Producto import Producto
from logic.Compra import Compra
from logic.ListaProductos import ListaProductos

app=Flask(__name__)
app.secret_key = 'clave'

@app.route('/')
def index():
    return render_template('index.html')

data = {}

@app.route('/datosCompra', methods=['POST'])
def datosCompra():
    user1 = Usuario(request.form.get('nombre'), 
                request.form.get('apellido'), 
                request.form.get('email'),
                request.form.get('celular'), 
                request.form.get('tipoDoc'), 
                request.form.get('numDoc'))
    
    data = {
        'nombre': user1.getNombres(),
        'tipoDoc': user1.getTipoDocumento(),
        'apellido': user1.getApellidos(),
        'celular': user1.getCelular(),
        'email': user1.getEmail(),
        'numDoc': user1.getNumDocumento()
    }
    session.update(data)
    return render_template('datosCompra.html', data=data)

@app.route('/opcionesProductos', methods=['GET'])
def obtener_opciones_productos():
    lista_productos = ListaProductos()
    opciones_productos = lista_productos.getOpcionesProductos()
    return jsonify(opciones_productos)

@app.route('/calcularPrecio', methods=['POST'])
def calcular_precio():
    try:
        precio = int(request.json.get("precio"))
        cantidad = int(request.json.get("cantidad"))

        total = precio * cantidad

        return jsonify({"total_pagar": total})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/datosEnvio', methods=['POST'])
def datosEnvio():
    listadeProductos = ListaProductos()
    productos = listadeProductos.productos
    
    nombreProducSelecc = request.form.get('producto')
    
    precioProducSelecc = None
    for producto in productos:
        if producto.getNombre() == nombreProducSelecc:
            precioProducSelecc = producto.getPrecio()
            break    
    
    producto1 = Producto(nombreProducSelecc, 
                        precioProducSelecc)
    
    compra = Compra(producto1, 
                    request.form.get('cantidad'), 
                    request.form.get('metodoPago'))
    
    data = session
    data.update ({
        'producto': compra.getProducto().getNombre(),
        'metodoPago': compra.getMetodoPago(),
        'precio': compra.getProducto().getPrecio(),
        'cantidad': compra.getCantidad()
    })
    return render_template('datosEnvio.html', data=data)

@app.route('/resumen', methods=['POST'])
def resumen():
    envio1 = Envio( request.form.get('ciudad'), 
                request.form.get('dirEntrega'), 
                request.form.get('descEntrega'), 
                request.form.get('propina'), 
                request.form.get('prioritario'))

    auxPropina = 0
    auxPrioritario = 0
    data = session  
    if envio1.getPropina() == 'Si':
        auxPropina = 5000
    if envio1.getEnvioPrioritario() == 'Si':
        auxPrioritario = 5000

    data.update ({
        'ciudad': envio1.getCiudad(),
        'direccionEntrega': envio1.getDireccionEntrega(),
        'descripcionExtra': envio1.getDescripcion(),
        'propina': envio1.getPropina(),
        'envioPrioritario': envio1.getEnvioPrioritario(),
        'totalGuardado': auxPrioritario + auxPropina + (int(data['cantidad']) * int(data['precio'])) 
    })
    print("este es el precio")
    print(data['propina'])
    return render_template('resumen.html', data=data)

if __name__=='__main__':
    app.run(debug=True, port=5000)
