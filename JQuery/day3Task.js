$(document).ready(function () {
    $('#u_err').hide();
    $('#e_err').hide();
    $('#p_err').hide();
    $('#c_err').hide();
    // $('#contact_err').hide();   //Initially hide the Error part


    let user_no_err = true;
    let email_no_err = true;
    let pwd_no_err = true;
    let c_pwd_no_err = true;



    //Username Validation
    $('#inputFulltName').keyup(function(){
        username_check();
    });

    function username_check() {
        let user_value = $('#inputFulltName').val();    //input field value
        let reg_user = /^[A-Z]{1}[a-z]{1,4}$/;
        if (user_value.length == ""){
            $('#u_err').show();
            $('#u_err').html('Required field')
            $('#u_err').css('color','red')
            user_no_err = false;
            return false

        }
        else if(!reg_user.test(user_value))
        {
            $('#u_err').show();
            $('#u_err').html('Wrong Pattern')
            $('#u_err').css('color','red')
            user_no_err = false;
            return false

        
        }
        else{
            $('#u_err').hide();
            user_no_err = true;
            return true;
        }
    }


    //Password Validation
    $('#inputPassword4').keyup(function(){
        password_check();
    });
    function password_check() {
        let pwd_value = $('#inputPassword4').val();
        let reg_pwd = /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[a-z]).{8,15}$/;
        if (pwd_value.length == ""){
            $('#p_err').show();
            $('#p_err').html('Required field')
            $('#p_err').css('color','red')
            $('#p_err').focus();


            pwd_no_err = false;
            return false

        }
        else if(!reg_pwd.test(pwd_value))
        {
            $('#p_err').show();
            $('#p_err').html('Wrong Pattern,Atleast 1 Uppercase letter, 1 Smallcase letter, 1 Special charecter, 1 Number');
            $('#p_err').css('color','red')
            $('#p_err').focus();
            pwd_no_err = false;
            return false

        
        }
        else{
            $('#p_err').hide();
            pwd_no_err = true;
            return true;
        }
    }


    //Email validation



    $('#inputEmail4').keyup(function(){
        email_check();
    });
    function email_check() {
        let email_value = $('#inputEmail4').val();
        let reg_email = /^[a-zA-Z0-9.-_]{1,}@[a-zA-Z.-]{2,}[.]{1}[a-zA-Z]{2,}$/;
        if (email_value.length == ""){
            $('#e_err').show();
            $('#e_err').html('Required field')
            $('#e_err').css('color','red')
            $('#e_err').focus();


            email_no_err = false;
            return false

        }
        else if(!reg_email.test(email_value))
        {
            $('#e_err').show();
            $('#e_err').html("@ or '.' missing");
            $('#e_err').css('color','red')
            $('#e_err').focus();
            email_no_err = false;
            return false

        
        }
        else{
            $('#e_err').hide();
            email_no_err = true;
            return true;
        }
    }


    //Confirm password
    $('#inputC_Password4').keyup(function(){
        cnf_check();
    });

    function cnf_check() {


        let password=$('#inputPassword4').val();
        let confirm_password=$('#inputC_Password4').val();

        
        if(confirm_password===""){
            $('#c_err').show();
            $('#c_err').html('Required field')
            $('#c_err').css('color','red')
            $('#c_err').focus();


            c_pwd_no_err = false;
            return false
        }
        
        else if(confirm_password!=password){
            $('#c_err').show();
            $('#c_err').html('Password Not match')
            $('#c_err').css('color','red')
            $('#c_err').focus();
            c_pwd_no_err = false;
            return false
            
        }
        else(confirm_password===password)
        {
            $('#c_err').show();
            $('#c_err').html('password Matched Sucessfully')
            $('#c_err').css('color','green')
            $('#c_err').focus();
            c_pwd_no_err = true;
            return true
        }
        
    }


    $("#submit").click(function (){
       
        let res1 =  username_check()
        let res2 =  password_check()
        let res3 =  cnf_check()
        let res4 = email_check()

        if(res1 == true && res2 == true && res3 == true && res4 == true){

            console.log("true");
            return true;  
        }
        else{
            console.log("false");
            return false
        }

    })

})