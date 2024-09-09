# My Simple LLM

This project is a basic implementation of an AI Language Model (LLM) using a pre-trained GPT-2 model from Hugging Face. The model is deployed via a Flask API, allowing users to generate text by providing a prompt.

## Features

- **Text Generation**: Generate text continuations based on an input prompt using GPT-2.
- **REST API**: A simple Flask-based API to interact with the model.

## Requirements

- Python 3.7+
- pip

## Setup and Installation

1. **Clone the Repository**:
    git clone https://github.com/abhetu/MySimpleLLM.git
    cd my-simple-llm


2. **Create a Virtual Environment (Optional but Recommended)**:<br>
    `python3 -m venv venv` <br>
    `source venv/bin/activate` <br>
    On Windows, use `venv\Scripts\activate`


4. **Install the Required Packages**:
    pip install -r requirements.txt

## Running the Application

1. **Start the Flask Server**:
    python app.py

2. **Test the API**:
    - Open a tool like Postman or cURL.
    - Send a POST request to `http://localhost:5000/predict` with a JSON payload:
        {
            "text": "Once upon a time"
        }
    - You will receive a response like:
        {
            "output": "Once upon a time, in a land far away, there was a..."
        }
       

