file = open('data.txt', "r+")

def printer(file):
    data = file.read()
    data = data.split(",")
    i = 0 
    while i < len(data):
        if int(data[i]) < 10:
            print(int(data[i]) / 10000)
        else: 
            print(int(data[i]) * 1000)
        i += 1
    file.close()

printer(file)