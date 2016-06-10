/*!
 * Start Bootstrap - Freelancer Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
var main = function() {
    $("#mainPic").width(0);
    $("#mainPic").css({ opacity: 0.1 });

    $("#mainPic").animate({
    width: 200,
    opacity:1.0
  }, 5000);
}

$(document).ready(main);
