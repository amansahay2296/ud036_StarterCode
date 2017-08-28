import media
import fresh_tomatoes

# Creating instances for class Movie

_3idiots = media.Movie("3 Idiots", "https://upload.wikimedia.org/wikipedia/" +
                       "en/d/df/3_idiots_poster.jpg",
                       "https://www.youtube.com/watch?v=K0eDlFX9GMc")

bourne_identity = media.Movie("The Bourne Identity", "https://upload" +
                              ".wikimedia.org/wikipedia/en/a/ae/Bourne" +
                              "Identityfilm.jpg", "https://www.youtube.com/" +
                              "watch?v=FpKaB5dvQ4g")


a_few_good_men = media.Movie("A Few Good Men", "https://upload.wikimedia" +
                             ".org/wikipedia/en/4/45/A_Few_Good_Men_poster" +
                             ".jpg", "https://www.youtube.com/watch?v=" +
                             "ePo91pMcu94")

batman_begins = media.Movie("Batman Begins", "https://upload.wikimedia.org/" +
                            "wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                            "https://www.youtube.com/watch?v=QhPqez3CwiM")

prestige = media.Movie("The Prestige", "https://upload.wikimedia.org/" +
                       "wikipedia/en/d/d2/Prestige_poster.jpg",
                       "https://www.youtube.com/watch?v=o4gHCmTQDVI")


rdb = media.Movie("Rang De Basanti", "https://upload.wikimedia.org/" +
                  "wikipedia/en/5/5f/RDB_poster.jpg",
                  "https://www.youtube.com/watch?v=l-BTOTtcGmk")

# Storing all Movie instances in a list
movies = [_3idiots, bourne_identity, a_few_good_men, batman_begins, prestige,
          rdb]

# function call
# open_movies_page(movies) takes a list of Movie objects as an argument
# and generates the movie trailer website.
fresh_tomatoes.open_movies_page(movies)

