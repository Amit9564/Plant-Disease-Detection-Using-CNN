from flask import Flask,render_template,request
from predict import predict_disease
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    if 'file' not in request.files:
        return "No File Uploaded"

    file = request.files['file']

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    prediction = predict_disease(filepath)

    return render_template(
        'result.html',
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)