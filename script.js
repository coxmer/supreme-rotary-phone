// script.js
const chatBox = document.getElementById('chat-box');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const form = document.getElementById('message-form');
const input = document.getElementById('message-input');
const button = document.getElementById('send-button');

//Add a message to accept the message
button.addEventListener('click', (e) => {
    e.preventDefault();
    const message = input.value.trim();
    if (message) {
        fetch('/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.error(error));
        input.value = '';
    }
});

// Function to add a message to the chat box
function addMessage(message, isSent) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isSent ? 'sent' : 'received');

    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');
    messageContent.textContent = message;

    messageDiv.appendChild(messageContent);
    chatBox.appendChild(messageDiv);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send button click event
sendBtn.addEventListener('click',() => {
    const message = chatInput.value.trim();
    if (message) {
        addMessage(message)
    }
})

// Add event listener to chatInput for Enter key press
chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault(); // Prevent default Enter key behavior
        const message = chatInput.value.trim();
        if (message) {
            addMessage(message, true); // Pass true to indicate sent message
            chatInput.value = ''; // Clear the input field
        }
    }
})
