// const getData = new Promise(function (resolve, reject) {
//   return resolve(20);
// });

// console.log(getData);
// getData.then((data) => console.log(data));

const getData2 = new Promise(function (resolve, reject) {
  return reject(20);
});

console.log(getData2);
getData2.then((data) => console.log(data)).catch((error) => console.log(error));

// fetch("https://fakestoreapi.com/products/1")
//   .then((response) => {
//     // console.log(response);
//     return response.json();
//   })
//   .then((data) => console.log(data))
//   .catch((error) => console.log(error));

// const loadData = async () => {
//   const response = await fetch("https://fakestoreapi.com/products/1");
//   //   console.log(response);
// //   console.log(response.json());
//   const data = await response.json();
//   console.log(data);
// };

const loadData = async () => {
  try {
    const response = await fetch("https://fakestoreapi.com/products/1");
    //   console.log(response);
    //   console.log(response.json());
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
};

loadData();
