def check_connection(connections, person1, person2):
    graph = {}
    for i in connections:
        split_connections = i.split("-")

        first_connection = split_connections[0]
        second_connection = split_connections[1]
        if first_connection not in graph:
            graph[first_connection] = [second_connection]

        else:
            graph[first_connection].append(second_connection)

        if second_connection not in graph:
            graph[second_connection] = [first_connection]
        else:
            graph[second_connection].append(first_connection)

    start = graph[person1]
    for i in start:
        if i == person2:
            print True
            return True
        else:
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