var changeHeading = function(e){
  //console.log(e);
  var h = document.getElementById("h");
  h.innerHTML = e;
  // console.log("changeHeading "+ e);
}

var removeItem = function(e){
  e.remove();
}

var lis = document.getElementsByTagName("li");

//console.log(lis);

for (var i=0; i<lis.length; i++){
  lis[i].setAttribute('val', i);
  lis[i].addEventListener('mouseover', function(){changeHeading("Item " + this.getAttribute("val"))});
  lis[i].addEventListener('mouseout', function(){changeHeading("Hello World!")});
  lis[i].addEventListener('click', function(){removeItem(this)});
}

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
  //console.log(list);
  var item = document.createElement("li");
  item.innerHtml = 'WORD';
  list.appendChild(item);
  //document.getElementById("theList").appendChild(item);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);
