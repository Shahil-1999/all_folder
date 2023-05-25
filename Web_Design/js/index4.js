//array methods/functios
// //withot parameter and without return type

// function myfunc() {

//     console.log("Hello all");
    
// }
// myfunc();

//with parameter
// function sum(num1, num2) {
//     let result = (num1 + num2);
//     console.log(result);
    
// }

//arguement
// sum(10, 20);


//task
// function calculate(x, y) {
//     let x2 = ((x**2) - (x*y) + (y**3));
   
//     console.log(x2);
    
// }

//arguement
// calculate(-2, 3);
// calculate(1, 2)


//with parameter with return

// function mul(x, y, z) {
//     let result = (x * y * z);
//     return result
// }
// console.log(mul(1, 2, 3));

// let r = mul(2,4,5);
// console.log(r); //prefer


//task

// function calculation(a, b) {
//     let result = (a * b);
//     return result  
// }

// let cal = calculation(3,2) + calculation(4,3) + calculation(1,4)
// console.log(cal)



// array function -> Push, pop, shift, unshift, splice

// push
// let arr = [1,5,6];
// let a = arr.push(55,99) //add value at the end
// console.log(arr, a);

//pop

// let arr1 = [1,5,6];
// let b = arr1.pop() //remove value at the end
// console.log(arr1, b);

//unshift

// let arr2 = [1,5,6];
// let c = arr2.unshift(55,99) //add value at the start
// console.log(arr2, c);

//shift

// let arr3 = [1,5,6];
// let d = arr3.shift() //remove value at the start
// console.log(arr3, d);


//splice (position, remove count, element to add)   splice do multiple element add, remove elemet at any position

// let arr4 = [1,5,6];
// let e = arr4.splice(1, 2, 9,10,45)
// console.log(arr4)


function display() {
    console.log("mouse hovered");
    
}

function display1() {
    console.log("mouse removed");
    
}