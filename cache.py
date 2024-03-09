# While loop so the user goes back to the menu after an algorithm runs.
while True:
    cache = []
    requests = []
    print("This program simulates cache management using the\n"
          "First In First Out (FIFO) and Least Frequently Used (LFU).\n"
          "algorithms.")

    # While loop checks and deals with the user's inputted integers.
    while True:
        user_integer = 'Null'
        while user_integer == 'Null':
            try:
                user_integer = int(input('Enter an integer or 0 if finished:'))
            except ValueError:
                print('Please enter a postive integer.')
        if user_integer == 0:
            break
        elif user_integer < 0:
            print('Please enter a postive integer.')
        else:
            requests.append(user_integer)
            continue

    # While loop deals with algorithm selection or quitting the program.
    while True:
        pick_algorithm = input("Please type 1 for fifo, type 2 for lfu\n"
                               "or type Q to quit the program:")
        if pick_algorithm not in ('1', '2', 'Q'):
            print("Enter either '1', '2' or 'Q'")
        else:
            break

    def fifo():
        """
        Performs the First In First Out algorithm.
        The for loop cycles through each page requested.
        The if statement checks the request against the cache list.
        The cache list is amended accordingly.
        Hit or miss is printed accordingly.
        """
        for i in requests:
            if len(cache) < 8 and i not in cache:
                cache.append(i)
                print('miss')
            elif len(cache) == 8 and i not in cache:
                cache.pop(0)
                cache.append(i)
                print('miss')
            else:
                print('hit')

    def lfu():
        '''
        Performs the Least Frequently Used algorithm.
        The page requests are stored in a dicitonary.
        The for loop cycles through each page requested.
        The page requests are incremented for each request.
        The if statement checks the request against the cache list.
        The cache list is amended accordingly.
        Hit or miss is printed accordingly.
        '''
        lfu_dict = {
        }
        for i in requests:
            lfu_dict[int(i)] = lfu_dict.get(int(i), 0) + 1
            if len(cache) < 8 and i not in cache:
                cache.append(i)
                print('miss')
            elif len(cache) == 8 and i not in cache:
                # Sorts by values (page requests) and they by key (page).
                lfu_dict_sorted = sorted(lfu_dict.items(), key=lambda y: (y[1], y[0]))
                # While loop to deal with two pages having
                # the same number of requests.
                # Also deals with the possible situation of the lowest
                # requested page in the dictionary not being in the cache.
                x = 0
                while x < len(lfu_dict_sorted):
                    # Checks if the page with the lowest requests is in cache.
                    if lfu_dict_sorted[x][0] in cache:
                        # Adds a page requested before back to the cache if it
                        # is requested again and is not already in the cache.
                        # Adds a new page to the cache if it is requested for the
                        # first time.
                        if lfu_dict_sorted[x][1] <= lfu_dict[int(i)] or lfu_dict[int(i)] == 1:
                            cache.remove(lfu_dict_sorted[x][0])
                            cache.append(i)
                        break
                    else:
                        x = x + 1
                print('miss')
            else:
                print('hit')

    # If statement for picking the algorithm to use or to quit the program.
    # Prints/clears the cache and goes to the menu after an algorithm runs.
    if pick_algorithm == '1':
        fifo()
        print(cache)
        cache = []
        requests = []
        continue
    elif pick_algorithm == '2':
        lfu()
        print(cache)
        cache = []
        requests = []
        continue
    else:
        print('Program terminated.')
        quit()
