
import cleaner 
import statistical 
import statistics as stats


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
    clean_data = cleaner.clean_heartrate_data(readData)
    data_average = statistical.average(clean_data)
    data_median = statistical.median(clean_data)
    data_range = statistical.range(clean_data)
    data_variance = statistical.variance(clean_data)
   

#     # print out your data quality measure to the console
    print(f"Cleaned data: {clean_data}")
#     # print out your descriptive statistics to the console
#     print(average, median, range)
    print(f"Data range: {data_range}")
    print(f"Data median: {data_median}")
    print(f"Data mean: {data_average}")
    print(f"Data variance: {data_variance}")

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
