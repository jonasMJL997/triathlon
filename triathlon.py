swimming_time = int(input("please enter the time of the swimming event in minutes:"))
cycling_time = int(input("please enter the time of the cycling event in minutes:"))
running_time = int(input("please enter the time of the running event in minutes:"))

durtime = swimming_time+cycling_time+running_time

if durtime >= 100:
    print("you have won within", durtime,"minutes a provincial colours award")

elif durtime <= 5:
    print("you have won within", durtime ," minutes half provincial color " )

elif durtime >= 10:
    print("you have won within", durtime ,"minutes a provincial  scroll")


elif durtime + 10:
    print("you have finished within", durtime , "no award ")






