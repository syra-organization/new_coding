// calculate the sum of n natural numbers

// example:- given num is 5
// 1 + 2 + 3 + 4 + 5 = 15

function calculateSumOfN(num) {
  var i = 1;
  var count= 0;
  while (i <= num) {
    count = i + count;

    i++;
  }
  console.log("given sum is num",+count);
}

calculateSumOfN(10);
