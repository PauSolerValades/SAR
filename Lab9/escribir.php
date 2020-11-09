<?php
    $nombre = trim($_POST['userr']);
    $mail = trim($_POST['mail']);
    if($_POST['checkbox'] == 'Si'){
        $bool = "si";
    }else{
        $bool = "no";
    }
    $comentario = trim($_POST['comentario']);
    $date = getdate();
    $date = "" . $date[6]. "/"  . $date[5] . "/" . $date[3];
    
    $visitas = simplexml_load_file('libro_visitas.xml'); // Cargamos el XML al que queremos acceder

    $nuevo = $visitas->addChild('visita'); //Creamos una visita que es la que luego tendra dentro cada uno de los parametros de cada comentario
    $nuevo->addChild('fecha',$date);
    $nuevo->addChild('nombre',$nombre);
    $nuevo->addChild('comentario',$comentario);
    $nuevo->addChild('email',$mail);
    $nuevo->addChild('mostrar', $bool);

    
    $visita_actual = $visitas['ult_id'];

    if(isset($visita_actual)){
        $visita_actual++;
    }else{
        $visita_actual = 1;
    }

    $nuevo->addChild('id', $visita_actual);
    $visitas['ult_id']= $visita_actual;
    

?>