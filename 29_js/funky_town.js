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
  return Math.floor(Math.random() * 3)
}
var randomStudent = () => {
  randIndex = randomNumber();
  return students[randIndex];
}

var b0 = document.getElementById("b0");
var b0val = document.getElementById("b0val").value;
var b1 = document.getElementById("b1");
var b1val0 = document.getElementById("b1val0").value;
var b1val1 = document.getElementById("b1val1").value;
var b2 = document.getElementById("b2");
b0.addEventListener('click', function(){
  console.log(b0val);
  if (b0val == null || b0val<0){
    console.log(fibonacci(5));
  }
  else {
    console.log(fibonacci(b0val));
  }
});
b1.addEventListener('click', function(){
  if (b1val0 == null || b1val1 == null){
    console.log("gcd(15, 255) = " + gcd(15, 255));
  }
  else {
    console.log("gcd("+b1val0+", "+b1val1+")" + gcd(b1val0, b1val1));
  }
});
b2.addEventListener('click', function(){
  console.log(randomStudent())
});
