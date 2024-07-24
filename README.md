#Discord-Bot

This repository contains a Discord bot implemented in Python using the `discord.py` library.
The bot performs various functions, including fetching images, generating ASCII art, retrieving Pokémon data, and providing weather information.

This bot automates several interactions and data retrieval processes within Discord:

Image and Meme Retrieval: Automates fetching and sending of images and memes based on user commands.
ASCII Art Generation: Automates the creation of visual text art.
Pokémon and Weather Information: Automates the retrieval and presentation of Pokémon data and weather updates.
Slot Machine Game: Simulates a slot machine game with an automated random result.
By automating these tasks, the bot provides a seamless and interactive experience for users, saving time and effort in obtaining information and entertainment.



## Features

- **Automated Image Retrieval**: Fetches random cat and dog pictures automatically from respective APIs.
- **Automated Meme Generation**: Retrieves random memes from a dedicated API.
- **Automated ASCII Art Creation**: Generates images of ASCII art based on input text.
- **Automated Pokémon Data Retrieval**: Fetches and displays Pokémon information using the PokeAPI.
- **Automated Weather Updates**: Provides weather information based on a zip code by integrating with weather and zip code APIs.
- **Slot Machine Simulation**: Automates a slot machine game with a chance-based outcome.

Install Dependencies:
'''
pip install discord requests pyfiglet python-dotenv pillow

discord.py for the Discord API wrapper.
pyfiglet for generating ASCII art.
Pillow for image processing.
Requests for making HTTP requests.

To manage sensitive info such as discord token use dotenv.

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
DISCORD_KEY = os.getenv('DISCORD_KEY')


Commands
$hello: Returns a greeting message.
$meme: Sends a random meme, automating the retrieval from an API.
$figlet <text>: Generates ASCII art from the given text, automating the art creation process.
$cat: Sends a random cat picture, fetched automatically from an API.
$dog: Sends a random dog picture, retrieved automatically.
$playJackpot: Simulates a slot machine game with an automated result.
$help: Displays a list of available commands and their usage.
$pokemon <pokemon_name>: Retrieves and displays Pokémon data based on the given name.
$weather <zip_code>: Retrieves and displays weather information based on a zip code.
$randomQuote: Sends a random quote, automating the quote retrieval.

API Endpoints
Cat API: https://api.thecatapi.com/v1/images/search
Dog API: https://dog.ceo/api/breeds/image/random
Meme API: https://meme-api.com/gimme
PokeAPI: https://pokeapi.co/api/v2/pokemon/{name}
Zip Code API: https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees
Weather API: https://api.weather.gov/points/{latitude},{longitude}/forecastHourly

I have used Discord embedded Formats to output some of its work.
Below I have shared some reference to Embedding.

Embedded formats, often referred to as "embeds" in the context of messaging platforms like Discord, are structured ways to display rich content. In Discord, an embed is a special type of message that includes a variety of elements such as titles, descriptions, fields, images, and colors. Embeds are used to present information in a visually appealing and organized manner.

Key Components of Discord Embeds:

Title: The main heading of the embed.
Description: A detailed description or content that follows the title.
Fields: Sections within the embed that can contain additional information, often in a key-value format.
Image: A visual element that can be included to enhance the message.
Thumbnail: A smaller image that appears in the corner of the embed.
Color: A border color that can be customized to match the theme or highlight important information.
Creating Embedded Formats
In Discord bots, embeds are often created programmatically using libraries such as discord.py. For example, to create an embed in discord.py, you use the discord.Embed class, which allows you to set the title, description, fields, and other properties.

Here's a basic example of creating an embed in discord.py:

python
Copy code
import discord

embed = discord.Embed(
    title="Sample Embed",
    description="This is a description of the embed.",
    color=discord.Color.blue()
)
embed.add_field(name="Field 1", value="This is the value of field 1", inline=True)
embed.add_field(name="Field 2", value="This is the value of field 2", inline=True)
embed.set_image(url="https://example.com/image.png")

# Sending the embed to a channel
await message.channel.send(embed=embed)

https://plainenglish.io/blog/send-an-embed-with-a-discord-bot-in-python

License:
This project is licensed under the MIT License.


By: Dinesha Shair
