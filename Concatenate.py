
def collect_all_csv_filenames():
    from glob import glob
    import os
    csv_filenames =  glob('*.csv')
    if "everyone.csv" in csv_filenames:  # Remove old everyone.csv file before creating new list
        os.remove('everyone.csv')
        csv_filenames.remove('everyone.csv')
    return csv_filenames

def read_and_write(files):
    import csv
    STDOUT = 0               # Count of how many teams use Camel Case
    first_name_index = 0
    last_name_index = 1
    netid_index = 2
    git_name_index = 3
    team_name_index = 4
    csv_list = []

    for file in files:
        with open(file) as csvfile:
            csv_reader = csv.reader(csvfile,delimiter=',')
            for row in csv_reader:
                if row != [] and row[netid_index]!= " mlp6" and row[team_name_index] != " Teamname" : # Empty array in here for some reason?
                    team_name = row[team_name_index]        # Identify column containing team name
                    net_id = row[netid_index]               # Identify column containing netid

                    name_no_lead_space = team_name.strip()  # Remove leading spaces before checking camel case
                    netid_no_lead_space = net_id.strip()    # Remove leading spaces - use this for json file name

                    camel_case = check_camel_case(name_no_lead_space)
                    if camel_case == 'Camel Case!':
                        STDOUT = STDOUT + 1

                    csv_list.append(row)                     # Create list containing everyone's info
                    write_data(row,netid_no_lead_space)      # Create JSON file from CSV
                    print(name_no_lead_space,":",camel_case)


    print("Camel Case Count:",STDOUT)                         # Print out number of teams who used CamelCase

    create_class_file(csv_list)                                # Compile all class info into everyone.csv
    return csv_list

def check_no_spaces(team_name):
        if team_name.find(" ") == -1:
            spaces = True
        else:
            spaces = False
        return spaces

def check_camel_case(team_name):

    no_spaces = check_no_spaces(team_name)        # Checks for spaces

    if team_name.isalpha() == True:               # Check for numbers
         no_numbers = True
    else: no_numbers = False

    if team_name[0].isupper():                    # Check that first letter is capitalized
        capitalized = True
    else: capitalized = False

    if no_numbers == True and no_spaces == True and capitalized == True:
        my_string = 'Camel Case!'
    else:
        my_string = 'Not Camel Case!'

    return my_string

def write_data(data,file_json):
    import json
    with open(file_json,'w') as new_file:
        new_file.write(json.dumps(data))

def create_class_file(list):
    import csv
    with open('everyone.csv','w') as class_file:
            writer = csv.writer(class_file)
            for line in list:
                writer.writerow(line)
            class_file.close()


# Execute code
file_names = collect_all_csv_filenames()
read_and_write(file_names)





