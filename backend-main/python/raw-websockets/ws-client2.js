const socket = new WebSocket("ws://localhost:8765");

const count = process.argv[2];

socket.onopen = () => {
    console.log("Connected to server");
    socket.send(count);
};

socket.onmessage = (event) => {
    console.log(`Received: ${event.data}`);
    if (event.data === "0") {
        socket.close(1000, "Bye!");
    }
};

socket.onerror = (error) => {
    console.error(`WebSocket error: ${error}`);
};

socket.onclose = () => {
    console.log("Connection closed");
};
