# from string import punctuation
# from string import ascii_letters
# from string import ascii_lowercase
# from string import ascii_uppercase

# from random import randint


# class Password():

#     alphaLowers = list(ascii_lowercase)
#     alphaUppers = list(ascii_uppercase)
#     specials = list(punctuation)
#     digits = [n for n in range(0, 10)]

#     def generatePassword(self, choice if choice > 8 else randint(8, 15)):
#         strong = ""
#         for x in range(0, choice):
#             choice = randint(1, 5)
#             if choice == 1:
#                 strong += str(self.digits[randint(0, len(self.digits)-1)])
#             elif choice == 2:
#                 strong += str(self.alphaLowers[randint(0,
#                                                        len(self.alphaLowers)-1)])
#             elif choice == 3:
#                 strong += str(self.alphaUppers[randint(0,
#                                                        len(self.alphaUppers)-1)])
#             elif choice == 4:
#                 strong += str(self.specials[randint(0,
#                                                     len(self.specials) - 1)])

#         print(strong)
#         return strong


# password = Password()

# password.generatePassword(10)
