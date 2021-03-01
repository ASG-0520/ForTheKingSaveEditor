import sqlite3 as sq
import os


class SaveEditor:

    def __init__(self):
        self.un = os.environ.get("USERNAME")
        self.player_db = f'C:\\Users\\{self.un}\\AppData\\LocalLow\\IronOak Games\\FTK\\save\\epic829cce0d4b4346b8989ef216f58ed67c\\player.db'
        self.backup_player_db = f'C:\\Users\\{self.un}\\AppData\\LocalLow\\IronOak Games\\FTK\\save\\epic829cce0d4b4346b8989ef216f58ed67c\\backup_player.db'

    def backup(self):
        with open(self.player_db, 'rb') as file:
            with open(self.backup_player_db, 'wb') as backup_file:
                backup_file.write(file.read())
        print('backup готов')

    def update_lore(self):
        with sq.connect(self.player_db) as con:
            cur = con.cursor()

            cur.execute("SELECT Value FROM sPlayerStatistic WHERE Name = 'STAT_LU_TOTAL_LORE'")
            result = cur.fetchone()
            print(f"You have: {result[0]} LORE.")

            price = int(input('LORE = '))
            cur.execute(f"UPDATE sPlayerStatistic SET Value = {price} WHERE Name = 'STAT_LU_TOTAL_LORE'")

            cur.execute('SELECT Value FROM sPlayerStatistic WHERE id = 67')
            result = cur.fetchone()
            print(f"You have: {result[0]} LORE.")

    def open_lore_shop(self):
        with sq.connect(self.player_db) as con:
            cur = con.cursor()
            cur.execute("UPDATE sPlayerStatistic SET Value = 1 WHERE Name LIKE 'STAT_LU%'")
        input('LORE Shop открыт')


save = SaveEditor()
inp = input("1 - save_backup\n2 - open_lore_shop\n3 - update_LORE\n")
if inp == '1':
    save.backup()
elif inp == '2':
    save.open_lore_shop()
elif inp == '3':
    save.update_lore()
else:
    print('wrong chose')
