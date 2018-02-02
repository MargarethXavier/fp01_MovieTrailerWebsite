import media
import fresh_tomatoes

up = media.Movie("Up",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",  # noqa
                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

the_martian = media.Movie("The Martian",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

hachi = media.Movie("Hachi: A Dog's Tale",
                    "https://upload.wikimedia.org/wikipedia/en/b/be/Hachi_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=mhEHr7B1QiU")

monsters_inc = media.Movie("Monsters Inc",
                          "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",  # noqa
                          "https://www.youtube.com/watch?v=1hZ9vFv1qzU")

planet_of_apes = media.Movie("War for the Planet of the Apes",
                             "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=UEP1Mk6Un98")

logan = media.Movie("Logan",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=KPND6SgkN7Q")

# List of all instances of class "Movie". This list will be provided as an
# argument to open_movies_page function.

movies = [up, the_martian, hachi, monsters_inc, planet_of_apes, logan]

# Function defined at the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
