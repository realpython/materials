/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        read_one: function (person_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_read_one_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                });
        },
        read: function () {
            let ajax_options = {
                type: 'GET',
                url: '/api/people',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_read_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                });
        },
        create: function (person) {
            let ajax_options = {
                type: 'POST',
                url: '/api/people',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(person)
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_create_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                });
        },
        update: function (person) {
            let ajax_options = {
                type: 'PUT',
                url: `/api/people/${person.person_id}`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(person)
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_update_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                });
        },
        'delete': function (person_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `/api/people/${person_id}`,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_delete_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                });
        }
    };
}());

// Create the view instance
ns.view = (function () {
    'use strict';

    const NEW_NOTE = 0,
        EXISTING_NOTE = 1;

    let $person_id = $('#person_id'),
        $fname = $('#fname'),
        $lname = $('#lname'),
        $create = $('#create'),
        $update = $('#update'),
        $delete = $('#delete'),
        $reset = $('#reset');

    // return the API
    return {
        NEW_NOTE: NEW_NOTE,
        EXISTING_NOTE: EXISTING_NOTE,
        reset: function () {
            $person_id.text('');
            $lname.val('');
            $fname.val('').focus();
        },
        update_editor: function (person) {
            $person_id.text(person.person_id);
            $lname.val(person.lname);
            $fname.val(person.fname).focus();
        },
        set_button_states: function (state) {
            if (state === NEW_NOTE) {
                $create.prop('disabled', false);
                $update.prop('disabled', true);
                $delete.prop('disabled', true);
            } else if (state === EXISTING_NOTE) {
                $create.prop('disabled', true);
                $update.prop('disabled', false);
                $delete.prop('disabled', false);
            }
        },
        build_table: function (people) {
            let source = $('#people-table-template').html(),
                template = Handlebars.compile(source),
                html;

            // clear the table
            $('.people table > tbody').empty();

            // did we get a people array?
            if (people) {

                // Create the HTML from the template and people
                html = template({people: people})

                // Append the html to the table
                $('table').append(html);
            }
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

// Create the controller
ns.controller = (function (m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $url_person_id = $('#url_person_id'),
        $person_id = $('#person_id'),
        $fname = $('#fname'),
        $lname = $('#lname');

    // Get the data from the model after the controller is done initializing
    setTimeout(function () {
        view.reset();
        model.read();
        if ($url_person_id.val() !== "") {
            model.read_one(parseInt($url_person_id.val()));
        }
    }, 100)

    // initialize the button states
    view.set_button_states(view.NEW_NOTE);

    // Validate input
    function validate(fname, lname) {
        return fname !== "" && lname !== "";
    }

    // Create our event handlers
    $('#create').click(function (e) {
        let fname = $fname.val(),
            lname = $lname.val();

        e.preventDefault();

        if (validate(fname, lname)) {
            model.create({
                'fname': fname,
                'lname': lname,
            })
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function (e) {
        let person_id = parseInt($person_id.text()),
            fname = $fname.val(),
            lname = $lname.val();

        e.preventDefault();

        if (validate(fname, lname)) {
            model.update({
                person_id: person_id,
                fname: fname,
                lname: lname,
            })
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function (e) {
        let person_id = parseInt($person_id.text());

        e.preventDefault();

        if (validate('placeholder', lname)) {
            model.delete(person_id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function () {
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    })

    $('table').on('click', 'tbody tr', function (e) {
        let $target = $(e.target).parent(),
            person_id = $target.data('person_id'),
            fname = $target.data('fname'),
            lname = $target.data('lname');

        view.update_editor({
            person_id: person_id,
            fname: fname,
            lname: lname,
        });
        view.set_button_states(view.EXISTING_NOTE);
    });

    $('table').on('dblclick', 'tbody tr', function (e) {
        let $target = $(e.target),
            person_id = $target.parent().attr('data-person_id');

        window.location.href = `/people/${person_id}/notes`;

    });

    // Handle the model events
    $event_pump.on('model_read_one_success', function (e, data) {
        view.update_editor(data);
        view.set_button_states(view.EXISTING_NOTE);
    });

    $event_pump.on('model_read_success', function (e, data) {
        view.build_table(data);
    });

    $event_pump.on('model_create_success', function (e, data) {
        model.read();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_update_success', function (e, data) {
        model.read();
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_delete_success', function (e, data) {
        model.read();
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_error', function (e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    });
}(ns.model, ns.view));


