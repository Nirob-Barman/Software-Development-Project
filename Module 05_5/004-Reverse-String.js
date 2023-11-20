function reverseString(inputString) {
  var reverseString = "";
  for (var i = inputString.length - 1; i >= 0; i--) {
    reverseString += inputString[i];
  }
  return reverseString;
}

const originalString = "Hello, World!";
const reversedString = reverseString(originalString);
console.log(reversedString);
