const nums = [2, 2, 3];
let temp = [];
for (let i = 0; i < nums.length; i++) {
  const element = nums[i];
  const square = element * element;
  temp.push(square);
}
// console.log(temp);

// const newArray = nums.map((num) => console.log(num));

const squareArray = nums.map((num) => num * num);
// console.log(squareArray);

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

// const result = products.filter((product) => console.log(product));
const result = products.filter((product) => product.color == "black");
// console.log(result);

const result2 = products.find((product) => product.color == "black");
// console.log(result2);
