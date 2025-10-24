import discord
from discord import app_commands
import random
from bot_logic import *
from youtubesearchpython import VideosSearch

# Zmienna intents przechowuje uprawnienia bota
intents = discord.Intents.default()
# Tworzenie bota w zmiennej client i przekazanie mu uprawnień
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)



@client.event
async def on_ready():
    await tree.sync()  # synchronizacja komend globalnie
    print(f'Zalogowaliśmy się jako {client.user}')

@tree.command(name="ping", description="Odpowiada Pong!")
async def cmd_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! lol!!!")
@tree.command(name="moneta", description="Rzuca monetą")
async def cmd_moneta(interaction: discord.Interaction):
    wynik = monet()
    await interaction.response.send_message(f"Wynik rzutu monetą to: {wynik}")
@tree.command(name="mynt_sv", description="kastar svenska mynt")
async def cmd_moneta_sv(interaction: discord.Interaction):
    wynik = monet_sv()
    await interaction.response.send_message(f"Det blev: {wynik}")
@tree.command(name="losuj", description="Losuje liczbę z podanego zakresu")
@app_commands.describe(liczba="Podaj górną granicę zakresu losowania")
async def cmd_losuj(interaction: discord.Interaction, liczba: int):
    wynik = losuj_liczbe(liczba)
    await interaction.response.send_message(f"Wylosowana liczba z zakresu 1-{liczba} to: {wynik}")      
@tree.command(name="roll", description="rick roluje(it is rickrolling)")
async def cmd_roll(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.youtube.com/watch?v=dQw4w9WgXcQ")



async def on_member_join(member: discord.Member):
    # Kanał powitalny — możesz ustawić ID swojego kanału
    channel = discord.utils.get(member.guild.text_channels, name="powitania")
    if channel is not None:
        await channel.send(f"Witaj {member.mention} na serwerze! 🎉 Miłego pobytu.")
@tree.command(name="youtube", description="Szukaj filmów na YouTube")
@app_commands.describe(query="Czego szukasz?")
async def cmd_youtube(interaction: discord.Interaction, query: str):
    search = VideosSearch(query, limit=1)
    wynik = search.result()
    if wynik['result']:
        link = wynik['result'][0]['link']
        await interaction.response.send_message(f"Oto pierwszy wynik wyszukiwania dla '{query}': {link}")

client.run("YOUR_BOT_TOKEN_HERE")