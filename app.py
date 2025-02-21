<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Caption & Hashtags</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

        body {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            margin: 50px;
            background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
            color: white;
        }
        .container {
            display: inline-block;
            background: rgba(10, 10, 10, 0.9);
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        textarea {
            width: 600px;
            height: 150px;
            padding: 12px;
            resize: none;
            background: rgba(20, 20, 20, 0.8);
            border: 1px solid rgba(138, 43, 226, 0.5);
            color: white;
            font-size: 18px;
            border-radius: 6px;
            margin-bottom: 15px;
        }
        button {
            background: linear-gradient(145deg, #a855f7, #6a0dad);
            color: white;
            border: none;
            padding: 12px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s ease-in-out;
            box-shadow: 0px 4px 10px rgba(138, 43, 226, 0.6);
            border-radius: 6px;
            margin: 10px;
        }
        button:hover {
            background: linear-gradient(145deg, #6a0dad, #a855f7);
            transform: scale(1.08);
        }
        .line {
            width: 90%;
            height: 2px;
            background: rgba(138, 43, 226, 0.4);
            margin: 20px auto;
        }
    </style>
</head>
<body>

    <h1>✨ Your AI-Generated Caption & Hashtags</h1>
    
    <div class="container">
        <h3>📝 Caption</h3>
        <textarea id="captionText" readonly>{{ caption }}</textarea>
        <button onclick="copyText('captionText')">📋 Copy Caption</button>

        <div class="line"></div>

        <h3>🔖 Hashtags</h3>
        <textarea id="hashtagText" readonly>{{ hashtags }}</textarea>
        <button onclick="copyText('hashtagText')">📋 Copy Hashtags</button>

        <div class="line"></div>

        <button onclick="goBack()">🔙 Back</button>
    </div>

    <script>
        function copyText(elementId) {
            var textArea = document.getElementById(elementId);
            textArea.select();
            document.execCommand("copy");
            alert("Copied to clipboard! 📋");
        }

        function goBack() {
            window.location.href = "/";
        }
    </script>

</body>
</html>