const passwordField = document.getElementById('id_password1');
const togglePasswordButton = document.getElementById('togglePassword');
const eyeIcon = document.getElementById('eyeIcon');
const passwordField1 = document.getElementById('id_password2');
const togglePasswordButton1 = document.getElementById('togglePassword1');
const eyeIcon1 = document.getElementById('eyeIcon1');

togglePasswordButton.addEventListener('click', () => {
    const cur_type = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = cur_type;

    if (cur_type === 'text') {
        eyeIcon.textContent = '🌚️';
    } else {
        eyeIcon.textContent = '👁️';
    }
});

togglePasswordButton1.addEventListener('click', () => {
    const cur_type1 = passwordField1.type === 'password' ? 'text' : 'password';
    passwordField1.type = cur_type1;

    if (cur_type1 === 'text') {
        eyeIcon1.textContent = '🌚';
    } else {
        eyeIcon1.textContent = '👁️';
    }
});