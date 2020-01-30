var popup = document.getElementById("change");
var old_title = document.getElementById("old_title");

function openPopup(id_number, title) {
	old_title.value = id_number + ". " + title;
	popup.style.display = "block";
}

function closePopup() {
	popup.style.display = "none";
}

function openPrompt(url){
	const will_delete = confirm("Are you sure you want to delete this story? The extensions won't be deleted but they will no longer be connected.");
	if(will_delete){
		window.location.href = url;
	}
}