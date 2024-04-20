from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel 
from random import randrange   

app = FastAPI()


class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts= [{"title" :"title of post 1","content": "content of post 1", "id":1},
                {"title" : "favorite foods", "content": "I like pizza","id":2}]


@app.get("/")
def read_root():
    return {"message": "Hello World"}  

@app.get("/posts")
def get_posts():
    return {"data":my_posts} 


@app.post("/posts")
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000) 
    my_posts.append(post_dict)
    return{"data": post_dict}