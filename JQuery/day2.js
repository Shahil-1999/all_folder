$(document).ready(function () {

  // $("#show").on("click", function () {
//   $("p").toggle(function () {

//   });
// });


  // $("#fadeIn").on("click", function () {
  //   $('#container').fadeIn();
  // });

  // $("#fadeOut").on("click", function () {
  //   $('#container').fadeOut();
  // });

  // $("#fadeToggle").on("click", function () {
  //   $('#container').fadeToggle();
  // });

  // $("#fadeTo").on("click", function () {
  //   $('#container').fadeTo(0,0.5);  //first parameter is time and second is opacity
  // });

  $("#show").on("click", function () {
      $('#container-down').slideDown();
    });

  $("#hide").on("click", function () {
    $('#container-down').slideUp();
  });
  $("#toggle").on("click", function () {
    $('#container-down').slideToggle();
  });


})


