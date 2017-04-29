import sys

#take in the source file name
sourceFile = sys.argv[1]
textFile = open(sourceFile)

#empty list for those vitamins with < 1% of recommended daily requirement
not_enough_name = []

for line in textFile :
    
    info = line.strip().split()
    
    #take in the 4 variables on each line
    amt_per_serving = float(info[0])
    units = info[1]
    daily_req = float(info[2])
    
    #viamin name is the rest of the line, including spaces
    vitamin_name = info[3:len(info)]
    vitamin_name = " ".join(vitamin_name)
    
    #if this is the last entry - negative first value, go here
    if amt_per_serving < 0: 
        #if there were vitamins with no significant amount, print now
        if len(not_enough_name) > 0:
            print ("Provides no signficant amount of: ")
            for i in range (len(not_enough_name)):
                print (not_enough_name[i])
        #end the program
        break 
    
    #if this is not the last entry - go here
    else:
        
        #get the percentage
        percentage = (amt_per_serving/daily_req) * 100
        
        #check to see if there is enough; print out info if there is
        if percentage > 1:
            print (vitamin_name, '%.1f' % amt_per_serving, units, '%.0f' % percentage +"%")
        
        #if there is not enough, append to the list of vitamin names to print
        #at the end
        else:
            not_enough_name.append(vitamin_name)





