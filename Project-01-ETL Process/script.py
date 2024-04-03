import os
import pandas as pd

# Step-1: Create directories as Company-A and Company-B
def create_directories():
    directories = ['Company-A', 'Company-B']

    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print(f'{directory} is created.')
        else:
            print(f'{directory} already exists.')

# Step-2: Create an excel, csv, and txt file in Company-A and store some data in files
def create_files_and_store_data_for_company_a():
    employees_data = {
        'Name': ['Tom', 'Nick', 'Anna', 'Jack', 'Eva'],
        'Age': [20, 21, 19, 18, 22]
    }

    df = pd.DataFrame(employees_data)

    df.to_excel('Company-A/employees.xlsx', index=False)
    print('Excel file is created in Company-A')

    df.to_csv('Company-A/employees.csv', index=False)
    print('Csv file is created in Company-A')

    df.to_csv('Company-A/employees.txt', sep=' ', index=False)
    print('Text file is created in Company-A')

# Step-3: Extract the excel, csv, and txt files from Company-A and transform these files and load them into Company-B
def extract_transform_load_files_into_company_b():
    # Extract
    df1 = pd.read_excel('Company-A/employees.xlsx')
    df2 = pd.read_csv('Company-A/employees.csv')
    df3 = pd.read_csv('Company-A/employees.txt', sep=' ')

    # Transformation: sort the DataFrames by name
    df1 = df1.sort_values('Name')
    df2 = df2.sort_values('Name')
    df3 = df3.sort_values('Name')

    # Load
    df1.to_excel('Company-B/employees.xlsx', index=False)
    print('Transformed excel file is created in Company-B')

    df2.to_csv('Company-B/employees.csv', index=False)
    print('Transformed csv file is created in Company-B')

    df3.to_csv('Company-B/employees.txt', sep=' ', index=False)
    print('Transformed text file is created in Company-B')

# Step-4: Run all methods
def run_script():
    create_directories()
    create_files_and_store_data_for_company_a()
    extract_transform_load_files_into_company_b()

run_script()
