<?php
  $pisos = simplexml_load_file('lista_pisos.xml');
  
  $provincia = '';
  if(($_GET['provincia'])  == 'A'){
    $provincia = 'A';
  }
  if(($_GET['provincia'])  == 'B'){
    $provincia = 'B';
  }
  if(($_GET['provincia'])  == 'G'){
    $provincia = 'G';
  }

  $precio = trim($_GET['precio']);
  $inicio = trim($_GET['inicio']);
  $final = trim($_GET['final']);
  $hab = trim($_GET['hab']);
  $bath = trim($_GET['bath']);
 

  filtrado($provincia, $precio, $hab, $bath, $inicio, $final);
  display($pisos);

  
  function filtrado($provincia, $precMax, $habEsc, $bath, $fechaInEsc, $fechaFinEsc){
    //si quero hacer busqueda general habesc=0 preciomax>10000 fechas=0
    //la fecha le quitamos la barra para operar
    foreach($pisos->piso as $piso){
      if($provincia==$piso->direccion['prov'] &&
        $piso->precio <$precMax && 
        $piso->habitaciones ==$habEsc ||$habEsc==0 &&
        $piso->banos ==$bath ||$bath==0 &&  
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
    <h1> polla  </h1>
  </body>
</html>




<?php
  function display($piso){
    echo ('<h1>Hola'.$piso->habitaciones.'</h1>');
    echo ($pisos);
  }
  ?>