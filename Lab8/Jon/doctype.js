var cars = ["BMW", "Volvo", "Saab", "Ford"];
var i, len, text, cuadro = "";

for (i = 0, len = cars.length, text = ""; i < len; i++) {
  text += cars[i] + "<br>";
  document.getElementById("demo").innerHTML = text;
  cuadro =+ cars[i] + "<br><br>"
  document.getElementById("demo2").innerHTML = cuadro;
}
