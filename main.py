

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
    return total_sum/len(data)
    
    print(average(file_object))

file_object = open("/Users/sarahnalepa/Desktop/TKH/Labs/hr_data_pipeline/Heart-Rate-Data-Analysis/data/phase0.txt")
readData = file_object.readlines()

print(clean_heartrate_data(readData))

# def median(data: list) -> float:
#    #Sort data in order
#    data.sort()
#     #find the length of the list 
#    list_length = len(data)
#    #assign median index to variable
#    index = list_length/2
#    if list_length % 2 == 0: 
#        my_median = (data[index - 1] + data[index]) / 2
        
#     else 
#         my_median = data[index]
#    #find the middle number 
#    return my_median





# def range(data: list) -> float:
#    #find min value 
#    data.sort()
#     max_value = max(data)
#     my_range = data(max_value) - data[0]
#    return my_range 


# def rolling_avg(data: list, k: int) -> float:
#     """
#     CHALLENGE FUNCTION (Optional)
#     """
#     pass


# def run(file: str):
#     """
#     Process heart rate data from the a file by cleaning and
#     calculating summary statistics. Print out final values.

#     Args:
#         filename (str): The path to the data file (e.g., 'data/phase0.txt').

#     Returns:
#         float, float, float: You will return the average, median, and range.
#     """
#     data = []

#     # open file using file I/O and read it into the `data` list
    
#     data = file_object.readlines()
#     #strip white space including /n .strip()
#     removed_values = data.strip(/n)
#     #Cast string values to numeric types with int() and float()
    
#     # Use `clean_heartrate_data` to clean the data and remove invalid entries
#     cleaned_list, removed_values = clean_heartrate_data(data)

#     # calculate the average, median, and range of this file using the functions you've wrote
#     average(data)
#     median(data)
#     range(data)

#     # print out your data quality measure to the console
#     print(data)
#     # print out your descriptive statistics to the console
#     print(average, median, range)


# if __name__ == "__main__":
#     run("data/phase0.txt")
#     run("data/phase1.txt")
#     run("data/phase2.txt")
#     run("data/phase3.txt")
