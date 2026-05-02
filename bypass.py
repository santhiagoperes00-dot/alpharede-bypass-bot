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
        })

    def bypass(self, url):
        print(f"[*] Iniciando bypass para: {url}")
        
        # 1. Acessar o link inicial do alpharede
        res = self.session.get(url, allow_redirects=True)
        current_url = res.url
        
        # Loop para as 5 etapas
        for step in range(1, 6):
            print(f"[*] Processando etapa {step}/5...")
            soup = BeautifulSoup(res.text, 'html.parser')
            
            # Simular o clique no anúncio (enviar sinal de validação se houver)
            # No caso do alpharede/forumdinheiro, ele muitas vezes valida via cookies ou tempo de foco
            # Vamos simular o tempo de espera
            time.sleep(10) 
            
            # Tentar encontrar o botão de continuar ou o próximo link
            # O link de "Continuar" geralmente é um formulário ou um link com token
            next_step_found = False
            
            # Procurar por links que pareçam ser o próximo passo
            for a in soup.find_all('a', href=True):
                if 'forumdinheiro.com' in a['href'] and a['href'] != current_url:
                    current_url = a['href']
                    res = self.session.get(current_url)
                    next_step_found = True
                    break
            
            if not next_step_found:
                # Se não encontrar link, pode ser um redirecionamento via JS ou o link final
                if "alpharede.com" not in current_url and "forumdinheiro.com" not in current_url:
                    print(f"[+] Link final encontrado: {current_url}")
                    return current_url
                
                # Tentar extrair link final de scripts
                match = re.search(r'window\.location\.href\s*=\s*["\']([^"\']+)["\']', res.text)
                if match:
                    final_url = match.group(1)
                    print(f"[+] Link final extraído: {final_url}")
                    return final_url

        return current_url

if __name__ == "__main__":
    # Teste simples
    test_url = "https://alpharede.com/yeIQFvd5Suj"
    bypasser = AlpharedeBypass()
    result = bypasser.bypass(test_url)
    print(f"Resultado: {result}")
