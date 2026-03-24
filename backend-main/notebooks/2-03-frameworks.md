# Frameworks

Answer to a need but which one?

````{div}
:class: center
***Simplified development framework***
````

Basically a <strike> spiritual </strike> guide, allowing to simply develop specific applications.

````{div}
:class: center
<iframe src="https://giphy.com/embed/MZW5o8f5RaH0Q" width="480" height="197" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Framework vs Library

````{div}
:class: center
Frameworks, Libraries, same thing? <br>
````

`````{div}
:class: columns

````{div}
:class: fifty center
<b> Libraries </b>

Set of programs performing specific operations, that you will use punctually within your programs following your own logic.

For example `NumPy` in Python 🐍 is a library

```{image} media/code-with-library.excalidraw.svg
:align: center
```
````

````{div}
:class: vertbar
````

````{div}
:class: fifty center bottom
<b> Framework </b>

Development framework in which the developer comes to register, i.e. develop functionalities/behaviors. There it is no longer the developer who sets his logic but the framework.  

A code with holes 🕳️ in a way

```{image} media/code-with-framework.excalidraw.svg
:align: center
```
````

`````

---

## Frontend, backend

````{div}
:class: center
⚠️ Web framework a very, too, generic term ⚠️
````

`````{div}
:class: columns

````{div}
:class: fifty center
Frontend framework

```{image} media/framework_frontend.png
:width: 50%
:align: center
```

Focused on client-side application development
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
Backend framework

```{image} media/framework_backend.png
:align: center
```

Focused on server-side development
````

`````

---

## backend frameworks: the main principles

````{div}
:class: center
```{image} media/framework-routes.excalidraw.svg
:width: 70%
```
````

To this a complete framework adds functionalities of:

````{div}
:class: center
`Web Template`, `Security`, `Access to databases`
````

---

## FastAPI Framework

Python 🐍 "lightweight" framework developed since 2018.

```{image} media/logos/logo-fastapi.svg
:align: center
:width: 300px
```

<br><br>
🚧 "lightweight" framework does not mean "not usable on big projects"  ⚠️
<br>
````{div}
:class: center
Netflix, Microsoft, Uber, ... use FastAPI for certain parts of their backends
````

very light and minimalist core, but super powerful

- uses Python **type annotations** for automatic data validation
- **automatic documentation** of APIs with Swagger UI and ReDoc
- **natively asynchronous**, hence very performant
- moreover, it can be enriched with **extensions**.

---

## Basic setup

(label-fastapi-install)=
### Installation

```bash
pip install fastapi[standard]
```

```{admonition} remark about bash
:class: dropdown

in all rigor it would be necessary to type  
`pip install "fastapi[standard]"`  
with quotes, to avoid your shell misinterpreting the brackets `[]`; do you know why?  
but well in practice the difference is minimal...
```

we will also install `httpie` to test APIs in command line  
it's just a very practical development tool, no need for this dependency in production

```bash
# ceci installe la commande http, disponible depuis le terminal
pip install httpie
```

---

### Hello world in FastAPI (run it)

`````{grid} 2 2 2 2
````{div}
let's create a file `hello.py` with this:


```python
# in hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

```{div}
:class: clignote
? What is `@app.get('/')` ?
```
````

````{div}
and to launch it type this
```bash
# in the terminal

fastapi dev hello.py
```

:::{admonition} a word about `uvicorn`
:class: dropdown tip
`uvicorn` is the recommended ASGI server for FastAPI.  
It is automatically installed with the `[standard]` option of FastAPI.  
And for info, in reality `fastapi dev` is an alias for  
`uvicorn hello:app --reload --debug`
:::
````
`````

---

### Hello world in FastAPI (use it)

after which we can query our API... we have the choice between:

`````{grid} 2 2 2 2
````{div}
open a web browser at the address  
[http://localhost:8000](http://localhost:8000)  
do it, you should see this:
```text
{"message":"Hello World"}
```
````

````{div}
use `http(ie)` in command line
```bash
# in verbose version
http GET http://localhost:8000

# in concise version
http :8000
```

the two forms are equivalent  
and in both cases observe that `http` shows us the HTTP *Headers* of the response

````

`````

---

## Routes

`@app.get` is a decorator that allows **to associate a function with a URL** (here of type GET).  
Obviously a web application is more than that, we want to manage several URLs, and of several types.  
So a FastAPI application is essentially a collection of routes.

For example:

```python
@app.post("/items/")
def create_item(item: Item):
    # code to create an item

@app.get("/items/")
def create_item(item: Item):
    # code to list items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # code to read an item
```

:::{admonition} `@app.api_route`
:class: dropdown tip
it is also possible to use `@app.api_route` to "capture" several types of requests in a single function
:::

---

## We're done ...

````{div}
:class: center
<iframe src="https://giphy.com/embed/3ohs7XbAurbpO5jIBy" width="480" height="267" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

... or not actually: we're going to put all this into practice with an exercise

