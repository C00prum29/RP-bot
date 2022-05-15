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

    if dice_value >= 20:
        emmed_color = 0x15D200
        emmed_name = 'Критический успех!'
    elif dice_value > 10:
        emmed_color = 0x90D200
        emmed_name = 'Успех'
    elif dice_value == 10:
        emmed_color = 0xD2D200
        emmed_name = 'Средне'
    elif dice_value > 0:
        emmed_color = 0xD22B00
        emmed_name = 'Провал!'
    else:
        emmed_color = 0xD22A00
        emmed_name = 'Критический провал!'

    embed = discord.Embed(color = emmed_color, title = 'Бросок кубика:')
    embed.add_field(name= emmed_name, value=f'Ваш результат: {dice_value}')
    return embed