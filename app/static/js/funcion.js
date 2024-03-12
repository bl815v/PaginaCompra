function volver(pag4){
    if(pag4){
        window.location.href = "/";
    }else{
        window.history.back();
    }
}
function seleccionarProducto() {
    const inputProducto = document.getElementById("producto");
    const dataList = document.getElementById("productos");
    let opcionesProductos = [];

    fetch('/opcionesProductos')
        .then(response => response.json())
        .then(data => {
            opcionesProductos = data;
            opcionesProductos.forEach(function(opcion) {
                const option = document.createElement("option");
                option.value = opcion.nombre;
                option.textContent = opcion.nombre;
                dataList.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching productos:', error);
        });

    dataList.addEventListener("click", function(event) {
        if (event.target.tagName === "OPTION") {
            inputProducto.value = event.target.value;
            dataList.style.display = "none";
            const productoSeleccionado = opcionesProductos.find(option => option.nombre === inputProducto.value);
            if (productoSeleccionado) {
                document.getElementById("precio").textContent = productoSeleccionado.precio;
            }
        }
    });

    inputProducto.addEventListener("input", function() {
        const textoUsuario = inputProducto.value.toLowerCase();
        dataList.innerHTML = "";
        opcionesProductos.forEach(function(opcion) {
            if (opcion.nombre.toLowerCase().includes(textoUsuario)) {
                const option = document.createElement("option");
                option.value = opcion.nombre;
                option.textContent = opcion.nombre;
                dataList.appendChild(option);
            }
        });

        dataList.style.display = "block";
    });

    document.addEventListener("click", function(event) {
        if (event.target !== inputProducto && event.target.parentNode !== dataList) {
            dataList.style.display = "none";
        }
        if (inputProducto.value === "") {
            dataList.innerHTML = ""; 
            opcionesProductos.forEach(function(opcion) {
                const option = document.createElement("option");
                option.value = opcion.nombre;
                option.textContent = opcion.nombre;
                dataList.appendChild(option);
            });
        }
    });
    inputProducto.addEventListener("focus", function() {
        dataList.style.display = "block";
    });
}

function calcularPrecio() {
    const precio = parseInt(document.getElementById("precio").innerText);
    const cantidad = parseInt(document.getElementById("cantidad").value);

    if (isNaN(precio) || isNaN(cantidad) || cantidad <= 0) {
        document.getElementById("totalPagar").textContent = "";    
        return;
    }

    fetch('/calcularPrecio', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ precio: precio, cantidad: cantidad })
    })
    .then(response => response.json())
    .then(data => {
        const totalPagar = data.total_pagar;
        if (totalPagar !== null) {
            document.getElementById("totalPagar").textContent = totalPagar;
        } else {
            document.getElementById("totalPagar").textContent = "Error en el cálculo";
        }
    })
    .catch(error => {
        console.error('Error al calcular el precio:', error);
        document.getElementById("totalPagar").textContent = "Error en el cálculo";
    });
}

document.addEventListener("DOMContentLoaded", function() {
    const pag1 =  document.getElementById("index");
    const pag2 =  document.getElementById("datosCompra");
    const pag3 =  document.getElementById("datosEnvio");
    const pag4 = document.getElementById("resumen");

    if(pag2 || pag3 || pag4){
        const boton2 = document.getElementById("volver");
        boton2.addEventListener("click", function() {
            volver(pag4);
        });
    }

    if(pag2){     
        seleccionarProducto();
        document.getElementById("producto").addEventListener("change", calcularPrecio);
        document.getElementById("cantidad").addEventListener("change", calcularPrecio);
        calcularPrecio();

    }

    if(pag3){
        const checkPropina = document.getElementById("propina");
        const checkPriori = document.getElementById("prioritario");
        const lPropina = document.querySelector('label[for="propina"]');
        const lPriori = document.querySelector('label[for="prioritario"]');
    
        function actualizarLabel(label, checkbox) {
            if (checkbox.checked) {
                label.style.color = "green"; 
                label.textContent += " + $5000"; 
            } else {
                label.style.color = ""; 
                label.textContent = label.textContent.replace(" + $5000", ""); 
            }
        }
    
        checkPropina.addEventListener("change", function() {
            actualizarLabel(lPropina, checkPropina);
        });
    
        checkPriori.addEventListener("change", function() {
            actualizarLabel(lPriori, checkPriori);
        });
    }
    
});
