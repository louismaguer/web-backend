# FastAPI - basics


---

## FastAPI

```{image} media/logos/logo-fastapi.svg
:align: right
:width: 25%
```

Python micro-framework 🐍 - fairly recent (2018)

occupies the same space as
- Flask - developed since 2010 - lightweight and extensible
- Django - developed since 2003 - perceived as more complete but also heavier

🚧 Micro-framework doesn't mean not usable on large projects ⚠️  

---

## FastAPI vs Flask

FastAPI is similar on the surface to Flask, but **much more modern**!

- encourages a more structured approach
  - leverages type information (type annotations / Pydantic)
  - especially for **automatic data validation** / conversion
  - so you can define separate models for creation, reading, updating, etc.  
    useful for example for password hashing (not exposed)
- in particular, automatically generates **interactive documentation**
- has native support for **asynchronous** programming
- as well as for **websockets**

---

## Why FastAPI (and not something else)

1️⃣ You all more or less know how to do Python 🐍  
so we eliminate everything that's not Python-based

2️⃣ We'll try to teach you things used elsewhere  
And the FastAPI trend indeed seems to be experiencing spectacular growth!

````{div}
:class: center

```{figure} media/web-framework-survey.png
:class: smaller
:width: 85%
Source: <a href="https://www.jetbrains.com/lp/devecosystem-2023/python/">https://www.jetbrains.com/lp/devecosystem-2023/python/</a>
```

````

---

## Graphical User Interface

But actually... why are we interested in this?  
The GUI (pronounce *gooey*) is what bridges 🌉 between:

````{div}
:class: center
a calculation/data processing code/...  
and a user interface  
````

```{admonition} note
that's what makes all this very relevant for the "Computer Science Projects" at the end of S2
```

---

### GUI - two approaches

`````{div}
:class: columns

````{div}
:class: fifty center
***Old school***  
Using graphical libraries and developing a "thick" client

```{image} media/old-school.excalidraw.svg
:width: 50%
:align: center
```
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
***New age***

Using the browser

```{image} media/new-age.excalidraw.svg
```
````

`````

---

## FastAPI: we already know a bit

We already vaguely know how to use it, remember, we've already seen  
```{div}
:class: center
[how to install FastAPI](#label-fastapi-install)  
and  
[how to make a minimal server with FastAPI](#label-exo-assocapi)
```

Notice how simple it is to get started 😯  
this is **a pro of Flask/FastAPI* over Django (which requires a more advanced setup)

---

### Quick recap

`````{div}
:class: columns

````{div}
:class: fifty
- Step 1️⃣:

```python
from fastapi import FastAPI
```
````

````{div}
:class: fifty
- Step 2️⃣

```python
app = FastAPI()
```
````
`````

Then we attach Python functions to URL paths  
we call these functions *route handlers* or *router functions*

```python
@app.get("/a/path/target")
def the_corresponding_function():
  // does very smart things
  return a_result    # which can be data (json) or html or whatever...
```

---

### And to start the server?


`````{div}
:class: columns

````{div}
:class: fifty
From the terminal
```{code} bash
:caption: the server in development mode
fastapi dev my_app.py
```
```{code} bash
:caption: or on another port
fastapi dev my_app.py --port 8080
```
````


````{div}
:class: fifty
or also
```{code} bash
:caption: in production mode
fastapi run my_app.py
```

````

`````

:::{admonition} using `uvicorn`
:class: dropdown
Note that fastapi is often also run through a [dedicated http server named `uvicorn`](https://uvicorn.dev/)
```bash
# for example, here in dev mode on port 8080, where
# (*) my_app is the Python module name (so without .py; replace / with . if in a subfolder)
# (*) app is the name of the Python variable that refers to the FastAPI instance

uvicorn my_app:app --reload --port 8080
```
:::

<!-- ---

### Pour ceux qui auraient la flemme !

`````{div}
:class: columns

````{div}
:class: sixty
```{div}
:class: center
<iframe src="https://giphy.com/embed/4KkSbPnZ5Skec" width="471" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````

````{div}
:class: fourty center

xxx no longer working xxx

[http://bit.ly/3Z5C5k7](http://bit.ly/3Z5C5k7)

```{image} media/qrcode/flask_sandbox.png
:width: 60%
```
````
`````
 -->
---

## Parameters in a `GET`

````{div}
:class: center

For `GET` requests, we can write slightly more sophisticated URLs:  

```{image} media/http-get-arguments.excalidraw.svg
:width: 80%
```

Of course then we need to **retrieve the arguments** in the *handler* function 🤔  
FastAPI has it all figured out
````

`````{div}
:class: columns

````{div}
:class: fifty
```python
@app.get("/some/route/data")
def get_parameters(
        name: str,
        age: int):
    return {'name': name, 'age': age}
````

````{div}
:class: fifty
you just need to declare the parameters  
with their type  
and FastAPI does the rest  
and even type conversion

````
`````

````{div}
:class: center
🚧 No notion of type in network exchanges, everything is a string 🚧
````

---

## Parametric URL

````{div}
:class: center
Now you can also - and more in line with best practices - **define parameters within a URL itself**  
e.g. then your users would call URLs like `/my/route/basile/42` instead

```{image} media/fastapi-route-param.excalidraw.svg
```
````

`````{div}
:class: columns

````{div}
:class: fifty
```{div}
:class: smaller
and of course you can also receive multiple parameters this way
```
```python
@app.get("/my/route/{name}/{age}")
def url_parameter(name: str, age: int):
    return ...
```
````

````{div}
:class: fifty smaller
**Note**: Special case for `/`

- by default a parameter does not contain a slash `/`
- **but** in a route you can declare  
  `@app.get"/my/route/{parameter:path}"`  

  to allow slashes `/` in the parameter itself
````
`````

---

## More kinds of parameters

`````{div}
:class: columns

````{div}
:class: fourty

in all generality, parameters can be passed in 5 different ways in an HTTP request:

1. in the URL path  
   (e.g. `/my/route/basile/42`)
2. in the URL query string  
   (e.g. `/my/route?name=basile&age=42`)
3. in the request body (e.g. for POST requests)
4. in the request headers
5. in cookies

here's an example of a request with parameters in all these different places, freely inpired from the pixels-war game
````

````{div}
:class: sixty
```{image} media/http-request-parameters.excalidraw.svg
```
````

`````
---

### Capturing parameters in the FastAPI route handler

::::{grid} 2

```{code} python
:linenos:
:emphasize-lines: 1,6,11,13-17
from fastapi import FastAPI, Header, Cookie, Query, Body
from pydantic import BaseModel

app = FastAPI()

class PixelPayload(BaseModel):
    i: int
    j: int
    color: str  # e.g. "#ff0000"

@app.post("/api/{map}/set")
async def set_pixel(
    map: str,
    defer: bool = Query(False),
    authorization: str = Header(...),
    signature: str = Cookie(...),
    payload: PixelPayload = Body(...),
):
    ...
```

````{div}
with this code, inside the router function, you can access the parameters as follows:

```{list-table}
:align: center
* - Python code
  - value
* - `map`
  -  `themap`
* - `defer`
  -  `True`
* - `authorization`
  -  `Bearer ...`
* - `signature`
  -  `f4d93b...`
* - `payload.i`
  - `3`
```

```{admonition} FastAPI does the heavy lifting for you
:class: tip smaller dropdown

as you can see FastAPI takes care of parsing the request and extracting
the parameters for you

in particular observe how the `payload` parameter is automatically converted from JSON to a `PixelPayload` object  
this is in anticipation of the next episode where we'll see how to use Pydantic models to define the structure of the data we expect in the body of a request

also notice how the `defer`, `authorization`, and `signature` parameters are extracted from the query string, headers, and cookies respectively.  
Cookie is a special case of Header, but FastAPI provides a convenient way to access cookies directly.
```

````
::::

---

## Returning data

```{div}
:class: center
remember: **everything is text over the network**  
by default, FastAPI returns data in **JSON format**  
```

::::{grid} 2

````{div}
this means that when you say e.g.
```{code} python
:linenos:
:emphasize-lines: 3-4
@app.get("/my/route/{name}/{age}"):
def url_parameter(name: str, age: int):
    return {'name': name,
            'age': age}
```
````

````{div}
what is sent back to the client will be **the text**:

```json
{
  "name": "basile",
  "age": 42
}
```
so remember to **interpret this text as JSON** on the client side
````

::::

```{admonition} note on using Pydantic models for return values
as we'll see in the next episode, it's often **more convenient to define a Pydantic model**
for the return value of a route handler,  
rather than returning a raw dictionary as in the example above  
this way FastAPI can also do automatic validation, conversion, and documentation for the return value
```

---

## A random generator (exercise)

**in `python/random-generator/`**
- read the code - at least the 2 first `get` endpoints for now
- start the server
- point your browser at the documentation page at `http://localhost:8000/docs`

---

### Exercise 1 - the docs

```{exercise}
:label: exo-random-docs

- explore the `/docs/` page
- see how you can interactively test the two endpoints
```

---

### Exercise 2 - from the browser

```{exercise}
:label: exo-random-browser

- use your browser to call the `/api/integer` endpoint
- how would you get 10 integers between 100 and 200 ?
```

```{admonition} hints
:class: tip dropdown
- remember that for GET requests, parameters are passed in the URL after a `?` and separated by `&`
- also remember that the interactive documentation page shows you the exact URL to use
```

---

### Exercise 3 - from the terminal

```{exercise}
:label: exo-random-terminal

- same question, but using `http` from the terminal
```

```{admonition} hints
:class: tip dropdown
- `http` is from the `httpie` package
- do not hesitate to pass `http` the `-v` option to see what is sent and received
- be aware that in `bash`, the `&` character is special (it puts the command in background),
  so you need to either escape it with a backslash `\&` or put the whole URL in quotes
- also be aware that with `http`, there are more convenient ways to pass parameters than just putting them in the URL - see the solution below for details
```

---

### Exercise 4 - error handling

```{exercise}
:label: exo-random-error
- what happens if you pass a max smaller than the min ?
- how could we handle that ?
```

---

## Exercise solutions

````{solution} exo-random-browser
:class: dropdown

in the browser, you need to type the full URL, i.e.
```{code} url
:linenos:
:emphasize-lines: 1
http://localhost:8000/api/integer?min=100&max=200&count=10
```
````

````{solution} exo-random-terminal
:class: dropdown

- first naive approach:  
  with `http`, you can use the same URL as in the browser  
  but **you need to quote it** because of the `&` characters, like this:

  ```{code} bash
  :linenos:
  :emphasize-lines: 4
  # long version - watch out for quotes!
  # you can do this, but it's a little awkward
  # because & is a special character in bash
  http "http://localhost:8000/api/integer?min=100&max=200&count=10"
  ```

- now, `http` makes it a little simpler / less awkward  
  for one thing, you can skip the `localhost` part and just use `:8000`  
  and also, you can pass parameters directly as arguments to `http`, like this:
  ```{code} bash
  :linenos:
  :emphasize-lines: 3
  # short version, to pass parameters with GET
  # however you MUST use ==
  http :8000/api/integer min==100 max==200 count==10
  ```

- **NOTE** using just `=` **would NOT WORK**


  ```{code} bash
  :linenos:
  :emphasize-lines: 3-4

  # WARNING: the simple = is for POST requests!
  # if we use = it doesn't do what we want!
  # DON'T DO IT LIKE THIS!
  # http GET :8000/api/integer min=100 max=200 count=10

  ```
````

````{solution} exo-random-error
:class: dropdown

as it stands, there is **no control** on the parameters  
so the server calls the `random.uniform` function with invalid parameters, and that generates a 500 error

to address this, several choices are possible:

- either we add a check in the `some_random_floats` function to verify that `min < max` and if not we raise an HTTP 400 (Bad Request) exception
- or we use Pydantic's validation features; but for now that's premature since we haven't seen Pydantic yet 😉

so for now we'll settle for the 1st solution

```{code} python
:linenos:
:emphasize-lines: 5

from fastapi import HTTPException

def some_random_floats(min: float, max: float) -> float:
    if min >= max:
        raise HTTPException(status_code=400, detail="Invalid range")
    return random.uniform(min, max)
````

---

## `HTTP` verbs

Quick reminder from the 1st episode, HTTP different possible requests

- `GET`: requests to **obtain** a resource from the server (html/css/js file, image, video, data, ...)
- `POST`: requests to **send** data to the server for processing (adding a user to a database, ...)
- `PATCH`: requests to **partially modify** a server resource (updating a user's email address in the database)
- `DELETE`: requests to **delete** a server resource (deleting a comment on an article, ... )

These are the main types of requests but there are others, for the complete list you can check here: [https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

:::{admonition} there's also a `PUT` verb
:class: dropdown

in theory, `PUT` is the verb that *should be used* for creating a new entity  
however for historical reasons, entity creation is often done with `POST` requests...
:::

---

## Parameters in a `POST`

```{admonition} seen above: GET parameters are in the URL
:class: tip dropdown smaller

like we've seen above, e.g. `/my/route?param1=val1&param2=val2`

and FYI, the HTTP protocol doesn't provide for putting parameters in the body of a GET request, if you do it anyway the behavior is undefined...
```

however for `POST`, `PATCH`, `DELETE` requests, ...  
the parameters are passed in the **body** of the request

Let's look at an example

---

### `POST` requests

And to start let's look at what is sent by `httpie` when we do a POST

````{admonition} the body of a POST request
:class: dropdown

Here it is

```{code} bash
:linenos:
:emphasize-lines: 2,7,11-13

❯ http -v :8000/api/seed seed_value=42
POST /api/seed HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
Host: localhost:8000
User-Agent: HTTPie/3.2.4

{
    "seed_value": "42"
}
```
````

As we can see, the parameters are sent

- **in JSON format**
- and **in the Body** of the request - i.e. after the *headers*

```{admonition}**Remember this well, it's important!**
:class: caution

This is the process we'll need to use every time we want to **send data to the server**  
(and typically when it's the frontend sending a request via JS)
```

:::{admonition} note on typing: `int` vs `str`
:class: tip dropdown

also note here that the value `42` is transferred over the wire as a string `"42"`  
this is because by default `http` treats all parameters as strings  
the actual conversion to integer will be done on the FastAPI side

we *could have* forced it to send an integer by using `seed_value:=42` instead of `seed_value=42`  
this is useful, especially when sending boolean or numeric values
:::

---

### On the FastAPI side

Here now is one FastAPI code that works well to handle this request

```{code} python
:linenos:
:emphasize-lines: 1,5

from fastapi import Body

@app.post("/api/seed")
# with Body() we indicate that the parameter comes from the request body
def set_seed(seed_value: int=Body(..., embed=True)):
    random.seed(seed_value)
    return {"message": f"Seed set to {seed_value}"}
```

```{admonition} it's simpler with Pydantic
:class: tip dropdown
we'll see this later, but things get a little simpler with a Pydantic model to define the parameters...  
interested students can check the code for `/api/seed2` in `python/random-generator/generator.py`
```

---

## What's next

At this point you know how to implement FastAPI *endpoints* that handle
GET and POST requests with parameters

We have many other things to see, including:

- how FastAPI leverages type annotations to do automatic validation
- how to return HTML rather than JSON data
- as well as a few other tips & tricks

We'll see that in the following episodes...
