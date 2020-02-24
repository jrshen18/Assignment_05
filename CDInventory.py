'''
Title: CDInventory.py
Desc: CD inventory script using dictionary
DBiesinger, 2020-Jan-01, Created starter file
Jeffrey Shen, 2020-Feb-23, Added script contents and comments
'''
# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
cd_dic = {} # initialize dicts
dicRow = {}
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
load_count = 0

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    # exit program
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

    # load existing data
    if strChoice == 'l' and load_count == 0:
        f = open('load.txt', 'r')
        for row in f:
            # extract data file and format list into dictionary and append
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        f.close()
        for row in lstTbl:
            print()
            for items in row.items():
                print(items)
        print('Existing file has been loaded\n')
        load_count = 1
    # if existing file has been loaded, prevent duplicate load copies
    elif strChoice == 'l' and load_count == 1:
        print('Existing data already loaded!')
        pass

    # adding additional user input data
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # add data to the table (2d-list) each time the user wants to add data
        cd_dic['id'] = int(input('Enter an ID: '))
        cd_dic['title'] = input('Enter the title: ')
        cd_dic['artist'] = input('Enter the artist: ')
        # Python does not implicitly copy objects so create a copy of the dic
        lstTbl.append(cd_dic.copy())
        
    # display current CD inventory
    elif strChoice == 'i':
        # display the current data to the user each time the user wants to display the data
        print('Current CD Inventory')
        print('ID, CD Title, Artist')
        # iterate using nested for loop
        for row in lstTbl:
            print()
            for v in row.values():
                print(v, end = '|\t')

    # delete an entry in CD inventory
    elif strChoice == 'd':
        for row in lstTbl:
            print()
            for v in row.values():
                print(v, end = '|\t')
        choice = int(input('Delete ID: '))-1
        # print delete confirmation
        print('Deleted following: ', lstTbl.pop(choice))
        pass

    # Saving CD inventory to text file
    elif strChoice == 's':
        # iterate through table values and save to text file name
        with open('CDInventory.txt', 'a+') as f:
            for row in lstTbl:
                txt_line = ", ".join([str(value) for value in row.values()]) + '\n'
                f.write(txt_line)
        f.close()
# modified code to support using dictionaries instead of lists
#        objFile = open('CDInventory.txt', 'a')
#        for row in lstTbl:
#            strRow = ''
#            for item in row:
#                strRow += str(item) + ','
#            strRow = strRow[:-1] + '\n'
#            objFile.write(strRow)
#        objFile.close()
        print('CD Inventory saved')
    else:
        print('Please choose either l, a, i, d, s or x!')