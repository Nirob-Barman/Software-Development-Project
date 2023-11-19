var num = 55;

if (num % 2 == 0) {
  console.log("Number is even");
} else {
  console.log("Number is odd");
}

var nums = [2, 3, 5, 8, 9, 4, 7];
console.log(nums.sort());
var nums = [2, 3, 5, 8, 9, 4, 7, 11, 14, 12, 13];
console.log(nums.sort());
console.log(
  nums.sort(function (a, b) {
    return a - b;
  })
);
console.log(
  nums.sort(function (a, b) {
    return b - a;
  })
);

var friends = ["rahim", "karim", "abul", "salam", "heroAlam"];

var maxLengthName = friends[0];

for (var i = 0; i < friends.length; i++) {
  var currentName = friends[i];
  if (currentName.length > maxLengthName.length) {
    maxLengthName = currentName;
  }
}
console.log(maxLengthName);
