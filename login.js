$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        if (username === 'root' && password === '74863840') {
            $('#loginMessage').text('Inicio de sesión exitoso.');
            window.location.href = '/dashboard'; // Redirigir a la página del dashboard
        } else {
            $('#loginMessage').text('Usuario o contraseña incorrectos.');
        }
    });
});

