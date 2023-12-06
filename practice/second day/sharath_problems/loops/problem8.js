// given a number
// write a program to find whether the number is prime or not

function checkPrime(num) {
  var i = 1;
  var numberOfFactor = 0;

  while (i <= num) {
    if (num % i == 0) {
      numberOfFactor++;
    }
  }
  if (numberOfFactor == 2) {
    console.log("Given number is prime");
  } else {
    console.log("Given number is not prime");
  }
}

checkPrime(17);
