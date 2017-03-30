import json
import pprint
import sys
import argparse

def createusers(amount):
    """Create a list of dict; users"""
    i = 1
    users = []
    while i <= amount:
        user = {"model": "gamestore.profile", \
                "pk": i, \
                "fields": { \
                    "username": "test-user-{}".format(i), \
                    "email": "test-user-{}@re.factory".format(i), \
                    "password": "testpass", \
                    "role": \
                    "developer" if i % 10 == 0 else "gamer"}}
        users.append(user)
        i += 1
    prettyprinter = pprint.PrettyPrinter(indent=4)
    prettyprinter.pprint(users)
    return users

def outputusers(users, destination):
    """Write the users to a json file"""
    with open(destination, 'w') as outfile:
        json.dump(users, outfile)

def main(argv):
    """A helper function to create a test set of users"""
    outputfile = "profiles.json"
    amount = 100
    parser = argparse.ArgumentParser(description="Create a set of test users")
    parser.add_argument("-a", "--amount", type=int,
                        help="specify the amount of users to be created (100 by default)")
    parser.add_argument("-o", "--output", help="specify the output file (profiles.json by default)")
    args = parser.parse_args()
    if args.amount is not None:
        amount = args.amount
    if args.output is not None:
        outputfile = args.output
    users = createusers(amount)
    outputusers(users, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
