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
'''
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


Commands:

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

API Endpoints:

Cat API: https://api.thecatapi.com/v1/images/search
Dog API: https://dog.ceo/api/breeds/image/random
Meme API: https://meme-api.com/gimme
PokeAPI: https://pokeapi.co/api/v2/pokemon/{name}
Zip Code API: https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees
Weather API: https://api.weather.gov/points/{latitude},{longitude}/forecastHourly

License
This project is licensed under the MIT License - see the LICENSE file for details.

By: Dinesha Shair
