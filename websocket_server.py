import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение: {message}")
        response = f"Сервер получил: {message}"
        await websocket.send(response)  # Отправляем ответ


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())


# import asyncio
# from websockets.asyncio.server import serve
#
# # Обработчик входящих сообщений
# async def echo(websocket):
#     async for message in websocket:
#         print(f"Получено сообщение: {message}")
#         response = f"Сервер получил: {message}"
#         await websocket.send(response)
#
# # Запуск WebSocket-сервера на порту 9001
# async def main():
#     # Важно: используем '127.0.0.1', чтобы браузер точно сопоставил localhost
#     async with serve(echo, "127.0.0.1", 9001) as server:
#         print("WebSocket сервер запущен на ws://localhost:9001")
#         await asyncio.get_running_loop().create_future()
#
# if __name__ == "__main__":
#     asyncio.run(main())


