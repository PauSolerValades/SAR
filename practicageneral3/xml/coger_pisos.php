<?php
  $pisos = simplexml_load_file('libro_visitas.xml');
  $lista_pisos=[]
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
          display($piso)
      }
    }
  }
?>





<?php


  
  function display($lista_pisos){



  }
  ?>
