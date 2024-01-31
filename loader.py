import openpyxl 

wb = openpyxl.load_workbook("tester.xlsx")
ws = wb ['sheet1']

rows = ws.iter_rows(min_row=1 , max_row=7,min_col=1,max_col=2)
print (rows)

for a, b in rows:
    print(a.value , b.value)