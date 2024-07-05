from typing import Union
from fastapi import FastAPI, HTTPException, Request, Response
from Models.Item import Item
from fastapi.middleware.cors import CORSMiddleware
from Utils.verifyUrlFormat import verify_url_format

from Service.UrlShortenerService import UrlShortenerService
urlShortenerService = UrlShortenerService()
from Service.UserService import UserService

userService = UserService()


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(request: Request, response: Response):
    from Service.UserService import UserService

    print(request.cookies, "cookies")
    userService = UserService()

    if "id" in request.cookies:
        try:
            id = userService.verify_user(request.cookies["id"])
            return userService.get_user_and_urls(request.cookies["id"])
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        try:
            user_id = userService.create_user()
            response.set_cookie(key="id", value=user_id)
            return {"message": "User created successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@app.post("/shortUrl")
def main(item: Item, request: Request, response: Response):

    verify_url = verify_url_format(item.url)

    print(verify_url, "verify_url")

    if not verify_url["res"]:
        raise HTTPException(status_code=400, detail=verify_url["message"])

    try:
        if "id" in request.cookies and userService.verify_user(request.cookies["id"]):
            user_id = request.cookies["id"]
        else:
            user_id = userService.create_user()
            response.set_cookie(key="id", value=user_id)

        short_url = urlShortenerService.shorten(item.url, user_id)
        return {"url": short_url}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.post("/originalUrl")
def get_original_url(item: Item):
    try:
        return {"url": urlShortenerService.get_original_url(item.url)}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
