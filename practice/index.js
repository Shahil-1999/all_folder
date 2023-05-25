
// $(document).ready(function(){
//     let u_no_err = true;
//     let p_no_err = true;

    
    

//     function user_check(){
//         let u_val = $("#text").val();
//         if(u_val.length == ""){
//             // alert("User Name is missing");
//             u_no_err = false;
//             return u_no_err
//         }
//         else{
//             u_no_err = true;
//             return u_no_err
//         }

//     }

//     function p_check(){
//         let p_val = $("#pasword").val();
//         if(p_val.length == ""){
//             // alert("password is missing");
//             p_no_err = false;
//             return p_no_err
//         }
//         else{
//             p_no_err = true;
//             return p_no_err
//         }

//     }

//     $("#btn").click(function(){
//         const user = user_check();
//         const pass = p_check();
        
//         if(user==true && pass==true){
//             alert("Login sucessfull")
//         } else if(user == false && pass == false){
//             alert("Both username and password is missing")
//         } else if(user==true && pass == false){
//             alert("password is missing");
//         }
//         else if(user==false && pass == true){
//         alert("username is missing");

//     }
//     })
    
// })



$(document).ready(function(){
    let u_no_err = true;
    let p_no_err =true;

    function user_check(){
        let user_val = $("#text").val();
        if(user_val.length == ""){
            alert("username is missing")
            u_no_err = false;
            return u_no_err
        }
        else{
            u_no_err =true;
            return u_no_err
        }
    }

    function pwd_check(){
        let pwd_val = $("#pasword").val();
        if(pwd_val.length == ""){
            alert("password is missing")
            p_no_err = false;
            return p_no_err
        }
        else{
            p_no_err =true;
            return p_no_err
        }
    }

    $("#btn").click(function(){
        const user = user_check();
        const pwd = pwd_check();
        if(user==true && pwd == true){
            alert("login Sucess")
        }
    })
})