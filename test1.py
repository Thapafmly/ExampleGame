weekSalary = 0
dayOfWeek = 1
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
while(True):
  if(week[dayOfWeek] == "Sunday"):
    print("Week Over, Its holiday!!")
    break
  weekSalary += 2000
  dayOfWeek += 1

print(str(weekSalary))