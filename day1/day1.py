# CHATGPT

# Initialize empty lists to store the columns
column1 = []
column2 = []

# Open the text file
with open('input.txt', 'r') as file:
    for line in file:
        # Strip any leading/trailing whitespace and split by space (or tab, depending on your file)
        values = line.strip().split()  # Assuming space-separated values, adjust if necessary
        
        # Convert the values to the appropriate type (e.g., float, int)
        column1.append(float(values[0]))  # Append the first value to column1
        column2.append(float(values[1]))  # Append the second value to column2

# Now you have two lists: column1 and column2
print(column1)
print(column2)

# END CHATGPT

# now that we have each column in two, sort the columns ascending
column1.sort()
column2.sort()

column3 = [a - b for a, b in zip(column1, column2)]

print(sum(column3))

# then use a loop to subtract the values against each other to get a 3rd list
# then sum the third list