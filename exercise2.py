# Print the sum of the current and previous number

for index in range(10):
    if index == 0:
        previous = 0 # Intialiaze previous number for the first iteration
    else:
        previous = current # Update previous number with the current number for subsequent iterations
    current = index + 1 # Update current number wuth the current index incremented by 1
    print(f"The sum of {previous} and {current} is: {previous + current}") 