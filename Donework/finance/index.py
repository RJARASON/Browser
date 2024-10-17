table_data = [
    ["Name", "Age", "City"],
    ["John Doe", 30, "New York"],
    ["Jane Smith", 25, "Chicago"],
    ["Mike Johnson", 35, "Los Angeles"]
]

def calculate_column_widths(data):
    column_widths = []
    for col in range(len(data[0])):
        column_width = max(len(str(row[col])) for row in data)
        column_widths.append(column_width)
    return column_widths

def print_table(data):
    column_widths = calculate_column_widths(data)

    for col, header in enumerate(data[0]):
        print(f"{header:<{column_widths[col]}}", end=" | ")
    print()
    
    for col_width in column_widths:
        print("-" * col_width, end=" | ")
    print()
    
    for row in data[1:]:
        for col, value in enumerate(row):
            print(f"{value:<{column_widths[col]}}", end=" | ")
        print()

print_table(table_data)







# num_rows = 5
# num_columns = 3

# def print_empty_table(rows, cols):
#     # Print headers
#     for col in range(cols):
#         print("+-----", end="")
#     print("+")

#     for row in range(rows):
#         for col in range(cols):
#             print("|     ", end="")
#         print("|")

#         # Print row separators
#         if row < rows - 1:
#             for col in range(cols):
#                 print("+-----", end="")
#             print("+")

# print_empty_table(num_rows, num_columns)
