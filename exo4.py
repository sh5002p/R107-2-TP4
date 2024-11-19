
def most_frequent(lst):

    most_frequent_element = None
    max_count = 0


    for num in lst:
        count = lst.count(num)


        if count > max_count:
            most_frequent_element = num
            max_count = count


    print(f"Le nombre le plus frequent dans la liste est le : {most_frequent_element} ({max_count} x)")



if __name__ == "__main__":
    lst = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
    most_frequent(lst)