<!DOCTYPE HTML>
<link rel="stylesheet" href="pisos.css" type="text/css">
<script type = "text/javascript" src = "a.js"></script>
<html>
  <head>
    <title>Ostatu - UPV/EHU</title>
    <meta charset="UTF-8"> 
  </head>
  <body>
  <div class="cabecera">
        <a title="UPV" href="https://www.ehu.eus/es/"><img class="image" src="log.png" alt="logo"></a>
        <span class="text1">OSTATU</span>
  </div>
    
    <?php
    echo('<div class = "espaciado">a');
    echo('</div>');
    function display($piso){
      
      echo('<div class = "piso" >');
     if($piso->fotos["ult_id"]!=0){ 
       echo('<div class = "tabla">');      
        echo('<div class = "arrow left" id = "left'.$piso["id"].'" onclick="anteriorImagen('.$piso["id"].','.$piso->fotos->foto["id"].','.$piso->fotos["ult_id"].','.$piso["id"].''.$piso->fotos->foto["id"].')"></div>');}
      echo('<div><image src ="'.$piso->fotos->foto.'"id = "'.$piso["id"].''.$piso->fotos->foto["id"].'" class = "imagenes"></div>');
      if($piso->fotos["ult_id"]!=0){
      echo('<div class = "arrow right" id = "right'.$piso["id"].'" onclick="siguienteImagen('.$piso["id"].','.$piso->fotos->foto["id"].','.$piso->fotos["ult_id"].','.$piso["id"].''.$piso->fotos->foto["id"].')"></div>');
      echo('</div>');}
      echo('<div style = "margin-top:2%;">');
      echo ('<span  class = "datoss">Calle : </span>');
      echo('<span class = "bd">'.$piso->direccion.'</span>');
      echo ('<span class = "datoss" style = "display:inline;">Precio: </span>');
      echo('<span class = "bd">'.$piso->precio.' €</span>');
      echo ('<span class = "datoss" style = "display:inline;">Habitaciones: </span>');
      echo('<span class = "bd">'.$piso->habitaciones.' </span>');
      echo ('<span class = "datoss" style = "display:inline;">Baños: </span>');
      echo('<span class = "bd">'.$piso->banos.' </span><br><br>');
      echo('<span class = "datoss" style = "display:inline;">Fianza: </span>');
      echo('<span class = "bd">'.$piso->fianza.' €</span>');
      echo('<span class = "datoss" style = "display:inline;">Inicio: </span>');
      echo('<span class = "bd">'.$piso->fechaIn.'</span>');
      echo('<span class = "datoss" style = "display:inline;">Final: </span>');
      echo('<span class = "bd">'.$piso->fechaFin.'</span>');
      echo('<span class = "datoss" style = "display:inline;">Nombre: </span>');
      echo('<span class = "bd">'.$piso->nombre.'</span><br><br>');
      echo('<span class = "datoss" style = "display:inline;">Telefono: </span>');
      echo('<span class = "bd">'.$piso->tel.'</span>');
      echo('<span class = "datoss" style = "display:inline;">Email: </span>');
      echo('<span class = "bd">'.$piso->mail.'</span><br><br>');
      echo('<span class  ="datoss">Servicios: </span>');
      echo('<img class = "iconos" src = "w.png" title = "WI-FI" alt = "WI-FI" style = "margin-right:-15px;">');
      if($piso->caracteristicas["wifi"] == 1){
        echo('<img class = "iconos" src = "s.png" title = "Si" alt = "Si" style = "padding-right:60px;">');
      }else{
        echo('<img class = "iconos" src = "n.png" title = "No" alt = "No" style = "padding-right:60px;">');
      }
      echo('<img class = "iconos" src = "lb.png" title = "Lavadora" alt = "Lavadora" style = "margin-right:-20px;">');
      if($piso->caracteristicas["lavadora"]== 1){
        echo('<img class = "iconos" src = "s.png" title = "Si" alt = "Si"  style = "padding-right:60px;">');
      }else{
        echo('<img class = "iconos" src = "n.png" title = "No" alt = "No" style = "padding-right:60px;">');
      }
      echo('<img class = "iconos" src = "lv.png" title = "Lavavajillas" alt = "Lavavajillas">');
      if($piso->caracteristicas["lavavajillas"]== 1){
        echo('<img class = "iconos" src = "s.png" title = "Si" alt = "Si" style = "padding-right:60px;">');
      }else{
        echo('<img class = "iconos" src = "n.png" title = "No" alt = "No" style = "padding-right:60px;">');
      }
      echo('<img class = "iconos" src = "t.png" title = "Terraza" alt = "Terraza" >');
      if($piso->caracteristicas["terraza"]== 1){
        echo('<img class = "iconos" src = "s.png" title = "Si" alt = "Si">');
      }else{
        echo('<img class = "iconos" src = "n.png" title = "No" alt = "No">');
      }
      echo('<br><span class = "datoss" style = "display:inline;">Descripcion:  </span><br>');
      echo('<span class = "bd">'.$piso->descripcion.'</span><br><br>');
      echo('</div>');
      echo('</div>');
      
  }
  
  
  ?>
  
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
 
  
  filtrado($pisos,$provincia, $precio, $hab, $bath, $inicio, $final);


  
  function filtrado($pisos,$provincia, $precMax, $habEsc, $bath, $fechaInEsc, $fechaFinEsc){
    //si quero hacer busqueda general habesc=0 preciomax>10000 fechas=0
    //la fecha le quitamos la barra para operar
    foreach($pisos->piso as $piso){
      if($provincia==$piso->direccion['prov'] &&
        $piso->precio <=$precMax && 
        ($piso->habitaciones ==$habEsc ||$habEsc==0 )&&
        ($piso->banos ==$bath ||$bath==0 )&& 
        (abs($fechaInEsc-$piso->fechaIn)<30 || isset($piso->fechaIn))&& 
        (abs($fechaFinEsc-$piso->fechaFin)<30 || isset($piso->fechaFin)))
      {
          display($piso);
      }
    }
  }
?>

  </body>
</html>