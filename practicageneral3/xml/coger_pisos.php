<?php
  $pisos = simplexml_load_file('lista_pisos.xml');
  
  filtrado();
  display($lista_pisos);

  
  function filtrado($provEsc,$precMax,$habEsc,$fechaInEsc,$fechaFinEsc){
    //si quero hacer busqueda general habesc=0 preciomax>10000 fechas=0
    //la fecha le quitamos la barra para operar
    foreach($pisos -> piso as $piso){
      if($provEsc==$piso->direccion['prov'] &&
        $piso->precio <$precMax && 
        $piso->habitaciones ==$habEsc ||$habEsc==0 && 
        abs($fechaInEsc-$piso->fechaIn)<30 || isset($piso->fechaIn)  && 
        abs($fechaFinEsc-$piso->fechaFin)<30 || isset($piso->fechaFin))
      {
          display($piso);
      }
    }
  }
?>

<!DOCTYPE HTML>

<html>
  <head>
  </head>
  <body>
    <h1> polla </h1>
  </body>
</html>




<?php


  
  function display($lista_pisos){



  }
  ?>
