from pathlib import Path

from flask import Flask, render_template_string, request

app = Flask(__name__)
LOG_FILE = Path(__file__).with_name("log.txt")

PAGE = """<!doctype html>
<html lang="th">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Submit Message</title>
</head>
<body>
    {% if message is not none %}
    <h1>Message received:</h1>
    <p style="white-space: pre-wrap">{{ message }}</p>
    <a href="/">กลับไปกรอกข้อความ</a>
    {% else %}
    <h1>Submit your message</h1>
    <form method="post" action="/">
        <label for="message">ข้อความ:</label><br>
        <textarea id="message" name="message" rows="5" cols="50" required></textarea><br>
        <button type="submit">ส่งข้อมูล (Submit)</button>
    </form>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        message = request.form.get("message", "")
        if not message.strip():
            return "กรุณากรอกข้อความ", 400
        with LOG_FILE.open("a", encoding="utf-8") as log:
            log.write(message + "\n")
    return render_template_string(PAGE, message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
