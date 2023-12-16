import asyncio
import io
import random
from collections import defaultdict

import discord
import requests

import image_utils

WILD_POKEMON_COLOR = (200, 150, 50)
POKEDEX_COLOR = (200, 50, 50)
POKEMON_EVERY_SECONDS = 20
N_POKEMONS = 151
RESIZE_TO = (40, 40)


def load_images():
    pokemon_id = 0  # for final print if N_POKEMONS <= 0

    for pokemon_id in range(1, N_POKEMONS + 1):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/')
        data = response.json()
        if 'mime' in data['name']:
            name = 'Mr. Mime'
        else:
            name = data['name'].title()
        image_url = data['sprites']['other']['official-artwork']['front_default']
        image = requests.get(image_url).content
        pokemons.append({'id': data['id'], 'name': name, 'image': image, 'thumbnail': image_utils.resize(image, RESIZE_TO)})
        if pokemon_id % 10 == 0:
            print(f'{pokemon_id} pokémons cargados.')

    print(f'{pokemon_id} pokémons cargados.')


async def run_pokegame(message: discord.Message):
    while True:
        current_pokemons[message.channel.id] = random.choice(pokemons)
        embed = discord.Embed(
            title='¡Un pokémon salvaje apareció!',
            description='¡Escribe su nombre para capturarlo!',
            color=discord.Color.from_rgb(*WILD_POKEMON_COLOR)
        )
        thumbnail_file = discord.File('images/pokeball.png', filename='pokeball.png')
        embed.set_thumbnail(url='attachment://pokeball.png')
        image_file = discord.File(fp=io.BytesIO(current_pokemons[message.channel.id]['image']), filename='pokemon.png')
        embed.set_image(url='attachment://pokemon.png')
        await message.channel.send(files=[thumbnail_file, image_file], embed=embed)

        await asyncio.sleep(POKEMON_EVERY_SECONDS)


async def show_pokedex(message: discord.Message):
    caught_pokemon_ids = users_pokedex[message.author.id]
    embed = discord.Embed(
        title=f'Pokédex de {message.author.name}.',
        description=f'Has atrapado {len(caught_pokemon_ids)} pokémons.',
        color=discord.Color.from_rgb(*POKEDEX_COLOR)
    )
    thumbnail_file = discord.File('images/pokedex.png', filename='pokedex.png')
    embed.set_thumbnail(url='attachment://pokedex.png')
    images = (pokemon['image'] for pokemon in pokemons)
    image_file = discord.File(fp=io.BytesIO(image_utils.collection(images, caught_pokemon_ids)), filename='caught_pokemons.png')
    embed.set_image(url='attachment://caught_pokemons.png')

    await message.channel.send(files=[thumbnail_file, image_file], embed=embed)


pokemons: list[dict] = []
current_pokemons: defaultdict[int, dict] = defaultdict(dict)
users_pokedex: defaultdict[int, set[int]] = defaultdict(set)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} activado (id: {client.user.id}).')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.content.startswith('/start'):
        asyncio.create_task(run_pokegame(message))
        return

    if message.content.startswith('/pokedex'):
        await show_pokedex(message)

    current_pokemon = current_pokemons[message.channel.id]
    if current_pokemon and current_pokemon['name'].lower() == message.content.strip().lower():
        current_pokemons[message.channel.id] = {}
        await message.channel.send(f'¡{message.author.name} ha capturado un {current_pokemon['name']}!')
        users_pokedex[message.author.id].add(current_pokemon['id'])


load_images()
client.run('bot token')
