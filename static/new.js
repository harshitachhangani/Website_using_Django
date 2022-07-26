var i = 0;
var txt = 'Lets Explore Some Interesting space topics....';
var speed = 50;

function typeWriter() {
  if (i < txt.length) {
    var a = document.getElementById("demo")
    a.innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
    a.style.fontSize = "30px";
    a.style.fontFamily = "cursive";
    a.style.color = "dark-grey";
    a.style.fontWeight = "800";

  }
}



