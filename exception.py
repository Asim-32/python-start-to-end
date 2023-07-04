# try:
#     # a = 1
#     # b = 0
#     # print(a/b)
#     # print("next line")
#     text = "test.txt"
#     open(text)
# except EOFError as e:
#      print(1,e)
# except IOError as e:
#     print(2,e)
# except Exception as e:
#     print(3,e)
#     print("pleas try again after sometime")
# finally:
#     print("database close")


try:
    a = 1
    b = 0
    print(a/b)
except EOFError as e:
     print(1,e)
except IOError as e:
    print(2,e)
except Exception as e:
    print(3,e)
    print("pleas try again after sometime")
else:
    print("working")