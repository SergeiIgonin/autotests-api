import httpx

from tools.facers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)


# Из полученных данных пользователя извлекаем токен и на его основе формируем валидный хэдер для следующего GET запроса update_user
update_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "Vasya",
  "middleName": "string"
}

update_user_response = httpx.patch( f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers=update_user_headers, json=update_user_payload)
update_user_response_data = update_user_response.json()
print('Get user data:', update_user_response_data)
print(update_user_response.status_code)
