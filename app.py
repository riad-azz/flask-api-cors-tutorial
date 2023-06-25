# Other modules
import names
from random import randint
# Flask modules
from flask import Flask, jsonify
from flask_cors import CORS

def get_dummy_data(count: int = 10):
	dummy_data = list()
	for _ in range(count):
		person = {
			"name": names.get_full_name(),
			"age": randint(18, 60),
			"is_working": randint(0, 1) == 1,
		}
		dummy_data.append(person)
	return dummy_data

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000"]}})

@app.route('/api/data', methods=['GET'])
def dummy_data():
    data = get_dummy_data()
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)