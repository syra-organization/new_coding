var num = 1;

if (num < 10 && num >= 1) {
  console.log("given number is single digit");
} else if (num >= 10 && num < 100) {
  console.log("given number is two digit");
} else if (num >= 100 && num < 1000) {
  console.log("given number is 3 digit");
}

