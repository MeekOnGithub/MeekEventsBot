from logging import exception
import os
import time
import sys
import asyncio
import random
import json
import nextcord
import random
from nextcord import Intents
from nextcord.ext import commands
from nextcord.ext import menus
from nextcord.ext import tasks
from colorama import init
from colorama import Fore, Back, Style
import aiohttp
import asyncio
import requests
from python_aternos import Client 
init()

URL = "https://mcapi.us/server/status?ip=survival-serv.mine.fun"

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

meekid = [724005731228975154]

bot = commands.Bot(command_prefix='-', intents=intents, help_command=None, case_insensitive=True, owner_ids = set(meekid))
stt = "Making money, lol"


botnormal = "[" + Fore.CYAN + "Bot"  + Style.RESET_ALL + "]"
boterror = "[" + Fore.RED + "Error"  + Style.RESET_ALL + "]"
botwarn = "[" + Fore.YELLOW + "Warn"  + Style.RESET_ALL + "]"
botevent = "[" + Fore.GREEN + "Event"  + Style.RESET_ALL + "]"

async def restartt():
    try:
        print(botwarn + " Redémarrage...")
        os.system("python main.py")
    except Exception:
        os.system("./start.sh")




@bot.slash_command(
    name="runbuild",
    description="Allumer le serveur de build")
async def runbuild(interaction: nextcord.Interaction, ip):
    await interaction.response.defer()
    aternos = Client.from_credentials('motdepasse', 'mdp')
    liste_de_serveur = aternos.list_servers()
    builsrv = None
    for serv in liste_de_serveur:
        if serv.address == ip:
            buildsrv = serv
    if buildsrv != None:
        print(botevent + f" Démarrage demander par {interaction.user}") 
        print("Version du serveur : " + buildsrv.software, buildsrv.version)

        embed=nextcord.Embed(title="Démarrage du serveur de build 🟠")
        embed.add_field(name=f"Ip : {buildsrv.address}", value=f"")
        await asyncio.sleep(10)
        await interaction.followup.send(msgoncm)
        buildsrv.start()

os.system("cls")
print(botnormal + " Connection au bot...")

@bot.event
async def on_ready():
    try:
        os.system("cls")
        print(botnormal + " Bot connecté avec succes")
        print(botnormal + " En tant que : "+ bot.user.name)
        await bot.change_presence(activity=nextcord.Game(stt))
    except Exception:
        print(botwarn + " Erreur inconnu")



@bot.slash_command(
    name="support",
    description="Supporte moi en me fesant un don !")
@commands.is_owner()
async def support(interaction: nextcord.Interaction):
    print(botnormal + " Commande support éffectuer avec succes !")
    try:
        mssloading = "Paypal : zaideladib@gmail.com"
        await interaction.send(mssloading, ephemeral=True)
    except Exception:
        print("lol")


@bot.slash_command(
    name="restart",
    description="Rédemmarer le bot ")
@commands.is_owner()
async def support(interaction: nextcord.Interaction):
    try:
        embed=nextcord.Embed(title="Attention ", description="Êtes-vous sûr de vouloir éteindre le bot ?")
        view = Restart()
        interaction = await interaction.send(embed=embed, view=view, ephemeral=True)
        await view.wait()
    except Exception:
        print("lol")




@bot.slash_command(
    name='ping',
    description='ping')
@commands.is_owner()
async def move(interaction):
    try:
        latency = round(bot.latency * 1000)
        view = Ping()
        embed=nextcord.Embed(title="Ping 🏓")
        embed.add_field(name="Ping du bot", value=f"`{latency} ms`")
        await interaction.send(embed=embed, view=view, ephemeral=True)
        await view.wait()
    except Exception as e:
        print(boterror + " " + str(e))





class Restart(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Oui", style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Redémmarage...", ephemeral=True)
        await restartt()
        self.value = True

        self.stop()


    @nextcord.ui.button(label="Non", style=nextcord.ButtonStyle.green)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Annulation avec succés", ephemeral=True)
        self.value = False
        self.stop()

class Ping(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label=None, style=nextcord.ButtonStyle.green, emoji="\U0001f5d1")
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.delete_original_response()
        self.value = True
        self.stop()




class Rules(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="J'accepte les régles", style=nextcord.ButtonStyle.green, emoji="\u2705")
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.user.add_roles(nextcord.Object(995614973583699979))
        messageee = "Vous avez acceptez le réglement avec succés !"
        await interaction.send(messageee, ephemeral=True)

class Suggestion(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Faites une suggestion vous aussi !", style=nextcord.ButtonStyle.grey, emoji=None, disabled=True)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        print("he")












class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())






@bot.slash_command()
@commands.is_owner()
async def kick(interaction, membre: nextcord.User, raison):
    """Permet de kick un utilisateur"""
    try:
            await membre.kick()
            embed=nextcord.Embed(title="Kick ❌")
            embed.add_field(name=f"{membre} a bien était kick", value=f"Pour {raison}")

            await interaction.send(embed=embed, ephemeral=True)

    except Exception as e: 
        print(str(e))


@bot.slash_command()
@commands.is_owner()
async def ban(interaction, membre: nextcord.User, raison):
    """Permet de ban un utilisateur"""
    try:
            await membre.ban()
            embed=nextcord.Embed(title="Ban ❌")
            embed.add_field(name=f"{membre} a bien était ban", value=f"Pour {raison}")

            await interaction.send(embed=embed, ephemeral=True)

    except Exception as e: 
        print(boterror + str(e))

@nextcord.ext.tasks.loop(seconds=5, reconnect=True)
async def joined(message):
    user = bot.get_user(724005731228975154)

    r = requests.get(url = URL)

    data = r.json()

    players = data['players.now']


    if players == 0:

        print("working")
        pass
        await joined.start()
    if players != 0:
        message = "Un joueur a rejoint le serveur !"
        await user.send(message)
        await joined.start()
            





class suggestion(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("Suggestion Event")  

     
        self.name = nextcord.ui.TextInput(
            label="L'idée",
            min_length=2,
            max_length=50,
        )
        self.add_item(self.name)

      
        self.description = nextcord.ui.TextInput(
            label="Explique-nous",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Pourquoi devrions nous choisir celui la",
            required=False,
            max_length=1800,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        try:
            embed=nextcord.Embed(title="Suggestion d'idée 🎈")
            embed.add_field(name="Idée 💡", value=f"{self.name.value}", inline=True)
            embed.add_field(name="Pourquoi :", value=f"{self.description.value}", inline=False)
            
            channel = bot.get_channel(1015268790667329576)

            view = Suggestion()
            
            await interaction.channel.send(embed=embed, view=view)
        except Exception as e:
            print(boterror + " " + (str(e)))


        
@bot.slash_command()
async def suggevent(interaction):
    """Suggestion d'event"""
    try:
        modal = suggestion()
        await interaction.response.send_modal(modal)
    except:
        print("err")








@bot.slash_command()
@commands.is_owner()
async def rules(interaction):
    embed=nextcord.Embed(title="Régles <a:923203708110635109:1012666339292364822> >")
    embed.add_field(name="1 -", value="`Pas de racisme, ni n-word etc...`", inline=True)
    embed.add_field(name="2 -", value="`Le contenu NSFW est strictement interdit`", inline=False)
    embed.add_field(name="3 -", value="`Pas de spam ou d'inondation du chat avec des messages`", inline=True)
    embed.add_field(name="4 -", value="`Pas de malédictions excessives. Jurer est évidemment autorisé, mais gardez-le au frais.`", inline=False)
    embed.add_field(name="5 -", value="`Aucune publicité pour d'autres sites / serveurs discord `", inline=True)
    embed.add_field(name="6 -", value="`Pas de faire passer le contenu de quelqu'un d'autre comme le vôtre.`", inline=False)
    embed.add_field(name="7 -", value="`Ne causez pas de nuisance dans la communauté, les plaintes répétées de plusieurs membres entraîneront des mesures administratives`", inline=False)
    embed.add_field(name="8 -", value="`Tout abus de mentions envers un membres du staff (mentions personnelles inclues) ou la communauté est interdit`", inline=True)
    
    embed.add_field(name="Régles Minecraft <a:923203708110635109:1012666339292364822>", value=">", inline=False)
    embed.add_field(name="1 -", value="`Toutes les régles du discord s'appliquent`", inline=True)
    embed.add_field(name="2 -", value="`Pas de cheat, ne trichez pas en utilisant des bugs pendant l'event`", inline=False)

    view = Rules()

    await interaction.send(embed=embed, view=view)


class CreateTicket(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="🎫︲Créé Un Ticket", style= nextcord.ButtonStyle.green, custom_id="create_ticket:green"
    )
    async def create_ticket(self, boutton: nextcord.ui.Button, interaction: nextcord.Interaction):
        msg= await interaction.response.send_message("Création de votre ticket...", ephemeral=True)

        overwrites = {
            interaction.guild.default_role: nextcord.PermissionOverwrite(view_channel= False),
            interaction.user: nextcord.PermissionOverwrite(view_channel=True),
            interaction.guild.get_role(1005605346435412088): nextcord.PermissionOverwrite(view_channel=True)
        }
        channel= await interaction.guild.create_text_channel(f"{interaction.user.name}︲ticket", overwrites= overwrites)
        await msg.edit(f"Le Ticket à été créé avec succès ! <a:verifygreen:1005583838254211122> ➔ {channel.mention}")
        embed = nextcord.Embed(title=f"Ticket créé", description=f"{interaction.user.mention} Votre ticket à été créé, un membre du staff viendra bientôt réglé votre problème. Quand votre problème sera résolu vous pouvez cliquer sur le bouton `🔒︲Close Ticket` pour fermé ce ticket.")
        await channel.send(embed=embed, view= TicketSettings())


class AddUser(nextcord.ui.Modal):
    def __init__(self, channel):
        super().__init__(
            "Ajouter une personne dans le ticket",
            timeout=300,
        )
        self.channel= channel

        self.user = nextcord.ui.TextInput(
            label= "User ID",
            min_length= 2,
            max_length= 50,
            required=True,
            placeholder="Entrez l'ID d'un utilisateur."
        )
        self.add_item(self.user)

    async def  callback(self, interaction: nextcord.Interaction) -> None:
        user = interaction.guild.get_member(int(self.user.value))
        if user is None:
            return await interaction.send(f"Utilisateur introuvable, êtes-vous sûr que l'utilisateur se trouve dans le serveur ?")
        overwrite= nextcord.PermissionOverwrite()
        overwrite.view_channel = True
        await self.channel.set_permissions(user, overwrite=overwrite)
        await interaction.send(f"{user.mention} à été ajouté au ticket.")

class RemoveUser(nextcord.ui.Modal):
    def __init__(self, channel):
        super().__init__(
            "Retirer une personne dans le ticket",
            timeout=300,
        )
        self.channel= channel

        self.user = nextcord.ui.TextInput(
            label= "User ID",
            min_length= 2,
            max_length= 50,
            required=True,
            placeholder="Entrez l'ID d'un utilisateur."
        )
        self.add_item(self.user)

    async def  callback(self, interaction: nextcord.Interaction) -> None:
        user = interaction.guild.get_member(int(self.user.value))
        if user is None:
            return await interaction.send(f"Utilisateur introuvable, êtes-vous sûr que l'utilisateur se trouve dans le serveur ?")
        overwrite= nextcord.PermissionOverwrite()
        overwrite.view_channel = False
        await self.channel.set_permissions(user, overwrite=overwrite)
        await interaction.send(f"{user.mention} à été retiré du ticket.")

class TicketSettings(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="🔒︲Supprimer le ticket", style= nextcord.ButtonStyle.red, custom_id="ticket_settings:red"
    )
    async def close_ticket(self, boutton: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Le Ticket à été fermé avec succès ! ", ephemeral=True)
        await interaction.channel.delete()
        await interaction.user.send(f"Le salon à été fermé avec succès ! {interaction.channel.mention}")

    @nextcord.ui.button(
        label="➕︲Ajouter un utilisateur", style= nextcord.ButtonStyle.green, custom_id="ticket_settings:green"
    )
    async def add_user(self, boutton: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(AddUser(interaction.channel))

    @nextcord.ui.button(
        label="➖︲Retirer un utilisateur", style= nextcord.ButtonStyle.gray, custom_id="ticket_settings:gray"
    )
    async def remove_user(self, boutton: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(RemoveUser(interaction.channel))

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(CreateTicket())
            self.persistent_views_added = True
            print("Persistent Viws added")
        print(f"Bot est prêt | Logged in as {self.user}")

@bot.slash_command()
@commands.has_permissions(manage_guild=True)
async def ticket(interaction):
    embed = nextcord.Embed(title="Claim / Support 🎫")
    embed.add_field(name="Créer en un en appuyant sur le bouton", value="None")
    await interaction.send(embed=embed, view= CreateTicket())

@bot.slash_command()
async def calc(interaction: nextcord.Interaction, calcul):
    if type(eval(calcul)) == int:
        try:
            print(botevent + f" Calcul : {calcul}, fait par {interaction.user}")
            embed = nextcord.Embed(title=f"Résultat de votre calcul 🧮", description=f"= {calcul}")
            await interaction.send(embed=embed)
        except ValueError as e:
            print(boterror + " " + e)
            await interaction.send("Une erreur est survenu !", ephemeral=True)
    else:
        await interaction.send("Tu ne peux pas calculer des lettres, fin ce n'est pas possible pour le moment x)", ephemeral=True)




@bot.slash_command()
@commands.has_permissions(manage_guild=True)
async def say(interaction: nextcord.Interaction, mot):
    await interaction.send(interaction.arguments)

@bot.event
async def on_message(message: nextcord.Message):
    if message.guild is None and not message.author.bot:
        print(f"{message.author} > : {message.content}")
        rsp = input("Bot : ")
        await message.channel.send(rsp)
    await bot.process_commands(message)

@bot.slash_command()
@commands.has_permissions(manage_guild=True)
async def sendmp(interaction, user: nextcord.User, *, message: str):
    try:
        await user.send(message)
        await interaction.send(f"`Message envoyé à` : {user.mention}", ephemeral=True)
    except Exception as e:
        await interaction.send(f"Impossible d'envoyer le message à {user.mention}", ephemeral=True)
        await interaction.send(f"{user.mention}, les messages privés sur ce serveur sont désactivés, je vous prie de les désactives ^^")
        print(boterror + " " + str(e))
    
delmesg = [f"Bien essayer, les liens sont interdit ! ", f"Faudra trouver mieux pour m'avoir et envoyer des liens", "Tss, arrête les liens la", "play.meekevent.fr"]
meekmnt = ["<@724005731228975154>, il t'appelle !", "Qui as 5 € a passez", "Qui veux nitro ?", "amogus", "Je vous bz sur fortnite / minecraft"]

#@bot.event 
#async def on_message(message: nextcord.Message):
#   try:
#       if message.content in ("<@724005731228975154>") and message.author.bot =! message.author.id:
#           print(botevent + f" Vous avez était mentionner par {message.author}")
#           await message.channel.send(random.choice(meekmnt))
#       if message.content.startswith("https://") or ("http://") and not message.author.bot or message.author.id == (724005731228975154):
#           await message.delete()
#           await message.channel.send(random.choice(delmesg))
#   except Exception as e:
#       print(boterror + " " + str(e))
#       await message.channel.send("J'allais faire une blague mais j'ai pas pu :/")

@bot.event 
async def on_message(message):
    if message.content in "Internal Exception: io.netty.handler.timeout.ReadTimeoutException" and message.channel.id == (1020371565789069312): 
        try:
            await message.channel.send(f"""
                Hey {message.author.mention} :wave:,

                Je pense que :
                    
                     1. `Le jeu sur votre ordinateur ne peut pas traiter les données du serveur assez rapidement, ce qui vous oblige à ne plus être synchronisé avec le serveur.`

                Tu devrais peût-etre faire :
                     1. `Vérifiez votre connexion Internet pour vous assurer qu'il n'y a pas de perte de paquets.`
                     2. `Assurez-vous que votre ordinateur est suffisamment rapide pour exécuter le jeu. Il faut plus de puissance de traitement pour y jouer sur un serveur qu'en solo.`

                     Ceci est un message automatique, merci de contacter un développeur si besoin !""")
        except Exception as e:
            print(boterror + " " + str(e))
            embed = nextcord.Embed(title="Erreurr ❌")
            emebed.add_field(name="Détail :", value =e)
            await message.channel.send(embed=embed)

            




bot.run("token")
