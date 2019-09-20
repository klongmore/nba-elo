# nba-elo
Ever thought that your NBA team got screwed by their schedule?

Does your friend keep bragging to you that their mediocre team somehow beat yours in the regular-season standings?

What if NBA teams were ranked by their ELO, not their W/L?

***FOR A TL;DR, READ FROM 'FINDINGS' ONWARDS.***

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

The full list of team re-rankings (with their respective ELO and how far they moved) can be found below.
**A team having a + number denotes that they may have had a difficult schedule for that season.**
**A team with a - number denotes that they may have had an easy schedule for that season.**

***2018-19***

West:
1. Houston Rockets (1334) **+3**        
2. Golden State Warriors (1328) **-1**     
3. Portland Trail Blazers (1324) **+0**   
4. Denver Nuggets (1296) **-2**            
5. Utah Jazz (1295) **+0**                
6. San Antonio Spurs (1272) **+1**        
7. Oklahoma City Thunder (1267) **-1**   
8. Los Angeles Clippers (1264) **+0**   
9. Sacramento Kings (1155) **+0**  
10. Minnesota Timberwolves (1150) **+1** 
11. Los Angeles Lakers (1150) **-1**
12. Memphis Grizzlies (1127) **+0**
13. Dallas Mavericks (1118) **+1**
14. New Orleans Pelicans (1106) **-1**
15. Phoenix Suns (1031) **+0**

East:
1. Milwaukee Bucks (1338) **+0**
2. Toronto Raptors (1316) **+0**
3. Philadelphia 76ers (1263) **+0**
4. Boston Celtics (1261) **+0**
5. Orlando Magic (1248) **+2**
6. Brooklyn Nets (1229) **+0**
7. Indiana Pacers (1220) **-2**
8. Detroit Pistons (1200) **+0**
9. Charlotte Hornets (1198) **+0**
10. Miami Heat (1187) **+0**
11. Atlanta Hawks (1135) **+1**
12. Washington Wizards (1101) **-1**
13. Chicago Bulls (1046) **+0**
14. Cleveland Cavaliers (1025) **+0**
15. New York Knicks (1001) **+0**

***2017-18***

West:
1. Houston Rockets (1410) **+0**           
2. Utah Jazz (1311) **+3**               
3. Portland Trail Blazers (1291) **+0**    
4. New Orleans Pelicans (1287) **+2**     
5. Golden State Warriors (1285) **-3**     
6. Oklahoma City Thunder (1278) **-2**  
7. Denver Nuggets (1266) **+2**            
8. San Antonio Spurs (1241) **-1**        
9. Minnesota Timberwolves (1238) **-1**   
10. Los Angeles Clippers (1214) **+0**     
11. Los Angeles Lakers (1163) **+0**     
12. Sacramento Kings (1099) **+0**         
13. Dallas Mavericks (1051) **+0**        
14. Memphis Grizzlies (1017) **+0**   
15. Phoenix Suns (1007) **+0**       

East:
1. Toronto Raptors (1341) **+0**
2. Philadelphia 76ers (1335) **+1**
3. Boston Celtics (1281) **-1**
4. Indiana Pacers (1278) **+1**
5. Cleveland Cavaliers (1268) **-1**
6. Milwaukee Bucks (1218) **+1**
7. Miami Heat (1215) **-1**
8. Washington Wizards (1186) **+0**
9. Detroit Pistons (1169) **+0**
10. Charlotte Hornets (1156) **+0**
11. Brooklyn Nets (1105) **+1**
12. Atlanta Hawks (1080) **+3**
13. Chicago Bulls (1071) **+0**
14. New York Knicks (1071) **-3**
15. Orlando Magic (1054) **-1**

***2016-17***

West:
1. Golden State Warriors (1412) **+0**
2. San Antonio Spurs (1331) **+0**        
3. Utah Jazz (1295) **+2**                 
4. Houston Rockets (1293) **-1**           
5. Los Angeles Clippers (1286) **-1**     
6. Oklahoma City Thunder (1250) **+0**    
7. Portland Trail Blazers (1243) **+1**  
8. Denver Nuggets (1224) **+1**          
9. Memphis Grizzlies (1181) **-2**       
10. New Orleans Pelicans (1171) **+0**    
11. Dallas Mavericks (1144) **+0**       
12. Sacramento Kings (1130) **+0**       
13. Minnesota Timberwolves (1128) **+0**
14. Los Angeles Lakers (1087) **+0**    
15. Phoenix Suns (1051) **+0**           

East:
1. Boston Celtics (1299) **+0**
2. Toronto Raptors (1280) **+1**
3. Washington Wizards (1268) **+1**
4. Miami Heat (1248) **+5**
5. Cleveland Cavaliers (1228) **-3**
6. Milwaukee Bucks (1222) **+0**
7. Indiana Pacers (1213) **+0**
8. Chicago Bulls (1204) **+0**
9. Atlanta Hawks (1195) **-4**
10. Detroit Pistons (1141) **+0**
11. Charlotte Hornets (1141) **+0**
12. New York Knicks (1097) **+0**
13. Orlando Magic (1085) **+0**
14. Philadelphia 76ers (1079) **+0**
15. Brooklyn Nets (1057) **+0**

***2015-16***

West:
1. Golden State Warriors (1462) **+0**   
2. San Antonio Spurs (1416) **+0**         
3. Oklahoma City Thunder (1303) **+0**     
4. Los Angeles Clippers (1301) **+0**     
5. Portland Trail Blazers (1267) **+0**    
6. Dallas Mavericks (1213) **+0**          
7. Houston Rockets (1210) **+1**           
8. Utah Jazz (1194) **+1**                 
9. Memphis Grizzlies (1162) **-2**         
10. Denver Nuggets (1133) **+1**        
11. Minnesota Timberwolves (1133) **+2** 
12. Sacramento Kings (1129) **-2**        
13. New Orleans Pelicans (1103) **-1**     
14. Phoenix Suns (1048) **+0**             
15. Los Angeles Lakers (1014) **+0**      

East:
1. Toronto Raptors (1329) **+1**
2. Cleveland Cavaliers (1305) **-1**
3. Charlotte Hornets (1274) **+3**
4. Boston Celtics (1271) **+1**
5. Atlanta Hawks (1270) **-1**
6. Miami Heat (1259) **-3**
7. Detroit Pistons (1239) **+1**
8. Indiana Pacers (1234) **-1**
9. Washington Wizards (1207) **+1**
10. Chicago Bulls (1188) **-1**
11. Orlando Magic (1142) **+0**
12. Milwaukee Bucks (1126) **+0**
13. New York Knicks (1095) **+0**
14. Brooklyn Nets (1019) **+0**
15. Philadelphia 76ers (938) **+0**

***2014-15***

West:
1. Golden State Warriors (1418) **+0**     
2. San Antonio Spurs (1355) **+4**        
3. Los Angeles Clippers (1346) **+0**      
4. Houston Rockets (1331) **-2**         
5. Memphis Grizzlies (1294) **+0**          
6. Dallas Mavericks (1266) **+1**          
7. Oklahoma City Thunder (1252) **+2**     
8. New Orleans Pelicans (1250) **+0**      
9. Portland Trail Blazers (1241) **-5**  
10. Utah Jazz (1219) **+1**               
11. Phoenix Suns (1164) **-1**             
12. Denver Nuggets (1109) **+0**         
13. Sacramento Kings (1092) **+0**          
14. Los Angeles Lakers (1020) **+0**       
15. Minnesota Timberwolves (989) **+0**    

East:
1. Cleveland Cavaliers (1321) **+1**
2. Atlanta Hawks (1314) **-1**
3. Chicago Bulls (1261) **+0** 
4. Boston Celtics (1246) **+3**
5. Toronto Raptors (1224) **-1**
6. Washington Wizards (1210) **-1**
7. Indiana Pacers (1209) **+2**
8. Brooklyn Nets (1202) **+0** 
9. Milwaukee Bucks (1183) **-3**
10. Miami Heat (1159) **+0** 
11. Detroit Pistons (1144) **+1**
12. Charlotte Hornets (1110) **-1**
13. Orlando Magic (1054) **+0** 
14. New York Knicks (1002) **+1**
15. Philadelphia 76ers (1001) **-1**

### Comments

Utah consistently gets pretty bad schedules - they eclipse all other teams will a total of +7 rankings across the 5 years when ranked by ELO. Heavily under-rated within the W/L system.

As for teams that seem to get favourable schedules: Golden State, Portland, Memphis, and Cleveland always seem to get an easier time / get over-rated by the W/L system.

### Records

Not particularly a surprise, but the highest single-season ELO by *far* belongs to the 2015-16 Warriors, with 1462 ELO.

2015-16 also housed the worst team in the last 5 years, the Philadelphia 76ers, who managed to dip below *950* ELO.

The most a team was disrespected by the W/L system in the last 5 years was the Miami Heat, in 2016-17. In real life, the Miami Heat missed the playoffs this year, at the 9th seed. If they were playing by ELO, they would have been the **4th** seed.

As for the team that got the most favourable schedule in the last 5 years, this belongs to the 2014-15 Portland Trail Blazers, who did an anti-Miami. They finished 4th in real life. If they were playing by ELO, **they would have missed the playoffs**.

Three teams managed to consistently get average schedules, with a total of +0. These teams are the New Orleans Pelicans, Philadelphia 76ers, Indiana Pacers, and Washington Wizards. These teams only have their individual skill to worry about :)

### Limitations in study

This program can only be run to perform this re-ranking for the last **5 years** of the NBA. This is due to an issue with the *basketball_reference_web_scraper* package previously mentioned, as it cannot take a datetime argument from basketball-reference for seasons before 2014-15 (for whatever reason).
