/**
 * JavaScript file for the Notes page
 */

/* jshint esversion: 8 */

/**
 * This is the model class which provides access to the server REST API
 * @type {{}}
 */
class Model {
    async read(person_id) {
        let options = {
            method: "GET",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            }
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${person_id}`, options);
        let data = await response.json();
        return data;
    }
    async readOne(person_id, note_id) {
        let options = {
            method: "GET",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            }
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${person_id}/notes/${note_id}`, options);
        let data = await response.json();
        return data;
    }
    async create(person_id, note) {
        let options = {
            method: "POST",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            },
            body: JSON.stringify(note)
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${person_id}/notes`, options);
        let data = await response.json();
        return data;
    }
    async update(person_id, note) {
        let options = {
            method: "PUT",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            },
            body: JSON.stringify(note)
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${person_id}/notes/${note.note_id}`, options);
        let data = await response.json();
        return data;
    }
    async delete(person_id, note_id) {
        let options = {
            method: "DELETE",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            }
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${person_id}/notes/${note_id}`, options);
        return response;
    }
}


/**
 * This is the view class which provides access to the DOM
 */
class View {
    constructor() {
        this.NEW_NOTE = 0;
        this.EXISTING_NOTE = 1;
        this.table = document.querySelector(".notes table");
        this.error = document.querySelector(".error");
        this.person_id = document.getElementById("person_id");
        this.fname = document.getElementById("fname");
        this.lname = document.getElementById("lname");
        this.timestamp = document.getElementById("timestamp");
        this.note_id = document.getElementById("note_id");
        this.note = document.getElementById("note");
        this.createButton = document.getElementById("create");
        this.updateButton = document.getElementById("update");
        this.deleteButton = document.getElementById("delete");
        this.resetButton = document.getElementById("reset");
    }
    reset() {
        this.note_id.textContent = "";
        this.note.value = "";
        this.note.focus();
    }
    updateEditor(note) {
        this.note_id.textContent = note.note_id;
        this.note.value = note.content;
        this.note.focus();
    }
    setButtonState(state) {
        if (state === this.NEW_NOTE) {
            this.createButton.disabled = false;
            this.updateButton.disabled = true;
            this.deleteButton.disabled = true;
        } else if (state === this.EXISTING_NOTE) {
            this.createButton.disabled = true;
            this.updateButton.disabled = false;
            this.deleteButton.disabled = false;
        }
    }
    buildTable(person) {
        let tbody,
            html = "";

        // Update the person data
        this.person_id.textContent = person.person_id;
        this.fname.textContent = person.fname;
        this.lname.textContent = person.lname;
        this.timestamp.textContent = person.timestamp;

        // Iterate over the notes and build the table
        person.notes.forEach((note) => {
            html += `
            <tr data-note_id="${note.note_id}" data-content="${note.content}">
                <td class="timestamp">${note.timestamp}</td>
                <td class="content">${note.content}</td>
            </tr>`;
        });
        // Is there currently a tbody in the table?
        if (this.table.tBodies.length !== 0) {
            this.table.removeChild(this.table.getElementsByTagName("tbody")[0]);
        }
        // Update tbody with our new content
        tbody = this.table.createTBody();
        tbody.innerHTML = html;
    }
    errorMessage(error_msg) {
        let error = document.querySelector(".error");

        error.innerHTML = error_msg;
        error.classList.add("visible");
        error.classList.remove("hidden");
        setTimeout(() => {
            error.classList.add("hidden");
            error.classList.remove("visible");
        }, 2000);
    }
}


/**
 * This is the controller class for the user interaction
 */
class Controller {
    constructor(model, view) {
        this.model = model;
        this.view = view;

        this.initialize();
    }
    async initialize() {
        await this.initializeTable();
        this.initializeTableEvents();
        this.initializeCreateEvent();
        this.initializeUpdateEvent();
        this.initializeDeleteEvent();
        this.initializeResetEvent();
    }
    async initializeTable() {
        try {
            let url_person_id = parseInt(document.getElementById("url_person_id").value),
                url_note_id = parseInt(document.getElementById("url_note_id").value),
                person = await this.model.read(url_person_id);

            this.view.buildTable(person);

            // Did we navigate here with a note selected?
            if (url_note_id) {
                let note = await this.model.readOne(url_person_id, url_note_id);
                this.view.updateEditor(note);
                this.view.setButtonState(this.view.EXISTING_NOTE);

            // Otherwise, nope, so leave the editor blank
            } else {
                this.view.reset();
                this.view.setButtonState(this.view.NEW_NOTE);
            }
            this.initializeTableEvents();
        } catch (err) {
            this.view.errorMessage(err);
        }
    }
    initializeTableEvents() {
        document.querySelector("table tbody").addEventListener("click", (evt) => {
            let target = evt.target.parentElement,
                note_id = target.getAttribute("data-note_id"),
                content = target.getAttribute("data-content");

            this.view.updateEditor({
                note_id: note_id,
                content: content
            });
            this.view.setButtonState(this.view.EXISTING_NOTE);
        });
    }
    initializeCreateEvent() {
        document.getElementById("create").addEventListener("click", async (evt) => {
            let url_person_id = parseInt(document.getElementById("person_id").textContent),
                note = document.getElementById("note").value;

            evt.preventDefault();
            try {
                await this.model.create(url_person_id, {
                    content: note
                });
                await this.initializeTable();
            } catch(err) {
                this.view.errorMessage(err);
            }
        });
    }
    initializeUpdateEvent() {
        document.getElementById("update").addEventListener("click", async (evt) => {
            let person_id = parseInt(document.getElementById("person_id").textContent),
                note_id = parseInt(document.getElementById("note_id").textContent),
                note = document.getElementById("note").value;

            evt.preventDefault();
            try {
                await this.model.update(person_id, {
                    person_id: person_id,
                    note_id: note_id,
                    content: note
                });
                await this.initializeTable();
            } catch(err) {
                this.view.errorMessage(err);
            }
        });
    }
    initializeDeleteEvent() {
        document.getElementById("delete").addEventListener("click", async (evt) => {
            let person_id = parseInt(document.getElementById("person_id").textContent),
                note_id = parseInt(document.getElementById("note_id").textContent);

            evt.preventDefault();
            try {
                await this.model.delete(person_id, note_id);
                await this.initializeTable();
            } catch(err) {
                this.view.errorMessage(err);
            }
        });
    }
    initializeResetEvent() {
        document.getElementById("reset").addEventListener("click", async (evt) => {
            evt.preventDefault();
            this.view.reset();
            this.view.setButtonState(this.view.NEW_NOTE);
        });
    }
}

/**
 * Create the namespace container for the model, view and controller
 */
const ns = (function() {
    "use strict";

    const model = new Model();
    const view = new View();
    const controller = new Controller(model, view);
    return {
        model: model,
        view: view,
        controller: controller
    }
}());


