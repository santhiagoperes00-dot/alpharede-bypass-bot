# 🚀 Alpharede Bypass Bot (Square Cloud Ready)

Este é um bot profissional desenvolvido para burlar automaticamente as 4 a 5 etapas de encurtadores como `alpharede.com` e `forumdinheiro.com`. Ele simula o comportamento humano, aguarda os timers e extrai o link final sem que você precise clicar em nada.

## 🛠️ Funcionalidades
- **Bypass Automático:** Pula todas as etapas de anúncios e timers.
- **Multi-Etapas:** Lida com o fluxo de 5 páginas seguidas.
- **Pronto para Square Cloud:** Configuração otimizada para baixo consumo de memória.
- **Interface via Discord:** Comando simples para obter o link.

## 📦 Como Instalar

### 1. Preparar o Bot no Discord
1. Vá ao [Discord Developer Portal](https://discord.com/developers/applications).
2. Crie uma nova aplicação e um Bot.
3. Ative a opção **Message Content Intent** na aba "Bot".
4. Copie o **Token** do seu bot.

### 2. Hospedar na Square Cloud
1. Crie um arquivo `.zip` com todos os arquivos deste repositório.
2. No painel da [Square Cloud](https://squarecloud.app/), clique em "Upload".
3. Após o upload, vá em **Variáveis de Ambiente** (Configurações).
4. Adicione uma variável chamada `DISCORD_TOKEN` e cole o seu token.
5. Inicie o bot.

## 🚀 Como Usar
No seu servidor do Discord, use o comando:
```
!bypass https://alpharede.com/seu-link
```
O bot responderá em cerca de 60 segundos com o link de destino final.

## 📄 Arquivos Inclusos
- `main.py`: Código principal do bot Discord.
- `bypass.py`: O "motor" que faz a mágica de burlar o link.
- `squarecloud.app`: Arquivo de configuração da Square Cloud.
- `requirements.txt`: Lista de bibliotecas necessárias.

---
**Aviso:** Este projeto foi criado para fins educacionais e de automação pessoal. Use com responsabilidade.
