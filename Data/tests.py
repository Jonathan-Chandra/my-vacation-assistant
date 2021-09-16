from replit import db
import models
import json

testContact1 = models.Contact("Jon", "first", "last", "123@gmail.com", "555-5555", "Test Address", "Token")
testContact2 = models.Contact("username1", "first1", "last1", "1234@gmail.com", "555-6666", "Test Address 1", "Token1")
testList = []
testList.append(testContact1)
testList.append(testContact2)
testEncoded = models.Contact.encode(testList)
testDecoded = models.Contact.decode(testEncoded)
print(testEncoded)
print(testDecoded)
print('\n')
print(testDecoded[0]["username"])
print('\n')
print(type(testDecoded))
