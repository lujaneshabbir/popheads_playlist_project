import csv
import argparse

def add_line(type, file, params): # adds a line of data to the database
    if len(params) == 5:
        add_to_db(type, file, params[0], params[1], params[2], params[3], params[4])
    if len(params) == 4:
        add_to_db(type, file, params[0], params[1], params[2], params[3])
    if len(params) == 3:
        add_to_db(type, file, params[0], params[1], params[2])
    if len(params) == 2:
        add_to_db(type, file, params[0], params[1])
    if len(params) == 1:
        add_to_db(type, file, params[0], "")

def add_all(type):
    with open("{}.csv".format(type), "r", newline='', encoding="utf8") as f:
        reader = csv.reader(f, delimiter=",")
        with open("{}_db.py".format(type), "a", encoding="utf8") as db_file:
            for row in reader:
                add_line(type, db_file, row)

def add_to_db(type, file, sentence, entity1, entity2="", entity3="", entity4=""): # adds a line of data to the database
    if entity1 == entity2 and not entity1 == "":
        print("add this one manually")

    if entity1 == "": #adds a datapoint without any entities in it
        file.write("\t\t(\n")
        file.write("\t\t\t\"" + sentence + "\",\n")
        file.write("\t\t\t{\"entities\": []}\n")
        file.write("\t\t),\n")
    else: # adds a datapoint with 1 or more entities
        file.write("\t\t(\n")
        file.write("\t\t\t\"" + sentence + "\",\n")
        file.write("\t\t\t{\"entities\": " + tuples(sentence, entity1, entity2, entity3, entity4) +"}\n")
        file.write("\t\t),\n")

def tuples(sentence, entity1, entity2, entity3, entity4): # creates a tuple for every entity
    if not entity4 == "":
        return "[" + generate_tuple(sentence, entity1) + ", " + generate_tuple(sentence, entity2) + ", " + generate_tuple(sentence, entity3) + ", " + generate_tuple(sentence, entity4) + "]"
    elif not entity3 == "":
        return "[" + generate_tuple(sentence, entity1) + ", " + generate_tuple(sentence, entity2) + ", " + generate_tuple(sentence, entity3) + "]"
    elif not entity2 == "":
        return "[" + generate_tuple(sentence, entity1) + ", " + generate_tuple(sentence, entity2) + "]"
    else:
        return "[" + generate_tuple(sentence, entity1) + "]"

def generate_tuple(sentence, entity): # generates a tuple for 1 entity
    print(sentence, entity)
    first_index = sentence.index(entity)
    second_index = first_index + len(entity)
    return "(" + str(first_index) + ", " + str(second_index) + ", LABEL)"


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", required=True)
args = vars(parser.parse_args())

add_all(args["type"])
