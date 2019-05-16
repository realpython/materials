/*
 * JavaScript file for the application to demonstrate
 * using the API for creating, updating and deleting notes
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
    'use strict';

    // Return the API
    return {
        read_one: function (person_id, note_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}/notes/${note_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
        },
        read: function (person_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
        },
        create: function (person_id, note) {
            let ajax_options = {
                type: 'POST',
                url: `/api/people/${person_id}/notes`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(note)
            };
            return $.ajax(ajax_options);
        },
        update: function (person_id, note) {
            let ajax_options = {
                type: 'PUT',
                url: `/api/people/${person_id}/notes/${note.note_id}`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(note)
            };
            return $.ajax(ajax_options);
        },
        'delete': function (person_id, note_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `/api/people/${person_id}/notes/${note_id}`,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            return $.ajax(ajax_options);
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
        reset: function () {
            $note_id.text('');
            $note.val('').focus();
        },
        update_editor: function (note) {
            $note_id.text(note.note_id);
            $note.val(note.content).focus();
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
        build_table: function (person) {
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
        $url_person_id = $('#url_person_id'),
        $url_note_id = $('#url_note_id'),
        $note_id = $('#note_id'),
        $note = $('#note');

    // read the person data with notes
    setTimeout(function () {
        view.reset();
        model.read(parseInt($url_person_id.val()))
            .done(function (data) {
                view.build_table(data);
                view.update_editor(data);
                view.set_button_states(view.NEW_NOTE);
            })
            .fail(function (xhr, textStatus, errorThrown) {
                error_handler(xhr, textStatus, errorThrown);
            });

        if ($url_note_id.val() !== "") {
            model.read_one(parseInt($url_person_id.val()), parseInt($url_note_id.val()))
                .done(function (data) {
                    view.update_editor(data);
                    view.set_button_states(view.EXISTING_NOTE);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });
        }
    }, 100);

    // generic error handler
    function error_handler(xhr, textStatus, errorThrown) {
        let error_msg = `${textStatus}: ${errorThrown} - ${xhr.responseJSON.detail}`;

        view.error(error_msg);
        console.log(error_msg);
    }

    // initialize the button states
    view.set_button_states(view.NEW_NOTE);

    // Validate input
    function validate(note) {
        return note !== "";
    }

    // Create our event handlers
    $('#create').click(function (e) {
        let note = $note.val();

        e.preventDefault();

        if (validate(note)) {
            model.create(parseInt($('#url_person_id').val()), {
                content: note
            })
                .done(function (data) {
                    model.read(parseInt($('#url_person_id').val()))
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                    view.set_button_states(view.NEW_NOTE);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

        } else {
            alert('Problem with note input');
        }
    });

    $('#update').click(function (e) {
        let person_id = parseInt($url_person_id.val()),
            note_id = parseInt($note_id.text()),
            note = $note.val();

        e.preventDefault();

        if (validate(note)) {
            model.update(person_id, {
                note_id: note_id,
                content: note
            })
                .done(function (data) {
                    model.read(data.person.person_id)
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                    view.set_button_states(view.NEW_NOTE);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#delete').click(function (e) {
        let person_id = parseInt($url_person_id.val()),
            note_id = parseInt($note_id.text());

        e.preventDefault();

        if (validate('placeholder', lname)) {
            model.delete(person_id, note_id)
                .done(function (data) {
                    model.read(parseInt($('#url_person_id').val()))
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                    view.set_button_states(view.NEW_NOTE);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#reset').click(function () {
        view.reset();
        view.set_button_states(view.NEW_NOTE);
    })

    $('table').on('click', 'tbody tr', function (e) {
        let $target = $(e.target).parent(),
            note_id = $target.data('note_id'),
            content = $target.data('content');

        view.update_editor({
            note_id: note_id,
            content: content,
        });
        view.set_button_states(view.EXISTING_NOTE);
    });
}(ns.model, ns.view));


