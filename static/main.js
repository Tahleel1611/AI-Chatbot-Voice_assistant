document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('command-form');
    const input = document.getElementById('command-input');
    const sendBtn = document.getElementById('send-btn');
    const chatBox = document.getElementById('chat-box');
    const loader = document.getElementById('loader');

    function appendMessage(sender, message) {
        const msgDiv = document.createElement('div');
        msgDiv.className = sender === 'You' ? 'user-msg' : 'ai-msg';
        msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const command = input.value.trim();
        if (!command) return;
        appendMessage('You', command);
        input.value = '';
        loader.style.display = 'block';

        try {
            const response = await fetch('/process-command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command })
            });
            const data = await response.json();
            if (data.response) {
                appendMessage('AI', data.response);
            } else if (data.error) {
                appendMessage('AI', `Error: ${data.error}`);
            }
        } catch (err) {
            appendMessage('AI', 'Network error. Please try again.');
        } finally {
            loader.style.display = 'none';
        }
    });

    // Optional: Allow send button to trigger submit
    sendBtn.addEventListener('click', function () {
        form.dispatchEvent(new Event('submit'));
    });
});
// Theme switcher
document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.addEventListener('click', function () {
        document.body.classList.toggle('theme-dark');
        document.body.classList.toggle('theme-light');
        themeToggle.textContent = document.body.classList.contains('theme-dark') ? 'Light Mode' : 'Dark Mode';
    });
});