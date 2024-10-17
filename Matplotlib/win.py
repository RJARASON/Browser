import win32com.client

# Open Excel application
excel = win32com.client.Dispatch("Excel.Application")

# Make Excel visible (optional)
excel.Visible = True

# Add a new workbook
workbook = excel.Workbooks.Add()

# Select the active sheet
sheet = workbook.ActiveSheet

# Write to the first cell
sheet.Cells(1, 1).Value = "Hello, World!"

# Save the workbook
workbook.SaveAs(r"C:\path\to\your\file.xlsx")

# Close Excel
excel.Quit()
