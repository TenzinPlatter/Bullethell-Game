def generate_garden(plants: str, numbers: str) -> str:
    """
    Generates a garden string where each character of 
    plants is a row in the garden and each row has 
    numbers[i] plants. 

    Params: 
        plants: string of 'plants'
        numbers: string of 'numbers'

    Returns the garden string
    """
    def isIn(val, list):
        i = 0
        while i < len(list):
            if list[i] == val: return True
            i += 1
        return False
    
    nums = [None] * len(numbers) 
    i = 0
    while i < len(numbers):
        try:
            nums[i] = int(numbers[i])
        except:
            pass
        i += 1
    inputPlants = [None] * len(plants)
    i = 0
    while i < len(plants):
        inputPlants[i] = plants[i]
        i += 1

    validPlants = ["\U0001F331", "\U0001F337", "\U0001F33D", "\U0001F349", "\U0001F34A", "\U0001F347"]
    loopLength = min(len(inputPlants), len(nums))
    gardenWidth = 0
    i = 0
    while i < loopLength:
        if nums[i] != None:
            if nums[i] > gardenWidth and isIn(inputPlants[i], validPlants):
                gardenWidth = nums[i]
        i += 1

    garden = "/" + "--" * gardenWidth + "\\\n"
    i = 0
    while i < loopLength:
        line = "|"
        if isIn(inputPlants[i], validPlants) and nums[i] != None:
            line += inputPlants[i] * nums[i]
            line += "  " * (gardenWidth - nums[i])
            line += "|\n"
            garden += line
        i += 1
    garden += "\\" + "--" * gardenWidth + "/" 

        

    return garden

def main():
    exitFlag = False
    count = 0
    while not exitFlag:
        count += 1
        if count == 1:
            print(f"ORDER {count}")
        else:
            print(f"\nORDER {count}")
        plants = input("What plants would you like in your garden?\n")
        if plants.lower() == "exit": break
        numbers = input("\nHow many of each plant do you want to plant?\n")
        if numbers.lower() == "exit": break
        print("\n"+generate_garden(plants, numbers))

    print("\nBye, hope to see you soon :)")
if __name__ == "__main__":
    main()
