amount_due = 50
while amount_due>0:
    print(f"Amount Due: {amount_due}")
    inserted=int(input("Insert coin: "))
    if inserted in [5,10,25]:
        amount_due = amount_due - inserted 
        if amount_due<=0:
            print(f"Change Owed: {abs(amount_due)} ")

            