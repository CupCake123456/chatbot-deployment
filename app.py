from flask import Flask, render_template, request , jsonify
from chat import get_response 


app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict") 
def predict():
    data = request.get_json()  # Get the JSON data from the request
    text = data.get("message")  # Extract the "message" field from the JSON data
    # TODO: Check if text is valid
    response = get_response(text)  # Pass the actual text to the get_response function
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)

