
import xlrd

wb = xlrd.open_workbook(r'C:\Users\ghz\Desktop\test.xlsx')
sheet = wb.sheet_by_index(0)

nrows = sheet.nrows
ncols = sheet.ncols

for row in range(nrows):
    for col in range(ncols):
        print(sheet.cell_value(row, col))

