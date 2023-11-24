const products = [
  { id: 1, name: "apple", price: 220, color: "red" },
  { id: 2, name: "redmi", price: 200, color: "blue" },
  { id: 3, name: "samsung", price: 300, color: "black" },
  { id: 4, name: "oneplus", price: 400, color: "white" },
  { id: 5, name: "oppo", price: 500, color: "pink" },
  { id: 6, name: "vivo", price: 600, color: "yellow" },
  { id: 7, name: "nokia", price: 700, color: "green" },
  { id: 8, name: "sony", price: 800, color: "black" },
];

// const result = products.forEach((product) => console.log(product));

// const productContainer = document.getElementById("product-container");
// const result = products.forEach((product) => {
//   //   console.log(product);
//   const h1 = document.createElement("h1");
//   const p=document.createElement("p");
//   p.innerText=product.price
//   h1.innerText = product.name;
//   //   document.body.appendChild(h1);
//   productContainer.appendChild(h1);
//   productContainer.appendChild(p);
// });

const productContainer = document.getElementById("product-container");

products.forEach((product) => {
  const productInfo = document.createElement("P");
  productInfo.innerText = `${product.name} : ${product.price}`;

  productContainer.appendChild(productInfo);
});
