
function hide (element) {
 /* elements = elements.length ? elements : [elements];
  for (var index = 0; index < elements.length; index++) {
    elements[index].style.display = 'none';
  }*/
  element.style.display = 'none';
}
hide(document.getElementById('loginModal'));
$("#signin").click(function(){
    $("#loginModal").show();
});