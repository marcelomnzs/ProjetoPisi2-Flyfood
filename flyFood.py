'''
    Universidade Federal Rural de Pernambuco - UFRPE
    Aluno: Marcelo Antonio 
    PISI2 - Projeto Flyfood

'''
def permutations(input):
    if len(input) == 1:
        return [input]

    combinations = []

    # Put the last value of the list in the variable last and gets all the elements left and store in front(as a list)
    *front, last = input
    
    for perm in permutations(front):
        for i in range(len(perm) + 1):
            new = perm[:i] + [last] + perm[i:]
            combinations.append(new)

    # Puts the list in order
    return sorted(combinations)

deliveryMap = []
points = []
coordinates = {}

# Reads the file and returns an array(deliveryMap) with the routes
with open('route.txt' ,'r') as routes:
    for route in routes:
        deliveryMap.append(route.split())

# print(deliveryMap)

# Specify the number of lines and columns read in the file
numberOfLines, numberOfColumns = int(deliveryMap[0][0]), int(deliveryMap[0][1])

# Erase the first element with the lines and columns from the list
deliveryMap.pop(0)

for line in range(numberOfLines):
    for column in range(numberOfColumns):
        if(deliveryMap[line][column] != '0'):
            points.append(deliveryMap[line][column])
            coordinates[deliveryMap[line][column]] = (line, column)
            # print('The element {} coordinates are {},{}'.format(deliveryMap[line][column], line, column))

# Removes the initial point to avoid the permutation with it
points.remove('R')

# Will return a list of all the possible permutations of the points
possibleCombinations = list(permutations(points))

# print(possibleCombinations)

# To make sure that the new number generated will be shorter than the lowerCost
lowestCost = float('inf')

for combination in possibleCombinations:
    counter = 0
    currentCost = 0
    combination = list(combination)

    combination.append('R')
    combination.insert(0, 'R')

    while counter < (len(combination) - 1):
        
        # For each point in the combination it will sum the distance to go from a point to another

        # print(combination)
        # print(counter)
        # print(coordinates[combination[counter]])
        # print(lowestCost)

        x = abs(coordinates[combination[counter]][0] - coordinates[combination[counter + 1]][0])
        y = abs(coordinates[combination[counter]][1] - coordinates[combination[counter + 1]][1])

        currentCost += x + y
        counter += 1
    
    if(currentCost < lowestCost):
        lowestCost = currentCost
        route = combination

print(lowestCost)
print(route)