document.getElementById('contactoForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que el formulario se envíe por defecto

  // Obtener los valores de los campos
  var nombre = document.getElementById('id_nombre').value.trim();
  var correo = document.getElementById('id_correo').value.trim();
  var mensaje = document.getElementById('id_mensaje').value.trim();

  // Obtener las referencias de los elementos de error
  var nombreError = document.getElementById('nombre_error');
  var correoError = document.getElementById('correo_error');
  var mensajeError = document.getElementById('mensaje_error');

  // Restablecer los mensajes de error
  resetErrorMessages();

  // Validar nombre
  if (nombre === '') {
      setError(nombreError, 'Por favor, ingresa tu nombre.');
      return;
  }

  // Validar correo electrónico
  if (correo === '') {
      setError(correoError, 'Por favor, ingresa tu correo electrónico.');
      return;
  } else if (!isValidEmail(correo)) {
      setError(correoError, 'El formato del correo electrónico es incorrecto.');
      return;
  }

  // Validar mensaje
  if (mensaje === '') {
      setError(mensajeError, 'Por favor, ingresa tu mensaje.');
      return;
  }

  // Si todas las validaciones pasan, se puede proceder con el envío del formulario
  alert("¡Formulario enviado exitosamente!");
  // Aquí puedes agregar código para enviar los datos del formulario a tu servidor
  document.getElementById('contactoForm').submit();
});

// Función para restablecer los mensajes de error
function resetErrorMessages() {
  document.getElementById('nombre_error').textContent = '';
  document.getElementById('correo_error').textContent = '';
  document.getElementById('mensaje_error').textContent = '';
}

// Función para establecer un mensaje de error
function setError(element, message) {
  element.textContent = message;
}

// Función para validar el formato del correo electrónico
function isValidEmail(correo) {
  const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/;
  return emailRegex.test(correo);
}