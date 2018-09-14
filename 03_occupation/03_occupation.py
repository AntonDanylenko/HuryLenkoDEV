import random

def main():
    file = open("occupations.csv", "r")
    #open the data file and reads the contents

    flines = file.readlines()[1:]
    #readlines reads the individual lines of the file starting from the second

    dict = {}
    #initializes the dictionary

    for line in flines:
        #print(line)
        quote = False
        #initializes whether or not the occupation is in quotes as false
        occupation = ""
        #initializes the occupation name
        num = False
        #initializes whether we are parsing through the percent as false
        percent = ""
        #initializes the percent string
        for character in line:
            if character == "\"":
                quote = not quote
                #if a char is a quote, either turn quote true to start the quote
                #or turn it false if the quote just ended.
            elif character == ",":
                if quote:
                    occupation += character
                    #if the comma in inside a quote, add it as part of the
                    #occupation name.
                else:
                    num = True
                    #if comma is not inside quote, start recording the percent
            else:
                if num:
                    percent += character
                    #if char is not a quote or a comma, and we are
                    #recording the percent, add the char to the percent string
                else:
                    occupation += character
                    #if char is not quote, comma, or part of the percent number,
                    #add char to the occupation string.
        #print(occupation)
        #print(percent)
        percent = percent.replace("\n", "")
        #newlines were added to the end of the percent string from the end
        #of every line, so we must remove them.
        dict[occupation]= (float)(percent)
        #the occupation and percent of each line are logged in the dictionary
    randNum=random.random()*dict["Total"]
    #gets a random number with one decimal from 0 to 99.7, starts at .1 because starting at 0 would mean that if the first occ had 0%, it could be chosen
    counter=0.0
    for occ in dict:
        if occ=="Total":
            print("current counter: ",counter)
            continue
            # in case total comes out of order because it would always become true
        if randNum <= counter+dict[occ]: #check if the rand number is between the original counter # and the max percent for the occ
            return occ
        else:
            counter+=dict[occ]



counters={"Management":0, 'Business and Financial operations': 0, 'Computer and Mathematical': 0, 'Architecture and Engineering': 0, 'Life, Physical and Social Science': 0, 'Community and Social Service': 0, 'Legal': 0, 'Education, training and library': 0, 'Arts, design, entertainment, sports and media': 0, 'Healthcare practioners and technical': 0, 'Healthcare support': 0, 'Protective service': 0, 'Food preparation and serving': 0, 'Building and grounds cleaning and maintenance': 0, 'Personal care and service': 0, 'Sales': 0, 'Office and administrative support': 0, 'Farming, fishing and forestry': 0, 'Construction and extraction': 0, 'Installation, maintenance and repair': 0, 'Production': 0, 'Transportation and material moving': 0, 'Total': 0}
for i in range(1,1000):
    test=main()
    counters[test]=counters[test]+1
print(counters)
total=0
for occ in counters:
    total+=counters[occ]
print(total)
