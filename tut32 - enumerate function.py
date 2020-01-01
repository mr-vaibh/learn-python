l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

# enumerate(iterable, start=0)

for index, item in enumerate(l1, start=1):
    if index % 2 is not 0:
        print(f"Jarvis please buy {item}")

