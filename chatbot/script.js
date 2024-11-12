document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("sendButton").addEventListener("click", sendMessage);
});

async function sendMessage() {
    console.log("Fonction sendMessage appelée");
    const userInput = document.getElementById("userInput");
    const userText = userInput.value.trim();
    if (userText === "") return;

    // Afficher le message de l'utilisateur
    displayMessage(userText, "user");

    try {
        // Afficher un message de chargement
        document.getElementById("loading").style.display = "block";

        // Envoyer la requête au serveur Flask
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userText })
        });

        const data = await response.json();
        const botResponse = data.response || "Désolé, je ne connais pas la réponse. Pose une autre question.";

        // Afficher la réponse du chatbot
        displayMessage(botResponse, "bot");

        // Cacher le message de chargement
        document.getElementById("loading").style.display = "none";
    } catch (error) {
        // Afficher une erreur si la requête échoue
        displayMessage("Désolé, une erreur est survenue. Essayez de nouveau.", "bot");
        console.error("Erreur lors de la requête:", error);
    }

    userInput.value = ""; // Réinitialiser le champ de saisie
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.classList.add(sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Faire défiler jusqu'au bas du chat
}
