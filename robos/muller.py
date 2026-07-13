from pathlib import Path
import re

print("Robô Müller iniciado")

arquivo = Path("amostra_muller.html")

conteudo = arquivo.read_text(encoding="utf-8")

titulos = re.findall(
    r"<h5>(.*?)</h5>",
    conteudo,
    re.DOTALL
)

print(f"Títulos encontrados: {len(titulos)}")

for titulo in titulos[:20]:
    print(titulo.strip())
