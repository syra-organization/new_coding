// count the number of even numbers from 1 to given number

// example: let say the given number is 10
// the number of even numbers between 1 to 10 is 5

function countEvenNumbers(num) {
  var i = 1;
  var count = 0;
  while (i <= num) {
    if (i % 2 == 0) {
      count++;
    }
    i++;
  }
  console.log("given the even number", count);
}

countEvenNumbers(10);
