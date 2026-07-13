from pathlib import Path
import re

print("=== ROBÔ MÜLLER ===")

arquivo = Path("amostra_muller.html")
conteudo = arquivo.read_text(encoding="utf-8")

links = sorted(set(
    re.findall(
        r"/item/\d+/detalhes\?page=1",
        conteudo
    )
))

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

for i in range(min(10, quantidade)):

    titulo = titulos[i]
    cidade = cidades[i].strip()
    endereco = enderecos[i].strip()

    tipo = "OUTRO"

    if "APARTAMENTO" in titulo.upper():
        tipo = "APARTAMENTO"

    elif "CASA" in titulo.upper():
        tipo = "CASA"

    elif "TERRENO" in titulo.upper():
        tipo = "TERRENO"

    imovel = {
        "tipo": tipo,
        "titulo": titulo,
        "cidade": cidade,
        "endereco": endereco,
        "link": links[i]
    }

    print(imovel)
