import json


# UserManagement Class for managing user administration
class UserManagement:
    def __init__(self):
        pass

    # Check to see if a user is valid by reading it from users.json file and returns User's  display_name.
    def loginUser(self):
        username = input("Enter Your UserName: ")
        password = input("Choose Your Password: ")

        with open('users.json') as json_file:
            data = json.load(json_file)
            for user in data["users"]:
                if username == user['name'] and password == user['password']:
                    return user['display_name']

    # Regisrters a new user in system and writes the details of new user in users.json file, which is read by loginUser function.
    def registerUser(self):
        display_name = input("Enter Your Name to be dispalyed: ")
        name = input("Enter Your User Name: ")
        email = input("Enter Your Email: ")
        password = input("Choose Your Password: ")

        try:
            with open('users.json') as json_file:
                data = json.load(json_file)
                temp = data["users"]
                y = {"name": name,
                     "email": email,
                     "display_name": display_name,
                     "password": password
                     }
                temp.append(y)
                
                with open("users.json", 'w') as f:
                    json.dump(data, f, indent=4)
        except:
            print("Something wrong with file operation")

    # Stores details winner of each game in winners.json file, which is read by readWinner function.
    def storeWinner(self, name, deck, deck_length):
        try:
            with open('winners.json') as json_file:
                data = json.load(json_file)
                temp = data["winners"]
                y = {"name": name,
                     #  "deck": deck,
                     "deck_length": deck_length
                     }
                temp.append(y)
                # write_json(data)
                with open("winners.json", 'w') as f:
                    json.dump(data, f, indent=4)
        except:
            print("Something wrong with file operation")

    # This function is called to read the top 5 winnders of the game. This function first reads the winners.json which is dictionary
    # Then converts the dictionary to a list to read the list of users and finally converts the list to tuple, which will be used for sorting
    # based on the index[1] of tuple.

    # Returns winners as a tuple to calling function.
    def readWinner(self):
        winners_as_dict = {}
        winners_as_list = []
        winners_as_tuple = []
        with open('winners.json', 'r') as f:
            winners_as_dict = json.load(f)
            for key, value in winners_as_dict.items():
                winners_as_list = value
            for each_item in winners_as_list:
                winners_as_tuple.append(
                    (each_item['name'], each_item['deck_length']))
            return winners_as_tuple
