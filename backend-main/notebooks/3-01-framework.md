# A framework?

## Recap of previous episodes

````{div}
:class: center
Classic Client <-> Server architecture with peer-to-peer, three-tier variations, ...
````

``````{div}
:class: columns

````{div}
:class: thirty-five center
```{image} media/osi-model.excalidraw.svg
```
````

`````{div}
:class: sixty-five

````{div}
:class: columns

```{image} media/ip-address.excalidraw.svg
:width: 30%
```

```{image} media/http-post-request.excalidraw.svg
:width: 70%
```
````

```{image} media/server-app.excalidraw.svg
```
```{image} media/logos/lets-encrypt.svg
:width: 150px
```
````
`````

``````

---

## Frameworks

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

<br>

For example `NumPy` in Python 🐍 is a library

```{image} media/code-with-library.excalidraw.svg
:align: center
```
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
<b> Framework </b>

Development framework in which the developer comes to register, i.e. develop functionalities/behaviors. There it is no longer the developer who sets his logic but the framework.

<br>

A code with holes 🕳️ in a way - like `arcade`

```{image} media/code-with-framework.excalidraw.svg
:align: center
```
````

`````

---

## Frontend, backend

````{div}
:class: center
⚠️ Web framework a very (way too much) generic term ⚠️
````

`````{div}
:class: columns

````{div}
:class: fifty center
Frontend framework

```{image} media/framework_frontend.png
:width: 60%
:align: center
```

Focused on client-side application development.
````

```{div}
:class: vertbar
```

````{div}
:class: fifty center
Backend framework

```{image} media/framework_backend.png
:width: 100%
```

<br>
Focused on server-side development
````
`````

In the context of this course we will only focus on the `backend` side

---

## The main principles of backend frameworks

````{div}
:class: center
```{image} media/framework-routes.excalidraw.svg
:width: 75%
```
````

To this a complete framework adds functionalities of:

````{div}
:class: center
*Web Template*, *Security*, *Access to databases*
````
