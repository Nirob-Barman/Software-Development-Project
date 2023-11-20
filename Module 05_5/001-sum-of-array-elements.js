function sumOfArrayElements(numbers) {
  var sum = 0;
  for (var i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var sum = sumOfArrayElements(numbers);
console.log(sum);
