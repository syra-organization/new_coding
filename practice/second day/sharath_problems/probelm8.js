function printprimeNumber(num) {
  var i = 1;

  while (i <= num) {
    if (num % i == 0) {
      console.log("print it is prime number", num);
      i++;
    } else i % 2==0  ;
    {
      console.log("print it is not prime number", num);
    }
  }
}

printprimeNumber(17);
