<html>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="doctype.css">
  <script type = "text/javascript" src="doctype.js"></script>
  <title>Lista de Reseñas</title>
</head>
<body>
  <h1><span>Libro de Visitas </span></h1>
  <h2><span>Comentarios añadidos recientemente</span></h2>
  <h3><span>Haz click <A href="modelo.html">aquí</A> si quierse añadir un comentario</span></h3><br>
  <?php
  $visitas = simplexml_load_file('libro_visitas.xml');
  $mail = "";
  foreach($visitas -> visita as $visita){
    echo('<table>');
    echo('<tr>');
    if($visita->mostrar == "si"){
      $mail = $visita->email;
    }
    echo('<th><p id="demo">'.$visita->fecha . '     ' . $visita->nombre. "             ".$mail.'</p></th><br>');
    echo('</tr>');
    echo('<tr>');
    echo('<td>'.$visita->comentario.'</td></tr></table>');
  }
  ?>
</body>
</html>