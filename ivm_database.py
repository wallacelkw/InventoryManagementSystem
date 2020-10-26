import sqlite3

def InventoryData():
    con=sqlite3.connect("IMSystem.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS INVENTORY(ID INTEGER PRIMARY KEY,Part_Number text, Description text, Quantity text, Date text, Location text, Remark text)")
    con.commit()
    con.close()

def addInv(part_num, description,quantity,r_date,location,r_remark):
    con = sqlite3.connect("IMSystem.db")
    cur=con.cursor()
    cur.execute("INSERT INTO INVENTORY VALUES (Null,?,?,?,?,?,?)", (part_num, description,quantity,r_date,location,r_remark))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("IMSystem.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM INVENTORY")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRecord(id):
    con = sqlite3.connect("IMSystem.db")
    cur=con.cursor()
    cur.execute("DELETE FROM INVENTORY WHERE ID=?",(id,))

    con.commit()
    con.close()

def searchData(part_num="" , description="" , quantity="" ,r_date="" , location="" ):
    con = sqlite3.connect("IMSystem.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM INVENTORY WHERE Part_Number=? OR Description=? OR Quantity=? OR Date=? OR Location=?",(part_num, description, quantity, r_date, location))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(part_num="",description="",quantity="",r_date="",location="",remark=""):
    con = sqlite3.connect("IMSystem.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET Part_Number=?,Description=?,Quantity=?,Date=?,Location=?,Remark=? WHERE id=?",(part_num, description, quantity, r_date, location,remark,id))
    con.commit()
    con.close()





InventoryData()