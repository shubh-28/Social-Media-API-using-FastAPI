from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

class Posts(BaseModel):
    title: str
    content: str 
    published: bool = True
    # rating: Optional[int] = None

app = FastAPI() 

my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1}, 
            {"title": "title of post 1", "content": "Content of post 1", "id": 1}]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Posts):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    print(post)
    return {"data": post_dict}