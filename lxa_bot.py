import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
lxa_bot = commands.Bot(intents=intents, command_prefix="$")

@lxa_bot.event
async def on_ready():
    for guild in lxa_bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{lxa_bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@lxa_bot.command(
    help="Uses some crazy logic to determine who I am.",
    brief="Returns back who I am."
)
async def info(ctx):
    string = """
    Hello, my name is Zero and I was developed
    to automate away responsibilities
    for Lambda Chi Alpha. Acts as a central repository of 
    information related to the transitioning of officer roles.
    If you have any questions, please contact my creator. 

    Best,
    Shashanka Sharma Theta Upsilon 1038

    In ZAX
    """
    await ctx.channel.send(string)

@lxa_bot.command(
    help="Displays the officer description.",
    brief="Example: $High Delta or $High Epsilon"
)
async def High(ctx, arg):
    OFFICER = arg

    if arg == 'Alpha':
        string = """
        The High Alpha is the leader of the chapter. 
        He looks out for the interests, well-being, and development of his chapter, 
        and guides each brother and associate member. 
        In order that he may carry out the duties of his office to the best of his ability, 
        the High Alpha should consider carefully these rules of action.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Alpha-PD.pdf
        Operations Guide: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Alpha-PD.pdf
        """
    elif arg == 'Beta':
        string = """
        The High Beta assists the High Alpha in performing his duties. 
        He oversees internal membership involvement and campus involvement. 
        The High Beta should serve as an ex-officio member of every committee within the 
        chapter including the Executive Committee. 
        Under the direction of the High Alpha, 
        it is his responsibility that all officers, committees, 
        and individual members are performing to the highest degree to 
        uphold the standards of Lambda Chi Alpha.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Beta-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighBetaOpsGuide.pdf
        """
    elif arg == 'Theta':
        string = """
        The High Theta's responsibilities are to originate, direct, 
        and inspire programs of external involvement for all members of the Fraternity 
        and to its various publics. Among these are the campus community, 
        the faculty and administration, 
        other fraternities and sororities, the non-fraternity students, parents, alumni, 
        and the community in which this chapter is located.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Theta-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighThetaOpsGuide.pdf
        """
    elif arg == 'Gamma':
        string = """
        The office of High Gamma is demanding both of time and attention to detail. 
        The High Gamma is fourth in the chain of command. 
        He is entrusted with the membership records of each member of the chapter and 
        responsible for reporting and submitting information in a timely manner to the 
        International Headquarters.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Gamma-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighGammaOpsGuide.pdf
        """
    elif arg == 'Tau':
        string = """
        The High Tau oversees the financial welfare of his chapter. 
        This officer must exemplify the highest 
        standards of integrity in maintaining the material property, financial assets, 
        and the financial records entrusted to his care.  
        The High Tau must administer, faithfully and impartially, the 
        financial affairs of the chapter, insist upon each member 
        fulfilling his individual obligations promptly, 
        and preserve the chapter assets in the development of long-range stability.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Tau-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighTauOpsGuide.pdf
        """
    elif arg == 'Iota':
        string = """
        The duty of the High Iota is to assist and protect others, particularly our own members. 
        The High Iota has the obligation to 
        administer a risk management program that promises 
        responsible and mature behavior by all members at all times, 
        and to preserve the ideals of the 
        Fraternity by conducting the operations of the chapter safely, 
        prudently, and in compliance with the laws and policies 
        both of Lambda Chi Alpha and the chapter's campus.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Iota-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighIotaOpsGuide.pdf
        """
    elif arg == 'Rho':
        string = """
        The High Rho is the chapter's link to the alumni of Lambda Chi Alpha, 
        both within and beyond this chapter. 
        He develops an effective program that provides events of 
        interest to the alumni, 
        recognizes outstanding service to the Fraternity by individual alumni, 
        encourages involvement, and prepares those beginning 
        to transition into dedicated alumni brothers.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Rho-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighRhoOpsGuide.pdf
        """
    elif arg == 'Kappa':
        string = """
        The High Kappa is entrusted with the education and 
        development of each and every chapter member as a 
        student, as a leader, and as a fully participating member in this chapter. 
        His goal is to develop and maintain a program of 
        mature acceptance of responsibility on the part of every undergraduate in 
        this chapter based on the history, 
        aims, ideals, and traditions of our country, the school, and Lambda Chi Alpha.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Kappa-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighKappaOpsGuide2.pdf
        """
    elif arg == 'Delta':
        string = """
        The High Delta provides for the future of his chapter by directing its membership recruitment program.
        His job is to lead recruitment efforts that will seek men with scholastic aptitude, 
        leadership potential, strength of character, and dedication to service.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Delta-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighDeltaOpsGuide.pdf
        """
    elif arg == 'Phi':
        string = """
        The High Phi is responsible with overseeing that the Fraternity's Initiation Ritual is performed 
        in the manner ensuring that the Fraternity's secrets are safe guarded. 
        His role is to advise the chapter on Lambda Chi Alpha's ceremonies 
        and ensuring they are performed in the proper manner. 
        He must inspire the brotherhood to delve into 
        the teachings of our Fraternity and instruct on 
        how to apply those teachings to their daily lives.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Phi-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/Open-Ceremonies-Guide-Final.pdf
        """
    elif arg == 'Sigma':
        string = """
        One of the principal objectives of Lambda Chi Alpha, as a co-curricular Fraternity, 
        is to develop in each member a realization of 
        his highest scholastic and intellectual potential. 
        The High Sigma is responsible in developing 
        and implementing an educational program 
        that encourages the broadest possible cultural and intellectual experience 
        for each member of the chapter.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Sigma-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighSigmaOpsGuide.pdf
        """
    elif arg == 'Epsilon':
        string = """
        The High Epsilon plays an important role in the social development 
        and participation of the members. 
        Entrusted to the High Epsilon are the responsibilities of 
        instilling in the members a constant awareness of, respect for, 
        and demonstration of acceptable standards of conduct; 
        those attributes of behavior 
        which distinguish a member of Lambda Chi Alpha as a gentleman.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Epsilon-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighEpsilonOpsGuide.pdf
        """
    elif arg == 'Pi':
        string = """
        The High Pi must be familiar with all facets of a situation before acting, 
        and then be candid yet diplomatic in 
        giving advice to the undergraduates of the chapter. 
        It is important for the High Pi to 
        present a good example by attending meetings and other activities,
        and by conscientiously following the highest standards of conduct and integrity.

        Additional Information
        Position Description: https://www.lambdachi.org/wp-content/uploads/2021/06/High-Pi-PD.pdf
        Operations Guide: https://lambdachi.org/wp-content/uploads/2020/08/HighPiOpsGuide.pdf
        """

    elif arg == 'Lucas':
        string = """
        Likes them big girls. :S
        """

    await ctx.channel.send(string)




lxa_bot.run(TOKEN)