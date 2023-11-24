const name = "This is Bangladesh. I love BD";

const name2 = `
what to do
when bored
`;

console.log(name2);

const test = "World";
// const hello = 'Hello ' + test
const hello = `Hello ${test}`;
// console.log(hello);

const number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(number);
console.log(...number);

const num = ["rahim", "karim", ...number];
console.log(num);
console.log(...num);

console.log(Math.max(number));
console.log(Math.max(...number));
