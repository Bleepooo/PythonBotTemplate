import discord
import datetime
import random
import requests
import json
from discord.ext import commands, tasks

date = datetime.datetime.now().strftime("%m/%d/%y")
footer = f"Bot Template | {date}"
prefix = '.'

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = {prefix}, intents=intents)

@client.event
async def on_ready():
  print("logged in as")
  print(client.user.name)
  print("ID")
  print(client.user.id)
  status.start()
  
 @client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
          title = "❌ Error",
          description = "Missing required argument",
          colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)
  
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
          title = "❌ Error",
          description = f"Command not found. Please use {prefix}help for all commands.",
          colour = discord.Colour.red()
        )
        
        await ctx.send(embed=embed)

    if isinstance(error, commands.UserInputError):
        embed = discord.Embed(
          title = "❌ Error",
          description = "Incorrect Use",
          colour = discord.Colour.red()
        )
        
        await ctx.send(embed=embed)
      
    if isinstance(error, commands.CheckFailure): 
        embed = discord.Embed(
          title = "❌ Error",
          description = "Missing Permissions!",
          colour = discord.Colour.red()
          )
        await ctx.send(embed=embed)

@tasks.loop(seconds=60)
async def status():
  status = ['github.com/Bleepooo', 'youtube.com/c/bleepo']
  await client.change_presence(activity=discord.Game(random.choice(status)))

@client.command()
async def dog(ctx):
  url = 'https://dog.ceo/api/breeds/image/random'
  response = requests.get(url)
  json_data = response.json()
  danger = json_data['message']
  embed = discord.Embed(
    title = "Woof!",
    description = "",
    colour = discord.Colour.orange()
    )
  embed.set_image(url=f"{danger}")
  embed.set_footer(text=f"{footer}")
  await ctx.send(embed=embed) 

@client.command() 
@commands.has_permissions(kick_members = True)
async def mute(ctx, user : discord.Member, *, reason):
  guild = ctx.guild
  role = discord.utils.get(ctx.guild.roles, name = "Muted")

  for channel in guild.channels:
    await channel.set_permissions(role, send_messages=False, add_reactions=False)

  await user.add_roles(role)
  embed = discord.Embed(
        title = "✅ " f'{user.name}'" has muted for:",
        description = "'" f'{reason}' "'",
        colour = discord.Colour.green()
        )
  embed.set_thumbnail(url=f"{user.avatar_url}")
  embed.set_footer(text=f"{footer}")
  await ctx.send(embed=embed)  

@client.command() 
@commands.has_permissions(kick_members = True)
async def unmute(ctx, user : discord.Member):
  role = discord.utils.get(ctx.guild.roles, name = "Muted")
  await user.remove_roles(role)
  embed = discord.Embed(
        title = "✅ " f'{user.name}'" has been unmuted",
        description = "",
        colour = discord.Colour.green()
        )
  embed.set_thumbnail(url=f"{user.avatar_url}")
  embed.set_footer(text=f"{footer}")
  await ctx.send(embed=embed) 

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
  if amount >= 101:
    embed = discord.Embed(
          title = "❌ Oops! You can only purge 100 messages at a time!",
          description = "",
          colour = discord.Colour.red()
        )
    embed.set_footer(text=f"{footer}")
    await ctx.send(embed=embed)
  else:
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
          title = "✅ Purged " f'{amount}' " messages",
          description = "This message will auto delete in 5 seconds",
          colour = discord.Colour.green()
        )
    embed.set_footer(text=f"{footer}")
    await ctx.send(embed=embed, delete_after=5.0)
  
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, Reason=None):
  channel = await member.create_dm()
  name = ctx.guild.name
  embed = discord.Embed(
          title = f"{member}, you been kicked from {name} for:",
          description = f"{Reason}",
          colour = discord.Colour.red()
        )
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_footer(text=f"{footer}")
  await channel.send(embed=embed)
  await member.kick(reason=Reason)

  embed = discord.Embed(
          title = f"✅ {member} has been kicked for:",
          description = f"{Reason}",
          colour = discord.Colour.green()
        )
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_footer(text=f"{footer}")
  await ctx.send(embed=embed)
  
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, Reason=None):
  channel = await member.create_dm()
  name = ctx.guild.name 
  embed = discord.Embed(
          title = f"{member}, you been banned from {name} for:",
          description = f"{Reason}",
          colour = discord.Colour.red()
        )
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_footer(text=f"{footer}")
  await channel.send(embed=embed)
  await member.ban(reason=Reason)

  embed = discord.Embed(
          title = "✅ " f'{member}' " has been banned for:",
          description = "'" f'{Reason}' "'",
          colour = discord.Colour.green()
        )
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_footer(text=f"{footer}")
  await ctx.send(embed=embed)
  
client.run("token")
