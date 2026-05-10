const ws = new WebSocket(
  `wss://chat-app-test-production.up.railway.app/ws/${prompt("Enter Username")}`
);

ws.onmessage = (e) => {
    document.getElementById("messages").innerHTML += `<p>${e.data}</p>`;
};

document.getElementById("sendBTn").onclick = () => {
    const input = document.getElementById("messageInput");
    ws.send(input.value);
    input.value = "";
};