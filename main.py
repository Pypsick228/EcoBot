import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
spisok = ["Вы знали ,что около 1/3 запасов алюминия используется для изготовления банок из-под колы?",
           "А вы знали ,что в условиях загрязнения птицы поют мелодичнее?Во время эксперимента исследователи кормили скворцов загрязнёнными червями. Со временем область мозга птиц, отвечающая за музицирование, увеличилась. Это позволило самцам петь более долгие и сложные рулады.",
           "Загрязненный воздух уменьшает мозг.В 2015 году провели исследование и оказалось ,что длительное воздействие загрязненного воздуха уменьшает объём мозга."]
@bot.command()
async def interesting_fact(ctx):
    fact = random.choice(spisok)
    await ctx.send(fact)
@bot.command()
async def ОбОзерах(ctx):
    await ctx.send("При загрязнении сточных озер вода может стать непригодной для питья(ясное дело).Осушение бессточных озёр может привести к засолению почв.")
@bot.command()
async def credits(ctx):
    await ctx.send("https://newsgomel.by")
@bot.command()
async def info(ctx):
    await ctx.send("!interesting_fact - выдает интересный фвакт о загрязнении окружающей среды./!сredits - источники./!ОбОзерах - информация об осушении/загрязнении озёр")
bot.run("XXX")
