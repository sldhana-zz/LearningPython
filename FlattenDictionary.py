"""
Nikola likes to categorize everything in sight. One time Stephan gave
him a label maker for his birthday, and the robots
 were peeling labels off of every surface in the ship for weeks. He
has since categorized all the reagents in his laboratory,
  books in the library and notes on the desk. But then he learned
about python dictionaries, and categorized all the
  possible configurations for Sophia's drones. Now the files are
organized in a deep nested structure, but Sophia doesn't
  like this. Let's help Sophia to flatten these dictionaries.
Python dictionaries are a convenient data type to store and process
configurations. They allow you to store data by keys
to create nested structures. You are given a dictionary where the keys
are strings and the values are strings or dictionaries.
 The goal is flatten the dictionary, but save the structures in the
keys. The result should be the a dictionary without
 the nested dictionaries. The keys should contain paths that contain
the parent keys from the original dictionary. The keys
 in the path are separated by a "/". If a value is an empty
dictionary, then it should be replaced by an empty string ("").
 Let's look at an example:
{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}
The result will be:
{"name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"}
Sophia has already written the code for this task, but it has a bug.
"""

def flatten(dictionary):
    if dictionary:
        result = {}

        for i in dictionary:
            if isinstance(dictionary[i], dict):
                res = flatten(dictionary[i])

                if res:
                    for j in res:
                        result[i + "/" + j] = res[j]
                else:
                    result[i] = ""

            else:
                result[i] = dictionary[i]

        print result
        return result

    else:
        return None


flatten({"empty": {}}) == {"empty": ""}

flatten({
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout"
})