function main() {

    setTimeout(function() {
       window.location.href = $('.loading').attr("data-directTo");
      }, 400);

}

$(document).ready(main);