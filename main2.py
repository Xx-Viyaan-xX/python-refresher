def nonotes(a):
    Q = [500,100,200,50,20,10]
    X = 0
    for i in range(7):
        q = Q[i]
        x = a//q
        print("notes of {} = {}".format(q,x))
        a = a%q

amount = int(input("Enter total amount")) 
nonotes(amount)