import random

# List of Hindi movie genres
hindi_genres = [
    "Action", "Comedy", "Drama", "Romance", "Thriller", "Horror",
    "Historical", "Musical", "Biographical", "Science Fiction",
    "Horror Comedy", "Romance Comedy", "Action Comedy", "Musical Drama"
]

# Dictionary of Bollywood movies categorized by genre
bollywood_movies = {
    "Action": [
        "Khiladi (1992)", "Mohra (1994)", "Main Khiladi Tu Anari (1994)",
        "Sabse Bada Khiladi (1995)", "Khiladiyon Ka Khiladi (1996)",
        "International Khiladi (1999)", "Khiladi 420 (2000)",
        "Rowdy Rathore (2012)", "Gabbar Is Back (2015)", "Airlift (2016)",
        "Wanted (2009)", "Dabangg (2010)", "Ek Tha Tiger (2012)",
        "Tiger Zinda Hai (2017)", "Uri: The Surgical Strike (2019)",
        "War (2019)", "Sultan (2016)", "Baaghi Series", "Heropanti (2014)",
        "Raees (2017)", "Khalnayak (1993)", "Commando Series",
        "Shershaah (2021)", "KGF: Chapter 1 (2018) - Hindi Dub", "Sanak (2021)"
    ],
    "Comedy": [
        "Hera Pheri (2000)", "Awara Paagal Deewana (2002)", "Mujhse Shaadi Karogi (2004)",
        "Garam Masala (2005)", "Phir Hera Pheri (2006)", "Welcome (2007)",
        "Singh Is Kinng (2008)", "Housefull (2010)", "Good Newwz (2019)",
        "3 Idiots (2009)", "Chup Chup Ke (2006)", "Pyaar Ka Punchnama (2011)",
        "Housefull 3 (2016)", "Golmaal Series", "Total Dhamaal (2019)",
        "Dhamaal (2007)", "Chashme Buddoor (1981)", "Bajrangi Bhaijaan (2015)",
        "Dil Hai Ki Manta Nahin (1991)", "Mujhse Fraaandship Karoge (2011)"
    ],
    "Drama": [
        "Dhadkan (2000)", "Kabhi Khushi Kabhie Gham (2001)", "Swades (2004)",
        "Pad Man (2018)", "Chhichhore (2019)", "Raazi (2018)", "Shershaah (2021)",
        "Taal (1999)", "Chakdey India (2007)", "Zindagi Na Milegi Dobara (2011)",
        "Panga (2020)", "Masaan (2015)", "Gully Boy (2019)", "Aashiqui (1990)",
        "Fifty Fifty (1984)", "Maqbool (2004)"
    ],
    "Romance": [
        "Yeh Dillagi (1994)", "Maine Pyar Kiya (1989)", "Dilwale Dulhania Le Jayenge (1995)",
        "Kal Ho Naa Ho (2003)", "Ae Dil Hai Mushkil (2016)", "Kabir Singh (2019)",
        "Raabta (2017)", "Hum Dil De Chuke Sanam (1999)", "Dil To Pagal Hai (1997)",
        "Jab Tak Hai Jaan (2012)", "Vivah (2006)", "Hum Aapke Hain Koun..! (1994)",
        "Kabhi Alvida Naa Kehna (2006)", "Mujhse Dosti Karoge! (2002)",
        "Pyaar Kiya To Darna Kya (1998)"
    ],
    "Thriller": [
        "Ajnabee (2001)", "Aankhen (2002)", "Kahaani (2012)", "Andhadhun (2018)",
        "Drishyam (2015)", "Kaante (2002)", "Special 26 (2013)", "Badla (2019)",
        "Raaz (2002)", "Kahaani 2 (2016)", "Murder (2004)", "Kahaani 3 (2022)",
        "Murder 2 (2011)", "Detective Byomkesh Bakshy! (2015)", "Guilty (2020)"
    ],
    "Horror": [
        "Bhool Bhulaiyaa (2007)", "Raaz (2002)", "Laxmii (2020)", "Bhoot (2003)",
        "1920 (2008)", "Ek Thi Daayan (2013)", "Psycho (2020)", "Tumbbad (2018)",
        "Stree (2018)", "Bhool Bhulaiyaa 2 (2022)", "Ragini MMS (2011)",
        "Raaz: The Mystery Continues (2009)", "Pari (2018)", "Chudail Story (2016)",
        "Horror Story (2013)"
    ],
    "Historical": [
        "Lagaan (2001)", "Tanaav (2022)", "Padmaavat (2018)", "Gangs of Wasseypur (2012)",
        "Mangal Pandey: The Rising (2005)", "Kesari (2019)", "The Legend of Bhagat Singh (2002)",
        "Tumbbad (2018)", "Bajirao Mastani (2015)", "Taanaji: The Unsung Warrior (2020)",
        "Shahid (2012)", "Gandhi: My Father (2007)"
    ],
    "Musical": [
        "Rockstar (2011)", "Aashiqui 2 (2013)", "Kabir Singh (2019)", "Kalank (2019)",
        "Chennai Express (2013)", "Saawariya (2007)", "Tezaab (1988)", "Gully Boy (2019)",
        "Dil Se (1998)", "Naseeb (1981)", "Dabangg (2010)", "Baaghi 2 (2018)"
    ],
    "Biographical": [
        "Bhaag Milkha Bhaag (2013)", "MS Dhoni: The Untold Story (2016)", "Sanju (2018)",
        "Shershaah (2021)", "Neerja (2016)", "The Accidental Prime Minister (2019)",
        "Soorma (2018)", "Super 30 (2019)", "Babu Bangaram (2016)",
        "Shutter Island (2010) - Hindi Dub"
    ],
    "Science Fiction": [
        "Koi... Mil Gaya (2003)", "Krrish (2006)", "Robot 2.0 (2018)", "Ra.One (2011)",
        "Raaz: The Mystery Continues (2009)", "Chup Chup Ke (2006)", "24 (2016)",
        "Love Story 2050 (2008)", "Shree 420 (1955)", "Koi... Mil Gaya (2003)"
    ],
    "Horror Comedy": [
        "Stree (2018)", "Laxmii (2020)", "Bhool Bhulaiyaa 2 (2022)", "Go Goa Gone (2013)",
        "Shaadi Ke Side Effects (2014)", "Bhoot Police (2021)", "Ragini MMS 2 (2014)",
        "Horror Story (2013)"
    ],
    "Romance Comedy": [
        "Pyaar Ka Punchnama (2011)", "Pyaar Ka Punchnama 2 (2015)", "Sonu Ke Titu Ki Sweety (2018)",
        "Dil Chata Hai (2001)", "Jaane Tu... Ya Jaane Na (2008)", "Badrinath Ki Dulhania (2017)",
        "Pati Patni Aur Woh (2019)", "Chalte Chalte (2003)"
    ],
    "Action Comedy": [
        "Singh Is Kinng (2008)", "Housefull (2010)", "Golmaal Series", "No Entry (2005)",
        "Chal Mohan Ranga (2018)", "Deshdrohi (2008)", "Judwaa (1997)", "Fukrey (2013)",
        "Dhamaal (2007)"
    ],
    "Musical Drama": [
        "Bajirao Mastani (2015)", "Gully Boy (2019)", "Rockstar (2011)", "La La Land (2016) - Hindi Dub",
        "Saawariya (2007)", "Chennai Express (2013)", "Aashiqui (1990)", "Dhadkan (2000)"
    ]
}

# ANSI escape codes for bold and large text (if supported by terminal)
BOLD = '\033[1m'
LARGE = '\033[1m\033[1;31m'  # Combining bold and red color to simulate large effect
END = '\033[0m'

print("Welcome to Movie Picker!")

print("You have the following genre options:")
[print(f"{index}.{i}") for index, i in enumerate(hindi_genres, start=1)]
print()

# Get user input for genre
selected_genre = input(f"Enter genre: ").title()

# Select and display a random movie from the chosen genre if available
if selected_genre in bollywood_movies:
    random_movie = random.choice(bollywood_movies[selected_genre])
    print(f"The movie I chose for you is: {LARGE}{random_movie}{END}")
else:
    print(f"No movies found for genre: {selected_genre}")