/*
 * JavaScript file for the application to demonstrate
 * using the API for creating, updating and deleting notes
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        read_one: function(person_id, note_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}/notes/${note_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_one_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        read: function(person_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(person_id, note) {
            let ajax_options = {
                type: 'POST',
                url: `/api/people/${person_id}/notes`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(note)
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(person_id, note) {
            let ajax_options = {
                type: 'PUT',
                url: `/api/people/${person_id}/notes/${note.note_id}`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(note)
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(person_id, note_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `/api/people/${person_id}/notes/${note_id}`,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    const NEW_NOTE = 0,
          EXISTING_NOTE = 1;

    let $person_id = $('#person_id'),
        $fname = $('#fname'),
        $lname = $('#lname'),
        $timestamp = $('#timestamp'),
        $note_id = $('#note_id'),
        $note = $('#note'),
        $create = $('#create'),
        $update = $('#update'),
        $delete = $('#delete'),
        $reset = $('#reset');

    // return the API
    return {
        NEW_NOTE: NEW_NOTE,
        EXISTING_NOTE: EXISTING_NOTE,
        reset: function() {
            $note_id.text('');
            $note.val('').focus();
        },
        update_editor: function(note) {
            $note_id.text(note.note_id);
            $note.val(note.content).focus();
        },
        set_button_states: function(state) {
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
        build_table: function(person) {
            let source = $('#notes-table-template').html(),
                template = Handlebars.compile(source),
                html;

            // update the person data
            $person_id.text(person.person_id);
            $fname.text(person.fname);
            $lname.text(person.lname);
            $timestamp.text(person.timestamp);

            // clear the table
            $('.notes table > tbody').empty();

            // did we get a note array?
            if (person.notes) {

                // Create the HTML from the template and notes
                html = template({notes: person.notes});

                // Append the html to the table
                $('table').append(html);
            }
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

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $url_person_id = $('#url_person_id'),
        $url_note_id = $('#url_note_id'),
        $note_id = $('#note_id'),
        $note = $('#note');

    // read the person data with notes
    setTimeout(function() {
        view.reset();
        model.read(parseInt($url_person_id.val()));
        if ($url_note_id.val() !== "") {
            model.read_one(parseInt($url_person_id.val()), parseInt($url_note_id.val()));
        }
    }, 100);

    // initialize the button states
    view.set_button_states(view.NEW_NOTE);

    // Validate input
    function validate(note) {
        return note !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let note = $note.val();

        e.preventDefault();

        if (validate(note)) {
            model.create(parseInt($('#url_person_id').val()), {
                content: note
            });
        } else {
            alert('Problem with note input');
        }
    });

    $('#update').click(function(e) {
        let person_id = parseInt($url_person_id.val()),
            note_id = parseInt($note_id.text()),
            note = $note.val();

        e.preventDefault();

        if (validate(note)) {
            model.update(person_id, {
                note_id: note_id,
                content: note
            })
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#delete').click(function(e) {
        let person_id = parseInt($url_person_id.val()),
            note_id = parseInt($note_id.text());

        e.preventDefault();

        if (validate('placeholder', lname)) {
            model.delete(person_id, note_id);
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    })

    $('table').on('click', 'tbody tr', function(e) {
        let $target = $(e.target).parent(),
            note_id = $target.data('note_id'),
            content = $target.data('content');

        view.update_editor({
            note_id: note_id,
            content: content,
        });
        view.set_button_states(view.EXISTING_NOTE);
    });

    // Handle the model events
    $event_pump.on('model_read_one_success', function(e, data) {
        view.update_editor(data);
        view.set_button_states(view.EXISTING_NOTE);
    });

    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read(parseInt($('#url_person_id').val()));
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read(data.person.person_id);
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read(parseInt($('#url_person_id').val()));
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));


