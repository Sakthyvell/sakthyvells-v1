$(document).ready(function(){
    
    $('.nav-link, .more').click(function(){
        $('html, body').animate({
            scrollTop: $( $(this).attr('href') ).offset().top - 50
        }, 1000);
        return false;
    });
});

