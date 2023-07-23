import os
from quart import Quart, request, render_template
from upload import upload_file_to_telegram

app = Quart(__name__)

@app.route("/upload", methods=["POST"])
async def upload_file():
    files = await request.files
    file = files.get('file')

    if not file.filename: return "No file selected", 400

    file_name = file.filename
    await upload_file_to_telegram(file.read(), "test", file_name)

    return f"File '{file_name}' uploaded successfully!", 200

@app.route("/", methods=["GET"])
async def index():
    return await render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)