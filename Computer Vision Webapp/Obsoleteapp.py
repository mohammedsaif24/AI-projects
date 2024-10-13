from flask import Flask, request, jsonify
from inference import run_inference

app = Flask(_name_)

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files['image']
    results = run_inference(image)
    return jsonify(results)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
