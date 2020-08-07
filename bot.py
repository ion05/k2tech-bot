##THIS IS THE MAIN BOT! NO ONE MAKES CHANGES TO THIS !!
import discord
import os
#TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
@client.event
async def on_ready():
    print('i\'m ready to get back to work')

@client.event
async def on_message(message):
    if message.content.startswith('$k2 about'):
        embed = discord.Embed(title='Thanks for adding me to your server! :heart:',  colour=1499502)\
        .add_field(
            name='K2Tech Bot',
            value='K2-Bot helps you conveniently display your google sheets data on a discord server.',
            inline=False).add_field(
            name='Contribute',
            value='We gladly accept contributions. To get started, ' +
            'check out [K2-Bot\'s GitHub repo](https://github.com/Technogic/discord-bot).',
            inline=False
        ).set_footer(text='Made by K2Tech', icon_url='https://techsyndicate.co/img/logo.png')
        await message.channel.send(embed=embed)

    if message.content.startswith("$k2 help") :
        embed = discord.Embed(
        title="K2-BOT\'s commands:",
        colour=1499502,
        description="""
> To use a  command type `$ts <command>`.
**General**\
`about` - To know about the bot.
`stats` - To check the bot's stats.
**Google Sheets **
`show "file name"` - To display the whole table
`show "file name" value` - To display rows of specific value
""")
        await message.channel.send(embed=embed)
client.run("NzQxMTc2NDk4Njg5NDA5MDk0.XyzwZw.x0DUuO0RPk0yZEjJ9edSWkGog6E")
