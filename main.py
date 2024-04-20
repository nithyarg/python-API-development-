from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel    

app = FastAPI()


class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def read_root():
    return {"message": "Hello World"}  

@app.get("/posts")
def get_posts():
    return {"data":"This is your posts"} 


@app.post("/createposts")
def create_posts(new_post: post):
    print(new_post)
    print(new_post.rating) 
    return{"data":"new post"}