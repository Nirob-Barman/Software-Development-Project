function removeDuplicates(inputArray) {
  var uniqueArray = [];
  for (var i = 0; i < inputArray.length; i++) {
    if (!uniqueArray.includes(inputArray[i])) {
      uniqueArray.push(inputArray[i]);
    }
  }
  return uniqueArray;
}

var inputArray = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4];
console.log(removeDuplicates(inputArray));
