from database.db import db_connect, execute_query, execute_read_query

def stat_read(stat, character):
    connection = db_connect('database/roleplay.db')

    stat_read_form = f'SELECT {stat} FROM stats WHERE character_id = "{character}";'
    stat = execute_read_query(connection, stat_read_form)[0][0]

    connection.close()
    return stat

def health_condition_read(character):    #доделать
    connection = db_connect('database/roleplay.db')

    health_form = f'SELECT * FROM health WHERE character_id = "{character}";'
    health = execute_read_query(connection, health_form)[0]

    connection.close()
    return health

def cause_damage(target, body_part, damage):
    connection = db_connect('database/roleplay.db')

    part_select_form = f'SELECT {body_part} FROM health WHERE character_id = "{target}";'
    health = execute_read_query(connection, part_select_form)[0][0] - damage

    cause_damage_form = f'UPDATE health SET {body_part} = {health} WHERE character_id = "{target}"'
    execute_query(connection,  cause_damage_form) 

    connection.close()
    return

def money_transaction(character, amount, target):
    connection = db_connect('database/roleplay.db')

    character_wallet_form = f'SELECT wallet FROM characters WHERE id = "{character}";'
    target_wallet_form = f'SELECT wallet FROM characters WHERE id = "{character}";'
    character_wallet = execute_read_query(connection, character_wallet_form)[0][0] - amount
    target_wallet = execute_read_query(connection, target_wallet_form)[0][0] + amount
        
    character_transact_money_form = f'UPDATE characters SET wallet = {character_wallet} WHERE id = "{character}"'
    execute_query(connection,  character_transact_money_form)
    target_transact_money_form = f'UPDATE characters SET wallet = {target_wallet} WHERE id = "{target}"'
    execute_query(connection,  target_transact_money_form)

    connection.close()
    return