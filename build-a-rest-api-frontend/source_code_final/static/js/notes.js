import { sendForm } from "./request.js";

export class Notes {
  constructor() {
    this.allNoteLists = document.querySelectorAll(".note-list");
    this.allNotes = document.querySelectorAll(".note-card");
    this.activateAllCreateForms();
    this.activateAllControls();
  }

  activateAllCreateForms() {
    this.allNoteLists.forEach((noteList) => {
      const personCard = noteList.closest(".person-card");
      const personID = personCard.getAttribute("data-person-id");
      new NoteCreateForm(noteList, personID);
    });
  }

  activateAllControls() {
    this.allNotes.forEach((noteCard) => {
      new NoteControl(noteCard);
    });
  }
}

export class NoteCreateForm {
  constructor(noteList, personID) {
    this.noteList = noteList;
    this.personID = personID;
    this.form = this.noteList.querySelector(".note-create-card form");
    this.createButton = this.form.querySelector(
      "button[data-action='create']"
    );
    this.createButton.addEventListener("click", this.onCreateClick.bind(this));
    this.connectPerson();
  }

  connectPerson() {
    let fieldPersonID = this.form.querySelector("input[name='person_id']");
    fieldPersonID.setAttribute("value", this.personID);
  }

  onCreateClick(event) {
    event.preventDefault();
    sendForm(this.form, "POST", "/api/notes", this.addNoteToList);
    this.form.reset();
  }

  addNoteToList(rawData) {
    const data = JSON.parse(rawData);
    const noteList = document
      .querySelector("[data-person-id= '" + data.person_id + "']")
      .querySelector(".note-list");
    const newNoteCard = document.querySelector(".note-card").cloneNode(true);
    newNoteCard.querySelector(".note-content").textContent = data.content;
    newNoteCard.setAttribute("data-note-id", data.id);
    new NoteControl(newNoteCard);
    noteList.insertBefore(newNoteCard, noteList.children[1]);
  }
}

class NoteControl {
  constructor(noteCard) {
    this.noteCard = noteCard;
    this.noteElement = this.noteCard.querySelector(".note-content");
    this.noteControl = this.noteCard.querySelector(".note-control");
    this.noteID = this.noteCard.getAttribute("data-note-id");
    this.form = this.noteCard.querySelector("form");

    this.editButton = this.noteCard.querySelector(".toggle-control");
    this.editButton.addEventListener("click", this.handleEditClick.bind(this));
    this.cancel = this.noteCard.querySelector("[data-action='cancel']");
    this.cancel.addEventListener("click", this.handleCancelClick.bind(this));
    this.delete = this.noteCard.querySelector("[data-action='delete']");
    this.delete.addEventListener("click", this.handleDeleteClick.bind(this));
    this.update = this.noteCard.querySelector("[data-action='update']");
    this.update.addEventListener("click", this.handleUpdateClick.bind(this));

    this.fillControlForm();
  }

  handleEditClick(event) {
    event.preventDefault();
    this.noteCard.classList.add("editing");
    this.noteElement.classList.add("hidden");
    this.editButton.classList.add("hidden");
    this.noteControl.classList.remove("hidden");
  }

  handleCancelClick(event) {
    event.preventDefault();
    this.noteCard.classList.remove("editing");
    this.noteElement.classList.remove("hidden");
    this.editButton.classList.remove("hidden");
    this.noteControl.classList.add("hidden");
  }

  handleDeleteClick(event) {
    event.preventDefault();
    const endpoint = "/api/notes/" + this.noteID;
    sendForm(this.form, "DELETE", endpoint, this.removeNoteFromList);
  }

  removeNoteFromList(data, inputForm) {
    const noteCard = inputForm.closest(".note-card");
    if (window.confirm("Do you really want to remove this note?")) {
      noteCard.remove();
    }
  }

  handleUpdateClick(event) {
    event.preventDefault();
    const endpoint = "/api/notes/" + this.noteID;
    sendForm(this.form, "PUT", endpoint, this.updateNoteInList);
    this.cancel.click();
  }

  updateNoteInList(rawData, inputForm) {
    const data = JSON.parse(rawData);
    const noteContent = inputForm
      .closest(".note-card")
      .querySelector(".note-content");
    noteContent.textContent = data.content;
  }

  fillControlForm() {
    const noteContent = this.noteElement.textContent;
    this.form.querySelector("[name='id']").setAttribute("value", this.noteID);
    this.form
      .querySelector("[name='content']")
      .setAttribute("value", noteContent);
  }
}
