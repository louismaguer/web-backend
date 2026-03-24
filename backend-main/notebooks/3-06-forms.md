# Forms and FastAPI

## Overview

This section shows a minimal example of implementing a user registration
**form** with FastAPI  
we want to focus on the aspects relating to **forms**, and for that reason we
deliberately keep things simple^singlemodel].

[^singlemodel]: we keep the schema minimal to focus on form handling; in practice you might
  want to use more specific types (e.g. `User` and `UserCreate`), and add
  constraints (e.g. email format validation), as we've seen in previous sections

In the mix, we'll take this chance **to say a word on CORS**, which is a rather
painful impediment in web development especially for beginners, so that you are
aware of it and know how to work around that.

---

## The backend

We're going to elaborate on the simplistic backend example from
`python/db-single-table`, remember:

```{literalinclude} ../python/db-single-table/users.py
:lang: python
:lines: 1-7
:emphasize-lines: 3-7
```

reminders:

- `table=True` tells SQLModel this class maps to a database table
- fields are validated automatically when used in FastAPI endpoints


---

## The `<form>` HTML element (frontend)

When building an HTML page that prompts the user to enter data, the most common
approach is to use a `<form>` element, which provides a structured way to
collect user input and submit it to a server.

So in our case we write a form with three input fields and a submit button like
so

```{literalinclude} ../python/fastapi-forms/register.html
:lang: html
:linenos: true
:lineno-start: 3
:lines: 3-21
```

---

## Implicit bindings & default encoding

Important observations:

- this is a plain HTML form — no FastAPI-specific markup
- the **`name` attributes match the field names** expected by the API, so the
  ones in the `User` model above
- also the `action` attribute points to the API endpoint URL[^endpoint]

[^endpoint]: here of course we assume you run the backend from the
    `db-single-table` folder, on port 8000

This means that the form is **implicitly bound** to the API endpoint, without
any explicit coupling in the code.

However, there's a catch: by default, the browser will **submit the form data as
`application/x-www-form-urlencoded`**[^1990s], which is not JSON !

[^1990s]: this encoding format is a legacy from the 1990s, the early days of the
    web, and is still the default in browsers for form submissions

And as we actually want to send JSON, we need to intercept the submission with
JavaScript.

---

## Converting form data to JSON

And here's how we can do that[^scriptinject]

[^scriptinject]: refer to [your frontend
    course](https://frontend.info-mines.paris/js-loading-nb/) to load this JS
    script in your html

```{literalinclude} ../python/fastapi-forms/hijack-forms.js
```

What happens here when the form gets submitted:

1. The browser collects form values into a `FormData` object
2. We convert it into a plain JavaScript object
3. The object is serialized to JSON
4. The request is sent with `Content-Type: application/json`

This keeps the backend clean and JSON-focused.

---

## Other types of inputs

In our html snippet, we've used 2 different types of inputs:

- `<input type="text">` for the name
- `<input type="email">` for the mail address
- `<input type="checkbox">` for the `active` boolean

but as you can imagine, there are many other types of inputs, e.g. `<input
type="date">` for dates, `<input type="file">` for file uploads, etc...  

Make sure to pick the one that works best for you.

---

## CORS breaks the naive way

When trying to run the above code a bit too naively, i.e. with

`````{admonition} The naive setup[^devnull]
:class: dropdown

````{grid} 2

```{code-block} bash
# run the backend on port 8000
cd python/db-single-table
fastapi users:app --reload --port 8000
```

```{code-block} bash
# run the frontend on port 5173
cd python/fastapi-forms
vite --config /dev/null
```
````
`````

[^devnull]: here we run `vite` with the `--config /dev/null` option to ignore the
    configuration in `vite.config.js`, in the next section we will see why this
    configuration is needed and how it solves the issue at hand

And then opening `http://localhost:5173/register.html`, you will notice **the
code won't work**

The obvious reason is this: **we have written`action="/users/"`** in the form,  
which means the browser will try to submit the form to
`http://localhost:5173/users/`,  
which is not where our backend is running - it listens on port 8000

Now, as an exercise, change the `action` attribute and replace it with
`http://localhost:8000/users/` - you will see that **this still won't work** !

Open your web console: in this configuration we hit a rather painful reality of
web development: **CORS restrictions in the browser**.

---

## What is CORS ?

CORS stands for Cross-Origin Resource Sharing, and it's a security mechanism
implemented by browsers to prevent malicious websites from making unauthorized
requests to other domains.

When you try to submit the form to `http://localhost:8000/users/` from a page
served on `http://localhost:5173`, the browser considers this a cross-origin
request and blocks it by default.

This situation happens every time a web page **tries to `fetch()` from another
domain than the one it was served from**, and it's a common hurdle in web
development.

---

## A workaround: `vite` as a proxy

For development purposes, a common workaround is to use a proxy, which allows us
to forward requests from the frontend server to the backend server, effectively
bypassing CORS restrictions.

You can see this in action in the `python/fastapi-forms` folder, where we have a
`vite.config.js` file which configures `vite` to proxy requests starting with
`/users` to `http://localhost:8000/users`.

This means you can run the original code by simply running `vite` without the
`--config /dev/null` option; this time vite will read the configuration and set
up the proxy, allowing you to keep the form's `action="/users/"` as it is, and
everything will work seamlessly.

---

## A production architecture

Once you have all these pieces working, you can then then envision a production architecture where:

- `vite` is replaced by a more robust proxy server (e.g. nginx, caddy, or a CDN)
- the proxy server reroutes requests to the relevant software piece based on the
  URL path, possibly performing rewrites on the way (e.g. stripping out the
  `/api` prefix before forwarding to the backend)

```{image} media/nginx-as-proxy.excalidraw.svg
```

and this has many advantages:

- only one place (the proxy) terminates TLS , which simplifies certificate management
- all the traffic apparently comes from the same domain, so no CORS issues
- the frontend and the backend can be scaled independently, and even deployed on
  different servers, without any change in the code

---

## Summary

- HTML forms **do not send JSON** by default
- You will need a small JavaScript layer, to easily convert form inputs into JSON
- Running the frontend and the backend on separate domains can be tricky, and
  require extra configuration[^corsmiddleware]
- As a rule of thumb, for your first developments, it is probably simpler if you
  serve the frontend from the same domain as the backend, to avoid CORS issues;
  you can then switch to a separate frontend server with a proxy once you have
  the basics working

[^corsmiddleware]: in particular, check [the `CORSMiddleware` in
    FastAPI](https://fastapi.tiangolo.com/tutorial/cors/#wildcards), which
    allows you to configure CORS policies on the backend side, but be careful
    with it, as a misconfiguration can lead to security vulnerabilities

---
