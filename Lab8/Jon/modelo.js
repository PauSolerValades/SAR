function boton(	){

	var username = "userr"

	alert(username)
}



function validateForm() {

	var userr = document.forms["Form"]["userr"].value;

	var comentario = document.forms["Form"]["comentario"].value;

	var email = document.forms["Form"]["email"].value;

	if(userr == "" && comentario == ""){

		document.getElementById("userr").style.borderColor="red";

		document.getElementById("comentario").style.borderColor="red";

		alert("Debes de rellenar nombre de usuario y comentario");

	}

	else if (userr == "") {

		document.getElementById("userr").style.borderColor="red";

		document.getElementById("comentario").style.borderColor = "transparent";

		document.getElementById("email").style.borderColor = "transparent";

		alert("Name must be filled out");

		return false;

	}else if (comentario == "") {

		document.getElementById("userr").style.borderColor = "transparent";

		document.getElementById("comentario").style.borderColor="red";

		document.getElementById("email").style.borderColor = "transparent";

		alert("Comentario must be filled out");

		return false;

	}else if(validateEmail() == true && email != ""){
		document.getElementById("email").style.borderColor = "red";

		alert("El email introducido no es correcto");
	}
	else{

		document.getElementById("email").style.borderColor = "transparent";

		document.getElementById("userr").style.borderColor = "transparent";

		document.getElementById("comentario").style.borderColor = "transparent";

	}

}

function validateEmail1(){

	var email = document.forms["Form"]["email"].value;
	if(email != ""){


	}

}

function validateEmail (){

	var email = document.forms["Form"]["email"].value;

	var checkbox = document.forms["Form"]["checkbox"].value;

	if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email)){	
			
			document.getElementById("checkbox").disabled = false;
			return false;

	}else{
		document.getElementById("checkbox").disabled = true;
		return true;
		alert();
	}

	

}
