from flask import Flask, render_template, request, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Produktliste speichern
products = []

def scrape_product(url):
    """ Holt Name, Preis und Bild von einer Produktseite """
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Hier müssen ggf. andere Selektoren genutzt werden
    name = soup.find("span", class_="product-title").text.strip()
    price = soup.find("span", class_="price").text.strip()
    image = soup.find("img", class_="product-image")["src"]

    return {"name": name, "price": price, "image": image, "url": url}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        product = scrape_product(url)
        if product:
            products.append(product)
        return redirect("/")
    
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
