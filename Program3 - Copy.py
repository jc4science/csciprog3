# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Music CSV Library
# Jeremy Stephens
# Last Modified: Feb. 26, 2018 
# ---------------------------------------
# finds, and analyzes data from the file music.csv in order to return the selected query's response.
# ---------------------------------------
import os
import csv
import random

#----------------------------------------
#For the record, my working variables for this function(rows instead of duration, and songs instead of titles) were a pretty bad time to work with.
#----------------------------------------

def longest_song():
    file_path = os.path.abspath("music.csv")
    file = open(file_path, "r")
    
    with open('music.csv', 'r') as csvfile:
        rowreader = csv.reader(csvfile)
        next(rowreader, None)
        duration = 0
        titles = []

        for row in rowreader:
            if float(row[9]) > float(duration):
                #print("greater")
                #print("replaced!!!", row[9], "is >", duration)

                del duration
                del titles[:]

                duration = row[9]
                #print(duration)
                titles.append(row[33])
                #print(titles)
                
            elif float(row[9]) == float(duration):
                #print("eq")
                duration.append(row[9])
                #print("appended!!!", duration)

                titles.append(row[33])
                #print(titles)    

    print("\nTitle:", "/".join(titles)) #this formats the titles.
    print("Length to nearest second:", round(float(duration))) #this formats the actual time

    file.close

#----------------------------------------
#Notes would go here, if I had any. This was for sure the simplest of the 4 to write.
#----------------------------------------

def songs_by_year(year):
    file_path = os.path.abspath("music.csv")
    file = open(file_path, "r")
    
    with open('music.csv', 'r') as csvfile:
        rowreader = csv.reader(csvfile)
        next(rowreader, None)
        tot_in_year = 0

        for row in rowreader:
            #print(row[34])
            if int(row[34]) == int(year):
                #print("It's a match!!", row[34])
                #print("PLUS ONE!!!", tot_in_year)
                tot_in_year += 1

    print("The number of songs from ", year, "is ", tot_in_year)        

    file.close()
    
#----------------------------------------
#This is the first one that I completed, and I based the rest of my functions(methods, whatever) off of this.
#----------------------------------------    

def all_songs_by_artist(artist):
    file_path = os.path.abspath("music.csv")
    file = open(file_path, "r")

    songs = []

    with open('music.csv', 'r') as csvfile:
        rowreader = csv.reader(csvfile)
        next(rowreader, None)
        #print(artist)
        
        for row in rowreader:
            #print(row[2].lower())
            if row[2].lower() == str(artist):
                #print(row[33])
                songs.append(row[33])
    songs.sort()
    print("\nSongs in Alphabetical Order")
    print("---------------------------")
    if songs:
        i = 0
        #print(len(songs))

        while i < len(songs):
            print(str(i+1), songs[i])
            i += 1
    else:
        print("There are no songs by this artist.")
    print("---------------------------")

    file.close()

#----------------------------------------
#This function generates a random number between 1 and 9999(inclusive, and using the random module) and then pulls the song info from that line's entry.
#This was the last function I wrote, and finished it up pretty quickly once I had the row reading code down, and decided what I wanted to do.
#----------------------------------------

def random_song():
    file_path = os.path.abspath("music.csv")
    file = open(file_path, "r")
    
    with open('music.csv', 'r') as csvfile:
        rowreader = csv.reader(csvfile)
        next(rowreader, None)
        i = 0
        songnum = random.randint(1, 9999)
        
        for row in rowreader:
            i += 1
            if songnum == i:
                print("Your song is:", '"' + row[33] + '"', "\nBy:", row[2])
                if int(row[34]) != int(0):
                    print("It was released in", row[34])
                else:
                    print("I'm not sure when it was released...sorry!")
        
    file.close()
    
# --------------------------------------

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. Find a random song.")
    print("5. Quit.")

# --------------------------------------

def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song()
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year)
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist)
        elif (choice == 4):
            random_song()
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

# --------------------------------------

main()
