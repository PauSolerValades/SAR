sliderChange = function(n){
  var e = document.getElementById("valor");
  e.innerHTML = n + "€";
}


function validateForm() {
  if(document.getElementById('araba').checked){
    return true;
  }else if(document.getElementById('bizkaia').checked){
      return true;
  }else if(document.getElementById('gipuzkoa').checked){
      return true;
  }else{
      alert("Seleccione una provincia");
      return false;
    }
}
