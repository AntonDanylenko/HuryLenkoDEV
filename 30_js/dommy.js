var changeHeading = function(e){
  var h = document.getElementById("h");
  h.innerHTML = e;
  console.log("changeHeading "+ e);
}

var removeItem = function(e){
  e.remove();
}

var lis = document.getElementsByTagName("li");

console.log(lis);

for (var i=0; i<lis.length; i++){
  //var temp = document.createElement('li');
  //lis[i].setAttribute('val', i);
  lis[i].addEventListener('mouseover', function(){changeHeading("Item "+i)});
  lis[i].addEventListener('mouseout', function(){changeHeading("Hello World!")});
  lis[i].addEventListener('click', function(){removeItem(lis[i])});
}
