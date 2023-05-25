const myForm = document.getElementById('form');
const fName = document.getElementById('name')
const error1 = document.getElementById('error1')
const error2 = document.getElementById('error2')
const error3 = document.getElementById('error3')
const error4 = document.getElementById('error4')

// CallBack functuion syntax
/*
let dis = () => {
    consol.log("Hello")
}
 */

fName.addEventListener('input',(event) => {
    // console.log(event.target.value);
    let fName_value = event.target.value;
    let name_reg = RegExp('^([A-Z]{1})([a-z]{2,19})$')

    if (fName_value === ""){

        error1.innerHTML = 'Required Feild'
        
    }
    else if(!name_reg.test(fName)){
        error1.innerHTML = 'First Letter of Your Name Must Be in Capital '

    }
    else{
        error1.innerHTML = ""
    }

})

mail.addEventListener('input',(event1) => {
    // console.log(event.target.value);
    let mail_value = event1.target.value;
    

    if (mail_value === ""){

        error2.innerHTML = 'Required Feild'
        
    }
    else if(mail_value.length <= 5){
        error2.innerHTML = 'Email Must Be More Than 5 Characters'

    }
    else{
        error2.innerHTML = ""
    }

})



password.addEventListener('input',(event2) => {
    // console.log(event.target.value);
    let password_value = event2.target.value;
    let validPass = RegExp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$')

    if (password_value === ""){

        error3.innerHTML = 'Required Feild'
        
    }
    else if(!validPass.test(password_value)){

        error3.innerHTML = "You must use one special character and your password shold be alpha numeric and use first Capital"
    }
    else if(password_value.length < 8){
        error3.innerHTML = 'Password Must Be More Than 8 Characters'

    }
    else{
        error3.innerHTML = ""
    }

})


number.addEventListener('input',(event3) => {
    // console.log(event.target.value);
    let number_value = event3.target.value;
    let num = RegExp('^[0-9]{10,}$')

    if (number_value === ""){

        error4.innerHTML = 'Required Feild'
        
    }
    else if(!num.test(number_value)){
        error4.innerHTML = 'Must be 10 digit with country code'

    }
    else{
        error4.innerHTML = ""
    }

})