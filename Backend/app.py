from flask import Flask, request, jsonify
import io
from PIL import Image
from flask_cors import CORS
import calculate

app = Flask(__name__)
cors = CORS(app)
@app.route('/upload', methods=["GET", "POST"])
def upload():
    if "image" in request.files:
        image_file = request.files["image"]
        image = image_file.read()
        image_stream = io.BytesIO(image)
        img = Image.open(image_stream)
        letter = calculate.findLetter(img)
        print(letter)
        return jsonify(letter)
    else:
        print("I am In this!!")
        return {"error": "No image file provided"}
    
if __name__ == '__main__':
    app.run(port=5000)
