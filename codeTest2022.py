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
visual(movieSeats)
valid = False
while not valid: 
  bookingName = input("Enter Your Full Name: ")
  if bookingName == "":
    print("Please Enter A Name")
  else:
    valid = True
booking = True
while booking:
    valid = False
    while not valid:
        numOfSeats = input("How Many Seats Are You Booking: ")
        if  numOfSeats.isdigit() :
            if int(numOfSeats) <= avalibleSeatCount(movieSeats):
                valid = True
            else: 
                print("Not Enough Seats Avalible")
        else:
            print("Please Enter A Number")
    visual(movieSeats)
    chosenSeats = []
    for i in range(0,int(numOfSeats)):
        valid = False
        while not valid:
            choice = input("Please Choose A Seat: ")
            transValid = translateAndValidate(choice)
            if transValid != False:
                if movieSeats[transValid[0]][transValid[1]] == "available":
                    chosenSeats.append(transValid)
                    valid = True
                else:
                    print("Seat unavailable")
            else:
                print("Invalid Seat")
        for i in chosenSeats:
          movieSeats[i[0]][i[1]] = "unavailable"
        visual(movieSeats)
        #put all arounf chosen seats as unavalible

    bookingName = input("Enter Your Full Name: ")
    if bookingName == "":
        booking = False
