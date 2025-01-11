from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users: List["User"] = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=5,
            max_length=20,
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=18,
            le=120,
            example=24
        )
    ]
):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        str,
        Path(
            title="Enter User ID",
            example="1"  # Пример user_id
        )
    ],
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=5,  # Минимальная длина имени: 5 символов
            max_length=20,  # Максимальная длина имени: 20 символов
            example="UrbanProfi"  # Пример имени
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=18,  # Минимальный возраст: 18
            le=120,  # Максимальный возраст: 120
            example=28  # Пример возраста
        )
    ]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[
        str,
        Path(
            title="Enter User ID",
            example="2"  # Пример user_id
        )
    ]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")