<!DOCTYPE HTML>
<link rel="stylesheet" href="pisos.css" type="text/css">
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
      echo('<image src ="'.$piso->fotos->foto.'" class = "imagenes">');
      echo('<div style = "margin-top:2%;">');
      echo ('<span  class = "datoss">Calle : </span>');
      echo('<span class = "bd">'.$piso->direccion.'</span>');
      echo ('<span class = "datoss" style = "display:inline;">Precio: </span>');
      echo('<span class = "bd">'.$piso->precio.' €</span>');
      echo ('<span class = "datoss" style = "display:inline;">Habitaciones: </span>');
      echo('<span class = "bd">'.$piso->habitaciones.' </span>');
      echo ('<span class = "datoss" style = "display:inline;">Banos: </span>');
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
        $piso->precio <$precMax && 
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
<div class = "espaciado">a</div>
<div class="mapas">
        <div class="contenedor">
            <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1060.0194745260221!2d-2.66946235879262!3d42.83964987697573!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd4fc2708677f32b%3A0x37980e0652a5437e!2sPabell%C3%B3n%20Universitario!5e1!3m2!1ses!2ses!4v1606603271126!5m2!1ses!2ses"></iframe>
        </div>
        <div class="contenedor">
            <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3674.494248047814!2d-2.0129823845134425!3d43.307893179134595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd51b0746f57e609%3A0x180a8b6e57549f9b!2sU.P.V%2C%20Plaza%20de%20Elhuyar%2C%201%2C%2020018%20San%20Sebasti%C3%A1n%2C%20Gipuzkoa!5e1!3m2!1ses!2ses!4v1606603855289!5m2!1ses!2ses"></iframe>
        </div>
        <div class="contenedor">
            <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1080.2153846268275!2d-2.9581881403836836!3d43.27331777028557!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd4e501534865915%3A0xbd4dfde36809d227!2sAv.%20Lehendakari%20Aguirre%2C%2081%2C%2048015%20Bilbao%2C%20Vizcaya!5e1!3m2!1ses!2ses!4v1606604095488!5m2!1ses!2ses"></iframe>
        </div>
        <div class="contenedor">
            <span class="text2">CAMPUS DE ARABA</span><br>
            <span class="text3">Pabellón universitario Los Apraiz 1, 1era planta <br>01006 Vitoria-Gasteiz<br>HORARIO:
                Lunes y jueves 10:00 a 13:00<br>
                <br>EMAIL: ostatu-ar@ehu.eus<br>TELEFONO: 945 0143 36</span>
        </div>
        <div class="contenedor">
            <span class="text2">CAMPUS DE GIPUZKOA</span><br>
            <span class="text3">Plaza Elhuyar 1, Planta baja<br>20018 San Sebastián<br>HORARIO: Lunes a viernes 09:00 a
                13:00<br>
                <br>EMAIL: ostatu-gi@ehu.eus<br>TELEFONO: 943 0156 67</span>

        </div>
        <div class="contenedor">
            <span class="text2">CAMPUS DE BIZKAIA</span><br>
            <span class="text3">Avda. Lehendakari Aguirre 81<br>48015 Bilbao<br>HORARIO: Lunes a viernes 09:00 a
                13:00<br>
                <br>EMAIL: ostatu-bi@ehu.eus<br>TELEFONO: 9460 171 43</span>

        </div>
    </div>
  </body>
</html>