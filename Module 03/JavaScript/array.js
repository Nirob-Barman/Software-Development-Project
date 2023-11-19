var friends = ["abul", "babul", "cabul", "dabul"];
console.log(friends);
console.log(friends[0]);
console.log(friends[1]);
console.log(friends[2]);
console.log(friends[3]);
friends.push("eabul");
console.log(friends);
friends.pop();
console.log(friends);

friends.unshift("zabul");
console.log(friends);
friends.shift();
console.log(friends);

console.log(friends.reverse);
console.log(friends.reverse());
console.log(friends);
console.log(friends.sort());
console.log(friends.sort().reverse());

console.log(friends.indexOf("abul"));
console.log(friends.indexOf("zabul"));

console.log(friends.slice(1, 3));
console.log(friends);
console.log(friends.slice(2, 4));
