function flechas(right,left,id,ult_id){
	if(id==ult_id){
		document.getElementById(right).style.visibility= 'hidden';
		document.getElementById(left).style.visibility= 'visible';
		
	}
	else if(id==0){
		document.getElementById(left).style.visibility= 'hidden';
		document.getElementById(right).style.visibility= 'visible';
	}
	else{
		document.getElementById(left).style.visibility= 'visible';
		document.getElementById(right).style.visibility= 'visible';

	}
}
function siguienteImagen(id,foto_id,ult_id,doId)
{
	// Crear el objeto XMLHttpRequest (dependiente del navegador)	
	var xhr;
	var a =foto_id+1;
	
	if(XMLHttpRequest)
		xhr = new XMLHttpRequest();
	else
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	// Establecer el método (GET), la URL (script PHP y parámetro) y
	//  si la solicitud es asíncrona (true)
	xhr.open('GET', 'ajax.php?id='+id+'&fotoId='+a, true);
	// Establecer rutina de atención (handler)
	xhr.onreadystatechange = function()
	{
		// Si la respuesta ha sido correcta
		if(xhr.readyState == 4 && xhr.status == 200){
			// Asignar el texto del comentario completo enviado
			//  por el servidor al elemento correspondiente de la lista
			document.getElementById(doId).src = xhr.responseText;
			document.getElementById('right'+id).setAttribute( "onClick", "siguienteImagen("+id+','+(a)+','+ult_id+','+(doId+1)+")" );
			document.getElementById(doId).id=doId+1;
			document.getElementById('left'+id).setAttribute( "onClick", "anteriorImagen("+id+','+(a)+','+ult_id+','+(doId+1)+")" );
			flechas('right'+id,'left'+id,a,ult_id);
	
		}
			
	}
	// Enviar la solicitud AJAX
	xhr.send('');
	
}
function anteriorImagen(id,foto_id,ult_id,doId)
{
	// Crear el objeto XMLHttpRequest (dependiente del navegador)
	var xhr;
	var a =foto_id-1;
	var poque=doId-1
	if(XMLHttpRequest)
		xhr = new XMLHttpRequest();
	else
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	// Establecer el método (GET), la URL (script PHP y parámetro) y
	//  si la solicitud es asíncrona (true)
	xhr.open('GET', 'ajax.php?id='+id+'&fotoId='+a, true);
	// Establecer rutina de atención (handler)
	xhr.onreadystatechange = function()
	{
		// Si la respuesta ha sido correcta
		if(xhr.readyState == 4 && xhr.status == 200){
			// Asignar el texto del comentario completo enviado
			//  por el servidor al elemento correspondiente de la lista
            document.getElementById(doId).src = xhr.responseText;
			document.getElementById('right'+id).setAttribute( "onClick", "siguienteImagen("+id+','+(a)+','+ult_id+','+(doId-1)+")" );
			document.getElementById(doId).id=poque;
			document.getElementById('left'+id).setAttribute( "onClick", "anteriorImagen("+id+','+(a)+','+ult_id+','+(doId-1)+")" );
			flechas('right'+id,'left'+id,a,ult_id);
		}
	}
	// Enviar la solicitud AJAX
	xhr.send('');
}
