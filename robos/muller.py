import requests

print("=== ROBÔ MÜLLER ===")

url = "https://www.mullerleiloes.com.br/lotes/imovel"

response = requests.get(
    url,
    timeout=30,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status:", response.status_code)
print("HTML recebido:", len(response.text))
