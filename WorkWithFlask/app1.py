from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (just for demonstration)
data_store = []

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({"data": data_store})

@app.route('/', methods=['POST'])
def post_data():
    content = request.json  # Expecting JSON data
    if not content or 'item' not in content:
        return jsonify({'error': 'No item provided'}), 400

    data_store.append(content['item'])
    return jsonify({'message': 'Item added', 'data': data_store}), 201

if __name__ == '__main__':
    app.run(debug=True)
