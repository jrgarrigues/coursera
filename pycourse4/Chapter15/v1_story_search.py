import sqlite3
import re


cols = ["Name", "Display Id", "Type", "Requested By", "Found By", "State", "Team Name", "Portfolio Item Display Id",
        "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name"]
sql = sqlite3.connect('caprs-v1.db')
cur = sql.cursor()


cur.execute(
    ''' SELECT "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name" FROM V1_tickets WHERE "Requested By" LIKE "%IM1_______%" ''')
result = cur.fetchall()
sql.commit()
print()
print('Begin V1-Story search')
print()
for i in range(len(result)):
    cycle = i
    if len(result[cycle][2]) > 10:
        carve = result[cycle][2]
        if carve[0:3] == 'IM1':
            print("{0:3}".format(cycle + 1),
                  result[cycle][0], ' - ', carve[0:10])
        else:
            print(carve, '-- the FIRST one is broken')
        if carve[-10:-7] == 'IM1':      # put an insert for the first IM here
            print("{0:3}".format(cycle + 1), result[cycle][0], ' - ', carve[-10:])
            cur.execute(''' INSERT INTO V1_tickets("Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name")
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', ((result[cycle][0] + ' and ' + carve[-10:]), result[cycle][0] + carve[-10:-8], result[cycle][1], carve[-10:], result[cycle][3], result[cycle][4], result[cycle][5], result[cycle][6], result[cycle][7], result[cycle][8], result[cycle][9], result[cycle][10]))
        elif carve[-11:-8] == 'IM1':
            print("{0:3}".format(cycle + 1), result[cycle][0], ' - ', carve[-11:-1])
            cur.execute(''' INSERT INTO V1_tickets("Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name")
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', (result[cycle][0] + ' and ' + carve[-11:-1], result[cycle][0] + carve[-11:-9], result[cycle][1], carve[-11:-1], result[cycle][3], result[cycle][4], result[cycle][5], result[cycle][6], result[cycle][7], result[cycle][8], result[cycle][9], result[cycle][10]))
        elif carve[-12:-9] == 'IM1':
            print("{0:3}".format(cycle + 1),
                  result[cycle][0], ' - ', carve[-12:-2])
            cur.execute(''' INSERT INTO V1_tickets("Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name")
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', (result[cycle][0] + ' and ' + carve[-12:-2], result[cycle][0] + carve[-12:-10], result[cycle][1], carve[-12:-2], result[cycle][3], result[cycle][4], result[cycle][5], result[cycle][6], result[cycle][7], result[cycle][8], result[cycle][9], result[cycle][10]))
        elif carve[-13:-10] == 'IM1':
            print("{0:3}".format(cycle + 1),
                  result[cycle][0], ' - ', carve[-13:-3])
            cur.execute(''' INSERT INTO V1_tickets("Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name")
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', (result[cycle][0] + ' and ' + carve[-13:-3], result[cycle][0] + carve[-13:-11], result[cycle][1], carve[-13:-3], result[cycle][3], result[cycle][4], result[cycle][5], result[cycle][6], result[cycle][7], result[cycle][8], result[cycle][9], result[cycle][10]))
        elif carve[-14:-11] == 'IM1':
            print("{0:3}".format(cycle + 1),
                  result[cycle][0], ' - ', carve[-14:-4])
            cur.execute(''' INSERT INTO V1_tickets("Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name")
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', (result[cycle][0] + ' and ' + carve[-14:-4], result[cycle][0] + carve[-14:-12], result[cycle][1], carve[-14:-4], result[cycle][3], result[cycle][4], result[cycle][5], result[cycle][6], result[cycle][7], result[cycle][8], result[cycle][9], result[cycle][10]))
        elif carve[-15:-12] == 'IM1':
            print("{0:3}".format(cycle + 1),
                  result[cycle][0], ' - ', carve[-15:-5])
            cur.execute(''' INSERT INTO V1_tickets("Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id", "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name")
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', (result[cycle][0] + ' and ' + carve[-15:-5], result[cycle][0] + carve[-15:-13], result[cycle][1], carve[-15:-5], result[cycle][3], result[cycle][4], result[cycle][5], result[cycle][6], result[cycle][7], result[cycle][8], result[cycle][9], result[cycle][10]))
        else:
            continue  # print(carve, '--- the SECOND one is broken')
    else:
        # break
        print("{0:3}".format(cycle + 1),
              result[cycle][0], ' - ', result[cycle][2])
print()
print('End of V1-Story search')
print()

sql.commit()
sql.close()

# cur.execute("SELECT * FROM list WHERE InstitutionName=?", (Variable,))


# 'IM1\d+'
# SQL Search statement: SELECT "Display Id","Requested By" FROM V1_tickets WHERE ("Requested By" LIKE "IM1_______" or "Requested By" LIKE "IM1_______ & IM1_______"  or "Requested By" LIKE "IM1_______, IM1_______" or  "Requested By" LIKE "IM1_______ and IM1_______")
