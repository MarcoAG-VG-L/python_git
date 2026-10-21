import requests


respuesta = requests.get("https://example.com", timeout=10)
respuesta.raise_for_status()
print("Contenido de https://example.com:")
print(respuesta.text)
