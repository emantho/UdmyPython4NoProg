def countDown(numb):
    if numb > 0:
        print(numb)
        countDown(numb - 1)
    else:
        print("Booom!!")

countDown(5)