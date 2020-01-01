
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)
    
    # Syntax to use coroutine
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
input('press enter')
print("Next method run")
search.send("harry")

search.close()
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

# Code With Harry
# https://www.youtube.com/watch?v=T3tmkWfOHa8&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=78

# Geeksforgeeks
# https://geeksforgeeks.org/coroutine-in-python