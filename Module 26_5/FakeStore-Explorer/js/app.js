const loadCategories = () => {
    fetch('https://fakestoreapi.com/products/categories')
        .then(res => res.json())
        .then(jsonData => {
            // console.log(jsonData)
            const categoriesContainer = document.getElementById('category-container');
            jsonData.forEach(category => {
                const button = document.createElement('button');
                button.className = 'btn btn-primary my-2'; // Add 'my-2' class for vertical margin
                button.textContent = category;
                button.addEventListener('click', () => loadSingleProducts(category));
                categoriesContainer.appendChild(button);
                // Add a line break after each button
                categoriesContainer.appendChild(document.createElement('br'));
            });
        });
};

const loadSingleProducts = (category) => {
    // console.log(category);
    document.getElementById('products-container').innerHTML = '';
    fetch(`https://fakestoreapi.com/products/category/${category}`)
        .then(res => res.json())
        .then(jsonData=>{
            // console.log(jsonData)
            const productsContainer = document.getElementById('products-container')
            jsonData.forEach(product => {
                productsContainer.innerHTML += `
                <div class="col my-2">
                    <div class="card" style="width: 18rem; height: 600px;">
                        <img src="${product.image}" class="card-img-top h-50 mx-auto" alt="${product.title}" style="object-fit: contain;">
                        <div class="card-body">
                            <h5 style="height: 85px" class="card-title">${product.title}</h5>
                            <p style="height: 50px" class="card-text">${product.description.slice(0, 50)}...</p>
                            <p class="card-text my-0"> <span class="fw-bold">Price:</span> $${product.price}</p>
                            <p class="card-text my-0"> <span class="fw-bold">Category:</span> ${product.category}</p>
                            <p class="card-text my-0"> <span class="fw-bold">Rating:</span> ${product.rating.rate} (${product.rating.count} reviews)</p>
                            <a target="_blank" href="productDetails.html?productId=${product.id}" class="btn btn-primary mt-2">Vies Details</a>
                        </div>
                    </div>
                </div>`
            })
        })
};


const loadProducts = () => {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(jsonData => {
            // console.log(jsonData)
            const productsContainer = document.getElementById('products-container');
            const fragment = document.createDocumentFragment();

            jsonData.forEach(product => {
                const card = document.createElement('div');
                card.className = 'col my-2';
                card.innerHTML = `
                    <div class="card" style="width: 18rem; height: 600px;">
                        <img src="${product.image}" class="card-img-top h-50 mx-auto" alt="${product.title}" style="object-fit: contain;">
                        <div class="card-body">
                            <h5 style="height: 85px" class="card-title">${product.title}</h5>
                            <p style="height: 50px" class="card-text">${product.description.slice(0, 50)}...</p>
                            <p class="card-text my-0"> <span class="fw-bold">Price:</span> $${product.price}</p>
                            <p class="card-text my-0"> <span class="fw-bold">Category:</span> ${product.category}</p>
                            <p class="card-text my-0"> <span class="fw-bold">Rating:</span> ${product.rating.rate} (${product.rating.count} reviews)</p>
                            <a target="_blank" href="productDetails.html?productId=${product.id}" class="btn btn-primary mt-2">View Details</a>
                        </div>
                    </div>`;

                fragment.appendChild(card);
            });

            productsContainer.innerHTML = ''; // Clear the container before appending
            productsContainer.appendChild(fragment);
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
};


loadProducts();
loadCategories();
