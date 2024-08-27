from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Load pre-trained model and tokenizer
model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['text']
    inputs = tokenizer.encode(data, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
