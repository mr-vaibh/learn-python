import time

'''
1. time() :- This function is used to count the number of seconds elapsed since the epoch.
2. gmtime(sec) :- This function returns a structure with 9 values each representing a time attribute in sequence.
                  It converts seconds into time attributes(days, years, months etc.) till specified seconds from epoch.
                  If no seconds are mentioned, time is calculated till present.
3. asctime(“time”) :- This function takes a time attributed string produced by gmtime() and returns a 24 character string denoting time.
4. ctime(sec) :- This function returns a 24 character time string but takes seconds as argument and computes time till mentioned seconds.
                  If no argument is passed, time is calculated till present.
5. sleep(sec) :- This method is used to hault the program execution for the time specified in the arguments.

Source - https://www.geeksforgeeks.org/time-functions-in-python-set-1-time-ctime-sleep/
'''
initialTimeWhile = time.time()

k = 0
while k<45:
    print('They this is for loop')
    k += 1

print('While loop ran in', time.time() - initialTimeWhile, 'seconds')

initialTimeFor = time.time()
for i in range(45):
    print('They this is for loop')

print('For loop ran in', time.time()-initialTimeFor, 'seconds')



# To get perfect local time
localTime = time.asctime(time.localtime(time.time()))
print(localTime)

# To pause the execution of program for specific time

print('5 seconds starts now')
time.sleep(5)    # hault the program for 5 seconds
print('5 seconds are over')