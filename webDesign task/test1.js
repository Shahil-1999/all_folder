document.querySelector(".hamburger").addEventListener("click", () => {
  document.querySelector("nav ul").classList.toggle("show");

  
});





let slide_index = 0;
setInterval(() => {
  slide_index = slide_index + 1;
  display(slide_index);
  if (slide_index > 2) {
    slide_index = 0;
  }
}, 3000);


function display(n) {
  if (n == 1) {
    document.getElementById("los").style.display = "none";
    document.getElementById("chicago").style.display = "flex";
    document.getElementById("newYork").style.display = "none";
  } else if (n == 2) {
    document.getElementById("chicago").style.display = "none";
    document.getElementById("los").style.display = "none";
    document.getElementById("newYork").style.display = "flex";
  } else {
    document.getElementById("newYork").style.display = "none";
    document.getElementById("chicago").style.display = "none";
    document.getElementById("los").style.display = "flex";
  }
}
