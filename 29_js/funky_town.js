/*Team MAD - Maryann Foley,Anton Danylenko
SoftDev1 pd8
K28 -- Sequential Progression
2018-12-18
*/

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
console.log(b0val)
var b1 = document.getElementById("b1");
var b1val0 = document.getElementById("b1val0").value;
var b1val1 = document.getElementById("b1val1").value;
var b2 = document.getElementById("b2");
b0.addEventListener('click', function(){

  var b0val = document.getElementById("b0val").value;
  console.log(b0val);
  if (b0val == undefined ||  b0val == "" || b0val == null || b0val<0){
    p0.innerHTML="Bad input";
  } else {
    console.log(fibonacci(b0val));
    p0.innerHTML=fibonacci(b0val);
  }
});
b1.addEventListener('click', function(){
  var b1val0 = document.getElementById("b1val0").value;
  var b1val1 = document.getElementById("b1val1").value;
  if (b1val1 == undefined || b1val1 == "" || b1val0 == "" || b1val0 == undefined || b1val0 == null || b1val1 == null){
    console.log("gcd(15, 255) = " + gcd(15, 255));
    p1.innerHTML="Bad input";
  }
  else {
    console.log("gcd("+b1val0+", "+b1val1+")" + gcd(b1val0, b1val1));
    p1.innerHTML=gcd(b1val0, b1val1);
  }
});
b2.addEventListener('click', function(){
  p2.innerHTML=randomStudent();
});
