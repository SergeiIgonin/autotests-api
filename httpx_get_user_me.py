import httpx


# Данные для входа в систему
login_payload = {
    "email": "igonin_s@example.com",
    "password": "123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Формируем JWT Access-токена
token = login_response_data["token"]["accessToken"]
# Выводим токен
print("Access token:", token)

# Данные хэдера
header_payload = {
    "Authorization": f"Bearer {token}"
}

# Выполняем запрос на получение данных пользователя
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=header_payload)
response_data = response.json()

print("Response:", response_data)
print("Status Code:", response.status_code)
