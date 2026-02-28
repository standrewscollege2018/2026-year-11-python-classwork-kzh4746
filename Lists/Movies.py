''' This program asks a user for the names of their 3 favourite movies in order from the most to least favourite'''
movies = []
print("Enter your 3 favourite movies of all time, in order from most favourite to least")
for i in range(1,4):
    movie = input("Enter name of movie:")
    movies.append(movie)
print("Your 3 favourite movies are:")
for i in range(len(movies)):
    print(f"{i+1}. {movies[i]}")