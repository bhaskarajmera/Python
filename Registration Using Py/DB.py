import sqlite3
import pandas as pd
import os 
import xlwt

def crt_table():
	conn = sqlite3.connect("Database1.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Credentials (FstName TEXT, LstName TEXT, Gmail TEXT, Username TEXT, Password TEXT)")
	conn.commit()
	conn.close()


def insert(FstName,LstName,Gmail,Username,Password):
	conn = sqlite3.connect("Database1.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO Credentials VALUES (?,?,?,?,?)", (FstName, LstName, Gmail, Username, Password))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("Database1.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM Credentials")
	data = cur.fetchall()
	conn.close()
	return data

	# sheet = "D:\Bhaskar\Py\Registration\Data.xlsx"

	# workbook = xlwt.Workbook(encoding='utf-8')
	# worksheet = workbook.add_sheet("Sheet1",cell_overwrite_ok=True)
	# worksheet.Title = "Database"
def dataToExcel():
	rootpath = os.getcwd()
	rootpath = rootpath+"/Data.xlsx"

	df = pd.DataFrame(data)
	data2Excel = pd.ExcelWriter(rootpath, engine='xlsxwriter')
	df.to_excel(data2Excel, sheet_name='Sheet1')
	data2Excel.save()

# def delete(Gmail):
# 	conn = sqlite3.connect("Database1.db")
# 	cur = conn.cursor()
# 	cur.execute("DELETE FROM Credentials WHERE Gmail=?",(Gmail,))
# 	conn.commit()
# 	conn.close()

crt_table()
# delete("bhaskar246@gmail.com")
# print(view())

