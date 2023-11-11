from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define routing rules
@app.route('/userservice/<path:path>', methods=['GET', 'POST'])
def route_to_userservice(path):
    userservice_url = "http://localhost:5002"
    
    
    if request.method == 'GET':
        # Route GET request to the user service
        response = requests.get(f"{userservice_url}/{path}")
        return jsonify(response.json(), response.status_code)

    elif request.method == 'POST':
        # Route POST request to the user service
        data = request.get_json()
        response = requests.post(f"{userservice_url}/{path}", json=data)
        return jsonify(response.json(), response.status_code)

@app.route('/productservice/<path:path>', methods=['GET', 'POST', 'DELETE'])
def route_to_productservice(path):
    productservice_url = "http://localhost:5002"
    if request.method == 'GET':
        # Route GET request to the user service
        response = requests.get(f"{productservice_url}/{path}")
        return jsonify(response.json(), response.status_code)

    elif request.method == 'POST':
        # Route POST request to the user service
        data = request.get_json()
        response = requests.post(f"{productservice_url}/{path}", json=data)
        return jsonify(response.json(), response.status_code)
        
    elif request.method == 'DELETE':
        # Route POST request to the user service
        data = request.get_json()
        response = requests.post(f"{productservice_url}/{path}", json=data)
        return jsonify(response.json(), response.status_code)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5001)
    
    
    
    
