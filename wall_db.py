import sqlite3


class MainDB:
    def __init__(self):
        self.db = sqlite3.connect('wall.db')
        self.cur = self.db.cursor()

    def init_table(self):
        sql1 = '''CREATE TABLE IF NOT EXISTS users
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name varchar,
                    passwd TEXT,
                    date TEXT,
                    is_admin boolean,
                    is_banned boolean
                );'''
        sql2 = '''CREATE TABLE IF NOT EXISTS message
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    src_id varchar,
                    text TEXT,
                    path varchar(60),
                    date TEXT
                );'''
        command = [self.cur.execute(i) for i in [sql1, sql2]]
        self.db.commit()

    def new_users(self, name, passwd, is_admin=False):
        sql1 = '''INSERT INTO users(name, passwd, date, is_admin, is_banned) VALUES(?, ?, datetime('now', 'localtime'), ?, ?)'''
        self.cur.execute(sql1, (name, passwd, is_admin, False))
        self.db.commit()

    def new_message(self, src_id, text, path):
        sql1 = '''INSERT INTO message(src_id, text, path, date) VALUES(?, ?, ?, datetime('now', 'localtime'))'''
        self.cur.execute(sql1, (src_id, text, path))
        self.db.commit()

    def ban(self, user_id):
        sql1 = '''UPDATE users SET is_banned = True WHERE id = ?'''
        self.cur.execute(sql1)
        self.db.commit()

    def check_name(self, name):
        sql1 = '''SELECT * FROM users WHERE name = ?;'''
        self.cur.execute(sql1, (name,))
        self.db.commit()
        x = self.cur.fetchall()
        if len(x) == 0:
            return True
        return False


'''
db = MainDB()
db.init_table()
# db.new_users('y', 'wdawdawd')
print(db.check_name('y'))
print(db.check_name('yg'))
'''
