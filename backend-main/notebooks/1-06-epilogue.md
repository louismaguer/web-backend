# Epilogue

## A word about authentication

To authenticate with a REST API, you must provide proof of who you are with each request. This generally involves associating a token with the request that allows the application to know

`````{div}
:class: columns
````{div}
:class: fifty

- Who we are
- What we have the right to do on which resources

````

````{div}
:class: fifty

```bash
Authorization: Bearer <token>
```

````
`````


Token acquisition is generally done via the Web interface of the targeted service.

````{div}
:class: center
⚠️ Attention a token should ***never*** be shared 💣️
````

In most cases a token is associated with:

- A set of accessible resources
- Rights on these resources (consultation, modification, creation, deletion)
- A validity period (token expiration date)

````{div}
:class: center
A solution to preserve application tokens is to use a `.env` file
````

---

## A usable API is a documented API

So to conclude on APIs, it is a very simple way to offer an interface to remote resources and data. The only difficulty in this area is the definition and especially the **documentation of APIs** 📑. So if you set up a Web service with an API and you want to open your service to the outside, please take the time to document your API.

Fortunately, FastAPI does all the heavy lifting for us (more on this later)

We find online plenty of open APIs a link to have a non-exhaustive list

`````{div}
:class: columns
````{div}
:class: fifty center
[https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)  
ou   
[http://bit.ly/3YHC1qX](http://bit.ly/3YHC1qX)  
ou  
```{image} media/qrcode/public_api_qr.png
:width: 40%
```
````

````{div}
:class: fifty center
notably an example of useful API<br> <https://data.geopf.fr/geocodage/openapi>
````
`````

---

## Illustration

Consider for example the case of a server generating lists of random numbers on demand. The API of such a server could be

- `/api/integer` returns a random integer
- `/api/float` returns a random floating number
- `/api/integer?n=100` returns 100 random integers
- ...

```{div}
:class: center
it happens in the `python/api-random` folder of the course
```

---

## For example

````{div}
:class: center
Here's how to generate some statistics on Github directly in Markdown
````

```md
![Basile's GitHub stats](https://github-readme-stats.vercel.app/api?username=basileMarchand&count_private=true&show_icons=true&theme=dark)
![Basile's top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=basileMarchand&hide=jupyter%20notebook&langs_count=10&theme=dark&layout=compact)
```

`````{div}
:class: columns
````{div}
:class: fifty center
![Basile's GitHub stats](https://github-readme-stats.vercel.app/api?username=basileMarchand&count_private=true&show_icons=true&theme=dark)
````

````{div}
:class: fifty center
![Basile's top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=basileMarchand&hide=jupyter%20notebook&langs_count=10&theme=dark&layout=compact)
````
`````

---

## A word about "No Code"

For a few years increasingly fashionable: **No Code**, **Low Code**

````{div}
:class: center
```{image} media/make.png
:width: 50%
```
````

````{div}
:class: center
mail support request that causes a new entry in a database<br>and a mail notification if "urgent" in the mail subject 🤯
````

---

## warning

```{admonition} the following apps are outdated !
:class: danger

you can [skip to the end of this notebook](#next-week)
```

---

## Application 1

I have set up a minimalist server offering an API allowing:

1. List all users in the database
2. Update your status
3. Send a message to a user
4. Retrieve messages that were sent to me.

````{div}
:class: center
🚀 https://mines.bmarchand.fr/api/doc 🚀
````

--

The idea is that you perform the following actions:

1. Using a Python 🐍 program:
   1. make a `GET` request to find what your user ID is
   2. make a `PATCH` request to update your status
   3. make `GET`/`POST` requests to send messages between you
2. For the more playful, using the HTML/CSS/JS combo
   1. Make the web client of this server 🤗!

---

## Application 2: using the Notion API

The objective here is to set up a Python program allowing to modify the content of a Notion database. **[A skeleton is available here](https://github.com/ue22-p24/backend-notion-api-skeleton)**. The application in the end must be able to:

`````{div}
:class: columns smaller

````{div}
:class: sixty
- List all tasks in a database
- Display the detail of a task defined by its ID
````
````{div}
:class: fourty
- Change the status of a task
- Add text to the task page
````
`````

---

`````{div}
:class: columns

````{div}
:class: fifty

**Step 1️⃣**: create a database in Notion  
[you can duplicate this one](https://bmarchand.notion.site/04620d6c67274d8e96211ddc738acf76?v=31bcb2e38fa242cfbc8eb9c51eca6108)

**Step 2️⃣**: create a Notion integration  
Go to the site [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and create an integration

```{image} media/notion-token.png
:width: 80%
```
````

````{div}
:class: fifty
**Step 3️⃣**: add the database to the integration created previously  
from the database page

```{image} media/notion-db-to-integ.png
:width: 45%
```

**Step 4️⃣**: retrieve the database ID  
```{image} media/notion-db-id.png
```
````
`````

---

## Next week❕

We go to the dark side, and we see how to define our APIs

````{div}
:class: center
```{iframe} https://giphy.com/embed/6x4CLjC8KofaU
<!-- :width: 469" height="380" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> -->
````
