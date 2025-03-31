document.getElementById("linkForm").addEventListener("submit", async function(event) {
  event.preventDefault();
  
  const productLink = document.getElementById("productLink").value;
  
  try {
    const response = await fetch("http://127.0.0.1:5000/extract", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: productLink })
    });

    const data = await response.json();
    displayProduct(data);

  } catch (error) {
    console.error("Fehler beim Abrufen der Produktinformationen", error);
  }
});

function displayProduct(product) {
  const productList = document.getElementById("productList");
  
  const productDiv = document.createElement("div");
  productDiv.classList.add("product");

  productDiv.innerHTML = `
    <h3>${product.name}</h3>
    <p>Preis: ${product.price}</p>
    <img src="${product.image_url}" alt="${product.name}" width="100%">
  `;

  productList.appendChild(productDiv);
}
