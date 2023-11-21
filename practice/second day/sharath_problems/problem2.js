// to test a number as how many digits
var n = 7895;
var num;
if (n < 100 && n >= 10) {
  console.log("it has two digits numbers");
} else if (n > 1000 && n >= 100) {
  console.log("it has three digits number");
} else if (n > 10000 && n >= 1000) {
  console.log("it has four digits number ");
} else {
  console.log("numbere is not between1 & 9999");
}
