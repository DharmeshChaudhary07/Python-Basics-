################  Searching  ####################
# # startswith(), endswith(), in(), find()

# phone = "+61-490-933-167"
# phone1 = "129-308-933-1621"
# phone2 = "+01-3920-933-167"
# #startswith()
# print(phone.startswith("+"))
# print(phone.startswith("1"))

# #endswith
# print(phone.endswith("7"))
# print(phone.startswith("1"))

# email = "Dharmesh@gmail.com"
# print(email.startswith("Dhar"))
# print(email.endswith('.com'))

# #in() 'substring' in string operator output: int
# email = "dharmeshchaudhary1999@gmail.com"
# print("@" in email)

# url ="https://api.company.australia.pok/data"
# print(".pok" in url)

# # find() # always combined with other method to add dynamnic
# # index() and find() return int → so maths works on them → then we feed that int into [] operator → which returns str

# phone = "+61-490-933-167"
# phone1 = "+129-308-933-1621"
# phone2 = "+01-3920-933-167"

# print(phone[4:])
# print(phone1[5:])
# print(phone2[4:])

# print(phone.find("-"))
# print(phone1.find("-"))

# # #if we have good amount of data and - lying on differnt index in every phone no then too sort.
# print(phone[phone.find("-")+1:])
# print(phone1[phone1.find("-")+1:])
# print(phone2[phone2.find("-")+1:])



