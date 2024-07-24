import discord
import requests
import json
from pyfiglet import Figlet
import random
import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import io

# Load environment variables
load_dotenv()

# DISCORD_KEY = "Your_Discord_Bot_token"
# API endpoints
BASEZIP_API = "https://www.zipcodeapi.com/rest/"
ZIP_APIKEY = "saeLYP6mua1UbZ0gVDSiX6M4nYLhUxoODxtsrGW1wpe1dGV6zary0ByHrtLX03Ub"
FORECAST_API = "https://api.weather.gov/points/"


# Method to get Cat picture
def getCat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    jsonData = json.loads(response.text)
    return jsonData[0]["url"]  # Access the first element to get the URL

def getDog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    jsonData = json.loads(response.text)
    return jsonData["message"]

# Method to get figlets
def getFiglet(messageFull):
    f = Figlet(font='digital')
    ascii_art = f.renderText(messageFull)
    
    # Create image from ASCII art
    font = ImageFont.load_default()
    dummy_image = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_image)
    bbox = draw.textbbox((0, 0), ascii_art, font=font)
    width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    image = Image.new('RGB', (width, height), color=(73, 109, 137))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ascii_art, fill=(255, 255, 255), font=font)
    
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        image_data = output.getvalue()
    
    return image_data


# Method to get Memes
def getMeme():
    response = requests.get("https://meme-api.com/gimme")
    jsonData = json.loads(response.text)
    return jsonData["url"]

# Method to get pokemon embed
def getPokemon(name):
    # Construct the URL with the provided Pokemon name
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    # Send GET request to PokeAPI
    response = requests.get(url)
    if response.status_code == 200:
        # parse JSON response
        jsonData = response.json()
        # Extract name, weight, types, and sprite URL
        pokemonName = jsonData['name']
        pokemonWeight = jsonData["weight"]
        # Extracting types
        types = [type_data['type']['name'] for type_data in jsonData['types']]
        # Extracting Sprites URL
        spriteUrl = jsonData["sprites"]["front_default"]
        pokemon_embed = discord.Embed(title=f"{pokemonName.capitalize()} Data", color=discord.Color.blue())
        pokemon_embed.add_field(name="Name", value=pokemonName.capitalize(), inline=True)
        pokemon_embed.add_field(name="Weight", value=pokemonWeight, inline=True)
        pokemon_embed.add_field(name="Types", value=", ".join(types), inline=False)
        pokemon_embed.set_image(url=spriteUrl)

        return pokemon_embed
    else:
        return "Wrong input for valid Pokemon, Try Again!"

    # Method gets a quote
def getQuote():
    response = requests.get("https://api.quotable.io/quotes/random")
    jsonData = json.loads(response.text)
    if response.status_code != 200:
        return "Could not fetch quote"
    quote = jsonData[0]["content"]
    author = jsonData[0]["author"]
    embed = discord.Embed(title="Random Quote", description=f"{quote}\n\n— {author}", color=discord.Color.green())
    return embed
    
# Function to fetch weather data using the integrated method
def fetchWeather(zipCode):
    try:
        # Fetch latitude and longitude using zipcodeapi.com
        endpoint = f"/info.json/{zipCode}/degrees"
        url = f"{BASEZIP_API}{ZIP_APIKEY}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()

        # Extract latitude, longitude, city, and state
        latitude = data["lat"]
        longitude = data["lng"]
        city = data["city"]
        state = data["state"]

        # Fetch forecast URL using weather.gov
        endpoint = f"{latitude},{longitude}"
        url = f"{FORECAST_API}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        forecastData = response.json()

        # Extract forecast URL
        forecastUrl = forecastData["properties"]["forecastHourly"]

        # Fetch current temperature and image URL from forecast hourly endpoint
        response = requests.get(forecastUrl)
        response.raise_for_status()
        hourlyForecastData = response.json()

        # Extract current temperature and image URL
        firstPeriod = hourlyForecastData["properties"]["periods"][0]
        temperature = firstPeriod["temperature"]
        imageUrl = firstPeriod["icon"]

        return city, state, temperature, imageUrl

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None, None, None

# Function to generate Discord embed with weather information
def getWeather(zipCode):
    city, state, temperature, image_url = fetchWeather(zipCode)

    if city and state and temperature is not None and image_url:
        embed = discord.Embed(title=f"Weather in {city}, {state}", description=f"Temperature: {temperature} °F", color=discord.Color.blue())
        embed.set_thumbnail(url=image_url)
        return embed
    else:
        return "Failed to fetch weather data. Please try again later."
        
# Play Jackpot
def playJackpot():
    slotList = ['🍒', ' 🍇', '🍉', '7️⃣']
    # Using random library choosing three pick
    # if equals we return the result
    result = random.choices(slotList, k=3)
    if result[0] == result[1] and result[0] == result[2]:
        resultString = "".join(result) + " Jackpot!!!"  # Append to list
    else:
        resultString = "".join(result) + " Thanks for playing!"  # Append to list
    embed = discord.Embed(title="Jackpot Result", description=resultString, color=discord.Color.gold())
    return embed
    
class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
    async def on_message(self, message):
        # if message.author == self.user:
         #   return
        if message.content.startswith("$hello"):
            await message.channel.send("Hello User!")
        elif message.content.startswith("$meme"):
            await message.channel.send(getMeme())
        elif message.content.startswith("$figlet"):
            fullMessage = message.content
            image_data = getFiglet(fullMessage[8:])
            file = discord.File(io.BytesIO(image_data), filename="figlet.png")
            await message.channel.send(file=file)
        elif message.content.startswith("$cat"):
            await message.channel.send(getCat())
        elif message.content.startswith("$dog"):
            await message.channel.send(getDog())
        elif message.content.startswith("$playJackpot"):
            await message.channel.send(embed=playJackpot())
        elif message.content.startswith("$help"):
            helpText = """
            *****DINDAN Bot Commands:*****
            $hello - returns hello user
            $meme - sends a meme to the user
            $figlet - to get creative style or the writing
            $cat - get a cat picture
            $dog - get a dog picture
            $playJackpot - runs slot once
            $help - to get help
            $pokemonNameOfPokemon - get pokemon card {ex: $pokemonCharizard}
            $weather zip - get weather data card {$weather 30605}
            """
            await message.channel.send(helpText)
        elif message.content.startswith("$pokemon"):
            fullMessage = message.content
            # Get the full content of the message
            pokemon_embed = getPokemon(fullMessage[8:])
            # Extract the Pokemon name from the message
            if isinstance(pokemon_embed, discord.Embed):
                await message.channel.send(embed=pokemon_embed)
                # Send the embed if Pokemon data is found
            else:
                await message.channel.send(pokemon_embed)
                # Send the error message if Pokemon data is not found
        elif message.content.startswith("$weather"):
            fullMessage = message.content
            zipCode = fullMessage[8:]
            zipCode = zipCode.strip()
            weather_embed = getWeather(zipCode)
            if isinstance(weather_embed, discord.Embed):
                await message.channel.send(embed=weather_embed)
            else:
                await message.channel.send(weather_embed)
        elif message.content.startswith("$randomQuote"):
            await message.channel.send(embed=getQuote())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_KEY)
