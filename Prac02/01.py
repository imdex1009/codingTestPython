my_list = [1, 2, 3]

while True :
    temp = input()
    if temp == "q":
        break

    try:
        temp = int(temp)
        if my_list.__contains__(temp):
            print("it has!!")
        else:
            print("nothing")
    except:
        print("error!!!!!!!!!!!!!")

