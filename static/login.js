$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        if (username === 'root' && password === '74863840') {
            $('#loginMessage').text('Inicio de sesión exitoso.');
            window.location.href = 'administrador'; // Redirigir a la página del dashboard
        } else {
            $('#errorMessage').show(); // Mostrar el mensaje de error
        }
    });

    $('#logoutButton').click(function() {
        fetch('/logout', { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/'; // Redirigir a la página de inicio de sesión
                }
            });
    });
});
