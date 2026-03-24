# My first server

## And by the way what does the server respond to GET&nbsp;?

`````{div}
:class: columns

````{div}
:class: fifty
```{image} media/http-get-request.excalidraw.svg
:width: 100%
:align: center
```
````

````{div}
:class: fifty
```{image} media/http-get-response.excalidraw.svg
:align: center
:width: 100%
```
````
`````

```{div}
:class: smaller
Indeed, the *Body* partof an HTTP GET request is empty;  
but well it's the general idea to remember: there's a header+body structure for both requests and responses
```

---

### in the browser

It's possible to see requests and responses in your browser  
via `Developer Tools → Network`

`````{div}
:class: columns

````{div}
:class: sixty

```{image} media/chrome-request-headers.png
```
````

````{div}
:class: fourty

```{image} media/chrome-response-headers.png
```
````
`````

---

## Let's make a basic HTTP server

`````{div}
:class: columns

````{div}
:class: fifty-five

```sh
## in your terminal:
## let's go to the course repo
cd /bla-bla-bla/backend

## there's an html folder
cd html

## to launch the server
python -m http.server

## NB: ... 
## at this stage the terminal is blocked
## to kill the server type "Control-C"
```
````

````{div}
:class: fourty-five

then open in your browser `http://localhost:8000/index.html` (*)
```{div}
:class: smaller
(*) you can also replace `localhost` with your IP address - [we talked about it here](#my-ip-address)
```
````
`````

```{div}
:class: smaller center

it's really the simplest possible method to make a server with Python 🐍  
but well it's just a toy you know
```

---

### A bit less basic

```{div}
:class: center
This time we're going to do it *by hand* and write some code, still in Python 🐍  
it happens in the `python/http-servers` folder  
📢 ⚠️ We look at the file `server1_static.py`
```

```{literalinclude} ../python/http-servers/server1_static.py
:align:center
```

---

## Request processing

The internal operation of an HTTP server is quite simple

1. **Listen** on a port (80 by default)
2. **Accept** a connection
3. **Read** the request
4. **Process** the request
5. **Send** the response
6. **Close** the connection

The important point is the transition between steps 3 and 4 which is the heart of the HTTP server  
because it defines how the server will process the request.

---

## Examples made by hand

📢 ⚠️ in the `python/http-servers` folder, we look at the files:

- `server2_static_byhand.py`
  - basically, same functions: knows how to respond to GET for static files
  - but written "by hand"
    <br><br>
- `server3_post_stateful.py`
  - the server is STATEFUL (it remembers the state) - see the `STATE` variable  
    (NB: in real life of course, the state will be stored in a SQL database - or other)
  - the POST: var=value assignments are memorized
  - the GET: whatever the PATH, displays in html the content of variables known in `STATE` (and other details)
    <br><br>
- `server4_template.py`
  - same functionalities but with a JINJA2 template

---

## of course frameworks exist for that&nbsp;!

all this is a bit tedious, that's why we use frameworks (→ following slides)  
but it's good to understand how it works  
still to remember: this story of templates; we'll talk about it again

