from releasecalendar import ReleaseCalendar

import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")
client = discord.Client()


def create_finishline_embed(product):
    title = product["displayName"]
    color = product["colorDescription"]
    image = product["thumbnailUrl"]

    product_id = product["productId"]
    color_id = product["color"]
    style_id = product["style"]

    product_url = "https://www.finishline.com/store/product/-/{}?styleId={}&colorId={}".format(product_id, style_id,
                                                                                               color_id)

    embed = discord.Embed(title=title, description=color, url=product_url, color=int("045CFF", 16))
    embed.set_author(name="FINISHLINE", url="https://www.finishline.com/")
    embed.set_thumbnail(url=image)
    embed.set_footer(text="Finishline | Scraper", icon_url="https://i.ibb.co/HPjxcQX/elevatejd.png")
    embed.add_field(name="Product ID", value=product_id, inline=True)
    embed.add_field(name="Color ID", value=color_id, inline=True)
    embed.add_field(name="Style ID", value=style_id, inline=True)

    return embed


@bot.event
async def on_ready():
    print("FNL Scraper ready!")
    print("Running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))
    print("\n\n")


@bot.command(name="fnl", pass_context=True)
async def finishline_individual(ctx, index):
    try:
        index = int(index) - 1

    except:
        await ctx.message.channel.send("Invalid input for index.  Make sure to input a positive integer.")
        return

    calendar = ReleaseCalendar(None)
    success, error = calendar.fetch_finishline_drops()
    if success:
        try:
            product = calendar.products[index]
            embed = create_finishline_embed(product)
            await ctx.message.channel.send(embed=embed)

        except:
            await ctx.message.channel.send(
                "The index you provided does not exist.  Please try again with another index.")
            return

    else:
        await ctx.message.channel.send(
            "There was an error while scraping the release calendar, please try again later.  Error: {}".format(
                str(error)))


@bot.command(name="fnl_feed", pass_context=True)
async def finishline_feed(ctx, index):
    try:
        index = int(index)
    except:
        await ctx.message.channel.send("Invalid input for index.  Make sure to input a positive integer.")
        return

    calendar = ReleaseCalendar(None)
    success, error = calendar.fetch_finishline_drops()
    if success:
        try:
            for i in range(index):
                product = calendar.products[i]
                embed = create_finishline_embed(product)
                await ctx.message.channel.send(embed=embed)

        except:
            await ctx.message.channel.send(
                "The index you provided does not exist.  Please try again with another index.")
            return

    else:
        await ctx.message.channel.send(
            "There was an error while scraping the release calendar, please try again later.  Error: {}".format(
                str(error)))


@bot.command(name="fnl_range", pass_context=True)
async def finishline_range(ctx, start, stop):
    try:
        start = int(start)
        stop = int(stop)
    except:
        await ctx.message.channel.send(
            "Invalid input for either start or stop.  Make sure to input a positive integer.")
        return

    calendar = ReleaseCalendar(None)
    success, error = calendar.fetch_finishline_drops()
    if success:
        try:
            start = start - 1
            for i in range(stop - start):
                product = calendar.products[start + i]
                embed = create_finishline_embed(product)
                await ctx.message.channel.send(embed=embed)

        except:
            await ctx.message.channel.send(
                "The index you provided does not exist.  Please try again with another index.")
            return

    else:
        await ctx.message.channel.send(
            "There was an error while scraping the release calendar, please try again later.  Error: {}".format(
                str(error)))


if __name__ == "__main__":
    bot_token = ""
    with open("config.json", "r") as c_json:
        config = json.load(c_json)
        bot_token = config["token"]

    bot.run(bot_token)
