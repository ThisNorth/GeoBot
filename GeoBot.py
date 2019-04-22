import discord
from discord.ext import commands
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

serverurl = "https://mcsrvstat.us/server/geographica.xyz"
client = commands.Bot(command_prefix = '!')
TOKEN = "NTY5NzA4Njk0MzEzMzY5NjAw.XL0koQ.DIjZIPNa4XrTwBHo2_-v5HwarJk"



#Region - Start -
@client.event
async def on_ready():
    print("Bot Is Online!")


#Region - Web Scrape -
@client.command(pass_context=True)
async def status(ctx):
    uClient = uReq(serverurl)
    pageRaw = uClient.read()
    page_soup = soup(pageRaw, "html.parser")
    s_table = page_soup.find("table",{"class":"table table-hover"})
    rows = s_table.find_all('tr')
    data = []
    for row in rows:
        data.append(str(row.find_all('td')[1].text))
        print(data)

    if any("MAINTENANCE" in s for s in data):
        await client.say("@everyone Server Down")
    else:
        await client.say("@everyone Server Up")











client.run(TOKEN)
