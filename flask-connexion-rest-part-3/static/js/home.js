/*
 * JavaScript file for the Home page
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {

    };
}());


// Create the view instance
ns.view = (function() {
    'use strict';

    // Return the API
    return {

    };
}());


// Create the controller instance
ns.controlle = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body');

    console.log('controller created');

    // Return the API
    return {

    };
}(ns.model, ns.view));