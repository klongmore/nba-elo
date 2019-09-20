# nba-elo
What would happen if NBA teams were ranked by ELO?

<br/>

# What is ELO?

ELO is a ranking system, named after a physics professor named Arpad Elo. The ELO ranking system differentiates itself from other ranking systems by the fact that it not only incorporates a win or a loss into a player or team's rank, but also the difficulty of their opponent. It does this by attempting to predict the outcome of the match.

### History of ELO

The ELO ranking system was created for zero-sum games (games where your success is based on the relative skill of you to your opponent per-match), in particular, **Chess**. This ranking system began being used by Chess federations in the 1960s, and was the international standard for Chess tournaments by the 1970s. 

### Pros and Cons of ELO

##### Pros:
 - Players are not punished for playing difficult matches.
 - It is worth superior players' time to seek and prepare for matches against similarly-skilled opponents.
 - Rankings change slowly when good players win, and can change quickly when rising players win.

##### Cons:
 - ELO does not account for the strength of a player/team *on the day of the match* (e.g. injuries, etc.)
 - 'Tanking' players/teams can take absurd amounts of ELO from the top players/teams if an upset occurs.
 - Some see ELO as a 'punishment for doing well', as you gain less ELO the more you win, generally speaking.

# How is ELO calculated?

ELO is calculated by creating a number 0 through 1, which is used as the **expected** value. If the number is 1.00, that means team 1 has a 100% chance of winning, according to the algorithm, if it is 0.00, that means team 2 has a 100% chance of winning. A 0.5 predicts a tie. This is then compared against the actual result of the match, and ELO is distributed accordingly.

### Arpad Elo's algorithm

Elo's implementation for chess is as follows:

The 'expected' value (E<sub>A</sub>) is found here:
https://wikimedia.org/api/rest_v1/media/math/render/svg/51346e1c65f857c0025647173ae48ddac904adcb

Where R<sub>A</sub> and R<sub>B</sub> are the respective current ELOs of each player.

The 'actual' value is 1 if player 1 wins, 0 if player 2 wins, and 0.5 if it is a tie.

The expected and actual values are then put here:
https://wikimedia.org/api/rest_v1/media/math/render/svg/09a11111b433582eccbb22c740486264549d1129

And this determines the new ELO for each player.
(Where R<sup>I</sup><sub>A</sub> is the new ELO for the player, R<sub>A</sub> is the current ELO for the player, *K* is equal to 800/the amount of games played by the player, S<sub>A</sub> is the actual outcome of the match, and E<sub>A</sub> is the expected outcome for the match).

### My implementation for the NBA

For the starting ELO for each NBA team, I used what many current implementations of ELO use as a starting ELO - 1200. 
I used Elo's exact algorithm to determine the expected outcome of each match.
Although I did have a catch-all for ties, I did not need to use it, as NBA implements overtime - i.e. all of the 'actual' outcomes were either 0 or 1. 
For the K value, since we are resetting ELO every season, I decided to divide 800 by 41 (to simulate always being exactly half-way through an NBA season), and keep this constant throughout the season, to avoid inflating teams' ratings at the beginning of the season.

# How did I program this? (Usage)

My programming implementation of this algorithm was completed as a python script. To run this script for yourself, open a terminal with python installed and run the command: *'python elo.py <year>'*.

### Retrieving NBA statistics

I retrieved statistics about NBA game results by using a python package called *basketball_reference_web_scraper*, which can be found on GitHub by a search of its name. This gives a simple framework to work with statistics from basketball-reference.com, without having to scrape all of the data myself.
  
# Findings

The full list of team re-rankings (with their respective ELO) can be found below:

***2018-19***

1. Houston Rockets (1334)           1. Milwaukee Bucks (1338)
2. Golden State Warriors (1328)     2. Toronto Raptors (1316)
3. Portland Trail Blazers (1324)    3. Philadelphia 76ers (1263)
4. Denver Nuggets (1296)            4. Boston Celtics (1261)
5. Utah Jazz (1295)                 5. Orlando Magic (1248)
6. San Antonio Spurs (1272)         6. Brooklyn Nets (1229)
7. Oklahoma City Thunder (1267)     7. Indiana Pacers (1220)
8. Los Angeles Clippers (1264)      8. Detroit Pistons (1200)
9. Sacramento Kings (1155)          9. Charlotte Hornets (1198)
10. Minnesota Timberwolves (1150)   10. Miami Heat (1187)
11. Los Angeles Lakers (1150)       11. Atlanta Hawks (1135)
12. Memphis Grizzlies (1127)        12. Washington Wizards (1101)
13. Dallas Mavericks (1118)         13. Chicago Bulls (1046)
14. New Orleans Pelicans (1106)     14. Cleveland Cavaliers (1025)
15. Phoenix Suns (1031)             15. New York Knicks (1001)

***2017-18***

1. Houston Rockets (1410)           1. Toronto Raptors (1341)
2. Utah Jazz (1311)                 2. Philadelphia 76ers (1335)
3. Portland Trail Blazers (1291)    3. Boston Celtics (1281)
4. New Orleans Pelicans (1287)      4. Indiana Pacers (1278)
5. Golden State Warriors (1285)     5. Cleveland Cavaliers (1268)
6. Oklahoma City Thunder (1278)     6. Milwaukee Bucks (1218)
7. Denver Nuggets (1266)            7. Miami Heat (1215)
8. San Antonio Spurs (1241)         8. Washington Wizards (1186)
9. Minnesota Timberwolves (1238)    9. Detroit Pistons (1169)
10. Los Angeles Clippers (1214)     10. Charlotte Hornets (1156)
11. Los Angeles Lakers (1163)       11. Brooklyn Nets (1105)
12. Sacramento Kings (1099)         12. Atlanta Hawks (1080)
13. Dallas Mavericks (1051)         13. Chicago Bulls (1071)
14. Memphis Grizzlies (1017)        14. New York Knicks (1071)
15. Phoenix Suns (1007)             15. Orlando Magic (1054)

***2016-17***

1. Golden State Warriors (1412)     1. Boston Celtics (1299)
2. San Antonio Spurs (1331)         2. Toronto Raptors (1280)
3. Utah Jazz (1295)                 3. Washington Wizards (1268)
4. Houston Rockets (1293)           4. Miami Heat (1248)
5. Los Angeles Clippers (1286)      5. Cleveland Cavaliers (1228)
6. Oklahoma City Thunder (1250)     6. Milwaukee Bucks (1222)
7. Portland Trail Blazers (1243)    7. Indiana Pacers (1213)
8. Denver Nuggets (1224)            8. Chicago Bulls (1204)
9. Memphis Grizzlies (1181)         9. Atlanta Hawks (1195)
10. New Orleans Pelicans (1171)     10. Detroit Pistons (1141)
11. Dallas Mavericks (1144)         11. Charlotte Hornets (1141)
12. Sacramento Kings (1130)         12. New York Knicks (1097)
13. Minnesota Timberwolves (1128)   13. Orlando Magic (1085)
14. Los Angeles Lakers (1087)       14. Philadelphia 76ers (1079)
15. Phoenix Suns (1051)             15. Brooklyn Nets (1057)

***2015-16***

1. Golden State Warriors (1462)     1. Toronto Raptors (1329)
2. San Antonio Spurs (1416)         2. Cleveland Cavaliers (1305)
3. Oklahoma City Thunder (1303)     3. Charlotte Hornets (1274)
4. Los Angeles Clippers (1301)      4. Boston Celtics (1271)
5. Portland Trail Blazers (1267)    5. Atlanta Hawks (1270)
6. Dallas Mavericks (1213)          6. Miami Heat (1259)
7. Houston Rockets (1210)           7. Detroit Pistons (1239)
8. Utah Jazz (1194)                 8. Indiana Pacers (1234)
9. Memphis Grizzlies (1162)         9. Washington Wizards (1207)
10. Denver Nuggets (1133)           10. Chicago Bulls (1188)
11. Minnesota Timberwolves (1133)   11. Orlando Magic (1142)
12. Sacramento Kings (1129)         12. Milwaukee Bucks (1126)
13. New Orleans Pelicans (1103)     13. New York Knicks (1095)
14. Phoenix Suns (1048)             14. Brooklyn Nets (1019)
15. Los Angeles Lakers (1014)       15. Philadelphia 76ers (938)

***2014-15***

1. Golden State Warriors (1418)     1. Cleveland Cavaliers (1321)
2. San Antonio Spurs (1355)         2. Atlanta Hawks (1314)
3. Los Angeles Clippers (1346)      3. Chicago Bulls (1261)
4. Houston Rockets (1331)           4. Boston Celtics (1246)
5. Memphis Grizzlies (1294)         5. Toronto Raptors (1224)
6. Dallas Mavericks (1266)          6. Washington Wizards (1210)
7. Oklahoma City Thunder (1252)     7. Indiana Pacers (1209)
8. New Orleans Pelicans (1250)      8. Brooklyn Nets (1202)
9. Portland Trail Blazers (1241)    9. Milwaukee Bucks (1183)
10. Utah Jazz (1219)                10. Miami Heat (1159)
11. Phoenix Suns (1164)             11. Detroit Pistons (1144)
12. Denver Nuggets (1109)           12. Charlotte Hornets (1110)
13. Sacramento Kings (1092)         13. Orlando Magic (1054)
14. Los Angeles Lakers (1020)       14. New York Knicks (1002)
15. Minnesota Timberwolves (989)    15. Philadelphia 76ers (1001)


### Limitations in study

This program can only be run to perform this re-ranking for the last **5 years** of the NBA. This is due to an issue with the *basketball_reference_web_scraper* package previously mentioned, as it cannot take a datetime argument from basketball-reference for seasons before 2014-15 (for whatever reason).

### Who got better?



### Who got worse?
### Study records
Highest ELO
Lowest ELO
Largest positive change
Largest negative change
Most consistent
