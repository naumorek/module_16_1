from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def root():
    return {"Главная страница"}



@app.get("/user/{username}/{age}")
async def read_username_age(username: str, age: int)-> dict:
    return {"User":username,"age": age}

@app.get("/user/admin")
async def id_admin():
    return {"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def id_user(user_id):
    return {f"Вы вошли как пользователь № {user_id}"}


