# Finishline Scraper
A Discord bot that scrapes Finishline products from the release calendar.

This was a quick project that I created to get the product IDs of upcoming Finishline releases through the release calendar. The project makes use of Finishline's mobile API to scrape product data and the Discord API to relay product data over Discord.

The bot commands are `!fnl [index]` to get individual product information, `!fnl_feed [amount]` to get batch product information, and `!fnl_range [start_index] [end_index]` to get product information within a certain range. 

To run this bot, edit the bot token in `config.json`.
