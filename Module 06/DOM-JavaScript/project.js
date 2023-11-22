// alert()

// function handleDeposit() {
//   //   console.log("handleDeposit");
//   var inputValue = document.getElementById("deposit-input").value;
//   //   console.log(inputValue);
//   var convertedInputValue = convertToNumber(inputValue);
//   var depositeAmount = document.getElementById("deposit-amount").innerText;
//   var convertedDepositeAmount = convertToNumber(depositeAmount);
//   //   console.log(depositeAmount);
//   var sum = convertedInputValue + convertedDepositeAmount;
//   console.log(sum);
//   document.getElementById("deposit-amount").innerText = sum;
//   document.getElementById("deposit-input").value = "";

//   var totalAmount = document.getElementById("total-amount").innerText;
//   var convertedTotalAmount = convertToNumber(totalAmount);
//   var totalSum = convertedInputValue + convertedTotalAmount;
//   document.getElementById("total-amount").innerText = totalSum;

//   // var convertedInputValue = getConvertedValue("deposit-input", "value");
// }

// function convertToNumber(value) {
//   return parseFloat(value);
// }

// function handleWithdraw() {
//   // console.log("handleWithdraw");

//   var inputWithdraw = document.getElementById("withdraw-input").value;
//   var convertedInputWithdraw = convertToNumber(inputWithdraw);

//   var withdrawAmount = document.getElementById("withdraw-amount").innerText;
//   var convertedWithdrawAmount = convertToNumber(withdrawAmount);

//   //   console.log(convertedInputWithdraw, convertedWithdrawAmount);
//   var sum = convertedInputWithdraw + convertedWithdrawAmount;
//   document.getElementById("withdraw-amount").innerText = sum;
//   document.getElementById("withdraw-input").value = "";

//   var totalAmount = document.getElementById("total-amount").innerText;
//   var convertedTotalAmount = convertToNumber(totalAmount);

//   var totalSum = convertedTotalAmount - convertedInputWithdraw;
//   document.getElementById("total-amount").innerText = totalSum;
// }

function handleDeposit() {
  var convertedInputValue = getConvertedValue("deposit-input", "value");

  var converteddepostiteAmount = getConvertedValue(
    "deposit-amount",
    "innerText"
  );
  var sum = convertedInputValue + converteddepostiteAmount;
  setInnerText("deposit-amount", sum);

  var convertedTotalAmount = getConvertedValue("total-amount", "innerText");
  var totalSum = convertedInputValue + convertedTotalAmount;
  setInnerText("total-amount", totalSum);
  document.getElementById("deposit-input").value = "";
}

function getConvertedValue(id, element) {
  if (element == "innerText") {
    var value = document.getElementById(id).innerText;
    return parseFloat(value);
  } else {
    var value = document.getElementById(id).value;
    return parseFloat(value);
  }
}

function handleWithdraw() {
  var convertedInputWithdraw = getConvertedValue("withdraw-input", "value");
  var convertedWithdrawAmount = getConvertedValue(
    "withdraw-amount",
    "innerText"
  );
  var sum = convertedInputWithdraw + convertedWithdrawAmount;
  setInnerText("withdraw-amount", sum);
  var convertedTotalAmount = getConvertedValue("total-amount", "innerText");
  var totalSum = convertedTotalAmount - convertedInputWithdraw;
  setInnerText("total-amount", totalSum);
  document.getElementById("withdraw-input").value = "";
}

function setInnerText(id, value) {
  document.getElementById(id).innerText = value;
}
