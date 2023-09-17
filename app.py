from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:  # Try-catch block for error handling
        user_input = request.form["user_input"]
        conversation_history = request.form.get("conversation_history", "")
        prompt = f"{conversation_history}User: {user_input}\nChatbot:"

        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completions.choices[0].text.strip()
        conversation_history += f"User: {user_input}\nChatbot: {response}\n"
        return jsonify({"response": response, "conversation_history": conversation_history})
    except Exception as e:  # Catch any exceptions and return an error message
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
