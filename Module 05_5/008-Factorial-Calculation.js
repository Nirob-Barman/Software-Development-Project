function calculateFactorial(number){
    var factorialValue = 1;

    for(var i = 2; i <= number; i++){
        factorialValue = factorialValue * i;
    }

    return factorialValue;
}

var inputNumber = 5;

var result = calculateFactorial(inputNumber);
console.log(result);