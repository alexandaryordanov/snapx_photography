const passwordField = document.getElementById('id_password1');
const togglePasswordButton = document.getElementById('togglePassword');
const eyeIcon = document.getElementById('eyeIcon');
const passwordField1 = document.getElementById('id_password2');
const togglePasswordButton1 = document.getElementById('togglePassword1');
const eyeIcon1 = document.getElementById('eyeIcon1');

if (togglePasswordButton)
    togglePasswordButton.addEventListener('click', () => {
        const cur_type = passwordField.type === 'password' ? 'text' : 'password';
        passwordField.type = cur_type;

        if (cur_type === 'text') {
            eyeIcon.textContent = '🌚️';
        } else {
            eyeIcon.textContent = '👁️';
        }
    });


if (togglePasswordButton1)
    togglePasswordButton1.addEventListener('click', () => {
        const cur_type1 = passwordField1.type === 'password' ? 'text' : 'password';
        passwordField1.type = cur_type1;

        if (cur_type1 === 'text') {
            eyeIcon1.textContent = '🌚';
        } else {
            eyeIcon1.textContent = '👁️';
        }
    });

document.addEventListener('DOMContentLoaded', function () {
        const modal = document.getElementById('photoModal');
        const modalImage = document.getElementById('modalImage');
        if (modal)
            modal.addEventListener('show.bs.modal', function (event) {
                const triggerImg = event.relatedTarget.querySelector('img');
                modalImage.src = triggerImg.src;
                modalImage.alt = triggerImg.alt || "Photo";
            });
    });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrftoken');

const voteButtons = document.querySelectorAll(".vote-button");

voteButtons.forEach(button => {
    button.addEventListener("click", function () {
        const photoId = this.getAttribute("data-photo-id");
        const voteCountSpan = document.getElementById(`vote-count-${photoId}`);

        const url = `/photos/${photoId}/vote/`;

        if (!confirm("Are you sure you want to vote?. This can`t be undone!!!")) {
            return;
        }

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken, // Add CSRF token to headers
            },
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(errorData => {
                    throw new Error(errorData.detail || "An error occurred.");
                });
            }
            return response.json();
        })
        .then(data => {
            voteCountSpan.innerText = `${data.votes}`;
            alert("Vote added successfully!");
        })
        .catch(error => {
            alert(`Failed to vote: ${error.message}`);
        });
    });
});