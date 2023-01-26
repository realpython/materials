import { sendForm } from "./request.js";

export class People {
  constructor() {
    this.allPeopleCards = document.querySelectorAll(".person-card");
    this.activateCreateForm();
  }

  activateCreateForm() {
    const peopleForm = document.querySelector(".person-create-card form");
    new CreatePersonForm(peopleForm);
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
    document.querySelector(".people-list").appendChild(personCard);
  }
}
