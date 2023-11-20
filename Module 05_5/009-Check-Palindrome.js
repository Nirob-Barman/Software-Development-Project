function isPalindrome(str) {
  var len = str.length;
  for (var i = 0; i < len / 2; i++) {
    if (str[i] !== str[len - 1 - i]) {
      return false;
    }
  }
  return true;
}

var testString = "racecar";
console.log(isPalindrome(testString));

// Output: true
