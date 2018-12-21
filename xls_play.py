import xlsxwriter

workbook = xlsxwriter.Workbook("yolo.xlsx")
spreadsheet = workbook.add_worksheet(name="ylolo")

spreadsheet.write(0, 0, "hello_world")
workbook.close()