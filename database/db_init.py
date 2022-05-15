from db import db_connect, execute_query

create_characters_table = """
CREATE TABLE IF NOT EXISTS characters (
  id TEXT NOT NULL, 
  user_id TEXT NOT NULL, 
  level INTEGER NOT NULL,
  wallet INTEGER NOT NULL
);
"""
create_stats_table = """
CREATE TABLE IF NOT EXISTS stats (
    character_id TEXT NOT NULL, 
    fortitude INTEGER NOT NULL,
    prudence INTEGER NOT NULL,
    temperance INTEGER NOT NULL,
    justice INTEGER NOT NULL,
    FOREIGN KEY (character_id) REFERENCES character (id)
);"""

create_health_table = """
CREATE TABLE IF NOT EXISTS health (
    character_id TEXT NOT NULL, 
    head INTEGER NOT NULL,
    arm_l INTEGER NOT NULL,
    arm_r INTEGER NOT NULL,
    body INTEGER NOT NULL,
    leg_l INTEGER NOT NULL,
    leg_r INTEGER NOT NULL,
    sp INTEGER NOT NULL,
    FOREIGN KEY (character_id) REFERENCES character (id)
);"""

create_augmentations_table = """
CREATE TABLE IF NOT EXISTS augmentations (
    character_id TEXT NOT NULL, 
    head TEXT NOT NULL,
    arm_l TEXT NOT NULL,
    arm_r TEXT NOT NULL,
    body TEXT NOT NULL,
    leg_l TEXT NOT NULL,
    leg_r TEXT NOT NULL,
    FOREIGN KEY (character_id) REFERENCES character (id)
);"""

create_characters="""
INSERT INTO
  characters (user_id, id, level, wallet)
VALUES
    ('Бобр#0977','Маргарита', 1, 100),
    ('Das kupfer#8909','Константин', 1, 100),
    ('CyberFox2077#0039', 'Рейсу', 1, 100),
    ('CyberFox2077#0039', 'Серафима', 1, 100),
    ('CyberFox2077#0039', 'Кси', 1, 100),
    ('CyberFox2077#0039', 'Ши', 1, 100);
"""

create_stats="""
INSERT INTO
  stats (character_id, fortitude, prudence, temperance, justice)
VALUES
    ('Маргарита','15', '17', '16', '12'),
    ('Рейсу', '14', '14', '15', '15');
"""   
create_health="""
INSERT INTO
  health (character_id, head, arm_l, arm_r, body, leg_l, leg_r, sp)
VALUES
    ('Маргарита','10', '10', '10', '10', '10', '10', 20),
    ('Рейсу','10', '10', '10', '10', '10', '10', 20);
"""   
create_augmentations=""" 
INSERT INTO
  augmentations (character_id, head, arm_l, arm_r, body, leg_l, leg_r)
VALUES
    ('Маргарита','Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет'),
    ('Рейсу', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет');
""" 


connection = db_connect('database/roleplay.db')
execute_query(connection,  create_characters_table)  
execute_query(connection,  create_stats_table)
execute_query(connection,  create_health_table)  
execute_query(connection,  create_augmentations_table)    
execute_query(connection,  create_characters)  
execute_query(connection,  create_stats)  
execute_query(connection,  create_health)  
execute_query(connection,  create_augmentations)  
