import os

folders = input("give folders to check files in it: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide valid folder name")
        break
    #print(files)


    for file in files:
        print(file)