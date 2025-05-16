import flet as ft
import httpx
import asyncio

async def fetch_classes(e, number):
    try:  
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://127.0.0.1:8000/search{number.value}")
            data = response.json()
            print(data)
            number.helper_text=data['message']
            number.update()
    except Exception as ex:
        print(f"Error: {ex}")

def main(page: ft.Page):
    page.window.always_on_top=True
    number = ft.TextField(
        width=300,
        on_submit=lambda e: asyncio.run(fetch_classes(e, number))
    )
    
    page.add(number)

ft.app(main)