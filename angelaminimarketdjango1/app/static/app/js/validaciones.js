document.getElementById('registroForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que el formulario se envíe por defecto

  // Obtener los valores de los campos
  var nombre = document.getElementById('nombre_login').value.trim();
  var email = document.getElementById('email_login').value.trim();
  var password = document.getElementById('password_login').value.trim();

  // Obtener las referencias de los elementos de error
  var nombreError = document.getElementById('nombre_error');
  var emailError = document.getElementById('email_error');
  var passwordError = document.getElementById('password_error');

  // Restablecer los mensajes de error
  resetErrorMessages();

  // Validar nombre de usuario
  if (nombre === '') {
      setError(nombreError, 'Por favor, ingresa tu nombre de usuario.');
      return;
  }

  // Validar correo electrónico
  if (email === '') {
      setError(emailError, 'Por favor, ingresa tu correo electrónico.');
      return;
  } else if (!isValidEmail(email)) {
      setError(emailError, 'El formato del correo electrónico es incorrecto.');
      return;
  }

  // Validar contraseña
  if (password === '') {
      setError(passwordError, 'Por favor, ingresa tu contraseña.');
      return;
  }

  // Si todas las validaciones pasan, se puede proceder con el envío del formulario
  alert("¡Usuario registrado exitosamente!");
  // Aquí puedes agregar código para enviar los datos del formulario a tu servidor
});

// Función para restablecer los mensajes de error
function resetErrorMessages() {
  document.getElementById('nombre_error').textContent = '';
  document.getElementById('email_error').textContent = '';
  document.getElementById('password_error').textContent = '';
}

// Función para establecer un mensaje de error
function setError(element, message) {
  element.textContent = message;
}

// Función para validar el formato del correo electrónico
function isValidEmail(email) {
  const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/;
  return emailRegex.test(email);
}

function validateForm() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  var usernameError = document.getElementById('usernameError');
  var passwordError = document.getElementById('passwordError');
  usernameError.innerHTML = '';
  passwordError.innerHTML = '';
  var isValid = true;

  if (!username) {
    usernameError.innerHTML = 'Por favor, ingresa tu nombre de usuario';
    isValid = false;
  }

  if (!password) {
    passwordError.innerHTML = 'Por favor, ingresa tu contraseña';
    isValid = false;
  }

  return isValid;
}