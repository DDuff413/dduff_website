# Import the libraries that Holus requires.
import xlrd 
import xlsxwriter
import os

#####################################################################################
#                                                                                   #
#                           Editing the return information.                         #
#                                                                                   #
#   To change the target sheet "tab" of the input files, change the "target_sheet"  #
#   variable.                                                                       #
#                                                                                   #
#   To change the number of rows read from each input file, change "num_rows".      #
#   Remember, the number of rows must include the title row.                        #
#   i.e. 68 rows will return the title of each column followed by 67 lines of data  #   
#                                                                                   #
#   To add a column to be returned you must do three things in this order.          #
#   1. Add the list to be initialised after the seven existing lists.               #
#   2. At the end of the "columns" list, add your new list in this format           #
#       [list, column_number] (column_numbers count from 0).                        #
#   3. Add the name of the column to the "sheets list" as a string (in quotes).     #
#                                                                                   #
#   To remove a column from being returned, do the above three steps in reverse.    #
#                                                                                   #
#####################################################################################

target_sheet = 1 #change this to change which sheet is being targeted
num_rows = 68

# Initalise 7 variable lists the will hold the information found in the input file.
cell_count = []
cell_confluence = []
cell_eccentricity = []
cell_irregularity = []
cell_area = []
cell_volume = []
cell_thickness = []

#Initalise and populate list of lists containing each variable list and the appropriate column number for said list.
columns = [[cell_count, 16], [cell_confluence, 17], [cell_eccentricity, 28], [cell_irregularity, 30], [cell_area, 19], [cell_volume, 35], [cell_thickness, 34]]

#Initalise the list of column names that will be used to name the sheets of the output file.
sheets = ["cell_count", "cell_confluence", "cell_eccentricity", "cell_irregularity", "cell_area", "cell_volume", "cell_thickness"]


######################## DON'T TOUCH ANYTHING BELOW HERE ########################
print("Greetings, Holus B. 'Excelsior' Collins at your survice. Press 'enter' to begin transference.")
input()
print("Proccessing...")

#Get list of files in the input directory.
input_files = os.listdir("input")
num_files = input_files.count

for file_name in input_files:
    input_loc = ('input\\' + file_name)

    wb = xlrd.open_workbook(input_loc) 
    sheet = wb.sheet_by_index(target_sheet) 
    # num_rows = sheet.nrows

    # Loop through each variable list saving the cells in the appropriate column for that list into it.
    for variable_list, column in columns:
        for count in range(num_rows):
            variable_list.append(sheet.cell_value(count, column))

    print("\n" + file_name + " has been scanned sir.")

print("\nExcelsior!")
print("All files have successfully been scanned.\n")

x = 0

for file_name in input_files:
    cell_count [x * num_rows] = file_name
    cell_confluence [x * num_rows] = file_name
    cell_eccentricity [x * num_rows] = file_name
    cell_irregularity [x * num_rows] = file_name
    cell_area [x * num_rows] = file_name
    cell_volume [x * num_rows] = file_name
    cell_thickness [x * num_rows] = file_name

    x += 1


output_loc = ('output\\HBEC_Output.xlsx')

# Open the output file.
workbook = xlsxwriter.Workbook(output_loc)

i = 0

# For each list in the list of lists, open a new worksheet and write the information in the list into said worksheet.
for column_info in columns:
    worksheet = workbook.add_worksheet(sheets[i]) 
            
    # Start from the first cell. 
    # Rows and columns are zero indexed. 
    row = 0
    column = 0
            
    # iterating through variable list 
    for item in column_info[0]:
        # Write the item into the file. 
        worksheet.write(row, column, item) 
        
        # Incrementing the value of row by one.
        row += 1

        if row == num_rows:
            row = 0
            column += 1
            
    i += 1

#Close the workbook.
workbook.close()  

print("The process is complete and I have fulfilled my purpose.")
print("Press 'enter' to end me...")
input()
print("\n\nIt has been a pleasure.")