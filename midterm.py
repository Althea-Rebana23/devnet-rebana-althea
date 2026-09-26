"""
Midterm Practical Exam — Movie Collection Manager
Student: Rebana, Maria Althea D.
"""

movie_list = []
movie = []
def display_menu():
   menu = ["1. Add a movie",
            "2. View all movies",
            "3. Count watched vs unwatched",
            "4. Find a movie",
            "5. Exit"]
   print("Movie List Manager")
   for item in menu:
       print(item)
   choice = int(input("Choose an option: "))
   pass

def add_movie(movie_list):
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    status = input("Watched or Unwatched: ")
    movie = {"title": title, "director": director, "status": status}
    mess = (print(f"Movie added successfully. "))
    movie_list.append(movie)

    pass


def view_movies(movie_list):
   if len(movie_list) == 0:
           print("No movies in the collection.")
   else:
           for movie in movie_list:
               print(f"Title: {movie['title']}, Director: {movie['director']}, Status: {movie['status']}")

def count_watched_unwatched(movie_list):
    watched_count = 0
    unwatched_count = 0
    for movie in movie_list:
        if movie["status"].lower() == "watched":
            watched_count +=1
        elif movie["status"].lower() == "unwatched":
            unwatched_count +=1
    print(f"Watched: {watched_count}, Unwatched: {unwatched_count}")
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
