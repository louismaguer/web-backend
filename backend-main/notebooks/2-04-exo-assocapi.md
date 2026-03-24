---
short_title: exo assocapi
---

# exo: assocapi with FastAPI

(label-exo-assocapi)=
## Small practical break

**Objective**: Set up an API allowing access to CSV file content

You have <https://github.com/ue22-p25/backend-assocapi-frontend> a ready-made frontend!  
And you have <https://github.com/ue22-p25/backend-assocapi-skeleton> a backend to complete

The backend API must **imperatively** respect the routes documented in the README.

```{admonition} automatic doc with FastAPI !
:class: smaller
Once your code works, go visit the `/docs/` route to see the interactive doc of your API.
```

````{admonition} tip for copying repositories
:class: smaller tip dropdown

 to copy the content of these repositories on your machine, rather than using `git clone`, you can use this
```bash
# if necessary (npx command not found)
# conda install conda-forge::nodejs

# download the repo in the 'frontend' folder
npx degit git@github.com:ue22-p25/backend-assocapi-frontend.git frontend
# same for the backend
npx degit git@github.com:ue22-p25/backend-assocapi-skeleton.git backend
```

which has the advantage of not recreating a git repository in the created folder; especially if you place yourself in an already existing repository like `backend-homework`  
(but doesn't prevent you from `git add` the result immediately)
````

---

## Tip #1: *auto-reload*

- you notice that FastAPI applications do not contain code to execute directly  
  (just route definitions)
- so if you launch the python file with `python my_file.py`, it does nothing!
- that's why it's **essential** to launch the app with `fastapi dev assocapi.py`
- also and especially, the server **restarts by itself** at each code modification  

````{div}
:class: smaller
and same for the frontend by the way; if you intend to touch it, it's better to launch it with `vite`, so it restarts by itself at each modification
````

---

## Tip #2: typed parameters

- a route can take a parameter, possibly typed

`````{div}
:class: columns
````{div}
:class: fifty
```python
# untyped parameter

@app.route('/hello/<name>')
  def hello(name):
    # here name is a simple str
    # it's up to you 
    # to check its content
    return f'Hello, {name}!'
```
````

````{div}
:class: fifty
```python
# here the parameter is typed

@app.route('/hello/<int:id>')
  def hello(id):
    # so fastapi does the
    # control and conversion
    # automatically
    return f'Hello, {id**2}!'
```
````
`````

---

## Tip #3: return types

to shorten the code, the return type of a route implies automatic processing  
we hardly need to convert objects to dict/json  
especially if we use Pydantic models (we'll talk about it again...)

| Route return                   | HTTP response                                                                      |
|--------------------------------------|-----------------------------------------------------------------------------------|
| `dict` or `list` or `int` or `float` | Automatically encoded in JSON.                                                   |
| `str`                                | Sent as raw text (`text/plain`)                                            |
| Pydantic `BaseModel`                 | JSON automatically.                                                             |
|                                      | Example: `return Item(name="Apple", price=1.5)` <br> → `{"name":"Apple","price":1.5}` |

---

## Tip #4: `httpie`

- it's practical to have a real frontend in HTML/CSS/JS
- BUT for development it's useful to test ***also*** the routes in command line in the terminal
- for this **we can use `httpie`** (or `curl` but it's less readable)
- which installs with

  ```bash
  pip install httpie
  ```

- and which is used like this

  ```bash
  # a GET
  http GET http://localhost:8000/hello
  # or abbreviated
  http :8000/hello

  # a POST
  http POST http://localhost:8000/hello var=value
  # by the way with an assignment of this type the POST is automatic
  # which makes the following command equivalent
  http :8000/hello var=value
  ```

- and as always, do `http --help` or see the doc for more details...

---
