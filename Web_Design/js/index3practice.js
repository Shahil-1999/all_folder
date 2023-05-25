// if else practice

// let deletePost = confirm("Do you really want to delete this post");
//         if(deletePost){
//             //code to delete the post
//             console.log("Your post has been deleted sucessfully");
//         }
//         else{
//             //code to cancel deletion of the post
//             console.log("Your post has not been deleted");
//         }



//DOM practice
let main = document.getElementById("main") //now we can access div which id is main
console.log(main);

let ul = document.getElementById("ul")
console.log(ul);

// let ul1 = document.getElementById("ul").innerHTML='<li>More</li>'    //if we want to take only one li
// console.log(ul1);

let containers = document.getElementsByClassName("container")
console.log(containers);
// console.log(containers[1]);  //we can access both containers by index number


let a = document.querySelectorAll("#ul>li")[0].innerHTML = "shahil";    //we can change specific 'li' by querrySelectorAll
console.log(a)
