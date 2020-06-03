def ticket():
    name = input("plz enter your name: ")
    contact = int(input("plz enter your contact no: "))
    time = input("enter the time you want to go from 10.am,1.pm,7.pm: ")
    start = input("enter the place where you want to start: ")
    destination = input("enter the place where you want to go: ")
    rate_per_Seat = 500
    no_of_seats = int(input("plz enter no of seats you want to book: "))
    total_price = rate_per_Seat * no_of_seats
    return [{'ticketData': [name, contact, time, start + " " "to" " " + destination, total_price]}]


def book():
    ticketData = []
    ticketData.extend(ticket())
    savedata(ticketData)
    return ticketData


def savedata(ticketData):
    fopen = open('booking.txt', 'a')
    fopen.write(str(ticketData) + '\n')
    fopen.close()


def fetchData():  # this is used when we need to read the data
    fopen = open('booking.txt', 'r')
    data = fopen.read()
    fopen.close()
    return data


# main program
print("------Bus Ticket Management System--------")
ticketBook = []
clear = ""
flag = True
print("Punbus >>>>Make your trip easier>>>>>> ")
while flag:
    print("for booking a ticket press 'b' or 'B'")
    print("for viewing a ticket press 'v' or 'V'")
    print("for canceling a ticket press 'c' or 'C'")

    print("----------------------------------------------")

    userinput = input("enter your choice: ")
    if userinput == 'b' or userinput == 'B':
        ticketBook.extend([book()])
        # print(ticketBook)
        print("-----------------------------------------")
    elif userinput == 'v' or userinput == 'V':
        viewData = fetchData()
        print(viewData)

    elif userinput == 'c' or userinput == 'C':
        fopen = open('booking.txt', 'r')
        clear = fopen.read()
        del clear
        print("Cancellation successfull")
        fopen.close()

    else:
        print(">>>Invalid Option!!! Please Try Again!!!")
