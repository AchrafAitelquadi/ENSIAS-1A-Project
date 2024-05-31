// Add event listener to send message on pressing "Enter"
document.getElementById("userInput").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    var userInput = document.getElementById("userInput").value.trim();

    if (userInput !== "") {
        const messagesDiv = document.getElementById("messages");

        // Display user message immediately
        messagesDiv.innerHTML += `
            <div class="message user">
                <img class="message-icon" src="static/js/user-icon.png" alt="User Icon">
                <div class="message-text">${userInput}</div>
            </div>`;
        
        // Scroll to the bottom
        messagesDiv.scrollTop = messagesDiv.scrollHeight;

        // Send the user message to the server
        fetch('/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            // Display bot response
            messagesDiv.innerHTML += `
                <div class="message bot">
                    <img class="message-icon" src="static/js/bot-icon.png" alt="Bot Icon">
                    <div class="message-text">${data.response}</div>
                </div>`;

            // Scroll to the bottom
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
        });

        // Clear the input field
        document.getElementById("userInput").value = "";
    }
}
