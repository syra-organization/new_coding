// given the number you need to print the reverse of it.

// example:- let say the given number is 12345
// you need to print 54321

function printReverseOfNumber(num) {
  var bag = "";

  while (num > 0) {
    var lastnum = num % 10;
    bag = bag + lastnum;
    num = Math.floor(num / 10);
  }
  console.log(Number(bag));
}

printReverseOfNumber(974452);

// changes
