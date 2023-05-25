// alert("Press OK to Continue")
// console.log("This is normal Message")
// console.warn("This is Warning Message")
// console.error("This is Error Message")

// variables - named memory location.
// there are 3 types of variables (var,let,const)
// data types = string,boolean,number

// same variable name redeclaration is possible for var, but not for let and const.
// variable value cannot be possible in const, but possible in let 

var a = "have a Nice day";
let num = -10.32;
const bool = true;

console.log("String : "+a);
console.log("Number : "+num);
console.log("Boolean : "+bool);



let arr = [1,5,6,8];
let days = ["sun","mon","tues","wednes"]
console.log(days[3]+"day");



// object (multiple different type of value hold)
let person = {
    f_name : "Shahil",
    l_name : "chourasia",
    age: 23
}

console.log(person.f_name,person.age);