import os
from flask import Flask, render_template_string

app = Flask(__name__)

COLOR = os.getenv("APP_COLOR", "white")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Color App</title>
    <style>
        body {
            background-color: {{ color }};
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 20%;
        }
    </style>
</head>
<body>
    <h1>Environment Color: {{ color }}</h1>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, color=COLOR)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
