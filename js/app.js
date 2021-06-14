$(document).ready(function(){


    $('#menu').click(function(){
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });

    $(window).on('scroll load', function(){

        $('#menu').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        if($(window).scrollTop() > 68){
            $('header .header-2').addClass('header-active');
        }else{
            $('header .header-2').removeClass('header-active');
        }
    });

    $('.home-slider').owlCarousel({
        item: 1,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayTimeout:1000,
        loop: true,
    });

    $('.small-image img').click(function(){
        $(this).addClass('image-active').siblings().removeClass('image-active');

        let image = $(this).attr('src');
        $('.big-image img').attr('src', image)
    });


});