import json
def readWinner():
    winners_as_dict = {}
    winners_as_list = []
    winners_as_tuple = []
    with open('winners_temp.json', 'r') as f:
        winners_as_dict = json.load(f)
        # print(winners_as_dict)
        for key, value in winners_as_dict.items():
            winners_as_list = value
        for each_item in winners_as_list:
            winners_as_tuple.append(   ( each_item['name'], each_item['deck_length']  )  )
        print(winners_as_tuple)

readWinner()