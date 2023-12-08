// Print "hello world" five times

// for (var i = 1; i <= 5; i++) {
//   console.log("Hello world");
// }

// given a number "num" print 1 to given num in horizontal

function printHorzontal(num) {
  var bag = "";
  for (var i = 1; i <= num; i++) {
    bag = bag + i + " ";
  }
  console.log(bag);
}

printHorzontal(10);
