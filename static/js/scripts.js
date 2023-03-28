const input = document.querySelector("input");
const msg = document.querySelector("#msg");
const listMsg = [];

function addMsg(text) {
	const div = document.createElement("div");
	div.innerText = text;
	msg.appendChild(div);
}

input.addEventListener("keydown", (event) => {
	if (!event.code.toLowerCase().includes("enter")) {
		return;
	}
	fetch("/msgFromHtml", {
		method: "POST",
		body: input.value,
	});
	input.value = "";
});
function getMessage() {
	fetch("/msgFromServer", {
		method: "POST",
		body: listMsg.length,
	})
		.then((resp) => {
			return resp.json();
		})
		.then((data) => {
			if (data === "no") {
				return;
			}
			for (let elem of data) {
				listMsg.push(elem);
				addMsg(elem);
			}
		});
}
setInterval(getMessage, 100);
