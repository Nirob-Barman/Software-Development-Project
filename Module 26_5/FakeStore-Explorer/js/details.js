const getParams = () => {
    const param = new URLSearchParams(window.location.search).get("productId");
    fetch(`https://fakestoreapi.com/products/${param}`)
        .then((res) => res.json())
        .then((json) => {
            const productsContainer = document.getElementById("product-details");
            productsContainer.innerHTML += `
                <div class="row mt-4">
                    <div class="col-md-6">
                        <img src="${json.image}" class="img-fluid" alt="Product Image">
                    </div>
                    <div class="col-md-6">
                        <h2 class="display-4">${json.title}</h2>
                        <p class="lead">${json.description}</p>
                        <p class="h4">Price: $${json.price}</p>
                        <p class="h5">Category: ${json.category}</p>
                        <p class="h5">Rating: ${json.rating.rate} (${json.rating.count} reviews)</p>
                        <button class="btn btn-primary btn-lg">Add to Cart</button>
                    </div>
                </div>
            `;
        });
};

getParams();