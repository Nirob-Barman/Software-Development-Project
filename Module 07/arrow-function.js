function test() {
  console.log("Test");
  return "Testing";
}

console.log(test);
const result = test();
console.log(result);

const test2 = () => {
  console.log("Test2");
  return "Testing2";
};

console.log(test2);
const result2 = test2();
console.log(result2);

const test3 = () => console.log("Test3");

const test4 = (a) => console.log(a);
test4(5);

const sum = (a, b) => {
  return a + b;
};
console.log(sum(1, 3));
