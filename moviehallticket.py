movies = {
    1: "ZODIAC",
    2: "SEZEN",
    3: "SHUTTER ISLAND"
}

theatres = {
    1: "Inox",
    2: "Wave",
    3: "PVR"
}

timings = {
    1: {
        1: "10.00-1.00",
        2: "1.10-4.10",
        3: "4.20-7.20",
        4: "7.30-10.30"
    },
    2: {
        1: "1:25-4:25",
        2: "4:30-7:35",
        3: "7:45-10:45"
    },
    3: {
        1: "10.15-1.15",
        2: "1.25-4.25",
        3: "4.35-7.35",
        4: "8.00-10.45"
    }
}

def select_movie():
    print("Which movie do you want to watch?")
    for key, value in movies.items():
        print(f"{key}. {value}")
    print("0. Back")
    movie = int(input("Choose your movie: "))
    if movie == 0:
        city()
    elif movie not in movies:
        print("Invalid choice. Please try again.")
        select_movie()
    else:
        select_theatre(movie)

def select_theatre(movie):
    print("Which theatre do you wish to see the movie?")
    for key, value in theatres.items():
        print(f"{key}. {value}")
    print("0. Back")
    theatre = int(input("Choose your option: "))
    if theatre == 0:
        select_movie()
    elif theatre not in theatres:
        print("Invalid choice. Please try again.")
        select_theatre(movie)
    else:
        select_timing(movie, theatre)

def select_timing(movie, theatre):
    print("Which screen do you want to watch the movie?")
    for key, value in timings[movie].items():
        print(f"{key}. {value}")
    print("0. Back")
    screen = int(input("Choose your screen: "))
    if screen == 0:
        select_theatre(movie)
    elif screen not in timings[movie]:
        print("Invalid choice. Please try again.")
        select_timing(movie, theatre)
    else:
        ticket = int(input("Number of tickets do you want?: "))
        time = timings[movie][screen]
        print(
            f"Successful! Enjoy the movie '{movies[movie]}' at {time} in {theatres[theatre]}"
        )

def city():
    print("Hi, welcome to the movie ticket booking:")
    print("Where do you want to watch the movie?")
    print("1. LUCKNOW")
    print("2. DELHI")
    print("3. MUMBAI")
    print("0. Exit")
    place = int(input("Choose your option: "))
    if place == 0:
        exit()
    elif place not in [1, 2, 3]:
        print("Invalid choice. Please try again.")
        city()
    else:
        select_movie()

# Start the program
city()