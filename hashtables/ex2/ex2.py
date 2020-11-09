#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    myHash = {}
    route = []

    for ticket in tickets:
        myHash[ticket.source] = ticket.destination

    route.append(myHash['NONE'])

    while len(route) < length:
        currentRoute = route[len(route) - 1]
        route.append(myHash[currentRoute])

    return route
