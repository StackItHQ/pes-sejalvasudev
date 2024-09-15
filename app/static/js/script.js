document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('upload-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const fileInput = form.querySelector('input[type="file"]');
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
          .then(data => console.log(data))
          .catch(error => console.error(error));
    });
});
