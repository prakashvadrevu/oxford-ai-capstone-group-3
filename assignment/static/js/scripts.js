document.addEventListener('DOMContentLoaded', (event) => {
    let history = [];

    window.sendQuestion = function() {
        const question = document.getElementById('question').value;
        if (question.trim() === "") return;

        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<div class="message user-message"><strong>You:</strong> ${question}</div>`;
        chatBox.innerHTML += `<div id="loading" class="message bot-message"><div class="spinner"><div></div><div></div><div></div></div></div>`;
        chatBox.scrollTop = chatBox.scrollHeight;

        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question, history: history })
        })
        .then(response => response.json())
        .then(data => {
            history.push({ question: question, answer: data.answer });
            const loadingElement = document.getElementById('loading');
            loadingElement.parentNode.removeChild(loadingElement);
            chatBox.innerHTML += `<div class="message bot-message"><strong>Bot:</strong> ${data.answer}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });

        document.getElementById('question').value = '';
    };

    window.newSession = function() {
        history = [];
        document.getElementById('chat-box').innerHTML = '';
    };

    window.checkEnter = function(event) {
        if (event.key === 'Enter') {
            sendQuestion();
        }
    };
});
