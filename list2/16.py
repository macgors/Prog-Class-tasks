from collections import OrderedDict

d = {
    "user1": "address1",
    "user2": "address2",
    "user0": "addressXX",
    "user9": "address0",
}

print(OrderedDict(sorted(d.items(), key=lambda x: x[1])))