import discord
from discord.ext import commands
import os
from bypass import AlpharedeBypass

# Configurações do Bot
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def bypass(ctx, url: str):
    if "alpharede.com" not in url:
        await ctx.send("❌ Por favor, envie um link válido da Alpharede.")
        return

    msg = await ctx.send(f"⏳ Iniciando bypass de `{url}`... Isso pode levar cerca de 60 segundos.")
    
    try:
        bypasser = AlpharedeBypass()
        final_url = bypasser.bypass(url)
        
        if final_url:
            await msg.edit(content=f"✅ **Link Burlado com Sucesso!**\n🔗 Destino: {final_url}")
        else:
            await msg.edit(content="❌ Não foi possível burlar esse link no momento.")
    except Exception as e:
        await msg.edit(content=f"⚠️ Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    if not TOKEN:
        print("ERRO: DISCORD_TOKEN não configurado nas variáveis de ambiente.")
    else:
        bot.run(TOKEN)
