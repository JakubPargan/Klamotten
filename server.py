from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract_data():
    data = request.json
    url = data.get("url")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Beispielhafter Extraktionscode:
        product_name = soup.find('h1').text.strip()
        product_price = soup.find(class_='price').text.strip()
        product_image = soup.find('img')['src']

        return jsonify({
            "name": product_name,
            "price": product_price,
            "image_url": product_image
        })

    except Exception as e:
        return jsonify({"error": "Fehler bei der Datenextraktion"}), 500

if __name__ == "__main__":
    app.run(debug=True)
