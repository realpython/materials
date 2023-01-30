import { sendForm } from "./request.js";
import { NoteCreateForm } from "./notes.js";

export class People {
  constructor() {
    this.allPeopleCards = document.querySelectorAll(".person-card");
    this.activateCreateForm();
    this.activateAllControls();
  }

  activateCreateForm() {
    const peopleForm = document.querySelector(".person-create-card form");
    new CreatePersonForm(peopleForm);
  }

  activateAllControls() {
    this.allPeopleCards.forEach((personCard) => {
      new PersonControl(personCard);
    });
  }
}

class CreatePersonForm {
  constructor(el) {
    this.form = el;
    this.createButton = el.querySelector("button[data-action='create']");
    this.createButton.addEventListener(
      "click",
      this.handleCreateClick.bind(this)
    );
  }

  handleCreateClick(event) {
    event.preventDefault();
    sendForm(this.form, "POST", "/api/people", this.addPersonToList);
    this.form.reset();
  }

  addPersonToList(rawData) {
    const data = JSON.parse(rawData);

    const personCard = document.querySelector(".person-card").cloneNode(true);
    const personContent = personCard.querySelector(".person-content");

    const personFirstName = personContent.querySelector("[data-person-fname]");
    personFirstName.textContent = data.fname;
    personFirstName.setAttribute("data-person-fname", data.fname);

    const personLastName = personContent.querySelector("[data-person-lname]");
    personLastName.textContent = data.lname;
    personLastName.setAttribute("data-person-lname", data.lname);

    personCard.setAttribute("data-person-id", data.id);
    new PersonControl(personCard);
    new NoteCreateForm(personCard.querySelector(".note-list"), data.id);
    personCard
      .querySelectorAll(".note-card")
      .forEach((noteCard) => noteCard.remove());
    document.querySelector(".people-list").appendChild(personCard);
  }
}

class PersonControl {
  constructor(personCard) {
    this.personCard = personCard;
    this.personElement = this.personCard.querySelector(".person-content");
    this.personControl = this.personCard.querySelector(".person-control");
    this.personID = this.personCard.getAttribute("data-person-id");
    this.form = this.personCard.querySelector("form");

    this.editBtn = this.personCard.querySelector(".toggle-control");
    this.editBtn.addEventListener("click", this.handleEditClick.bind(this));
    this.cancelBtn = this.personCard.querySelector("[data-action='cancel']");
    this.cancelBtn.addEventListener(
      "click",
      this.handleCancelClick.bind(this)
    );
    this.deleteBtn = this.personCard.querySelector("[data-action='delete']");
    this.deleteBtn.addEventListener(
      "click",
      this.handleDeleteClick.bind(this)
    );
    this.updateBtn = this.personCard.querySelector("[data-action='update']");
    this.updateBtn.addEventListener(
      "click",
      this.handleUpdateClick.bind(this)
    );

    this.fillControlForm();
  }

  handleEditClick(event) {
    event.preventDefault();
    this.personCard
      .querySelector(".person-control-card")
      .classList.add("editing");
    this.personElement.classList.add("hidden");
    this.editBtn.classList.add("hidden");
    this.personControl.classList.remove("hidden");
  }

  handleCancelClick(event) {
    event.preventDefault();
    this.personCard
      .querySelector(".person-control-card")
      .classList.remove("editing");
    this.personElement.classList.remove("hidden");
    this.editBtn.classList.remove("hidden");
    this.personControl.classList.add("hidden");
  }

  handleDeleteClick(event) {
    event.preventDefault();
    const endpoint = "/api/people/" + this.personID;
    sendForm(this.form, "DELETE", endpoint, (data, inputForm) => {
      let personCard = inputForm.closest(".person-card");
      if (window.confirm("Do you really want to remove this person?")) {
        personCard.remove();
      }
    });
  }

  handleUpdateClick(event) {
    event.preventDefault();
    const endpoint = "/api/people/" + this.personID;
    sendForm(this.form, "PUT", endpoint, this.updatePersonInList);
    this.cancelBtn.click();
  }

  updatePersonInList(rawData, inputForm) {
    const data = JSON.parse(rawData);
    const personCard = inputForm.closest(".person-card");

    const personFirstName = personCard.querySelector("[data-person-fname]");
    personFirstName.textContent = data.fname;
    personFirstName.setAttribute("data-person-fname", data.fname);

    const personLastName = personCard.querySelector("[data-person-lname]");
    personLastName.textContent = data.lname;
    personLastName.setAttribute("data-person-lname", data.lname);
  }

  fillControlForm() {
    const personFirstName = this.personElement.querySelector(
      "[data-person-fname]"
    ).textContent;
    const personLastName = this.personElement.querySelector(
      "[data-person-lname]"
    ).textContent;
    this.form
      .querySelector("[name='id']")
      .setAttribute("value", this.personID);
    this.form
      .querySelector("[name='fname']")
      .setAttribute("value", personFirstName);
    this.form
      .querySelector("[name='lname']")
      .setAttribute("value", personLastName);
  }
}
