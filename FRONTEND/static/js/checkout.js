const inputQuery = document.getElementById('inputQuery');
const resultsDIV = document.getElementById('results');

inputQuery.addEventListener('input', function() {
    if(inputQuery.value.trim().length < 2) {
        resultsDIV.innerHTML = '';
        return;
    }
    const query = inputQuery.value.trim();
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const products = JSON.parse(xhr.responseText);
                showResults(products);
            }
            else {
                console.error('Hubo un error al hacer la solicitud:', xhr.responseText);
            }
        }
    };

    xhr.open('GET', API_URL + '/inventory/all/' + query, true);
    xhr.send();
});

function showResults(products) {
    resultsDIV.innerHTML = '';
    products.forEach(product => {
        const card = document.createElement('div');
        const image = document.createElement('img');
        const name = document.createElement('p');
        const price = document.createElement('p');
        const addbutton = document.createElement('button');
        image.src = product.product_image;
        name.innerText = product.product_name;
        price.innerText = product.product_price;
        addbutton.innerHTML = 'Agregar';
        addbutton.addEventListener('click', function() {
            addToCart(product);
        });
        card.classList.add('card');
        card.appendChild(image);
        card.appendChild(name);
        card.appendChild(price);
        card.appendChild(addbutton);
        resultsDIV.appendChild(card);
    });
}

function evaluateCart(product) {
    var table = document.getElementById("ticket-body");
    var rows = table.getElementsByTagName("tr");
    var productAlreadyInCart = false;
    if (rows.length != 0) {
        for (var i = 0; i < rows.length; i++) {
            if (rows[i].cells[1].innerHTML === product.product_name) {
                productAlreadyInCart = true;
                break
            }
        }
    }
    return productAlreadyInCart;
}

function addToCart(product) {
    if (evaluateCart(product)) {
        var quantityInput = document.getElementById("quantity-of-"+ product.id_product);
        quantityInput.value = parseInt(quantityInput.value) + 1;
        var total = product.product_price * quantityInput.value;
        var row = quantityInput.parentNode.parentNode;
        row.cells[4].innerHTML = total;
    }
    else {
        var table = document.getElementById("ticket-body");
        var row = table.insertRow();
        row.insertCell().innerHTML = product.product_image;
        row.insertCell().innerHTML = product.product_name;
        row.insertCell().innerHTML = '<input type="number" id="quantity-of-'+product.id_product+'" name="quantity-of-'+product.id_product+'" min="1" max="100" value="1">';
        document.getElementById("quantity-of-"+product.id_product).addEventListener('change', function() {
            var total = product.product_price * document.getElementById("quantity-of-"+product.id_product).value;
            row.cells[4].innerHTML = total;
        });
        row.insertCell().innerHTML = product.product_price;
        row.insertCell().innerHTML = product.product_price * document.getElementById("quantity-of-"+product.id_product).value;
        row.insertCell().innerHTML = '<button class="btn btn-danger" onclick="removeFromCart(this)">Eliminar</button>';
    }
}

function removeFromCart(button) {
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

function emptyCart() {
    var table = document.getElementById("ticket-body");
    var rows = table.getElementsByTagName("tr");
    while (rows.length != 0) {
        rows[0].parentNode.removeChild(rows[0]);
    }
}
