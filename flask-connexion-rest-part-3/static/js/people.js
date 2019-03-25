/*
 * JavaScript file for the application to demonstrate
 * using the API for the People SPA
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
    'use strict';

    // Return the API
    return {
        read_one: function (person_id) {
            let ajax_options = {
                type: 'GET',
                url: `/api/people/${person_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
        },
        read: function () {
            let ajax_options = {
                type: 'GET',
                url: '/api/people',
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
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
            return $.ajax(ajax_options);
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
            return $.ajax(ajax_options);
        },
        'delete': function (person_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `/api/people/${person_id}`,
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
        set_button_state: function (state) {
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
        $url_person_id = $('#url_person_id'),
        $person_id = $('#person_id'),
        $fname = $('#fname'),
        $lname = $('#lname');

    // Get the data from the model after the controller is done initializing
    setTimeout(function () {
        view.reset();
        model.read()
            .done(function(data) {
                view.build_table(data);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                error_handler(xhr, textStatus, errorThrown);
            })

        if ($url_person_id.val() !== "") {
            model.read_one(parseInt($url_person_id.val()))
                .done(function(data) {
                    view.update_editor(data);
                    view.set_button_state(view.EXISTING_NOTE);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });
        }
    }, 100)

    // generic error handler
    function error_handler(xhr, textStatus, errorThrown) {
        let error_msg = `${textStatus}: ${errorThrown} - ${xhr.responseJSON.detail}`;

        view.error(error_msg);
        console.log(error_msg);
    }
    // initialize the button states
    view.set_button_state(view.NEW_NOTE);

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
                .done(function(data) {
                    model.read()
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.set_button_state(view.NEW_NOTE);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

            view.reset();

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
                .done(function(data) {
                    model.read()
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                    view.set_button_state(view.NEW_NOTE);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
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
                .done(function(data) {
                    model.read()
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                    view.set_button_state(view.NEW_NOTE);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#reset').click(function () {
        view.reset();
        view.set_button_state(view.NEW_NOTE);
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
        view.set_button_state(view.EXISTING_NOTE);
    });

    $('table').on('dblclick', 'tbody tr', function (e) {
        let $target = $(e.target),
            person_id = $target.parent().attr('data-person_id');

        window.location.href = `/people/${person_id}/notes`;

    });
}(ns.model, ns.view));


