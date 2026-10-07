from playwright.sync_api import sync_playwright
import os
d=os.getcwd()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    for n in ['kids','parents','timeline']:
        pg=b.new_page(); pg.goto(f'file://{d}/{n}.html'); pg.pdf(path=f'{n}.pdf',prefer_css_page_size=True,print_background=True)
    b.close()
