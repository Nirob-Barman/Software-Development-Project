console.log(1);
console.log(2);
console.log(3);
console.log(4);
// console.log(5);
name(5);
console.log(6);
console.log(7);
console.log(8);
console.log(9);
console.log(10);

// function name(x) {
//   // synchronous
//   //   console.log(x);

//   // asynchronous
//   fetch("https://fakestoreapi.com/products/1")
//     .then((response) => response.json())
//     .then((jsonFile) => {
//       console.log(jsonFile);
//     });
// }

// function name(x) {
//   // synchronous
//     console.log(x);

//   // asynchronous
//   fetch("https://fakestoreapi.com/products/1")
//     .then((response) => response.json())
//     .then((jsonFile) => {
//       console.log(jsonFile);
//     });
// }

// asynchronous
function name(x) {
  setTimeout(() => {
    console.log(x);
  }, 2000);
}
