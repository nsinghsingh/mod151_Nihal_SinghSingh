var popup = document.getElementById("change");
var old_title = document.getElementById("old_title");

function openPopup(id_number, title) {
	old_title.value = id_number + ". " + title;
	popup.style.display = "block";
}

function closePopup() {
	popup.style.display = "none";
}