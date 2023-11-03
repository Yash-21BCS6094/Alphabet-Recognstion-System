document.querySelector('.button-78').addEventListener('click', () => {
    const fileInput = document.getElementById('upload');
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append('image', file);
        // console.log(formData[0]);
        fetch("http://localhost:5000/upload", {
            method: 'POST',
            body: formData
        }).then(response => response.json())
            .then(data => {
                console.log(data);
                const messageDiv = document.createElement('div');
                messageDiv.textContent = `${data} is predicted by the model`;
                messageDiv.classList.add('message-box');
                messageDiv.setAttribute('id', 'error-div');
                document.body.appendChild(messageDiv);
            })
            .catch(error => {
                console.log(error);
            });

    } else {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = "No file has been selected";
        messageDiv.classList.add('message-box');
        messageDiv.setAttribute('id', 'error-div');
        document.body.appendChild(messageDiv);
    }
});