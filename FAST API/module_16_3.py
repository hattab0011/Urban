from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

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
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя:{username}, Возраст:{age}"
    return f"User {new_id} is registered"

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
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    return f"User {user_id} not found"

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
    if user_id in users:
        # Удаляем пользователя
        del users[user_id]
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"