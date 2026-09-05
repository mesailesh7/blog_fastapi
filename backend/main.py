from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
    {
        "id": 3,
        "author": "John Smith",
        "title": "Async Operations in Modern Python",
        "content": "Understanding async and await can dramatically improve your API performance under heavy load.",
        "date_posted": "April 22, 2025",
    },
    {
        "id": 4,
        "author": "Alex Rivera",
        "title": "Pydantic V2 Deep Dive",
        "content": "Data validation with Rust-backed Pydantic feels instantaneous compared to older patterns.",
        "date_posted": "April 24, 2025",
    },
    {
        "id": 5,
        "author": "Taylor Swift",
        "title": "Deploying Microservices with Docker",
        "content": "Containerizing your backend ensures consistent environments from local staging to production.",
        "date_posted": "April 25, 2025",
    },
]


# @app.get("/", response_class=HTMLResponse, include_in_schema=False)
# @app.get("/posts", response_class=HTMLResponse,include_in_schema=False)
# def home():
#     return f"<h1>{posts[0]['title']}</h1>"

@app.get("/",  include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})




@app.get("/api/posts")
def get_posts():
    return posts