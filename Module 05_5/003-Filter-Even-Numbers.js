function filterEvenNumbers(numbers) {
  //   var evenNumbers = numbers.filter((num) => num % 2 === 0);
  //   return evenNumbers;

  const evenNumbers = [];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      evenNumbers.push(numbers[i]);
    }
  }

  return evenNumbers;
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(filterEvenNumbers(numbers));
