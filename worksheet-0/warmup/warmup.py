# Daily time (in hours): [study, entertainment, sleep]
import matplotlib.pyplot as plt

time_data = [
(3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
(4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
(5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
(3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
(4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]

#t1
low = []
moderate = []
high = []
for study, entertainment, sleep in time_data:
    if study < 3:
        low.append((study, entertainment, sleep))
    elif study >= 3 and study <= 5:
        moderate.append((study, entertainment, sleep))
    else:
        high.append((study, entertainment, sleep))
        
    
print("Low hrs: ", low)
print("Moderate hrs: ", moderate)
print("High hrs: ", high)

#t2
low_days = 0 
for i in low:
    low_days += 1

print("days of low hrs: ", low_days)

moderate_days = 0 
for i in moderate:
    moderate_days += 1
print("days of moderate hrs: ", moderate_days)

high_days = 0
for i in high:
    high_days += 1 
print("days of high hrs: ", high_days)

#t3
study_minutes = []

for study, entertainment, sleep in time_data:
    study_minutes.append(study*60)
print(study_minutes)

#t4
study_hrs = []
entertainment_hrs = []
sleep_hrs = []

for study, entertainment, sleep in time_data:
    study_hrs.append(study)
    entertainment_hrs.append(entertainment)
    sleep_hrs.append(sleep)

print("study hrs: ", study_hrs)

studyn = 0
entertainmentn = 0
sleepn = 0
total_study = 0
total_entertainment = 0
total_sleep = 0 

for i in study_hrs:
    studyn += 1
    total_study += i
avg_study = total_study/studyn
print(avg_study)

for j in entertainment_hrs:
    entertainmentn += 1
    total_entertainment += j
avg_entertainment = total_entertainment/entertainmentn
print(avg_entertainment)

for k in sleep_hrs:
    sleepn += 1 
    total_sleep += k
avg_sleep = total_sleep/sleepn
print(avg_sleep)

#t5
#try to add color as per the studyhrs, low = red high = green
plt.scatter(study_hrs, sleep_hrs, color= 'black')
plt.xlabel("study")
plt.ylabel("sleep")
plt.title("study sleep comparasion")
plt.grid(True)
plt.show()