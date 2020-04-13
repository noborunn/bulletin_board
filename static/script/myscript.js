$(document).ready(function() {
    /*$('html, body').scrollTop(1000);*/

    /*$('.chat')[0].offset().top;*/
    var count = $('.chat').length;
    var height = $('.chat').eq(count-1).offset().top;
    $('html, body').scrollTop(height);

    /*$("#chat").slideUp();*/


});

/*$('.nav-item').click(function() {
    $('.nav-item').removeClass('active');
    $(this).addClass('active');
});*/