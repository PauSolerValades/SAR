<?php
  $pisos = simplexml_load_file('libro_visitas.xml');

  
  function filtrado($provEsc,$precMax,$habEsc,$fechaInEsc,$fechaFinEsc){
    //si quero hacer busqueda general habesc=0 preciomax>10000 fechas=0
    //la fecha le quitamos la barra para operar
    foreach($pisos -> piso as $piso){
        if($provEsc==$piso->direccion['prov'] &&
           $piso->precio <$precMax && 
           $piso->habitaciones ==$habEsc ||$habEsc==0 && 
           abs($fechaInEsc-$piso->fechaIn)<30 && 
           abs($fechaFinEsc-$piso->fechaFin)<30)
           {
            $mail = $piso->email;
        }
        echo('<th><p id="demo">'.$piso->fecha . '     ' . $piso->nombre. "             ".$mail.'</p></th><br>');
        echo('</tr>');
        echo('<tr>');
        echo('<td>'.$piso->comentario.'</td></tr></table>');
    }
  }
  function display(){



  }
  ?>