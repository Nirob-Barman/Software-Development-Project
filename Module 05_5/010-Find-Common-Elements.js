function findCommonElements(arr1, arr2) {
  var commonElements = [];
  for (var i = 0; i < arr1.length; i++) {
    for (var j = 0; j < arr2.length; j++) {
      if (arr1[i] === arr2[j]) {
        commonElements.push(arr1[i]);
      }
    }
  }
  return commonElements;
}

var arr1 = [1, 2, 3, 4, 5];
var arr2 = [2, 4, 6, 8, 10];
var commonElements = findCommonElements(arr1, arr2);
console.log(commonElements);

// Output: [2, 4]
