class People {
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
    this.createButton.addEventListener("click", this.onCreateClick.bind(this));
  }

  onCreateClick(event) {
    event.preventDefault();
    sendForm(this.form, "POST", "/api/people", this.addPersonToList);
    this.form.reset();
  }

  addPersonToList(rawData) {
    const data = JSON.parse(rawData);
    const peopleList = document.querySelector(".people-list");
    const template = document.querySelector(".person-card");
    let personCard = template.cloneNode(true);
    const noteList = personCard.querySelector(".note-list");
    const noteCards = personCard.querySelectorAll(".note-card");
    let personContent = personCard.querySelector(".person-content");
    let personFirstName = personContent.querySelector("[data-person-fname]");
    let personLastName = personContent.querySelector("[data-person-lname]");
    personFirstName.textContent = data.fname;
    personFirstName.setAttribute("data-person-fname", data.fname);
    personLastName.textContent = data.lname;
    personLastName.setAttribute("data-person-lname", data.lname);
    personCard.setAttribute("data-person-id", data.id);
    new PersonControl(personCard);
    new NoteCreateForm(noteList, data.id);
    noteCards.forEach((noteCard) => {
      noteCard.remove();
    });
    peopleList.appendChild(personCard);
  }
}

class PersonControl {
  constructor(personCard) {
    this.personCard = personCard;
    this.personElement = this.personCard.querySelector(".person-content");
    this.personControl = this.personCard.querySelector(".person-control");
    this.personID = this.personCard.getAttribute("data-person-id");
    this.form = this.personCard.querySelector("form");
    this.editButton = this.personCard.querySelector(".toggle-control");
    this.editButton.addEventListener("click", this.onEditClick.bind(this));
    this.cancel = this.personCard.querySelector("[data-action='cancel']");
    this.cancel.addEventListener("click", this.onCancelClick.bind(this));
    this.delete = this.personCard.querySelector("[data-action='delete']");
    this.delete.addEventListener("click", this.onDeleteClick.bind(this));
    this.update = this.personCard.querySelector("[data-action='update']");
    this.update.addEventListener("click", this.onUpdateClick.bind(this));
    this.fillControlForm();
  }

  onEditClick(event) {
    event.preventDefault();
    this.personCard.querySelector(".person-control-card").classList.add("editing");
    this.personElement.classList.add("hidden");
    this.editButton.classList.add("hidden");
    this.personControl.classList.remove("hidden");
  }

  onCancelClick(event) {
    event.preventDefault();
    this.personCard.querySelector(".person-control-card").classList.remove("editing");
    this.personElement.classList.remove("hidden");
    this.editButton.classList.remove("hidden");
    this.personControl.classList.add("hidden");
  }

  onDeleteClick(event) {
    event.preventDefault();
    const endpoint = "/api/people/" + this.personID;
    sendForm(this.form, "DELETE", endpoint, this.removePersonFromList);
  }

  removePersonFromList(data, inputForm) {
    let personCard = inputForm.closest(".person-card");
    if (window.confirm("Do you really want to remove this person?")) {
      personCard.remove();
    }
  }

  onUpdateClick(event) {
    event.preventDefault();
    const endpoint = "/api/people/" + this.personID;
    sendForm(this.form, "PUT", endpoint, this.updatePersonInList);
    this.cancel.click();
  }

  updatePersonInList(rawData, inputForm) {
    const data = JSON.parse(rawData);
    const personCard = inputForm.closest(".person-card");
    let personFirstName = personCard.querySelector("[data-person-fname]");
    let personLastName = personCard.querySelector("[data-person-lname]");
    personFirstName.textContent = data.fname;
    personFirstName.setAttribute("data-person-fname", data.fname);
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
    let fieldPersonID = this.form.querySelector("[name='id']");
    let fieldPersonFirstName = this.form.querySelector("[name='fname']");
    let fieldPersonLastName = this.form.querySelector("[name='lname']");
    fieldPersonID.setAttribute("value", this.personID);
    fieldPersonFirstName.setAttribute("value", personFirstName);
    fieldPersonLastName.setAttribute("value", personLastName);
  }
}

new People();
