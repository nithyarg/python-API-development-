from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
 
 
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i 

@app.get("/")
def read_root():
    return {"message": "Hello World"}  

@app.get("/posts")
def get_posts():
    return {"data":my_posts} 


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000) 
    my_posts.append(post_dict)
    return{"data": post_dict}



 
@app.get("/posts/{id}")
def get_post(id: int):
   
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return{"post_detail": post} 

@app.delete("/posts/{id}")
def delete_post(id: int): 
    # deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id)

    my_posts.pop(index)
    return {'message':'post was successfuly deleted'} 



