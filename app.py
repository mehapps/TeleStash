import os
from quart import Quart, request

app = Quart(__name__)

UPLOAD_FOLDER = "uploads"  # Folder where uploaded files will be stored
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}  # Allowed file extensions


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
async def upload():
    if "file" not in request.files:
        return "No file part in the request", 400

    file = request.files["file"]

    if file.filename == "":
        return "No file selected", 400

    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save the file to the specified upload folder
        await file.save(file_path)

        return f"File '{filename}' uploaded successfully!", 200
    else:
        return "Invalid file or file type not allowed", 400


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the uploads folder if it doesn't exist
    app.run(debug=True)
