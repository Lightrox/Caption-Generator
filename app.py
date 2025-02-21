from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def generate_caption(topic, style):
    styles = {
        "casual": "Make it simple and conversational.",
        "funny": "Make it witty and humorous.",
        "motivational": "Make it inspiring and uplifting.",
        "aesthetic": "Make it poetic and deep.",
        "short": "Make it short, catchy, and trendy."
    }

    prompt = f"Generate an Instagram caption about {topic}. {styles.get(style, 'Make it engaging.')}"

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text  # Extract caption from response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic")
        style = request.form.get("style")
        
        if not topic or not style:
            return render_template("index.html", error="Please fill all fields.")
        
        # Redirect to the caption page with topic and style as URL parameters
        return redirect(url_for("caption", topic=topic, style=style))

    return render_template("index.html")

@app.route("/caption")
def caption():
    topic = request.args.get("topic")
    style = request.args.get("style")

    if not topic or not style:
        return redirect(url_for("index"))

    caption_text = generate_caption(topic, style)
    return render_template("caption.html", caption=caption_text)

if __name__ == "__main__":
    app.run(debug=True)

