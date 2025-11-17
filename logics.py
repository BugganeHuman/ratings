"""
надо функции:

добавление в файл строки ("title, viewing_time, rating)
просмотра все записей
удаление записи по название (не учитывая регистр)
редактирование записи по названия (не учитывая регистр)

"""
def add_in_file (title, viewing_time, rating) :
    with open("ratings.txt", 'a') as file :
        file.write(f"{title} - {viewing_time} - {rating}\n")
        print("\ndone\n")


def show_file () :
    with open ("ratings.txt", 'r') as file :
        list_file_strings = file.readlines()
        for string in list_file_strings :
            print(string)


def delete_string (title) :
    list_file_strings = {}
    with open ("ratings.txt", 'r') as file:
        list_file_strings = file.readlines()
        index_counter = 0
        for string in list_file_strings :
            list_with_words = string.split (sep=" - ")
            if list_with_words[0] == title :
                list_file_strings.pop(index_counter)
            index_counter += 1
    with open("ratings.txt", 'w+') as file :
            file.writelines(list_file_strings)
            print("\ndone\n")


def update_string(updating_title, title, viewing_time, rating ) :
    list_file_strings = {}
    with open("ratings.txt", 'r') as file:
        list_file_strings = file.readlines()
        index_counter = 0
        for string in list_file_strings:
            list_with_words = string.split(sep=" - ")
            if list_with_words[0] == updating_title:
                list_file_strings.pop(index_counter)
                list_file_strings.insert(index_counter, f"{title} - {viewing_time} - {rating}\n")
            index_counter += 1
    with open("ratings.txt", 'w+') as file:
        file.writelines(list_file_strings)
        print ("\ndone\n")

