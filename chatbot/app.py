from flask import Flask, render_template, request, jsonify
import openai
from flask_cors import CORS

# Crée l'application Flask
app = Flask(__name__)

# Permet les requêtes CORS si nécessaire
CORS(app)

# Configure OpenAI avec votre clé API
openai.api_key = "YOUR_OPENAI_API_KEY"

# Informations de ton CV que le bot utilisera pour répondre
cv_info = """
Nom: Quentin SACLA
Profession: Développeur web et mobile
Email: quentinsacla@gmail.com
Téléphone: +22961924532
Localisation: Cotonou, Bénin
Age: 26 ans

Expérience:
- Coordonnateur de l'ONG GHV, Guinée (depuis Oct. 2023)
- Développeur web freelance pour CIUP, Gabon (Oct. 2023 - Janv. 2024)
- Développeur web freelance pour ONG-AISD, Bénin (depuis Févr. 2023)
- Développeur web et mobile chez Mégatech, Bénin (Juin 2023 - Nov. 2023)
- Développeur freelance pour Torritransport, France (depuis Févr. 2024)

Compétences:
HTML, CSS, JavaScript, Node.js, Vue.js, PHP, Python, ReactJS, Flutter, MySQL, MongoDB, etc.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    print(f"Message reçu: {user_input}")  # Afficher la question dans la console

    # Construire le prompt pour OpenAI
    prompt = f"{cv_info}\n\nQ: {user_input}\nA:"

    try:
        # Utiliser la nouvelle méthode d'API Chat d'OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Tu peux utiliser "gpt-3.5-turbo" ou une autre version du modèle
            messages=[
                {"role": "system", "content": "Vous êtes un assistant utile."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content'].strip()
        print(f"Réponse générée: {answer}")  # Afficher la réponse dans la console
        return jsonify({"response": answer})
    except Exception as e:
        print(f"Erreur lors de l'appel à OpenAI: {str(e)}")  # Log pour les erreurs
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
