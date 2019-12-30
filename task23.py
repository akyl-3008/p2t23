jyl = int(input("Vvedite god: "))
if jyl % 4 != 0 or (jyl % 100 == 0 and jyl % 400 != 0):
    print("365 dnei")
else:
    print("366 dnei")