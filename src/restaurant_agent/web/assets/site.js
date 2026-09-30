const menuToggle = document.querySelector("[data-menu-toggle]");
const navigation = document.querySelector("#primary-navigation");
const chatDialog = document.querySelector("#chat-dialog");
const chatClose = document.querySelector("[data-close-chat]");
const reservationForm = document.querySelector("#reservation-form");
let chatOpener = null;

function closeMenu() {
  menuToggle.setAttribute("aria-expanded", "false");
  navigation.classList.remove("is-open");
}

menuToggle.addEventListener("click", () => {
  const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
  menuToggle.setAttribute("aria-expanded", String(!isOpen));
  navigation.classList.toggle("is-open", !isOpen);
});

navigation.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", closeMenu);
});

document.querySelectorAll("[data-open-chat]").forEach((button) => {
  button.addEventListener("click", () => {
    chatOpener = button;
    closeMenu();
    chatDialog.showModal();
    chatClose.focus();
  });
});

chatClose.addEventListener("click", () => chatDialog.close());
chatDialog.addEventListener("close", () => chatOpener?.focus());

reservationForm.addEventListener("submit", (event) => {
  event.preventDefault();
  document.querySelector("#reservation-status").textContent =
    "Online availability is coming soon.";
});
