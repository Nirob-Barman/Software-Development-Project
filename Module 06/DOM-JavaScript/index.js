// alert("Hello World!");

// console.log("Hello World!"); // displays in the browser console

// document.getElementsByTagName("h1")
// console.log(document.getElementsByTagName("h1"));

var h1 = document.getElementsByTagName("h1");
// console.log(h1);

var title = document.getElementById("title");
// console.log(title);

var child = document.getElementsByClassName("child");
// console.log(child);
// console.log(child[0]);
// console.log(child[1]);

// title.style.color = "red";
var title = (document.getElementById("title").style.color = "blue");
document.getElementById("title").style.removeProperty("color");

var img = document.getElementById("img");
// img.src = "https://picsum.photos/200";
// console.log(img.getAttribute("src"));
img.setAttribute("alt", "image");
// console.log(img.getAttribute("alt"));

img.classList.add("testClass");
// console.log(img)

var hero = document.getElementById("hero");
// console.log(hero);
// console.log(hero.innerHTML);
// console.log(hero.innerText);
// console.log(hero.textContent);

var input = document.getElementById("input");
// console.log(input);
// console.log(input.value);
var input = document.getElementById("input").value;
// console.log(input);
// console.log(typeof input);

// var parent = document.getElementById("parent");
// console.log(parent);
// console.log(parent.children);
// console.log(parent.children[0]);
// console.log(parent.children[1]);
// console.log(parent.children[2]);
var parent = document.getElementById("parent").innerHTML;
// console.log(parent);

var testDiv = document.getElementsByClassName("test");
// console.log(testDiv);
// console.log(testDiv[0]);
// console.log(testDiv[0].childNodes);
// console.log(testDiv[0].childNodes[1]);
// console.log(testDiv[0].childNodes[1].parentNode);
// console.log(testDiv[0].childNodes[1].parentNode.parentNode);
// console.log(testDiv[0].childNodes[1].parentNode.parentNode.parentNode);
// console.log(testDiv[0].childNodes[1].parentNode.parentNode.parentNode.parentNode);
// console.log(testDiv[0].childNodes[1].parentNode.parentNode.parentNode.parentNode.parentNode);
// console.log(testDiv[0].childNodes[1].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode);

// console.log(testDiv[0].children);

var p = document.createElement("p");
p.innerText = "New World";
console.log(p);

var newDiv = document.getElementById("newDiv");
newDiv.appendChild(p);

function createE1() {
  var p = document.createElement("p");
  p.innerText = "New World";
  newDiv.appendChild(p);
}
createE1();
// createE1();
// createE1();

document.getElementById("submit-btn").addEventListener("click", function (e) {
  //   console.log("Yess Boss");
  //   createE1();
  var inputValue = document.getElementById("input").value;
  console.log(inputValue);
  //   var p = document.createElement("p");
  //   p.innerText = inputValue;
  //   newDiv.appendChild(p);
});

document.getElementById("input").addEventListener("blur", function (e) {
  //   console.log("Blur");
  //   console.log(e);
  //   console.log(e.target);
  //   console.log(e.target.value);
});

document.getElementById("input").addEventListener("blur", inputChange);
function inputChange(e) {
  // console.log("Blur");
  //   console.log(e);
  //   console.log(e.target);
  //   console.log(e.target.value);
}

// onBlue event
// document.getElementById("input").addEventListener("blur", inputChange);
function inputChange(e) {
  console.log("Blur");
  //   console.log(e);
  //   console.log(e.target);
  //   console.log(e.target.value);
}

function clickHandler(e) {
  //   console.log("Yess Boss");
  //   createE1();
  var inputValue = document.getElementById("clickInput").value;
  console.log(inputValue);
  //   var p = document.createElement("p");
  //   p.innerText = inputValue;
  //   newDiv.appendChild(p);
}
