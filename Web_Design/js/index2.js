document.getElementById("firstDiv").innerHTML='<h2>First Div</h2>'
document.getElementById("secondDiv").innerHTML=`<p> lorem ipsum </>
                                                <h1>hello</h1>` // back ticks receive multiple html elements.




//Alert in JS dosent return anything(give alert to user when you have to only tell the user that this happened like subscription has been expired and then only click "okay" they won't have any other option)
        // alert("Your Subscription has been Expired")

        // let a = prompt("What is your name?")   //First arguement is message  any message you want to display and second you give is default arguement.
        // console.log(a) 


        //Confirm is used when u deleting a file or u doing something in which u have to give warning to the user.(for double checking we use confirm)
        // let deletePost = confirm("Do you really want to delete this post");



                                        
// Mathematical Operators

// let num1 = prompt("Enter First Number: ");
// let num2 = prompt("Enter Second Number: ");


// let sum = 6 + 3;
// let sub = num1 - num2;
// let mul = num1 * num2;
// let div = num1 / num2;
// let rem = num1 % num2;
// let pow = num1 ** num2;

// console.log(num1, num2, '\n', sub, mul, div, rem, pow);
// console.log("Sum of two number is : ", sum);



// Conditational Statements
// >,<,>=,<=,!=,==


// Syntax

// if (condition) {
//     statements;
// }
// else{
//     statements;
// }



// Syntax of nested if else

// if (condition) {
//     statements;
// }
// else if(Condition) {
//     statements;

// }
// else{
//     statements;
// }

// example to check number is positive or not

// let a = 10;

// if (a == 0) {
//     console.log(a, " is not positive or negative");
// }
// else if(a > 0) {
//     console.log(a, " is positive");

// }
// else{
//     console.log(a, " is negative");
// }



// task

// age verification

// let b = 18;
// if(b >= 18) {
//     console.log("Eligible to vote");

// }
// else{
//     console.log("Not eligible to vote");
// }


// age verification using prompt

// let age = prompt("Enter Your Age: ");
// if(age >= 18) {
//     console.log("Eligible to vote");
// }
// else{
//     console.log("Not eligible to vote");
// }


// ternary operator
// (condition) ? true statements : false statements

// let age = prompt("Enter age");
// (age >= 18) ? console.log("you are eligible to vote") : console.log("You are not eligible to vote");;


// switch case

// let num = prompt("Enter number b/n 1 - 4")
// switch (num) {
//     case '1': console.log("sunday");
        
//         break;
//     case '2': console.log("monday");
        
//         break;
//     case '3': console.log("tuesday");
        
//         break;
//     case '4': console.log("wednesday");
        
//         break;


//     default: console.error("enter valid number");
//         break;
// }



// function
function greet() {
    console.log("Good Night");
    
}
greet();
greet();