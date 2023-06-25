# Flask API with CORS Tutorial

This repository provides a simple tutorial on building a Flask API with CORS (Cross-Origin Resource Sharing) enabled. The tutorial explains the concepts of CORS and demonstrates how to implement CORS in a Flask API. The API serves as a foundation for developing web applications that require cross-origin requests.

You can find a detailed step-by-step tutorial about this repository on our blog: [Flask API with CORS Tutorial](https://utopia-insights.dev/building-a-simple-flask-api-with-cors-a-comprehensive-tutorial-for-cross-origin-resource-sharing)

## Features

- Sets up a basic Flask API with routes for handling requests.
- Implements CORS to allow cross-origin requests from specific origins.
- Provides an example route for retrieving data.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/riad-azz/flask-api-cors-tutorial.git
```

2. Navigate to the project directory:

```bash
cd flask-api-cors-tutorial
```

3. Create a virtual environment:

```bash
python -m venv myenv
```


4. Activate the virtual environment:

For Mac/Linux:

```bash
source myenv/bin/activate
```

For Windows:

```bash
myenv\Scripts\activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask API:

```bash
python app.py
```

2. Access the API using a web browser or a tool like cURL or Postman:

```bash
http://localhost:5000/api/data
```

This endpoint returns a JSON response containing a list of random people as dummy data. 

## License

This project is licensed under the [MIT License](LICENSE).