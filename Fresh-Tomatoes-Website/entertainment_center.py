import fresh_tomatoes
import media

coming_to_america = media.Movie("Coming to America",
"https://upload.wikimedia.org/wikipedia/en/3/38/ComingtoAmerica1988MoviePoster.jpg",
"https://www.youtube.com/watch?v=fqfJqLFQSIk")

legends_of_the_fall = media.Movie("Legends of the Fall",
"https://upload.wikimedia.org/wikipedia/en/1/1d/Legendsoffallposter.jpg",
"https://www.youtube.com/watch?v=JnJoaUzvXc4")

ferris_bueller = media.Movie("Ferris Bueller's Day Off",
"https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
"https://www.youtube.com/watch?v=D6gABQFR94U")

raising_arizona = media.Movie("Raising Arizona",
"https://upload.wikimedia.org/wikipedia/en/3/31/Raising-Arizona-Poster.jpg",
"https://www.youtube.com/watch?v=bLvqoHBptjg")

up = media.Movie("Up",
"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
"https://www.youtube.com/watch?v=OjWu8i6eMZo")

friday = media.Movie("Friday",
"http://icecube.com/wp-content/uploads/2015/03/friday-movie-poster.jpg",
"https://www.youtube.com/watch?v=dxduMVVnrvU")

movies = [coming_to_america, legends_of_the_fall, ferris_bueller, raising_arizona, up, friday]

fresh_tomatoes.open_movies_page(movies)
