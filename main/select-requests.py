from main_py import connection


def sorting_songs_by_year(year):
    list_sorting_by_year = connection.execute(f"""SELECT name_album, year_album FROM album
                                              WHERE year_album = {year}""").fetchall()
    return list_sorting_by_year


def the_longest_song():
    songs_list = connection.execute("""SELECT name_song, duration FROM song
                                  ORDER BY DURATION """).fetchall()
    return songs_list[-1]


def sorting_by_duration(duration):
    list_sorting_by_duration = connection.execute(f"""SELECT name_song FROM song
                                  WHERE duration >= {duration} """).fetchall()
    return list_sorting_by_duration


def sorting_collections_by_years(first_year, last_year):
    list_sorting_by_years = connection.execute(f"""SELECT name_collection FROM collection
                                                  WHERE year_collection 
                                                  BETWEEN {first_year} and {last_year}""").fetchall()
    return list_sorting_by_years


def sorting_executors_by_length(length):
    executors_list = connection.execute("""SELECT name_executor FROM executor""").fetchall()
    sorting_executors_list = []
    for executor in executors_list:
        x = executor[0].split(' ')
        if len(x) == length:
            sorting_executors_list.append(x)
    return sorting_executors_list


def sorting_songs_by_words(word):
    list_songs = connection.execute(f"""SELECT name_song FROM song
                                  WHERE name_song LIKE '%%{word}%%'""").fetchall()
    return list_songs


if __name__ == '__main__':
    print(sorting_songs_by_year(2018))
    print(the_longest_song())
    print(sorting_by_duration(210))
    print(sorting_collections_by_years(2018, 2020))
    print(sorting_executors_by_length(1))
    print(sorting_songs_by_words('мой'))
    print(sorting_songs_by_words('my'))
