function eliminarpublicacion(post_id){
    if (window.confirm("¿Quieres eliminar esta publicación con sus respectivos comentarios?")) {
        window.location.href = `/delete/post/${post_id}`;
    }
}