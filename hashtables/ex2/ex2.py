#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #`source` string represents the starting airport and the `destination` string represents the next airport along our trip.
    # The ticket for your first flight has a destination with a `source` of `NONE`, and the ticket for your final flight has a `source` with a `destination` of `NONE`. 
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
    #initialize empty list
    flights = []
    #retrieve destination (NONE)
    destination = hash_table_retrieve(hashtable, 'NONE')

    while destination != "NONE":
        #loop inserting ht then stopping at none
        #inserting destination into emppty list flights
        flights.append(destination)
        destination=hash_table_retrieve(hashtable, destination)
        print(flights)
    return flights
