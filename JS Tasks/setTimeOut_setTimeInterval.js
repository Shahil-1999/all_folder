// Syntax SetTimeOut
//setTimeout(() => {
        
// }, timeout);

function display () {
    setTimeout(() => {
        console.log("Hello Js");
        document.getElementById('time').innerHTML = 'setTimeOut Active'
    }, 5000);
    
}


// function display1() {
//     setInterval(() => {
//         console.log("Set Interval activated");
//     }, 2000);
    
// }









function myTimer() {
  const time = new Date();
  document.getElementById("time").innerHTML = time.toLocaleTimeString();
}
const myInterval = setInterval(myTimer, 1000);


function display1() {
    setTimeout(() => {
        clearInterval(myInterval);  //stop timer  10 second after pressing click meee
    }, 10000);
    
  }
