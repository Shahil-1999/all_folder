// console.log($);
$(document).ready(function () {
  // $('h1').on('click',function(){
  //     $(this).css('background-color','yellow')    //for adding single property

  // })

  // $('h1').on('click',function(){
  //     $(this).css({'background-color':'yellow',
  // 'color':'white'})    //for adding multiple property

  // })

  // $('button').on('click', function(){
  //     $('p').css({'background-color':'red',
  //     'color':'white',
  // 'font-size':'40px'})
  // })

  $("#hide").on("click", function () {
    // $('h1').hide
    // $('h1').hide('slow')   //Time include
    $("h1").hide(3000, function () {
      //After Hide alert fired
      alert("Hidden");
    });
  });

  $("#show").on("click", function () {
    // $('h1').show()
    // $('h1').show('slow')
    $("h1").show(3000, function () {
      alert("shown");
    });
  });
});
