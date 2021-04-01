[$(document).ready(function(){
  $('#submit').click(function () {
    console.log('click');
    $.post('eliminar_usuario').submit();
  });
})]