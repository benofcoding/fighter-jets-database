

#import
import sqlite3


#constants/varibles
DATABASE = "fighters.db"


#functions
def print_all_aircraft():
    db = sqlite3.connect("fighters.db")
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop all results
    print("Name           speed     Max_G     climb     range     payload ")
    for fighter in results:
        print(f"{fighter[1]:<15}{fighter[2]:<10}{fighter[3]:<10}{fighter[4]:<10}{fighter[5]:<10}{fighter[6]}")
    
    db.close


#main code
print_all_aircraft()
