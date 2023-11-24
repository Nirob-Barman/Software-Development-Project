// fetch("https://fakestoreapi.com/products/1")
//   .then((res) => res.json())
//   .then((jsonFile) => console.log(jsonFile));

// fetch("https://fakestoreapi.com/products/1")
//   .then((response) => {
//     console.log(response);
//     return response.json();
//   })
//   .then((jsonFile) => {
//     console.log(jsonFile);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

fetch("https://fakestoreapi.com/products/1")
  .then((response) => response.json())
  .then((jsonFile) => {
    console.log(jsonFile);
  })
  .catch((error) => {
    console.log(error);
  });
