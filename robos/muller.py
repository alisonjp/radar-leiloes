from pathlib import Path
import re

print("Robô Müller iniciado")

arquivo = Path("amostra_muller.html")

conteudo = arquivo.read_text(encoding="utf-8")

links = sorted(set(
    re.findall(r"/item/\d+/detalhes\?page=1", conteudo)
))

print(f"Links encontrados: {len(links)}")

for link in links[:20]:
    print(link)
