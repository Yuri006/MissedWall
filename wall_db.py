import sqlite3


class MainDB:
    def __init__(self, path):
        self.path = path

    def init_table(self):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
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
        command = [cur.execute(i) for i in [sql1, sql2]]
        db.commit()

    def new_users(self, name, passwd, is_admin=False):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        sql1 = '''INSERT INTO users(name, passwd, date, is_admin, is_banned) VALUES(?, ?, datetime('now', 'localtime'), ?, ?)'''
        cur.execute(sql1, (name, passwd, is_admin, False))
        db.commit()

    def new_message(self, src_id, text, path):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        sql1 = '''INSERT INTO message(src_id, text, path, date) VALUES(?, ?, ?, datetime('now', 'localtime'))'''
        cur.execute(sql1, (src_id, text, path))
        db.commit()

    def ban(self, user_id):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        sql1 = '''UPDATE users SET is_banned = True WHERE id = ?'''
        cur.execute(sql1)
        db.commit()

    def unban(self, user_id):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        sql1 = '''UPDATE users SET is_banned = True WHERE id = ?'''
        cur.execute(sql1)
        db.commit()

    def check_name(self, name):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        sql1 = '''SELECT * FROM users WHERE name = ?;'''
        cur.execute(sql1, (name,))
        db.commit()
        x = cur.fetchall()
        if len(x) == 0:
            return True
        return False

    def users_all(self, name):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        sql1 = '''SELECT * FROM users WHERE name = ?;'''
        cur.execute(sql1, (name,))
        db.commit()
        x = cur.fetchall()
        return x[0]

    def check_password(self, name, password):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        if not self.check_name(name):
            sql1 = '''SELECT passwd FROM users WHERE name = ?;'''
            cur.execute(sql1, (name,))
            db.commit()
            passwd = cur.fetchall()[0][0]
            if passwd == password:
                return 0
            return 1
        return -1


'''
db = MainDB('wall.db')
db.init_table()
# db.new_users('y', 'wdawdawd')
print(db.check_name('y'))
print(db.check_name('yg'))
db.users_all('y')
print(db.check_password('y', 'wdawdwd'))
'''
