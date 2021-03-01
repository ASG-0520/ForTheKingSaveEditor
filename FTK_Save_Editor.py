import sqlite3 as sq
import os


class SaveEditor:

    def __init__(self):
        self.un = os.environ.get("USERNAME")

    def backup(self):
        fil = f'C:\\Users\\{self.un}\\AppData\\LocalLow\\IronOak Games\\FTK\\save\\epic829cce0d4b4346b8989ef216f58ed67c\\player.db'
        backup_fil = f'C:\\Users\\{self.un}\\AppData\\LocalLow\\IronOak Games\\FTK\\save\\epic829cce0d4b4346b8989ef216f58ed67c\\backup_player.db'
        with open(fil, 'rb') as file:
            with open(backup_fil, 'wb') as backup_file:
                backup_file.write(file.read())

        input('backup готов')

    def update_lore(self):
        path = f'C:\\Users\\{self.un}\\AppData\\LocalLow\\IronOak Games\\FTK\\save\\epic829cce0d4b4346b8989ef216f58ed67c\\player.db'

        with sq.connect(path) as con:
            cur = con.cursor()

            cur.execute("SELECT Value FROM sPlayerStatistic WHERE Name = 'STAT_LU_TOTAL_LORE'")
            result = cur.fetchone()
            print(f"You have: {result[0]} LORE.")

            price = int(input('LORE = '))
            cur.execute(f"UPDATE sPlayerStatistic SET Value = {price} WHERE Name = 'STAT_LU_TOTAL_LORE'")

            cur.execute('SELECT Value FROM sPlayerStatistic WHERE id = 67')
            result = cur.fetchone()
            print(f"You have: {result[0]} LORE.")

            input()

    def open_lore_shop(self):
        with sq.connect(r'E:\Googl_Disc\PycharmProjects\Wazzaaap _p\SQLite3\player.db') as con:
            cur = con.cursor()
            cur.execute("UPDATE sPlayerStatistic SET Value = 1 WHERE Name LIKE 'STAT_LU%'")


# ID 80 (ДАНЬ КАМЕННОМУ ГЕРОЮ) = 5
save = SaveEditor()
inp = input("1 - backup.save\n2 - update_morney")
if inp == '1':
    save.backup()
elif inp == '2':
    save.open_lore_shop()
elif inp == '2':
    save.update_lore()
else:
    print('wrong chose')
