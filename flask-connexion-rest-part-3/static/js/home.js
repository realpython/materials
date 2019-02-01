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
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: '/api/notes',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                });
        }
    };
}());


// Create the view instance
ns.view = (function() {
    'use strict';

    var $table = $(".blog table");

    // Return the API
    return {
        build_table: function(data) {
            let source = $('#blog-table-template').html(),
                template = Handlebars.compile(source),
                html;

            // Create the HTML from the template and notes
            html = template({notes: data});

            // Append the rows to the table tbody
            $table.append(html);
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());


// Create the controller instance
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body');

    // Get the note data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100);

    // handle application events
    $('table').on('dblclick', 'tbody td.name', function(e) {
       let $target = $(e.target).parent(),
           person_id = $target.data('person_id');

       window.location = `/people/${person_id}`;

    });

    $('table').on('dblclick', 'tbody td.content', function(e) {
       let $target = $(e.target).parent(),
           person_id = $target.data('person_id'),
           note_id = $target.data('note_id');

       window.location = `people/${person_id}/notes/${note_id}`;
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })


}(ns.model, ns.view));