import csv

# Grade to credit mapping for units 4-10
unit_credits = {4: 6, 5: 6, 6: 6, 7: 9, 8: 6, 9: 6, 10: 6}

# Credit to UCAS point mapping
credit_points = {6: {'P': 6.4, 'M': 12.8, 'D': 19.2}, 9: {'P': 9.6 , 'M': 19.2, 'D': 28.8}}

# Open the input file in read mode
with open('C:/Users/User/Documents/pythonfiles/grades.csv', 'r') as grades_file:
    # Create a CSV reader object
    grades_reader = csv.reader(grades_file)
    # Skip the header row
    next(grades_reader)
    # Open the output file in write mode
    with open('C:/Users/User/Documents/pythonfiles/results.csv', 'w', newline='') as results_file:
        # Create a CSV writer object
        results_writer = csv.writer(results_file)
        # Write the header row to the output file
        results_writer.writerow(['Forename', 'Surname', 'Pass credits', 'Merit credits', 'Distinction credits', 'UCAS Score'])
        # Iterate over the rows in the input file
        for row in grades_reader:
            # Extract the student's name and grades
            forename, surname, *grades = row
            # Initialize the credit and UCAS point totals
            pass_total, merit_total, distinction_total, ucas_total = 0, 0, 0, 0
            # Iterate over the units 4-10
            for unit, grade in enumerate(grades[3:], start=4):
                if grade in ('P', 'M', 'D'):
                    # Increment the appropriate credit total
                    if grade == 'P':
                        pass_total += unit_credits[unit]
                    elif grade == 'M':
                        merit_total += unit_credits[unit]
                    else:
                        distinction_total += unit_credits[unit]
                    # Increment the UCAS point total using credit_points
                    ucas_total += credit_points[unit_credits[unit]][grade]
            # Write the student's name and totals to the output file
            results_writer.writerow([forename, surname, pass_total, merit_total, distinction_total, ucas_total])
            # Print the student's name and totals to the console
            print(f'{forename} {surname}: Credit Total of Passes: {pass_total}, Credit Total of Merits: {merit_total}, Credit Total of Distinctions: {distinction_total}, UCAS Score: {ucas_total}')






















