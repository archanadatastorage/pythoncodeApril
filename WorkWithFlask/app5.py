from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store strings
string_list = []

@app.route('/add_string', methods=['POST'])
def add_string():
    # Expecting raw text, not JSON
    string_data = request.data.decode('utf-8')

    if not string_data:
        return jsonify({'error': 'No string provided'}), 400

    string_list.append(string_data)

    return jsonify({
        'message': 'String added successfully',
        'strings': string_list
    }), 201

if __name__ == '__main__':
    app.run(debug=True)