import statistics as stats
import matplotlib.pyplot as plt

def lineplot(data: list) -> float: 
    # [5,10,15,]
    x = []
    count = 0
    for _ in data:
        count += 5
        x.append(count)

    y = data 

    plt.plot(x , y)

    plt.xlabel('Minutes')
    plt.ylabel('Heartrate')
    plt.title('Heartrate Per 5 Minutes')

    plt.show()