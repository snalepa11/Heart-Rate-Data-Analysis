

def clean_heartrate_data(data: list) -> tuple:
    # print(data)
    cleaned_list = []
    for x in data:  
        # if x != '\n':
        x =  x.replace('\n', "")

        # if x == 'NO DATA':
        x = x.replace('NO DATA', "")

        if len(x) != 0: 
            cleaned_list.append(int(x))
    
    return cleaned_list




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
   #find min value 
    data.sort()
    max_value = None 
    for number in data :
        if max_value == None or number > max_value:
            max_value = number
    my_range = max_value - data[0]
    return my_range 





def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """

#     # open file using file I/O and read it into the `data` list
    file_object = open(file)
    readData = file_object.readlines()

#     # calculate the average, median, and range of this file using the functions you've wrote
#     average(data)
#     median(data)
#     range(data)
    clean_data = clean_heartrate_data(readData)
    data_average = average(clean_data)
    data_median = median(clean_data)
    data_range = range(clean_data)
   

#     # print out your data quality measure to the console
    print(clean_data)
#     # print out your descriptive statistics to the console
#     print(average, median, range)
    print(data_range)
    print(data_median)
    print(data_average)

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
