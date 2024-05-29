import pandas as pd
file_path = "graduation requirements.xsls"
sheet_name = 'test'
df = pd.read_excel(file_path, sheet_name=sheet_name)

#later change this to be the input of the user
search_value = 'Jane Doe'

#reads the value of the first cell in each column as the column name
#name_columns is a LIST of values made by the df.columns function.
name_columns = df.columns
#makes a new boolean set to 'false' (this may change later)
found = False
#column_name is a new variable in the "for" loop.
for column_name in name_columns:
   #checking to make sure the column HAS a name
    if df[column_name].iloc[0] == column_name:
        #searches for search_value in the column and assigns the result to found_row
        found_row = df[df[column_name] == search_value]
        if not found_row.empty: #checks to see if the search came up not empty, meaning the term was found
            next_column_index = df.columns.get_loc(column_name) + 1
            if next_column_index < len(df.columns):
                next_column_name = df.columns[next_column_index]
                next_value = found_row[next_column_name].values[0]
                print('You took: "{search_value}"')
                print('Your grade was: "{next_value}"')
