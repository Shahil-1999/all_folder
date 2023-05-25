

window.onscroll = function () {
    scrollFunction()
    
};

function scrollFunction() {
    if(document.documentElement.scrollTop > 20){
        document.querySelector('#navbar').style.padding = ' 0px 100px'
        document.querySelector('#navbar').style.backgroundColor = ' black'


    }
    else{
        document.querySelector('#navbar').style.height = '3px 22px;'
        document.querySelector('#navbar').style.backgroundColor = ' none'

    }
    

    
    
}
