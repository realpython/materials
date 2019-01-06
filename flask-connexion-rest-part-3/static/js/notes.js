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
        'read': function(person_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}?get_notes=true`,
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
            $note.val(note.content);
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
            let rows = '';
            var notes = person.notes;

            // update the person data
            $person_id.text(person.person_id);
            $fname.text(person.fname);
            $lname.text(person.lname);
            $timestamp.text(person.timestamp);

            // clear the table
            $('.notes table > tbody').empty();

            // did we get a note array?
            if (notes) {
                for (let i=0, l=notes.length; i < l; i++) {
                    rows += `<tr data-note-id="${notes[i].note_id}">
                        <td class="content">${notes[i].content}</td>
                        <td class="timestamp">${notes[i].timestamp}</td>
                    </tr>`;
                }
                $('table > tbody').append(rows);
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
        person_id = window.location.pathname.split('/').slice(-1)[0],
        $note_id = $('#note_id'),
        $note = $('#note');

    // read the person data with notes
    model.read(person_id);

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
            model.create(person_id, {
                content: note
            });
        } else {
            alert('Problem with note input');
        }
    });

    $('#update').click(function(e) {
        let note_id = parseInt($note_id.text()),
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
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let note_id = parseInt($note_id.text());

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

    $('table > tbody').on('click', 'tr', function(e) {
        let $target = $(e.target),
            note_id,
            content;

        note_id = $target
            .parent()
            .attr('data-note-id');

        content = $target
            .parent()
            .find('td.content')
            .text();

        view.update_editor({
            note_id: note_id,
            content: content,
        });
        view.set_button_states(view.EXISTING_NOTE);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read(person_id);
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read(person_id);
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read(person_id);
        view.set_button_states(view.NEW_NOTE);
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));


