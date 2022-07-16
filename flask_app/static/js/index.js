var formLogin = document.getElementById("formLogin");

formLogin.onsubmit = function(event){
    // "event" es el evento que estoy escuchando(por defecto), quiero prevenir el evento por default de mi formulario
    event.preventDefault();
    // obtener los datos del formulario
    var formulario = new FormData(formLogin)

    fetch("/login", {method: 'POST', body: formulario})
        .then(res => res.json())
        .then(data => {
            console.log(data)
            if(data.message == "Correcto"){
                window.location.href = "/dashboard"
            } else {
                var mensajeAlerta = document.getElementById("mensajeAlerta");
                mensajeAlerta.innerHTML = data.message
                mensajeAlerta.classList.add("alert");
                mensajeAlerta.classList.add("alert-danger");
            }
        })
}