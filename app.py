from flask import Flask, render_template, request, jsonify
import openai

# Set up your API key
openai.api_key = "your_api_key"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
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

if __name__ == "__main__":
    app.run(debug=True)
