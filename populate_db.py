#!/usr/bin/env python
# coding: utf-8

# In[24]:


import sqlite3


# '''THIS WAS ADDED TO SQLITE3 (from the COMMAND LINE)'''
# SQLite version 3.33.0 2020-08-14 13:23:32
# Enter ".help" for usage hints.
# Connected to a transient in-memory database.
# Use ".open FILENAME" to reopen on a persistent database.
# sqlite> sqlite3 app.db
#    ...> CREATE TABLE IF NOT EXISTS stock (
#    ...>     id INTEGER PRIMARY KEY,
#    ...>     symbol TEXT NOT NULL UNIQUE,
#    ...>     company TEXT NOT NULL
#    ...> );
# Error: near "sqlite3": syntax error
# sqlite> CREATE TABLE IF NOT EXISTS stock (
#    ...>     id INTEGER PRIMARY KEY,
#    ...>     symbol TEXT NOT NULL UNIQUE,
#    ...>     company TEXT NOT NULL
#    ...> );
# sqlite> .schema
# CREATE TABLE stock (
#     id INTEGER PRIMARY KEY,
#     symbol TEXT NOT NULL UNIQUE,
#     company TEXT NOT NULL
# );
# sqlite> CREATE TABLE IF NOT EXISTS stock_price (
#    ...>     id INTEGER PRIMARY KEY,
#    ...>     stock_id INTEGER,
#    ...>     date NOT NULL,
#    ...>     open NOT NULL,
#    ...>     high NOT NULL,
#    ...>     low NOT NULL,
#    ...>     close NOT NULL,
#    ...>     adjusted_close NOT NULL,
#    ...>     volume NOT NULL,
#    ...>     FOREIGN KEY (stock_id) REFERENCES stock (id)
#    ...> );
# sqlite> SELECT * FROM stock;
# sqlite> sqlite3 app.db
#    ...> SELECT * FROM stock;
# Error: near "sqlite3": syntax error
# sqlite> SELECT * FROM stock;
# sqlite> sqlite3 app.db
#    ...> .schema
#    ...> SELECT * FROM stock;
# Error: near "sqlite3": syntax error
# sqlite> sqlite3 app.db
#    ...> SELECT * FROM stock;
# Error: near "sqlite3": syntax error
# sqlite> .schema
# CREATE TABLE stock (
#     id INTEGER PRIMARY KEY,
#     symbol TEXT NOT NULL UNIQUE,
#     company TEXT NOT NULL
# );
# CREATE TABLE stock_price (
#     id INTEGER PRIMARY KEY,
#     stock_id INTEGER,
#     date NOT NULL,
#     open NOT NULL,
#     high NOT NULL,
#     low NOT NULL,
#     close NOT NULL,
#     adjusted_close NOT NULL,
#     volume NOT NULL,
#     FOREIGN KEY (stock_id) REFERENCES stock (id)
# );
# sqlite> SELECT * FROM stock;
# sqlite>

# In[39]:


connection = sqlite3.connect('app.db')
cursor = connection.cursor()
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('ADBE', 'Adobe Inc.')")
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('VZ', 'Verizon')")
connection.commit()


# In[40]:


import sqlite3
connection = sqlite3.connect('app.db')
cursor = connection.cursor()
cursor.execute("DELETE FROM stock")
connection.commit()


# In[41]:


pip install alpaca-trade-api


# In[42]:


import alpaca_trade_api as tradeapi
api = tradeapi.REST('PKJGCH2HKNL7KN06VEDN', 'zgOYKGQyKIM4562crRzVaFQIF2HC19Bh5I14ZNxj', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
assets = api.list_assets()
for asset in assets:
    print(asset)


# In[43]:


import sqlite3
import alpaca_trade_api as tradeapi
connection = sqlite3.connect("app.db")
cursor = connection.cursor()
api = tradeapi.REST('PKJGCH2HKNL7KN06VEDN', 'zgOYKGQyKIM4562crRzVaFQIF2HC19Bh5I14ZNxj', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
assets = api.list_assets()
for asset in assets:
    # print(asset)
    cursor.execute("""
            INSERT INTO stock (symbol, name, exchange)
            VALUES (?, ?, ?)
    """, (asset.symbol, asset.name, asset.exchange))
connection.commit()


# In[ ]:


import sqlite3
import alpaca_trade_api as tradeapi
connection = sqlite3.connect("app.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
api = tradeapi.REST('PKJGCH2HKNL7KN06VEDN', 'zgOYKGQyKIM4562crRzVaFQIF2HC19Bh5I14ZNxj', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
assets = api.list_assets()
for asset in assets:
    #print(asset)
    try:
        cursor.execute("""
            INSERT INTO stock (symbol, name, exchange)
            VALUES (?, ?, ?)
        """, (asset.symbol, asset.name, asset.exchange))
    except Exception as e:
        print(e)
        print(asset)
connection.commit()


# In[ ]:


for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)


# sqlite3 app.db #now try to run this in the command line
# 
# sqlite> SELECT * FROM stock;

# Looks like we have a pretty good database. That’s it for this tutorial, we covered a lot! We now know to connect to SQLite from Python and execute SQL queries with a cursor. We also learned to retrieve a list of tradable assets using the Alpaca Trade API. With the data we retrieved from Alpaca, we were able to populate a database by using INSERT statements in a loop. In addition, we learned how to validate and handle exceptions that may occur, including duplicate and inactive symbols. Finally, we learned to verify that our data makes sense and browse our populated database from the command line.
# 
# In the next tutorial, we will set up scheduled jobs to automatically fetch new symbols and stock prices every day. This will allow us to keep our database up to date with the latest information.

# In[ ]:


cursor.execute("""
    SELECT symbol, company FROM stock
""")
rows = cursor.fetchall()
for row in rows:
    print(row['symbol'])
    # try:
    #     if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
    #         print(f"Adding a new asset {asset.symbol} {asset.name}")
    #         cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    # except Exception as e:
    #     print(asset.symbol)
    #     print(e)


# In[ ]:





# In[ ]:




