#using bubblesort method
# This method will make it difficult with the bigger list.

""" unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    high_idx = len(the_list) -1

    for i in range(high_idx):

        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]


            if item > next:
                the_list[j] = next
                the_list[j+1] =item

            print(the_list, i, j)

bubblesort(unsorted_list) """


# Now we can add the boolean so that the method can run with the bigger list. 

unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    high_idx = len(the_list) -1

    for i in range(high_idx):

        list_changed = False              #added boolean

        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]


            if item > next:
                the_list[j] = next
                the_list[j+1] =item
                list_changed = True       #added boolean

            print(the_list, i, j)
        print(list_changed)
        if list_changed== False:           #added boolean
            break

bubblesort(unsorted_list)