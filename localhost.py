import discord
import asyncio
from discord.ext import commands
from datetime import datetime, timedelta
from colorama import init, Fore
import os
import colorama
from colorama import Fore
colorama.init()
init()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Invalid Syntax", description="Command has an invalid syntax", color=discord.Color.red())
        embed.add_field(name="Example Usage", value=f"{ctx.command} {ctx.command.signature}", inline=False)
        await ctx.send(embed=embed)

    elif isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(title='Insufficient Permissions', color=discord.Color.red())
        embed.add_field(name='Uh oh!', value='You lack sufficient permissions to execute this command.')
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(10)
        await msg.delete()
        await ctx.message.delete()

    elif isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title='Member not found!', color=discord.Color.red())
        embed.add_field(name='Uh oh!', value='The specified member was not found.')
        await ctx.send(embed=embed)

    elif isinstance(error, commands.errors.BadArgument):
        embed = discord.Embed(title='Invalid Argument!', color=discord.Color.red())
        embed.add_field(name='Uh oh!', value='One or more arguments were invalid.')
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="playing With Your Mum"))
    print('Voided Utilities Has Loaded!')
    print(Fore.LIGHTRED_EX + """
    ██    ██  ██████  ██ ██████  ███████ ██████      ██    ██ ████████ ██ ██      ██ ████████ ██ ███████ ███████ 
    ██    ██ ██    ██ ██ ██   ██ ██      ██   ██     ██    ██    ██    ██ ██      ██    ██    ██ ██      ██      
    ██    ██ ██    ██ ██ ██   ██ █████   ██   ██     ██    ██    ██    ██ ██      ██    ██    ██ █████   ███████ 
     ██  ██  ██    ██ ██ ██   ██ ██      ██   ██     ██    ██    ██    ██ ██      ██    ██    ██ ██           ██ 
      ████    ██████  ██ ██████  ███████ ██████       ██████     ██    ██ ███████ ██    ██    ██ ███████ ███████ 
    """)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def tempmute(ctx, member: discord.Member, duration: int, *, reason: str = "No reason provided."):
    """Mutes the specified member for the specified duration."""
    # Get the mute role from the server
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if mute_role is None:
        # If the mute role doesn't exist, create it
        mute_role = await ctx.guild.create_role(name="Muted", reason="To mute problematic users.")
        for channel in ctx.guild.channels:
            # Deny send messages permissions for the muted role in all channels
            await channel.set_permissions(mute_role, send_messages=False)
    # Assign the mute role to the member
    await member.add_roles(mute_role, reason=reason)
    # Send a confirmation message as an embed
    embed = discord.Embed(title="Member Muted", description=f"{member.mention} has been muted")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # check if user has the muted role
    role = message.guild.get_role(1093849572926816336)
    if role in message.author.roles:
        return

    # get the last 5 messages in the channel
    async for msg in message.channel.history(limit=5):
        if msg.author == message.author and msg.created_at > message.created_at - timedelta(seconds=5):
            await message.author.add_roles(role)
            embed = discord.Embed(title=f'{message.author.display_name} Has Been Muted!', color=discord.Color.red())
            embed.add_field(name=f'{message.author.display_name} Has Been Automatically muted due to spam', value='Muted For 5 Minutes')
            embed.set_footer(text='Action Carried Out By CONSOLE.')
            await message.channel.send(embed=embed)

            def check(m):
                return m.author == message.author

            try:
                await bot.wait_for('message', check=check, timeout=300) # wait for 5 minutes
            except asyncio.TimeoutError:
                await message.author.remove_roles(role)
                embed = discord.Embed(title=f'{message.author.display_name} Has Been Unmuted!', color=discord.Color.blue())
                embed.set_footer(text='Action Carried Out By CONSOLE.')
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title=f'{message.author.display_name} Has Been Deleted!', color=discord.Color.orange())
                embed.add_field(name=f'{message.author.display_name}\'s message has been smited!', value=message.content)
                embed.set_footer(text='Action Carried Out By Voided Utilities.')
                await message.channel.send(embed=embed)
                await message.delete()
            break # exit the loop if a spammer is found

    await bot.process_commands(message)
@bot.command()
@commands.has_permissions(ban_members=True)
async def smite(ctx, member: discord.Member, *, reason: str = None):
    embed = discord.Embed(title=f'{member.display_name} Has Been SMITED!', color=discord.Color.red())
    embed.add_field(name=f'{member.display_name} has been SMITED from the server.', value=f'Reason: {reason}')
    embed.set_footer(text='Action Carried Out By CONSOLE.')
    await member.ban(reason=reason)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = "No reason provided."):
    """Kicks the specified member."""
    # Kick the member
    await member.kick(reason=reason)
    # Send a confirmation message
    embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. Reason: {reason}", color=discord.Color.blue())
    await ctx.send(embed=embed)

#brayden Mode
brayden_mode_users = {}
whitelisted_users = [827437464414978069, 843493314862252032]

@bot.event
async def on_message(message):
    if message.author.id == 832060648329707571 and brayden_mode_users.get(message.guild.id):
        await message.delete()
        user = message.guild.get_member(832060648329707571)
        await message.channel.send(f"{user.mention}, No.")
        print(Fore.BLUE + "[BRAYDENMODE]: Message was successfully intercepted and deleted!")
    await bot.process_commands(message)

@bot.command()
async def stfubrayden(ctx):
    if ctx.author.id not in whitelisted_users:
        await ctx.send("LMFAO IMAGINE NO BRAYDENMODE PERMS 🤣")
        return
    brayden_mode_users[ctx.guild.id] = True
    user = ctx.guild.get_member(832060648329707571)
    await ctx.send(f"Brayden Mode Has Been Enabled. {user.mention}, shut the fuck up")

@bot.command()
async def disablebraydenmode(ctx):
    if ctx.author.id not in whitelisted_users:
        await ctx.send("LMFAO IMAGINE NO BRAYDENMODE PERMS 🤣")
        return
    brayden_mode_users[ctx.guild.id] = False
    await ctx.send("Brayden Mode Has Been Disabled Successfully!")


bot.run('MTA4OTQ1ODU2MzUyMjUxMDkzOA.GF2wDA.lpwnZGkMx8iRFbafhbAJ9O67YS6-MgqcujejOM')
