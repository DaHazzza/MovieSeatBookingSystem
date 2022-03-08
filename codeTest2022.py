def visual(seatMatrix):
    alphabetLables = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    print("  1  2  3  4    5  6  7  8  9  10 11 12 13 14 15 16   17 18 19 20")
    for i in range(0,12):
        line =  f"{alphabetLables[i]} "
        if i ==3: #creates walkway between c-d
            print("")
        for j in range(0,20):
            if j == 4 or j == 16: #creates the walkways between row 4-5 and 16-17
                line += "  "
            if A320_seats[i][j] == "available":
                line +=  "O  "
            elif A320_seats[i][j] == "unavailable":
                line +=  "X  "
            else:
              line += "   "
        print(line)

A320_seats = []
blockedSeats = [[2,4],[2,10],[11,18]]

for i in range(0,12):
    A320_seats.append([])
    for j in range(0,20):
        if i >=3 and i <=9 and j <= 3:
             A320_seats[i].append("n/a") #blanks out from d1 to k4 as seen in the diagram
        else:
             A320_seats[i].append("available")

for i in blockedSeats:
    A320_seats[i[0]][i[1]] = "n/a"
visual(A320_seats)
