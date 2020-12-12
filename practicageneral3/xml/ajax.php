<?php
	
	
	// Verificar que ha sido enviado el 'id' que identifica al comentario
	//  y que existe el fichero XML con la lista de comentarios
	if(isset($_GET['id']) && )isset($_GET['fotoId'])
	{
        $id=$_GET['id'];
        $fotoId=$_GET['fotoId'];
		// Cargar el fichero XML con la lista de comentarios
		$pisos=simplexml_load_file('lista_pisos.xml');
		// Recorrer la lista de comentarios hasta encontrar el del 'id' dado
		foreach($pisos->piso as $piso)
		{
			if($piso['id'] == $id)
			{
                foreach($piso->fotos as $foto)
		        {
                // Devolver el comentario encontrado y terminar
                    if($foto['FotoId'] == $id)
			        {
				        echo($foto);
                        break;
                    }
                }
			}
		}
	}
?>
