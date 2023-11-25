// print all the numbers between 1 to given number which is divisble by 5

function isDivisibleBy5(num) {
  var i = 1;
  var count = 0;
  while (i <= num) {
    if (i % 5 == 0) {
      count++;
    }
    i++;
  }
  console.log("given counting", count);
}
isDivisibleBy5(100);
