#   Nicolas Callier
#   CSCI102 - SECTION H
#   Assessment 10
#   Time it took: 1 hour

import csv


with open('formations.csv', 'r') as infile:

    with open('formations_parsed.csv', 'w', newline='') as outfile:

        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(['Depth', 'Start Depth', 'End Depth', 'Difference in Depth', 'Formation', 'Age of Formation'])

        next(reader)

        for row in reader:

            start_depth, end_depth = map(float, row[0].split('-'))

            diff_depth = end_depth - start_depth

            if start_depth < 700:
                age = 'Paleocene'
            else:
                age = 'Cretaceous'

            writer.writerow([row[0], start_depth, end_depth, f'{diff_depth:.2f}', row[1], age])

