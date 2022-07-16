function eliminarcomentario(comment_id, post_id){
  if (window.confirm("¿Quieres eliminar este comentario?")) {
      window.location.href = `/delete/comment/${post_id}/${comment_id}`;
  }
}
function eliminarsubcomentario(subcomment_id, post_id){
  if (window.confirm("¿Quieres eliminar este comentario?")) {
      window.location.href = `/delete/subcomment/${post_id}/${subcomment_id}`;
  }
}
function apareceinput(element){
  var aparece = element.parentNode.parentNode.children[2].children[element.parentNode.parentNode.children[2].children.length - 1]
  if(element.parentNode.parentNode.children[2].children[element.parentNode.parentNode.children[2].children.length - 2]){
    var borde = element.parentNode.parentNode.children[2].children[element.parentNode.parentNode.children[2].children.length - 2]
    borde.removeAttribute('id');
  }
  aparece.classList.add('display_block')
  aparece.children[0].children[3].children[0].focus()
}
function desapareceinput(element){
  element.classList.remove('display_block')
  var borde = element.parentNode.parentNode.parentNode.children[element.parentNode.parentNode.parentNode.children.length - 2]
  borde.setAttribute("id","last_border")
}


// last_border