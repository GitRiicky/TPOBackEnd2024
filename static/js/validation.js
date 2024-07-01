function validateForm() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var message = document.getElementById('message').value;
    var reason = document.getElementById('reason').value;

    if (name == "" || email == "" || phone == "" || message == "" || reason == "") {
        alert("Por favor, complete todos los campos obligatorios.");
        return false;
    }

    document.getElementById('confirmation').style.display = 'block';

    resetForm();

    return false;
}

function resetForm() {
    document.getElementById('contactForm').reset();
}