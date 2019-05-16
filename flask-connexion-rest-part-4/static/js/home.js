/**
 * JavaScript file for the Home page
 */

"use strict";


/**
 * This is the model class which provides access to the server REST API
 * @type {{}}
 */
class Model {
    options;
    constructor () {
        this.options = {
            method: "GET",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            }
        };
    }

    read() {
        return fetch("/api/notes", this.options)
    }
}


/**
 * This is the view class which provides access to the DOM
 */
class View {
    constructor() {
        this._table = document.querySelector(".blog table");
        console.log("hello");
    }

    build_table(data) {
        let tbody = this._table.createTBody();
        tbody.innerHTML = `
            <tr>
                <td>Hello</td>
                <td>there</td>
            </tr>
            <tr>
                <td>Doug</td>
                <td>Farrell</td>
            </tr>
        `;
    }
    error(error_msg) {

    }
}


/**
 * This is the controller which provides for the user interaction
 */
class Controller {

    initialize(model, view) {
        this.model = model;
        this.view = view;

        this.view.build_table();
    }
}

/**
 * This class defines our namespace container
 * @type {{}}
 */
class NameSpace{
    constructor(model, view, controller) {
        this._model = model;
        this._view = view;
        this._controller = controller;
        this._controller.initialize(this._model, this._view);
    }
};

/**
 * Create the namespace object
 * @type {{}}
 */
const nameSpace = new NameSpace(new Model(), new View(), new Controller());
debugger;





// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
    'use strict';

    // Return the API
    return {
        'read': function () {
            let ajax_options = {
                type: 'GET',
                url: '/api/notes',
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
        }
    };
}());


// Create the view instance
ns.view = (function () {
    'use strict';

    var $table = $(".blog table");

    // Return the API
    return {
        build_table: function (data) {
            let source = $('#blog-table-template').html(),
                template = Handlebars.compile(source),
                html;

            // Create the HTML from the template and notes
            html = template({notes: data});

            // Append the rows to the table tbody
            $table.append(html);
        },
        error: function (error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function () {
                $('.error').fadeOut();
            }, 2000)
        }
    };
}());


// Create the controller instance
ns.controller = (function (m, v) {
    'use strict';

    let model = m,
        view = v;

    // Get the note data from the model after the controller is done initializing
    setTimeout(function () {

        // Attach event handlers to the promise returned by model.read()
        model.read()
            .done(function (data) {
                view.build_table(data);
            })
            .fail(function (xhr, textStatus, errorThrown) {
                error_handler(xhr, textStatus, errorThrown);
            });
    }, 100);

    // generic error handler
    function error_handler(xhr, textStatus, errorThrown) {
        let error_msg = `${textStatus}: ${errorThrown} - ${xhr.responseJSON.detail}`;

        view.error(error_msg);
        console.log(error_msg);
    }

    // handle application events
    $('table').on('dblclick', 'tbody td.name', function (e) {
        let $target = $(e.target).parent(),
            person_id = $target.data('person_id');

        window.location = `/people/${person_id}`;

    });

    $('table').on('dblclick', 'tbody td.content', function (e) {
        let $target = $(e.target).parent(),
            person_id = $target.data('person_id'),
            note_id = $target.data('note_id');

        window.location = `people/${person_id}/notes/${note_id}`;
    });
}(ns.model, ns.view));