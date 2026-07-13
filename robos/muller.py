import os
import re
from pathlib import Path

from supabase import create_client

print("=== MULLER -> SUPABASE ===")

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

supabase = create_client(url, key)

arquivo = Path("amostra_muller.html")

conteudo = arquivo.read_text(encoding="utf-8")

links = sorted(
    set(
        re.findall(
            r"/item/\d+/detalhes\?page=1",
            conteudo
        )
    )
)

titulos = re.findall(
    r"<h5>(.*?)</h5>",
    conteudo,
    re.DOTALL
)

titulos = [
    t.strip()
    for t in titulos
    if t.strip() != "Lance Inicial"
]

cidades = re.findall(
    r"<b>Cidade:</b>\s*([^<]+)",
    conteudo
)

enderecos = re.findall(
    r"<br><b>Endereço:</b>\s*([^<]+)",
    conteudo
)

quantidade = min(
    len(links),
    len(titulos),
    len(cidades),
    len(enderecos)
)

print(f"Imóveis encontrados: {quantidade}")

titulo = titulos[0]
cidade = cidades[0].strip()
endereco = enderecos[0].strip()
link = links[0]

tipo = "OUTRO"

if "APARTAMENTO" in titulo.upper():
    tipo = "APARTAMENTO"
elif "CASA" in titulo.upper():
    tipo = "CASA"
elif "TERRENO" in titulo.upper():
    tipo = "TERRENO"

dados = {
    "titulo": titulo,
    "tipo_imovel": tipo,
    "cidade": cidade,
    "endereco": endereco,
    "url_lote": f"https://www.mullerleiloes.com.br{link}",
    "leiloeiro": "MULLER",
    "status": "ATIVO",
    "fonte_id": 1
}

resultado = supabase.table("imoveis").insert(dados).execute()

print("Imóvel inserido com sucesso")
print(titulo)
