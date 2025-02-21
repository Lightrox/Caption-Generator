from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
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

    return response.text if response else "Failed to generate caption."

def generate_hashtags(topic):
    prompt = f"Generate a list of 20 trending hashtags for {topic} on Instagram."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text if response else "#NoHashtagsGenerated"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic")
        style = request.form.get("style")

        if not topic or not style:
            return render_template("index.html", error="Please fill all fields.")

        caption = generate_caption(topic, style)
        hashtags = generate_hashtags(topic)

        return render_template("caption.html", topic=topic, style=style, caption=caption, hashtags=hashtags)
    
    return render_template("index.html")

@app.route("/back")
def back():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
