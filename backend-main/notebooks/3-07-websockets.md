# FastAPI & websockets

---

(label-websockets)=
`````{div}
:class: columns

````{div}
:class: fifty
## What are WebSockets?

a new mechanism introduced circa 2011 to overcome the limitations of HTTP for
real-time applications:

- **bidirectional** connection between a client and the server  
  we talk about *full-duplex* connection
- allows the server to **push** information to the client without the client having asked for anything 😲
````

````{div}
:class: fifty center
```{image} media/timeline-ws.excalidraw.svg
:width: 70%
```
````

`````

---

## a simple example

you can refer to the code in the `python/fastapi-websockets` folder for a
complete example of a websocket server and client using FastAPI and vanilla JS.

let's start with `app.py` and its companion `index.html`[^app2]

[^app2]: the `app2.py`/`index2.html` duo is a slightly modified version, that
    uses JSON instead of raw messages

**what it does**: the app shows a single page with a button and a status text.
When the button is clicked, it toggles the status between "ON" and "OFF".  
The interesting thing here is: the status is **shared across all clients**
connected to the server, so if one client toggles the status, all other clients
will see the updated status in real-time.

```{admonition} Try it out!
:class: tip dropdown

as you will have guessed, you need to
- run the `app.py` server (on port 8000, this is hard wired in the html)
- and then open multiple browser tabs on the html file (use vite if you intend on doing changes in the html)
```

---

## builtin in FastAPI !

let's take a look at the code, and for starters look at the `app.py` file  
the interesting snippet is below, where we define a websocket endpoint at `/ws`, like so

```{literalinclude} ../python/fastapi-websockets/app.py
:linenos:
:emphasize-lines: 1-2
:start-at: app.websocket
```

what this code does is: whenever a client connects to the `/ws` endpoint, it is
added to the `manager` (whose job is simply to keep track of all connected
clients and send messages to them), and everytime any client sends a message,
the server receives it and broadcasts it to all connected clients

the gory details of how the `ConnectionManager` works are not exactly important,
just note how it leverages the `Websocket` class provided by FastAPI to manage
the connection with each client

---

## and builtin in JS !

looking now at the JS code (in `index.html`), we can see how the client connects
to the websocket server and sends/receives messages

```{literalinclude} ../python/fastapi-websockets/index.html
:linenos:
:emphasize-lines: 4,7,17
:start-at: <script>
:end-at: </script>
```

---

## see also: SocketIO

websockets are a powerful tool for building real-time applications, and FastAPI
makes it easy to implement them on the server side.

now, it is admittedly a rather low-level API, and you may want to look into
higher-level libraries like SocketIO, which are built on top of websockets, but
provide **additional features** like **automatic reconnection**, **rooms**,
**namespaces**, etc.

these can be tedious to implement yourself, so using a library can save you a
lot of time and effort; but this goes a bit beyond the scope of this course, so
I encourage you to explore it on your own if you're interested in building
real-time applications!
