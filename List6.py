import sqlite3

con = sqlite3.connect("GreatUkrainian.db")
curs = con.cursor()

curs.execute("""CREATE TABLE People
		  (id INTEGER PRIMARY KEY, 
                  first_name TEXT, 
                  second_name INTEGER, 
                  sex TEXT,
                  year TEXT,
                  city TEXT,
                  FOREIGN KEY (second_name) REFERENCES Status(name),
                  FOREIGN KEY (year) REFERENCES Post(born))""")
curs.execute("""CREATE TABLE Status
		  (id INTEGER PRIMARY KEY, 
                  name INTEGER, 
                  magnum_opus TEXT, 
                  year TEXT)
		  """)
curs.execute("""CREATE TABLE Post
		  (id INTEGER PRIMARY KEY,
		  born TEXT,	
                  died TEXT,
		  address TEXT)
		  """)
curs.execute(
    'INSERT INTO People (first_name , second_name , sex , year , city) VALUES ("Taras" , "Shevchenko" , "m" , "1814" , "v.Morynci")')
curs.execute(
    'INSERT INTO People (first_name , second_name , sex , year , city) VALUES("Lesya" , "Ukrainka" , "f" , "1871" , "Novohrad-Volynskyi")')
curs.execute(
    'INSERT INTO People (first_name , second_name , sex , year , city) VALUES ("Ivan" , "Franko" , "m" , "1856", "Nahuievychi")')

curs.execute('INSERT INTO Status (name , magnum_opus , year) VALUES ("Shevchenko" , "Kobzar" , "1837")')
curs.execute('INSERT INTO Status (name , magnum_opus , year) VALUES ("Ukrainka" , "The Forest Song" , "1911")')
curs.execute('INSERT INTO Status (name , magnum_opus , year) VALUES ("Franko" , "Zahar Berkyt" , "1882")')

curs.execute('INSERT INTO Post (born , died , address) VALUES ("1814" , "1861" , "Saint Peterburg")')
curs.execute('INSERT INTO Post (born , died , address) VALUES ("1871" , "1913" , "Surami")')
curs.execute('INSERT INTO Post (born , died , address) VALUES ("1856" , "1916" , "Lemberg")')

con.commit()
curs.close()
con.close()
