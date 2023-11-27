const inputQuery = document.getElementById('inputQuery');
const resultsDIV = document.getElementById('results');

inputQuery.addEventListener('input', function() {
    if(inputQuery.value.trim().length < 1) {
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

function addToCart(product) {
    console.log(product)
}
