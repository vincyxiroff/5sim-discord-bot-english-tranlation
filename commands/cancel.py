#imports
import requests, discord, datetime, json, config as CONFIG
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime
#imports

#semi-config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents = intents)
bot.remove_command('help')
token = (CONFIG.API_TOKEN)
headers = {
    
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}
#semi-config
Activation  =  False
#code
@bot.command()
async def cancel_order(ctx, id=None):
    if id is None:
        await ctx.send("🆔 You must provide the order ID to use this command.")
        return    
    r = requests.get(f'https://5sim.net/v1/user/cancel/{id}', headers=headers)
    
    if r.status_code == 200:
        r = json.loads(r.text)
        embed = discord.Embed(
            title=':no_entry: Canceled!',
            colour=discord.Color.red()
        )
        
        embed.add_field(name='Order ID', value=r['id'], inline=True)
        embed.add_field(name='Country', value=r['country'], inline=True)
        embed.add_field(name='Número', value=r['phone'], inline=True)
        embed.add_field(name='Price', value=r['price'], inline=True)
        embed.add_field(name='Product', value=r['product'], inline=True)
        embed.add_field(name='Status', value=r['status'], inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name='Result', value='Order canceled', inline=False)

        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title=':x: ERROR :x:',
            colour=discord.Color.red()
        )
        
        embed.add_field(name='Error', value='Order not found', inline=False)

        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_command(cancel_order)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀
