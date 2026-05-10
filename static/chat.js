const ws = new WebSocket(`ws://localhost:8000/ws/${prompt("Enter Username")}`);

ws.onmessage = (e) => {
    document.getElementById("messages").innerHTML += `<p>${e.data}</p>`;
};

document.getElementById("sendBTn").onclick = () => {
    const input = document.getElementById("messageInput");
    ws.send(input.value);
    input.value = "";
};