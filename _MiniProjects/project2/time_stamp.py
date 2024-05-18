from datetime import datetime


#print(datetime.now().date())
#print(datetime.now().day)
#print(datetime.now().year)
#print(datetime.now().month)

timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
print(timestamp)
