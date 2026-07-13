import os
from supabase import create_client

print("=== TESTE SUPABASE ===")

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_ANON_KEY"]

supabase = create_client(url, key)

dados = {
    "titulo": "TESTE MULLER",
    "tipo_imovel": "APARTAMENTO",
    "cidade": "PORTO ALEGRE",
    "endereco": "RUA TESTE",
    "url_lote": "/teste",
    "leiloeiro": "MULLER",
    "status": "ATIVO"
}

resultado = supabase.table("imoveis").insert(dados).execute()

print("Inserido com sucesso")
