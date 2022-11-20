CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS user_note
                                    (

                                        user_id INTEGER NOT NULL,
                                        note_name TEXT DEFAULT 'Undefined',
                                        note TEXT DEFAULT 'Undefined'

                                    );'''


INSERT_INTO = '''INSERT INTO user_note VALUES((?),(?),(?));'''

SELECT_FROM = '''SELECT note_name, note FROM user_note WHERE user_id = (?)'''
SELECT_FROM_NAME = '''SELECT note_name, note FROM user_note WHERE user_id = (?), note_name = (?)'''
SELECT_FROM = '''SELECT note_name, note FROM user_note WHERE user_id = (?)'''
SELECT_FROM = '''SELECT note_name, note FROM user_note WHERE user_id = (?)'''
