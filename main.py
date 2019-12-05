
import pandas as pd
import sqlite3


def read_sql():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM conta_task
                where done = 'Pagar';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql2():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM conta_task
                where done = 'Pago';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db
