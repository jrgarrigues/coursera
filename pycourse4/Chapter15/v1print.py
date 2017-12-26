import sqlite3
import csv


cols = ["Name", "Display Id", "Type", "Requested By", "State", "Team Name", "Portfolio Item Display Id",
        "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name"]
sql = sqlite3.connect('caprs-v1.db')
cur = sql.cursor()


cur.execute(
    'SELECT "Display Id","Requested By" FROM V1_tickets WHERE "Requested By" LIKE "%IM1_______%" ')
result = cur.fetchall()
match_list = []
sql.commit()

print()
print('egin CAPRS print run')
print()   
for i in range(len(result)):
    cycle = i
    if len(result[cycle][1]) > 9:
        carve = result[cycle][1]
        if carve[0:3] == 'IM1':
            print("{0:3}".format(cycle + 1),
              result[cycle][0][0:7], ' - ', result[cycle][1][0:10])
            match_list.append([result[cycle][0][0:7], result[cycle][1][0:10]])  
print()
print('Processed',len(result),'records')
print('End of CAPRS print run')
print()          

# print(match_list)

# write match_list to CSV
CAPRS_V1_csv = 'CAPRS_V1.csv'
with open('CAPRS_V1.csv','w') as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerow(["V1 Story","CAPRS IM"])
	for val in match_list:
		writer.writerows([val])

sql.commit()
sql.close()


# 'IM1\d+'
# SQL Search statement: SELECT "Display Id","Requested By" FROM V1_tickets WHERE ("Requested By" LIKE "IM1_______" or "Requested By" LIKE "IM1_______ & IM1_______"  or "Requested By" LIKE "IM1_______, IM1_______" or  "Requested By" LIKE "IM1_______ and IM1_______")