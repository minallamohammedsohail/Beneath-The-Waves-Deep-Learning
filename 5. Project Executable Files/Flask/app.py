from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

# Load the trained model
model_path = 'D:/jeeva/project/Flask/waves_img.h5'
model = load_model(model_path)

def model_predict(img_path, model):
    img = load_img(img_path, target_size=(299, 299))  # Ensure this matches the input shape expected by the model
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize image

    prediction = model.predict(img_array)
    return prediction

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/inner')
def inner():
    return render_template("inner.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'static/uploads', file.filename)
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        file.save(filepath)
        
        # Make prediction
        prediction = model_predict(filepath, model)
        index = ['Bleached Coral', 'Healthy Coral']
        result = index[int(np.argmax(prediction, axis=1))]
        
        return jsonify({'prediction': result})
    
    return jsonify({'error': 'File not saved'}), 500

@app.route('/output')
def output():
    return render_template("output.html")

if __name__ == '__main__':
    app.run(debug=True, port=2222)
