# A credit card company computes a customer's "minimum payment" according to the following rule. The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater; however, if a $10 minimum payment exceeds the balance, then the minimum payment is the balance. Write a program to return the minimum payment. Assume that the variable balance contains the customer's balance.
#   Example 1: if your balance is 1000, then your program should return 21. 
#   Example 2: if your balance is 600, then your program should return 12.6. 
#   Example 3: if your balance is 25, then your program should return 10. 
#   Example 4: if your balance is 8, then your program should return 8. 

def computeMinimumPayment( balance ):
    if balance * 0.021 > 10: #this helps tell the program that when the user has a balance times 0.021% and it is less than 10 then the payment should equal to the balance times 0.021.
        payment = balance * 0.021
    else: #this tells the program that if the payment equals to 10 and if the payment is equal to the balance due the the program needs to retun payment.
        payment = 10 
    if balance < 10:
        payment = balance
    return payment

    #TODO write code inside this function that achieves the functionality described above
