@app.route('/extract', methods=['POST'])
def extract_data():
    data = request.json
    url = data.get("url")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüfen Sie den HTTP-Statuscode
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

    except requests.exceptions.RequestException as req_err:
        return jsonify({"error": f"Anfragefehler: {req_err}"}), 500
    except AttributeError as attr_err:
        return jsonify({"error": f"Attributfehler: {attr_err}"}), 500
    except Exception as e:
        return jsonify({"error": f"Fehler bei der Datenextraktion: {e}"}), 500
