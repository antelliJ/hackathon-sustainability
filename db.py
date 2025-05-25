import sqlite3

#PRIMARY SCREENING
#FULL NAME INPUTS
#GENDER INPUT
#SYMPTOMS INPUT


#SECONDARY SCREENING
#HISTORY INPUT
#FEELINGS INPUT
#LAST MEAL
#LAST DRINK



def get_db():
    db = sqlite3.connect("lite.db",detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row

    return db


def view():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    #Select data of all columns
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall() 
    #since only reading data no need to commit
    conn.close()
    return rows


if __name__ == "__main__":
    print(view())