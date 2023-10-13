#imports
import discord, requests, config as CONFIG
from discord.ext import commands
from data import loggers 
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
@bot.command()
async def check_api(ctx):

    try:

        response = requests.get("https://5sim.net/v1/user/profile", headers=headers)
        embed = discord.Embed(title=":x: ERROR :x:", description="", colour=discord.Colour.red())

        if response.status_code == 200:
            embed = discord.Embed(title="✅ HECHO ✅", 
                                  description="", 
                                  colour=discord.Colour.green())
            embed.add_field(name="Request Perfect", 
                            value="Everything is working perfectly.")
            await ctx.send(embed=embed)

        if response.status_code == 401:
            embed.add_field(name=":x: ERROR :x:", 
                            value="Remember to put the api in the `config.py`.")
            await ctx.send(embed=embed)

        if response.status_code == 429:
            embed.add_field(name="⏰ TAKE A BREAK ⏰", 
                            value="You are under rate limit, wait a few minutes and try again. ")
            await ctx.send(embed=embed)

    except AttributeError:
        embed = discord.Embed(title=":x: ERROR :x:", 
                              description="", 
                              colour=discord.Colour.red())
        embed.add_field(name="[401] Unauthorized", value="Remember to put ur api key in the `config.py`.")
        await ctx.send(embed=embed)

    except Exception:
        raise Exception

def setup(bot):
    bot.add_command(check_api)
    







#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀


