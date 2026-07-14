from playwright.sync_api import sync_playwright

print("Iniciando Playwright")

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page()

    page.goto(
        "https://www.mullerleiloes.com.br/lotes/imovel",
        wait_until="networkidle",
        timeout=60000
    )

    print("Título da página:")
    print(page.title())

    print("URL final:")
    print(page.url)

    browser.close()
