//DSONG AND AD

var fibonacci = (n) => {
  if (n == 0)
    return 0;
  else if (n == 1)
    return 1;
  else
    return fibonacci(n - 2) + fibonacci(n - 1);
};

var gcd = (a, b) => {
  if (a > b) {
    for (x = b; x > 0; x--)
      if (((a % x) == 0) && ((b % x) == 0))
        return x;
  }
  else {
    for (x = a; x > 0; x--)
      if (((a % x) == 0) && ((b % x) == 0))
        return x;
  }
}

var students = ["bob", "sally", "john", "john2"];

var randomNumber = () => {
  return Math.random() * 3
}
var randomStudent = () => {
  randIndex = randomNumber();
  return students[randIndex];
}
