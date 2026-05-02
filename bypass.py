import requests
import time
from bs4 import BeautifulSoup
import re

class AlpharedeBypass:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://alpharede.com/',
        })

    def bypass(self, url):
        print(f"[*] Iniciando bypass para: {url}")
        
        try:
            # 1. Acessar o link inicial
            res = self.session.get(url, allow_redirects=True, timeout=15)
            
            # Loop para as etapas (geralmente 5)
            for step in range(1, 8):
                print(f"[*] Processando etapa {step}...")
                
                # Se chegamos ao MediaFire, retornamos imediatamente
                if "mediafire.com" in res.url:
                    print(f"[+] MediaFire detectado: {res.url}")
                    return res.url

                # Aguardar o timer do site (simulando comportamento humano)
                time.sleep(12) 
                
                soup = BeautifulSoup(res.text, 'html.parser')
                
                # ESTRATÉGIA: Procurar pelo botão que contém "Continuar" ou "Get Link"
                found_next = False
                
                # 1. Tentar encontrar links que contenham palavras-chave de redirecionamento
                links = soup.find_all('a', href=True)
                for link in links:
                    href = link['href']
                    text = link.get_text().upper()
                    
                    # Ignorar links de navegação comuns do blog
                    if any(x in href for x in ["/about", "/contact", "/policy", "/terms", "/topics", "/popular"]):
                        continue
                        
                    # Se o texto do link parece um botão de continuar
                    if any(x in text for x in ["CONTINUAR", "GET LINK", "PROXIMO", "CLIQUE", "AVANTE"]):
                        print(f"[*] Botão encontrado: {text} -> {href}")
                        if "mediafire.com" in href:
                            return href
                        res = self.session.get(href, timeout=15)
                        found_next = True
                        break
                
                if found_next: continue

                # 2. Tentar encontrar formulários de redirecionamento
                forms = soup.find_all('form')
                for form in forms:
                    action = form.get('action')
                    if action:
                        data = {i.get('name'): i.get('value', '') for i in form.find_all('input') if i.get('name')}
                        res = self.session.post(action, data=data, timeout=15)
                        found_next = True
                        break
                
                if found_next: continue
                
                # 3. Se não encontrou nada e já passou de algumas etapas, pode ser que o link final esteja na página
                if step > 3:
                    for link in links:
                        if "mediafire.com" in link['href']:
                            return link['href']

                # Se chegamos aqui sem encontrar o próximo passo, paramos para não entrar em loop infinito
                if not found_next:
                    print(f"[!] Fim do fluxo ou botão não encontrado na etapa {step}")
                    # Verifica se a URL atual já é o destino (não forumdinheiro/alpharede)
                    if "forumdinheiro.com" not in res.url and "alpharede.com" not in res.url:
                        return res.url
                    break

            return res.url
        except Exception as e:
            print(f"[!] Erro durante o bypass: {e}")
            return None

if __name__ == "__main__":
    test_url = "https://alpharede.com/yeIQFvd5Suj"
    bypasser = AlpharedeBypass()
    print(f"Resultado: {bypasser.bypass(test_url)}")
