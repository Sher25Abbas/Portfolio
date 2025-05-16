from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    # Use your OpenAI API key
    openai.api_key = "your-api-key"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
