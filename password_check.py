

def check__passwords(passwords_list, week_words_list):
    status_list = []

    if not passwords_list or not week_words_list or passwords_list is None or week_words_list is None:
        return None
    if len(passwords_list) == 0 or len(week_words_list) == 0:
        return None

    for password in passwords_list:
        if not password.strip():
            status_list.append((password.strip(), "week"))
        elif password in week_words_list:
            status_list.append((password.strip(), "week"))
        elif password.isnumeric():
            status_list.append((password.strip(), "week"))
        else:
            for week_pass in week_words_list:
                if week_pass in password.strip():
                    status_list.append((password.strip(), "week"))
                    break
            else:
                status_list.append((password.strip(), "strong"))
    print(*status_list, sep="\n")
    return status_list


if __name__ == '__main__':
    passwords_list = ["89_xaxa_100", "AabbB", "brabra", "1234", "kakaMaka", "cafeAladin", "ananas", "ananasAA", "", " "]
    week_words_list = ["kaka", "cafe","ananas"]

    check__passwords(passwords_list, week_words_list)