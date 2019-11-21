# ruepractice

Rue 21 Code Kata 

Our client wants us to take a CSV file of their Purchase Orders(POs), parse it, and 
upload it into a DB. They will then upload a second CSV file with updates and new POs. Log any updates or new insertions that result from uploading the second CSV 
file. 

Example 
PO: 00001234 updated Color Red to Blue PO: 00003334 added to DB 

PO is the primary key and will not be updated, all other fields can be updated. 

Table 
PO Item Color Size Description Qty 
00001234 Shirt Red M Red Striped shirt 12 
0000123EU Pants Blue L Denim Jeans 14 
00001445 Shoes Green 12 Nike Jordans 15 
0000144H Jacket Orange M Wind breaker 2 

💡 Please use any language you feel comfortable with. DB doesn't have to be 
persistent. Logging changes to console or txt file is fine. 

Tools used:
Django Framework
Django admin
Sqlite DB
Django import-export library

Challenges:
Parsing data with trailing commas
Dealing with empty rows and columns

