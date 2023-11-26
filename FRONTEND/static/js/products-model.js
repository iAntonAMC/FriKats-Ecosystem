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

function getAllPoducts () {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", API_URL + InventoryPATH + "/all", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("Allow-Control-Allow-Origin", "*");
    xhr.send();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
            var products = JSON.parse(xhr.responseText);
            var table = document.getElementById("products-table");
            for (var i = 0; i < products.length; i++) {
                var row = table.insertRow();
                row.insertCell().innerHTML = products[i].product_sku;
                row.insertCell().innerHTML = products[i].product_name;
                row.insertCell().innerHTML = products[i].product_description;
                row.insertCell().innerHTML = products[i].product_price;
                row.insertCell().innerHTML = products[i].product_stock;
                row.insertCell().innerHTML = products[i].id_category;
                row.insertCell().innerHTML = products[i].product_image;
            }
        }
    }
}
