import discord

def form_heath_condition_emmed(health):
    embed = discord.Embed(color = 0xFFFFFF, title = 'Анализ состояния:')
    embed.add_field(name= health[0], value=f'''
    Голова - {health[1]}
    Рука(Л) - {health[2]}
    Рука(П) - {health[3]}
    Торс - {health[4]}
    Нога(Л) - {health[5]}
    Нога(П) - {health[6]}
    ''')
    return embed

def form_roll_result_emmed(dice_value):

    if dice_value < 0:
        emmed_color = 0xFF0000

    embed = discord.Embed(color = 0xFFFFFF, title = 'Анализ состояния:')
    embed.add_field(name= health[0], value=f'a')
    return embed