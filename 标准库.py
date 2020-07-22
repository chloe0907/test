import os

# print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")

if not os.path.exists("b/note.txt"):
    # f = open("b/note.txt", 'w')
    # f.write("hello, text")
    # f.close()
    with open("b/text.txt", 'w') as f:
        f.write("hello, text")