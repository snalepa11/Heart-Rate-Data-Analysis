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