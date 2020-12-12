function siguienteImaggen(){
    var img = document.getElementById("imag");
    img.src='imagenes/b.jpg';
}
function siguienteImagen(id,foto_id,ult_id)
{
	// Crear el objeto XMLHttpRequest (dependiente del navegador)
	var xhr;
	if(XMLHttpRequest)
		xhr = new XMLHttpRequest();
	else
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	// Establecer el método (GET), la URL (script PHP y parámetro) y
	//  si la solicitud es asíncrona (true)
	xhr.open('GET', 'ajax.php?id='+id+'&fotoId='+foto_id+1, true);
	// Establecer rutina de atención (handler)
	xhr.onreadystatechange = function()
	{
		// Si la respuesta ha sido correcta
		if(xhr.readyState == 4 && xhr.status == 200)
			// Asignar el texto del comentario completo enviado
			//  por el servidor al elemento correspondiente de la lista
            document.getElementById(foto_id).src = xhr.responseText;
            document.getElementById(foto_id).id=foto_id+1;
	}
	// Enviar la solicitud AJAX
	xhr.send('');
}
function anteriorImagen(id,foto_id,ult_id)
{
	// Crear el objeto XMLHttpRequest (dependiente del navegador)
	var xhr;
	if(XMLHttpRequest)
		xhr = new XMLHttpRequest();
	else
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	// Establecer el método (GET), la URL (script PHP y parámetro) y
	//  si la solicitud es asíncrona (true)
	xhr.open('GET', 'ajax.php?id='+id+'&fotoId='+foto_id-1, true);
	// Establecer rutina de atención (handler)
	xhr.onreadystatechange = function()
	{
		// Si la respuesta ha sido correcta
		if(xhr.readyState == 4 && xhr.status == 200)
			// Asignar el texto del comentario completo enviado
			//  por el servidor al elemento correspondiente de la lista
            document.getElementById(foto_id).src = xhr.responseText;
            document.getElementById(foto_id).id=foto_id-1;
	}
	// Enviar la solicitud AJAX
	xhr.send('');
}
