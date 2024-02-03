# Project Description  
This project is to develop an application that will create a usable schedule
for the Pasadena American Little League (PALL).  The league consists of 7 levels that 
are defined by age and skill level.  At each level, there are between 2 and 7
teams.  Throughout the course of a roughly 10-week spring season, PALL teams will
play against other teams in both PALL and other little leagues in the region.  
  
PALL has 7 fields that it can use for games that it hosts.  Not all fields are
appropriate for games at all levels.  Each partnering little league has fields
to host games as well.  

The number of games played per week per team is usually two, though T-Ball, the 
lowest level plays only one game per week.  

## Release 1 Goals
The goal for the first release is to create the functions and data structures 
necessary to output a workable schedule in format, according to the rules for 
each level of play.  

### Data
#### Fields
Each league level has fields suitable for play at that level.  Fields are identified
by Location and Field.  For Example `Hamilton 1` indicates field 1 at Hamilton Park.  
When a team hosts a game as the Home team, it must be played at a field belonging
that league and that is appropriate to the level of play.
#### Games per Week
Each league level will play a specified number of games per week.  Usually 1 or 2.
#### Team Names
Each team has a name.  PALL teams are named `$level - $name`.  Teams from other
leagues are named `$league - $level - $name`.
#### Allowable Game Days
Games can be played Mondays, Tuesdays, Wednesdays, Thursdays, and Saturdays.  
Friday games are allowed but are highly discouraged.  No games on Sundays.
#### Game Length
Game length is determined by level.

### Rules
Schedules must obey these rules:  
* Teams should play an equal number of Home games (games played at one of their fields) and Away games.
* Each team should play every other team an equal number of times.  
* Fields can only be used for one game at a time.  We cannot schedule more than one game per field at the same time.
* There must be 30 minutes between the end of one game and the start of the next on that field.
* For leagues that play two games per week, one of those games must be on Saturday.
* Games must not be scheduled to begin after 5pm until after Daylight Savings Time begins, or unless the field has lights.

### Output
The schedule output must be in csv format and include the following fields:
* Date
* Location and Field
* Start Time
* End Time
* Home Team
* Away Team
* League Level
* 