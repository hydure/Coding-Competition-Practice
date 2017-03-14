import fileinput

stuffToSubtract = 0.0
establishedSections = []
count = 0
first = 0

for line in fileinput.input():
    newestSection = line.strip().split()
    if len(newestSection) == 1:
        highwayLength = float(newestSection[0])
    
    if len(newestSection) == 2:
        newestSection[0] = float(newestSection[0])
        newestSection[1] = float(newestSection[1])

        if newestSection[0] > newestSection[1]:
            print(establishedSections)
            # Look at each established section and add its space to the total spaces not available
            for establishedSection in establishedSections:
                stuffToSubtract += establishedSection[1] - establishedSection[0]
            print("The total planting length is: %", (highwayLength - stuffToSubtract))
            # Reset everything to be run for the next dataset
            stuffToSubtract = 0.0
            establishedSections = []
            first = 0
            continue

        if first == 0:
            establishedSections.append([newestSection[0], newestSection[1]])
            first = 1

        for establishedSection in establishedSections:
    
            # If the established section needs to be expanded on the lower end only 
            if newestSection[0] < establishedSection[0] and newestSection[1] >= establishedSection[0] and newestSection[1] <= establishedSection[1]:
                establishedSection[0] = newestSection[0]

            # If the established section needs to be expanded on the higher end only
            elif newestSection[0] >= establishedSection[0] and newestSection[0] <= establishedSection[1] and newestSection[1] > establishedSection[1]:
                establishedSection[1] = newestSection[1]

            # If the established section is engulfed by the newest section 
            elif newestSection[0] < establishedSection[0] and newestSection[1] > establishedSection[1]:
                establishedSection[1] = newestSection[1]
                establishedSection[0] = newestSection[0]

            # If newest section is engulfed by the established section
            elif newestSection[0] >= establishedSection[0] and newestSection[1] <= establishedSection[1]:
                continue

            # If the sections do not overlap
            else:
                count = 1

        # If the newest section did not overlap with any stored sections, append the section to establishedSections
        if count != 0:
            establishedSections.append([newestSection[0], newestSection[1]])
            # Reset to be run for the next established section
            count = 0