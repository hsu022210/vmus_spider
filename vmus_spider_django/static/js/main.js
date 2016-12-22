function main() {

    setTimeout(function() {
//       window.location.href = $('.start').attr("href");
       window.location.href = $('.loading').attr("data-directTo");
      }, 400);

//    $('.loading').hide();
//
//    $('.start').click(function(){
//        $(this).hide();
//        $('.loading').show(100, function(){
//            location.href = $('.start').attr("href");
//        });
//    })

}

$(document).ready(main);