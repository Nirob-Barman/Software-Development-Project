function findMaxValue(numbers) {
  var max = numbers[0];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  return max;
}

console.log(findMaxValue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));

// Output: 10
