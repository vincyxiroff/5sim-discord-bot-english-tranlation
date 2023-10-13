#imports
import discord, datetime, config as CONFIG
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime
#imports

#semi-config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents = intents)
bot.remove_command('help')
#semi-config
Activation  =  False
#code
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Comandos',
        description='🔥 **Lista de comandos disponibles:**',
        color=discord.Colour(0x87cbec)
    )
    embed.add_field(
        name="",
        value="\u200b",  
        inline=False
    )
    embed.add_field(
        name="💸 `?buy` | country | operator | producto",
        value="> **Buy a phone number.**",
        inline=True
    )
    embed.add_field(
        name="❌ `?cancel_order` | order ID",
        value="> **Cancel an order you have placed.**",
        inline=True
    )
    embed.add_field(
        name="🚩 `?finish_order` | order ID",
        value="> **Finalize an order after you have received the phone number.**",
        inline=True
    )
    embed.add_field(
        name="",
        value="\u200b",  
        inline=False
    )
    embed.add_field(
        name="🔎 `?check_order` | order ID",
        value="> **Check the status of an order.**",
        inline=True
    )
    embed.add_field(
        name="🎈 `?balance`",
        value="> **Revisa el balance de tu cuenta.**",
        inline=True
    )
    embed.add_field(
        name=" 💵 `?prices`",
        value="> **Revisa el precio de los números de teléfono (LycaMobile & Virtual34).**",
        inline=True
    )
    embed.add_field(
        name="",
        value="\u200b",  
        inline=False
    )
    embed.add_field(
        name=" 🚫 `?ban_order` | order ID",
        value="> **Banea una order cuando el número de teléfono cuándo el número esta baneado por discord.**",
        inline=True
    )    
    embed.add_field(
        name="💯 `?best_price` | producto",
        value="> **Consigue el mejor precio para un producto.**",
        inline=True
    )
    embed.add_field(
        name="⚔️ `?check_api`",
        value="> **Revisa si todo está funcionando correctamente.**",
        inline=True
    )
    await ctx.send(embed=embed)





def setup(bot):
    bot.add_command(help)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀
