from playwright.sync_api import sync_playwright

print("Iniciando Playwright")

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page()

    page.goto(
        "https://www.mullerleiloes.com.br/lotes/imovel",
        wait_until="domcontentloaded",
        timeout=120000
    )

    print("Aguardando Cloudflare...")

    page.wait_for_timeout(20000)

    print("Título:")
    print(page.title())

    print("URL:")
    print(page.url)

    html = page.content()

    print("HTML:")
    print(len(html))

    if "APARTAMENTO" in html.upper():
        print("SUCESSO - ENCONTROU IMOVEIS")
    else:
        print("AINDA BLOQUEADO")

    browser.close()
