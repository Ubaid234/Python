from os import times


times = input("How many times do I have to tell you? ")
times = int(times)

for times in range(times):
    print(f"Time {times + 1}: Clean up your room")
