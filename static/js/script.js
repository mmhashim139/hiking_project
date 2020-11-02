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