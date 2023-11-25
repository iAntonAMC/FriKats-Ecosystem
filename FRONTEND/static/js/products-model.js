function getProductValues() {
    var product = {
        product_sku: document.getElementById("sku").value,
        product_name: document.getElementById("name").value,
        product_description: document.getElementById("description").value,
        product_price: document.getElementById("price").value,
        product_stock: document.getElementById("stock").value,
        id_category: document.getElementById("category").value,
        product_image: "ruta/de/imagen"
    };
    return product;
}

function registerProduct() {
    var product = getProductValues();
    var xhr = new XMLHttpRequest();
    xhr.open("POST", API_URL + InventoryPATH + "/create", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("Allow-Control-Allow-Origin", "*");
    xhr.send(JSON.stringify(product));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 201) {
            alert("Producto registrado con éxito");
            window.location.href = "http://localhost:666/FRONTEND/inventory/insert-product.html";
        }
    }
}
