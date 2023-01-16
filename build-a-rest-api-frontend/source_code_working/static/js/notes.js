import { sendForm } from "./request.js";

export class Notes {
  constructor() {
    this.allNoteLists = document.querySelectorAll(".note-list");
    this.allNotes = document.querySelectorAll(".note-card");
    this.activateAllCreateForms();
  }

  activateAllCreateForms() {
    this.allNoteLists.forEach((noteList) => {
      const personCard = noteList.closest(".person-card");
      const personID = personCard.getAttribute("data-person-id");
      new NoteCreateForm(noteList, personID);
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
    this.createButton.addEventListener(
      "click",
      this.handleCreateClick.bind(this)
    );
    this.connectPerson();
  }

  connectPerson() {
    let fieldPersonID = this.form.querySelector("input[name='person_id']");
    fieldPersonID.setAttribute("value", this.personID);
  }

  handleCreateClick(event) {
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
    noteList.insertBefore(newNoteCard, noteList.children[1]);
  }
}
