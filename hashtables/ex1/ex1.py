#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for zeroth in range(0, length):
        # **The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index. IF PAIR DOESNT EXIST SHOULD RETURN NONE LINE 23**

        # * If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`.
        first = hash_table_retrieve(ht, (limit - weights[zeroth]))
        if first != None:
            #Your function will return an instance of an `Answer` tuple that has the following form
           answer = (zeroth, first)
           print(answer)
           return answer
           # IF KEY DOESNT EXIST THEN INSERT IT and retry
        hash_table_insert(ht, weights[zeroth], zeroth)
    

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
