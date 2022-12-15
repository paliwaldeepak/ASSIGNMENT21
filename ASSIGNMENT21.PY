#1. Add the current date to the text file today.txt as a string.
#ans:-
import datetime
file = open('today.txt','w')
file.write(datetime.datetime.now().strftime("%d-%m-%Y"))
file.close()
file = open('today.txt','r')
print(file.read())
file.close()

#2. Read the text file today.txt into the string today_string
#ans:-
file = open('today.txt','r')
today_string = file.read()
print(today_string)

#3. Parse the date from today_string.
#ans:-
from datetime import datetime
parsed_data = datetime.strptime(today_string, '%d-%m-%Y')
print(parsed_data)

#4. List the files in your current directory
#ans:-
import os
for folders, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        print(file)

#5. Create a list of all of the files in your parent directory (minimum five files should be available).
#ans:-
import os
os.listdir()

#6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
#ans:-
import multiprocessing


def printsec(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())


if __name__ == '__main__':
    import random

    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()

#7. Create a date object of your day of birth.
#ans:-
from datetime import datetime
my_dob = datetime.strptime('10/03/1992','%d/%m/%Y')
print(my_dob, type(my_dob))

#8. What day of the week was your day of birth?
#ans:-
from datetime import datetime
my_dob = datetime(1992,3,10)
print(my_dob.strftime("%A"))

#9. When will you be (or when were you) 10,000 days old?
#ans:-
from datetime import datetime, timedelta
my_dob = datetime.strptime("10/03/1992",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
print(future_date)