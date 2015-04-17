""""
Sophia's drones are not soulless and stupid drones; they can make and have friends. In fact, they already are
working for the their own social network just for drones! Sophia has received the data about the connections
between drones and she wants to know more about relations between them.

We have an array of straight connections between drones. Each connection is represented as a string with two names
of friends separated by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should
write a function that allow determine more complex connection between drones. You are given two names also. Try
to determine if they are related through common bonds by any depth. For example: if two drones have a common
friends or friends who have common friends and so on.
"""

def check_connection(connections, person1, person2):
    """
    :param connections: the tuples passed in containing connections
    :param person1: the first person
    :param person2: the second person the first person is supposed to be connected to
    :return: True or False depending on if a link exists
    """

    """
    My idea for this is a bi-directional graph.  If person1 has a connection to person2,
    the same connection also appears in the other direction.  In order to store the data,
    I am using a dictionary with the values being a list.
    """
    graph = {}
    # going through the tuple and splitting the data to be placed into the dictionary
    for i in connections:
        split_connections = i.split("-")

        first_connection = split_connections[0]
        second_connection = split_connections[1]

        # the logic here ensures no duplicates exists in the lists
        if first_connection not in graph:
            graph[first_connection] = [second_connection]

        else:
            graph[first_connection].append(second_connection)

        if second_connection not in graph:
            graph[second_connection] = [first_connection]
        else:
            graph[second_connection].append(first_connection)

    # start the connection finding
    start = graph[person1]
    for i in start:
        # if we manage to find person2 within the list, we return right away
        if i == person2:
            print True
            return True
        else:
            """
            This is the tricky one.  The person might not be in the direct list,
            so we need to get the subsequent lists and ensure we traverse it and
            add the data to the original list
            """
            other_connections = graph[i]
            for j in other_connections:
                if j not in start:
                    start.append(j)

    print False
    return False



check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False