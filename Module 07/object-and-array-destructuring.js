const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// destructuring
const [first, second, ...rest] = numbers;

// console.log(first);
// console.log(second);
// console.log(rest);

const obj = {
  name: "Nirob",
  age: 25,
  address: "Dhaka",
  country: "Bangladesh",
  language: "Bangla",
  salary: 25000,
  married: true,
};

const Age = obj.age;
// console.log("Age", Age);
const {
  name: personName,
  age,
  address,
  country,
  language,
  salary,
  married,
} = obj;

// console.log("personName:", personName);
// console.log(age);
// console.log(address);
// console.log(country);
// console.log(language);
// console.log(salary);
// console.log(married);

const test = [
  {
    name: "John",
    age: 30,
    address: "New York",
    friends: ["Rahim", "Karim", "David"],
    country: "USA",
    language: "English",
    salary: 55000,
    married: true,
  },
  {
    name: "Alice",
    age: 28,
    address: "Los Angeles",
    friends: ["Bob", "Eva", "Michael"],
    country: "USA",
    language: "English",
    salary: 52000,
    married: false,
  },
  {
    name: "Michael",
    age: 35,
    address: "Chicago",
    friends: ["Sophie", "James", "Lily"],
    country: "USA",
    language: "English",
    salary: 58000,
    married: true,
  },
];

// console.log(test);
// console.log(test.length);

// const [person1, person2, person3] = test;
// console.log(person1);
// console.log(person2);
// console.log(person3);

// console.log(test[0])
// console.log(test[1])
// console.log(test[2])

// console.log(test[0].friends);
// console.log(test[0].friends[1]);
