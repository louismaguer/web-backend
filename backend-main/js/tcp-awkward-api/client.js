// client.js
import { connect } from "net";

class ContactClient {
    constructor(host, port) {
        this.host = host;
        this.port = port;
    }

    connect() {
        return new Promise((resolve, reject) => {
            const socket = connect(this.port, this.host, () => resolve(socket));
            socket.on("error", reject);
        });
    }

    async command(cmd, args = {}) {
        try {
            const socket = await this.connect();
            const data = JSON.stringify({ cmd, args });

            socket.write(data);

            let receivedData = "";

            socket.on("data", (chunk) => {
                receivedData += chunk.toString();
            });

            return new Promise((resolve) => {
                socket.on("end", () => {
                    const response = JSON.parse(receivedData);
                    if (!response.status) {
                        console.error("ERROR:", response.msg);
                        resolve(null);
                    } else {
                        resolve({ msg: response.msg, data: response.data });
                    }
                });
            });
        } catch (error) {
            console.error("Connection error:", error);
        }
    }
}

const client = new ContactClient("127.0.0.1", 3001);

(async () => {
    console.log("----------- list command --------------");
    const listResponse = await client.command("list");
    console.log(listResponse);

    console.log("----------- add command --------------");
    const addResponse = await client.command("add", {
        name: "Basile Marchand",
        mail: "basile.marchand@mines-paristech.fr"
    });
    console.log(addResponse);
})();