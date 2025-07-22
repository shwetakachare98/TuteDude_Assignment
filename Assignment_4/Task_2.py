chr1=input("Enter text to write to the file:")
with open("output.txt","w") as task2:
    writing=task2.write(chr1+"\n")
    print("Data successfully written to file output.txt.")
chr2=input("Enter additional text to append:")
with open("output.txt","a") as task2:
    appending=task2.write(chr2)
    print("Data successfully appended.")
with open("output.txt","r") as task2:
    reading_task2=task2.read()
    print("Final content of output.txt:\n",reading_task2)