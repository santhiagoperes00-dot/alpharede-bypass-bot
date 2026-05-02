import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bypass import AlpharedeBypass

# Configuração de logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Token do Telegram (Configurado na Square Cloud)
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Eu sou o Alpharede Bypass Bot.\n\n"
        "Envie o comando `/bypass [link]` para pular as etapas do encurtador.\n"
        "Exemplo: `/bypass https://alpharede.com/yeIQFvd5Suj`"
    )

async def bypass_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Por favor, envie o link após o comando. Ex: `/bypass [link]`")
        return

    url = context.args[0]
    if "alpharede.com" not in url:
        await update.message.reply_text("❌ Por favor, envie um link válido da Alpharede.")
        return

    status_msg = await update.message.reply_text(f"⏳ Iniciando bypass... Isso leva cerca de 60 segundos (5 etapas).")
    
    try:
        bypasser = AlpharedeBypass()
        final_url = bypasser.bypass(url)
        
        if final_url:
            await status_msg.edit_text(f"✅ **Link Burlado com Sucesso!**\n\n🔗 **Destino:** {final_url}")
        else:
            await status_msg.edit_text("❌ Não foi possível burlar esse link no momento.")
    except Exception as e:
        await status_msg.edit_text(f"⚠️ Ocorreu um erro: {str(e)}")

if __name__ == '__main__':
    if not TOKEN:
        print("ERRO: TELEGRAM_TOKEN não configurado nas variáveis de ambiente.")
    else:
        application = ApplicationBuilder().token(TOKEN).build()
        
        start_handler = CommandHandler('start', start)
        bypass_handler = CommandHandler('bypass', bypass_command)
        
        application.add_handler(start_handler)
        application.add_handler(bypass_handler)
        
        print("Bot Telegram iniciado...")
        application.run_polling()
