from database.db import db_connect, execute_query, execute_read_query

def stat_read(stat, character):
    connection = db_connect('database/roleplay.db')
    form = f'SELECT {stat} FROM stats WHERE character_id = "{character}";'
    stat = execute_read_query(connection, form)[0][0]
    connection.close()
    return stat

def health_condition_read(character):
    connection = db_connect('database/roleplay.db')
    form = f'SELECT * FROM health WHERE character_id = "{character}";'
    health = execute_read_query(connection, form)

def cause_damage(target, body_part, damage):
    connection = db_connect('database/roleplay.db')
    part_select = f'SELECT {body_part} FROM health WHERE character_id = "{target}";'
    health = execute_read_query(connection, part_select)[0][0] - damage
    cause_damage = f'''
UPDATE
health
SET
{body_part} = {health}
WHERE
character_id = "{target}"
'''
    execute_query(connection,  cause_damage) 
    connection.close()
    return