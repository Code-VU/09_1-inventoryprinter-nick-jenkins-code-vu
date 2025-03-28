stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    print("Inventory:")
    for item, list in inventory.items():
        print (item, list)
    #define what we're going to put in the 
    #we need to put items into  dictionary value
    #we nee to pull from the dictionary and add up all the numbers
    result = sum(stuff.values())
    print ("total number of results:", (result))



if __name__ == "__main__":
    displayInventory(stuff)
