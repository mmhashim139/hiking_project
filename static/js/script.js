  $(document).ready(function(){
    $('.sidenav').sidenav();
  });
    // Slider
  $(document).ready(function(){
    $('.slider').slider({
        indicators: false,
        height: 550,
        transition: 500,
        interval: 5000
        });
  });
  
      // Hikers profiles in home page 
      // initialize Owl Carousel , Added animation options

$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
    loop:true,
    margin:10,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true,
            autoplay: true,
            autoplayTimeout:5000,
            autoplayHoverPause:true,
            animateOut:true,
            loop:true
        },
        600:{
            items:2,
            nav:true,
            autoplay: true,
            autoplayTimeout:4000,
            autoplayHoverPause:true,
            animateOut:true,
            margin: 15,
            stagePadding: 25,
            loop:true
        },
        1000:{
            items:3,
            nav:true,
            autoplay: true,
            autoplayTimeout:3500,
            autoplayHoverPause:true,
            animateOut:true,
            margin: 15,
            stagePadding: 25,
            loop:true
        }
    }
  });
}); 


      // Hiker images gallery in hiker profile 
       
  $(document).ready(function(){
    $('.materialboxed').materialbox();
  });

  // Initialize Modal Form for sign up ..

  $(document).ready(function(){
    $('.modal').modal({
        opacity: 0.8
    });
  });


 // Initialize Materialize Parallax ..
    $(document).ready(function(){
    $('.parallax').parallax();
  });
        
 // Initialize Materialize Tool tipped ..
    $(document).ready(function(){
    $('.tooltipped').tooltip();
  });
        