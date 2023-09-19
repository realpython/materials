/*
 * Javascript to run the app
 */

$(document).ready(function() {

    let base_path = $(location)
        .attr("pathname")
        .toLowerCase()
        .split("/")[1];
    
    // clear default active link
    $(".navbar-nav a.active")
        .removeClass("active");

    // set new active link based on location
    // if (base_path === "albums")
    //     $(".navbar-nav a[href$='/albums']")
    //         .addClass("active");
    $(`.navbar-nav a[href$='/${base_path}']`)
        .addClass("active");

});

