
############################################# for else use cases #############################################

# #task : check for missing names in a list
# names = ['Ram', 'tuba', 'Ayushi', 'shriya']
# for name in names:
#     if name == None:
#         print("name is empty")
#         break
# else:
#     print("no empty names in the list")


# # check if all the files are csv
# files = ['data.csv', 'report.csv', 'python.pdf']
# for file in files:
#     if not file.endswith('.csv'):
#         print("All the files are not .csv")
#         break
# else:
#     print(" All the files are .csv")


# # printing the name of file which has issue. or doesnt end with.csv 
# files = ['data.csv', 'report.csv', 'python.pdf']
# for file in files:
#     if not file.endswith('.csv'):
#         print(f'{file} file is not .csv')
#         break
# else:
#     print(" All the files are .csv")


# # if we use continue instead of break
# # output - python.pdf file is not .csv, sql.txt file is not .csv, All the files are .csv (which is incorrect)
# # it makes no sense to use else + continue together 
# files = ['data.csv', 'report.csv', 'python.pdf', 'sql.txt']
# for file in files:
#     if not file.endswith('.csv'):
#         print(f'{file} file is not .csv')
#         continue 
# else:
#     print("All the files are .csv")

############################################ python challenge #################################################

# # check wither any filename appears more than once 

# files = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
# for file in files:
#     print(files.count(file))

# files = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
# for file in files:
#     if files.count(file) > 1:
#         print("duplicate file found")
#         break
# else:
#     print("all files are unique")

##############################################################################################################

###################################### Nested loops ##########################################################

# # its just a loop inside a loop

# for x in (1,2,3):
#     for y in (4,5):
#         print(x , y)

# for x in (1,2,3):
#     for y in (4,5):
#         for z in (6,7):
#             print(x , y, z)

# for x in range(3):
#     for y in range(2):
#         print(f'({x}, {y})')

# for x in range(3):
#     for y in range(2):
#         for z in range(2):
#             print(f'({x}, {y}, {z})')        

#### use case ####
# # crossing the data - all possible combinations, navigating hierarchy:, navigating through data base(table , columns and rows)

# colors = ['red', 'blue', 'green']
# sizes = ['s', 'm', 'l', 'xl']
# for color in colors:
#     for size in sizes:
#         print(f'{color} size- {size}')  # crossing the data

# years = ['2024', '2025', '2026']
# months = ['jan', 'feb']
# for y in years:
#     for m in months:
#         for d in range(1,31):
#             print(f'{y} - {m} -{d}') # navigating hierarchy 

table = ['customer', 'order', 'products', 'prices']
columns = ['id', 'create_date']
for t in table:
    for column in columns:
        print(f'select count from {t} to {column} is null')
