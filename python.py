import sqlite3
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

# Connecting to sqlite
# connection object
Player = input('What is your name? ')
MatchLength = input('How long was the match (in minutes)? ')
Score = input('What was the score? ')
Temperature = input('What was the temperature? ')
OpponentName = input('Who did you play against? ')
OpponentTeam = input('What team did ' + OpponentName + ' play for? ')
OpponentGrade = input('Was ' + OpponentName + ' a Freshman, Sophomore, Junior, or Senior? ')
Line = input('What line did you play? ')
Weather = input('What was the weather like? ')
Location = input('Where did you play? ')
Winner = input('Who won the match? ')
CourtNumber = input('What court number did you play on? ')
DistanceRan = input('How far did you run? ')
Region = input('Was the match region or non-region? ')
Caffeine = input('Did you have caffeine that day? ')
Breakfast = input('Did you have breakfast that day? ')
Lunch = input('Did you have lunch that day? ')
DateofMatch = input('What day was your match? ')
Times = input('When did you get on and off the court? ')
# ("Braden", 76, "6-3, 6-2", 68, "MichaelSpinks", "Adairsville", "Junior", "1st Singles", "Cloudy", "Adairsville Highschool", "Braden", "Court 1", 4, "Non-Region", "No Caffeine", "No Breakfast", "Had Lunch", "December 20, 2005", "1:23 - 3:43")
connection_obj = sqlite3.connect('tennis.db')
query = """INSERT INTO tennis (Player, MatchLength, Score, Temperature, OpponentName, OpponentTeam, OpponentGrade, Line, Weather, Location, Winner, CourtNumber, DistanceRan, Region, Caffeine, Breakfast, Lunch, DateofMatch, Times) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
tuple1 = (Player, MatchLength, Score, Temperature, OpponentName, OpponentTeam, OpponentGrade, Line, Weather, Location, Winner, CourtNumber, DistanceRan, Region, Caffeine, Breakfast, Lunch, DateofMatch, Times)
connection_obj.execute(query, tuple1)
connection_obj.commit()

# Close the connection
connection_obj.close()
