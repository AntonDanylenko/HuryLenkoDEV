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
    print(dict)

main()
