/**
 * JavaScript file for the People page
 */

/* jshint esversion: 8 */

/**
 * This is the model class which provides access to the server REST API
 * @type {{}}
 */
class Model {
    async read() {
        let options = {
            method: "GET",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            }
        };
        // Call the REST endpoint and wait for data
        let response = await fetch("/api/people", options);
        let data = await response.json();
        return data;
    }

    async readOne(personId) {
        let options = {
            method: "GET",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            }
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${personId}`, options);
        let data = await response.json();
        return data;
    }

    async create(person) {
        let options = {
            method: "POST",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            },
            body: JSON.stringify(person)
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people`, options);
        let data = await response.json();
        return data;
    }

    async update(person) {
        let options = {
            method: "PUT",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            },
            body: JSON.stringify(person)
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${person.personId}`, options);
        let data = await response.json();
        return data;
    }

    async delete(personId) {
        let options = {
            method: "DELETE",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
                "accepts": "application/json"
            }
        };
        // Call the REST endpoint and wait for data
        let response = await fetch(`/api/people/${personId}`, options);
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
        this.table = document.querySelector(".people table");
        this.error = document.querySelector(".error");
        this.personId = document.getElementById("person_id");
        this.fname = document.getElementById("fname");
        this.lname = document.getElementById("lname");
        this.createButton = document.getElementById("create");
        this.updateButton = document.getElementById("update");
        this.deleteButton = document.getElementById("delete");
        this.resetButton = document.getElementById("reset");
    }

    reset() {
        this.personId.textContent = "";
        this.lname.value = "";
        this.fname.value = "";
        this.fname.focus();
    }

    updateEditor(person) {
        this.personId.textContent = person.person_id;
        this.lname.value = person.lname;
        this.fname.value = person.fname;
        this.fname.focus();
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

    buildTable(people) {
        let tbody,
            html = "";

        // Iterate over the people and build the table
        people.forEach((person) => {
            html += `
            <tr data-person_id="${person.person_id}" data-fname="${person.fname}" data-lname="${person.lname}">
                <td class="timestamp">${person.timestamp}</td>
                <td class="name">${person.fname} ${person.lname}</td>
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

    errorMessage(message) {
        this.error.innerHTML = message;
        this.error.classList.add("visible");
        this.error.classList.remove("hidden");
        setTimeout(() => {
            this.error.classList.add("hidden");
            this.error.classList.remove("visible");
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
            let urlPersonId = +document.getElementById("url_person_id").value,
                people = await this.model.read();

            this.view.buildTable(people);

            // Did we navigate here with a person selected?
            if (urlPersonId) {
                let person = await this.model.readOne(urlPersonId);
                this.view.updateEditor(person);
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
        document.querySelector("table tbody").addEventListener("dblclick", (evt) => {
            let target = evt.target,
                parent = target.parentElement;

            evt.preventDefault();

            // Is this the name td?
            if (target) {
                let personId = parent.getAttribute("data-person_id");

                window.location = `/people/${personId}/notes`;
            }
        });
        document.querySelector("table tbody").addEventListener("click", (evt) => {
            let target = evt.target.parentElement,
                person_id = target.getAttribute("data-person_id"),
                fname = target.getAttribute("data-fname"),
                lname = target.getAttribute("data-lname");

            this.view.updateEditor({
                person_id: person_id,
                fname: fname,
                lname: lname
            });
            this.view.setButtonState(this.view.EXISTING_NOTE);
        });
    }

    initializeCreateEvent() {
        document.getElementById("create").addEventListener("click", async (evt) => {
            let fname = document.getElementById("fname").value,
                lname = document.getElementById("lname").value;

            evt.preventDefault();
            try {
                await this.model.create({
                    fname: fname,
                    lname: lname
                });
                await this.initializeTable();
            } catch(err) {
                this.view.errorMessage(err);
            }
        });
    }

    initializeUpdateEvent() {
        document.getElementById("update").addEventListener("click", async (evt) => {
            let personId = +document.getElementById("person_id").textContent,
                fname = document.getElementById("fname").value,
                lname = document.getElementById("lname").value;

            evt.preventDefault();
            try {
                await this.model.update({
                    personId: personId,
                    fname: fname,
                    lname: lname
                });
                await this.initializeTable();
            } catch(err) {
                this.view.errorMessage(err);
            }
        });
    }

    initializeDeleteEvent() {
        document.getElementById("delete").addEventListener("click", async (evt) => {
            let personId = +document.getElementById("person_id").textContent;

            evt.preventDefault();
            try {
                await this.model.delete(personId);
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

// Create the MVC components
const model = new Model();
const view = new View();
const controller = new Controller(model, view);

// export the MVC components as the default
export default {
    model,
    view,
    controller
};
