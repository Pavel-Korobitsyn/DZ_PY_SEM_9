def open_txt():

    file1 = open('Phonebook.txt', "r", encoding = 'utf-8')
    lines = file1.readlines()
    file1.close

    return lines

def open_csv():

    file1 = open('Phonebook.csv', "r", encoding = 'utf-8')
    lines = file1.readlines()
    file1.close

    return lines