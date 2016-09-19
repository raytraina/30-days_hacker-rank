# Day 8: Dictionaries and Maps
# Task: Given N names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for; for each queried, print the associated entry from your phone book (in the form name=phoneNumber) or Not Found if there is no entry for name.


# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
phone_book = {}

for contact in range(1, n + 1):
    contact = raw_input().split(' ')
    name = contact[0]
    phoneNumber = contact[1]
    phone_book[name] = phoneNumber
    
i = 0
while True:
    query = str(raw_input())
    
    if not query.strip():
        break
        
    if query in phone_book.keys():
        string = query +'='+ str(phone_book[query])
        print(string)
        i += 1
        
    else:
        print("Not found")
        i += 1