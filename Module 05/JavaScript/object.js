var person = {
  name: "abul",
  age: 30,
  isMarried: false,
  hands: 2,
  legs: 2,
  eyes: 2,
  friends: 5,
  address: "Dhaka",
  college: {
    name: "Daffodil International University",
    address: "Sylhet",
    department: "CSE",
    year: 4,
    cgpa: 3.5,
  },
};
console.log(person);
console.log(Object.keys(person));
console.log(Object.values(person));
console.log(Object.entries(person));

console.log(person.address);
console.log(person["address"]);
console.log(person.college.address);
console.log(person.college["address"]);
