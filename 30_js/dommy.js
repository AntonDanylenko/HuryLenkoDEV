var changeHeading = function(e){
  //console.log(e);
  var h = document.getElementById("h");
  h.innerHTML = e;
  // console.log("changeHeading "+ e);
};

var removeItem = function(e){
  e.remove();
};

var lis = document.getElementsByTagName("li");

//console.log(lis);

for (var i=0; i<lis.length; i++){
  lis[i].setAttribute('val', i);
  lis[i].addEventListener('mouseover', function(){changeHeading("Item " + this.getAttribute("val"))});
  lis[i].addEventListener('mouseout', function(){changeHeading("Hello World!")});
  lis[i].addEventListener('click', function(){removeItem(this)});
};

/*for (var i=0; i<lis.length; i++){
  (function(){
    var b = i;
    lis[i].addEventListener('mouseover', function(){changeHeading("Item " + b)});
    lis[i].addEventListener('mouseout', function(){changeHeading("Hello World!")});
    lis[i].addEventListener('click', function(){removeItem(this)});
  })
}*/

var addItem = function(e){
  var list = document.getElementById("theList");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  list.appendChild(item);
  item.addEventListener('mouseover', function(){changeHeading("WORD")});
  item.addEventListener('mouseout', function(){changeHeading("Hello World!")});
  item.addEventListener('click', function(){removeItem(this)});
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  if (n<2){
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
};

var currentFibIndex = 0;

var addFib = function(e){
  console.log(e);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  item.innerHTML = fib(e);
  list.appendChild(item);
  currentFibIndex++;
};

var fib2 = function(n){
  var result = [0,1];
  for (var i = 2; i<=n; i++){
    result.push(result[i-2] + result[i-1]);
  }
  return result[n];
};

var addFib2 = function(e){
  console.log(e);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  item.innerHTML = fib2(e);
  list.appendChild(item);
  currentFibIndex++;
};

var fb = document.getElementById("fb");
fb.addEventListener("click", function(){addFib2(currentFibIndex)});
