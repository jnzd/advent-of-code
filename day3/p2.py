# --- Part Two ---
# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

# Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:

# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
# For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

# Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
# Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
# In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
# In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
# In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
# As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
# Then, to determine the CO2 scrubber rating value from the same example above:

# Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
# Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
# In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
# As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
# Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

def mostCommonDigitAtPos(listOfLists, pos):
    """
    Find the most common digit at a given position in a list of lists
    """
    # Get the list of digits at the given position
    digits = [digit[pos] for digit in listOfLists]
    # Get the most common digit
    numOnes = digits.count('1')
    numZeros = digits.count('0')
    mostCommon = '1' if numOnes == numZeros else max(set(digits), key=digits.count)
    return mostCommon

def leastCommonDigitAtPos(listOfLists, pos):
    """
    Find the least common digit at a given position in a list of lists
    """
    # Get the list of digits at the given position
    digits = [digit[pos] for digit in listOfLists]
    # Get the least common digit
    numOnes = digits.count('1')
    numZeros = digits.count('0')
    leastCommon = '0' if numOnes == numZeros else min(set(digits), key=digits.count)
    return leastCommon




with open("in.txt", "r") as f:
    lines = f.read().splitlines()
    l1 = lines
    l2 = lines
    # print(l1)
    while len(l1) > 1:
        for i in range(len(l1[0])):
            mostCommon = mostCommonDigitAtPos(l1, i)
            # print(str(i) + ", " + str(mostCommon))
            l1 = list(filter(lambda x: x[i] == mostCommon, l1))
            # print(l1)
            if len(l1) == 1:
                break
    
    while len(l2) > 1:
        for i in range(0, len(l2[0])-1):
            leastCommon = leastCommonDigitAtPos(l2, i)
            l2 = list(filter(lambda x: x[i] == leastCommon, l2))
            if len(l2) == 1:
                break
    
    oRate = int(l1[0], 2)
    co2Rate = int(l2[0], 2)
    
    # print(l1)
    # print(l2)
    
    # print(oRate)
    # print(co2Rate)
    print(oRate * co2Rate)