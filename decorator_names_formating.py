import operator

def person_lister(func):
    formated_persons = []

    def inner(*args):
        print("Formating: ")
        for person in args[0]:
            formated_persons.append(func(str(person[0]).split()))

        print(*formated_persons, sep="\n")
    return inner



@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [
            ['Mike Thomson 20 M'],
            ['Robert Bustle 32 M'],
            ['Andria Bustle 30 F']
    ]
    print("Original list")
    print(*people, sep="\n")
    name_format(people)