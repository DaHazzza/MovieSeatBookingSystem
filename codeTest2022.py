from os import system


def visual(seatMatrix):
    alphabetLables = ["A","B","C","D","E","F","G","H","I","J","K","L"]
    print("  1  2  3  4    5  6  7  8  9  10 11 12 13 14 15 16   17 18 19 20")
    for i in range(0,12):
        line =  f"{alphabetLables[i]} "
        if i ==3: #creates walkway between c-d
            print("")
        for j in range(0,20):
            if j == 4 or j == 16: #creates the walkways between row 4-5 and 16-17
                line += "  "
            if seatMatrix[i][j] == "available":
                line +=  "O  "
            elif seatMatrix[i][j] == "unavailable":
                line +=  "X  "
            else:
              line += "   "
        print(line)

def avalibleSeatCount(seatMatrix):
    count = 0
    for i in seatMatrix:
        for j in i:
            if j =="available":
                count += 1
    return count

def translateAndValidate(selection):
  if selection != "":
      translated = []
      alphabetLables = ["A","B","C","D","E","F","G","H","I","J","K","L"]
      letter = selection[0]
      selection= selection[1:]
      number = selection
  
      if letter.upper() in alphabetLables:
          translated.append( alphabetLables.index(letter.upper()))
          if number.isdigit() and int(number )<= 20:
              translated.append(int(number)-1)
              return translated
          else:
              return False
      else:
          return False
  else:
    return False

def blockAround(seatChoices, seatMatrix):
    for i in seatChoices:
        #[1,1]
        if i[0] != 0 and seatMatrix[i[0]-1][i[1]] == "available": # all seats above
            seatMatrix[i[0]-1][i[1]] = "unavailable"
        if i[0] != 11 and seatMatrix[i[0]+1][i[1]] == "available":# all seats below
            seatMatrix[i[0]+1][i[1]] = "unavailable"
        if i[1]!=0 and seatMatrix[i[0]][i[1]-1] == "available":# all seats left
            seatMatrix[i[0]][i[1]-1] = "unavailable"
        if i[1] != 19 and seatMatrix[i[0]][i[1]+1] == "available":# all seats right
            seatMatrix[i[0]][i[1]+1] = "unavailable"
    return seatMatrix

def bookSeats(seatMatrix):
    bookingName = input("Enter Your Full Name: ")
    valid = False
    while not valid:
        numOfSeats = input("How Many Seats Are You Booking: ")
        if  numOfSeats.isdigit() :
            if int(numOfSeats) <= avalibleSeatCount(seatMatrix):
                valid = True
            else: 
                print("Not Enough Seats Avalible")
        else:
            print("Please Enter A Number")
    visual(seatMatrix)
    chosenSeats = []
    for i in range(0,int(numOfSeats)):
        valid = False
        while not valid:
            choice = input("Please Choose A Seat: ")
            transValid = translateAndValidate(choice)
            if transValid != False:
                if seatMatrix[transValid[0]][transValid[1]] == "available":
                    chosenSeats.append(transValid)
                    valid = True
                else:
                    print("Seat unavailable")
            else:
                print("Invalid Seat")
        seatMatrix[transValid[0]][transValid[1]] = "unavailable"
    seatMatrix = blockAround(chosenSeats, seatMatrix)
    visual(seatMatrix)
    return seatMatrix, bookingName

movieSeats = []
blockedSeats = [[2,4],[2,10],[10,18]]

for i in range(0,12):
    movieSeats.append([])
    for j in range(0,20):
        if i >=3 and i <=9 and j <= 3:
             movieSeats[i].append("n/a") #blanks out from d1 to k4 as seen in the diagram
        else:
             movieSeats[i].append("available")

for i in blockedSeats:
    movieSeats[i[0]][i[1]] = "n/a"

SystemOn = True
while SystemOn:
    valid = False
    while not valid:
        selection = input("Book Seats: 1 \nEmployee Lookup: 2\n")
        if selection == "2" or selection == "1" or selection == "":
            valid = True
    if selection == "1":
        name =""
        movieSeats, name = bookSeats(movieSeats)
        visual(movieSeats)
    if selection == "2":
        print("Havent Coded it lol")
    if selection == "":
        SystemOn = False
