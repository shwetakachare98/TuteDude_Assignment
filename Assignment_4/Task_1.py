try:
    with open('sample.txt','r') as task1:
        reading_task1=task1.read()
        print(reading_task1)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


