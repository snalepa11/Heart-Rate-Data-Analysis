def average(data: list) -> float:
    total_sum = 0
   
    #Calculate the sum of the list 
    for number in data:
        total_sum += number
        
    #Calculate average
    new_number = total_sum/len(data)
    return f"{new_number:.2f}"
    



def median(data: list) -> float:
   #Sort data in order
    data.sort()
    #find the length of the list 
    list_length = len(data)
   #assign median index to variable
    index = list_length / 2
    index = int(index)
    if list_length % 2 == 0: 
        my_median = (data[index - 1] + data[index]) / 2
        
    else:
        my_median = data[index]
   #find the middle number 
    return my_median


def range(data: list) -> float:
   #sort the data from least to greatest value
    data.sort()
    max_value = None 
    #for loop finding the max value by looping through all munbers
    for number in data :
        if max_value == None or number > max_value:
            max_value = number
    #find range by subtracting first index in list by the max value
    my_range = max_value - data[0]
    return my_range 





def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass

