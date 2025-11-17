from logics import add_in_file, show_file, delete_string, update_string


def main () :
    while True :

        main_meny_choice = input("\npress:\n"
                                 "1 - add rating\n\n"
                                 "2 - show all ratings\n\n"
                                 "3 - delete rating\n\n"
                                 "4 - update rating\n\n"
                                 "0 - to exit\n"
                                 "                "
                                )

        if main_meny_choice == "0" :

            break


        elif main_meny_choice == "1" :

            title = input("write titles name: ")
            viewing_time = input("write how long you was watching: ")
            rating = input("write the rating: ")
            add_in_file(title, viewing_time, rating)

        elif main_meny_choice == "2" :
            show_file()


        elif main_meny_choice == "3" :
            delete_title = input("write titles name for remove: ")
            delete_string (delete_title)


        elif main_meny_choice == "4" :
            updating_title = input("write titles name for update anything: ")
            title = input("write new titles name: ")
            viewing_time = input("write new how long you was watching: ")
            rating = input("input new rating: ")
            update_string(updating_title, title, viewing_time, rating)


if __name__ == "__main__" :
    main()
