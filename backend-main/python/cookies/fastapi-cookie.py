"""
this app sets a cookie in the browser called 'visit'
that tracks the number of times the user has visited the page.

the FastAPI version of the cookie-setting server
somewhat shorter and simpler than the standard library version

NOTES:
- same defect as the standard library version: the counter increases TWICE per page load
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/{path:path}", response_class=HTMLResponse)
async def serve_with_cookie(path: str, request: Request):
    """
    display the number of times the page has been visited
    """

    cookies = request.cookies
    if "visit" in cookies:
        visit = int(cookies["visit"]) + 1
    else:
        visit = 0

    # the text to display
    if visit == 0:
        html = "<h1>Welcome for your first time here !</h1>"
    else:
        html = f"<h1>You have seen this page {visit} times !</h1>"
    html += f"this is the fastapi version - you were visiting path /<code>{path}</code> !"

    response = HTMLResponse(content=html)
    response.set_cookie(key="visit", value=str(visit))

    return response
