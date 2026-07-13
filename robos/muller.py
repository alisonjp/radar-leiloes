from pathlib import Path
import re

print("=== ROBÔ MÜLLER ===")

arquivo = Path("amostra_muller.html")

conteudo = arquivo.read_text(encoding="utf-8")

# LINKS
links = sorted(
    set(
        re.findall(
            r"/item/\d+/detalhes\?page=1",
            conteudo
        )
    )
)

# TITULOS
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

# CIDADES
cidades = re.findall(
    r"<b>Cidade:</b>\s*([^<]+)",
    conteudo
)

# ENDEREÇOS
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

print(f"\nImóveis encontrados: {quantidade}\n")

for i in range(min(15, quantidade)):

    titulo = titulos[i]
    cidade = cidades[i].strip()
    endereco = enderecos[i].strip()
    link = links[i]

    tipo = "OUTRO"

    titulo_upper = titulo.upper()

    if "APARTAMENTO" in titulo_upper:
        tipo = "APARTAMENTO"

    elif "CASA" in titulo_upper:
        tipo = "CASA"

    elif "TERRENO" in titulo_upper:
        tipo = "TERRENO"

    print("=" * 50)
    print(f"TIPO      : {tipo}")
    print(f"TITULO    : {titulo}")
    print(f"CIDADE    : {cidade}")
    print(f"ENDERECO  : {endereco}")
    print(f"LINK      : {link}")
