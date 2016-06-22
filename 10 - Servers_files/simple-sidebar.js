// $("#menu-toggle").click(function(e) {
//   e.preventDefault();
//   $("#wrapper").toggleClass("toggled");
// });
// $("#menu-toggle-2").click(function(e) {
//   e.preventDefault();
//   $("#wrapper").toggleClass("toggled-2");
//   $('#menu ul').hide();
// });

function initMenu() {
  var onElement = null;

  // $('#menu > li > a').each( function(i, elem) {
  //   var segment = elem.href.replace(/\/$/, '').split("/").reverse()[0];
  //   if(window.location.href.indexOf(segment) != -1) {
  //     $(elem).parents("li").removeClass("closed").addClass('opened');
  //     // keep it open
  //   } else {
  //   //   $(elem).parents("li").addClass('closed');
  //     // $(elem).next("ul").hide();
  //   }
  // })

  // $('#menu > li > a').click(function() {
  //   // var checkElement = $(this).next();
  //   // if((checkElement.is('ul')) && (checkElement.is(':visible')) && checkElement.find('a')[0]) {
  //   //   // onElement = null;
  //   //   setTimeout( function() {
  //   //     $(checkElement).parents("li").addClass('closed');
  //   //     // if(onElement !== checkElement[0])
  //   //       // $(checkElement).slideUp('normal');
  //   //   }, 0);
  //   //   return false;
  //   // }
  // });

  $('#menu > li.expandable > a').click(
    function() {
      $(this).parents("li").toggleClass("closed");
      // var checkElement = $(this).next();
      // var li = $(this).parents("li");
      // // onElement = checkElement[0];
      // if(li.hasClass("closed")) {
      //   $('#menu ul:visible').slideUp('normal');
      //   $(checkElement).parents("li").removeClass('closed');
      //   // checkElement.slideDown('normal');
      //   return false;
      //   }
      return false;
  });
}
$(document).ready(function() {initMenu();});
