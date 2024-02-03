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
necessary to output a workable schedule in csv format, according to the rules for 
each level of play.  

## Data
Application data resides in two principal places:  A configuration file and a sqlite
database.  
### SQLite Database
There is a sqlite database that is initiated and populated by `model/create_load`.
The tables are as follows:  
*  *Levels* - describes the various levels of play  
    * ID
    * level
*  *Leagues* - describes the different area leagues that participate in the season.  
    * ID
    * League
*  *Teams* - describes the different teams that play in the season.
    * ID
    * level_id (fk Levels)
    * league_id (fk Leagues)
    * name
*  *Fields* - describes the location, field name, and home league for the fields represented in the schedule.
    * ID
    * location
    * field
    * league_id (fk Leagues)
    * lights
*  *field_level* - indicates which field-locations are appropriate for which levels of play.
    * field_id (fk Fields)
    * level_id (fk Levels)
*  *games_per_week* - indicates, by level, how many games are played per week.
    * level_id (fk Levels)
    * gpw  
*  *day_time* - indicates the day name, day number, and start time available for games
    * ID
    * day_text
    * day_num
    * start_time

### Configuration File
The configuration file provides level name, level game length, allowable game days, and games per season for each level as well
as league information, such as the date for opening day.  

## General Scheduling Rules  
1.  Teams should play a roughly equal number of Home and Away Games.
2.  Home teams host the game at a location associated with their home league.  This relationship is defined by the `league_id` column in Teams and the `league_id` column in Fields.
3.  Games must be played at a field appropriate to their level.  This relationship is defined in the `field_level` table.
4.  Games must be played on days allowable to their level.  This relationship is defined in  `allowable_days` in a level's object in the config file.
5.  Games must be assigned a day/time timeslot from the `day_time` table.
6.  Location-Field-Date-Time assignments must be unique.
7.  Per level, each team should play every other team the same number of times.
8.  Per level, each team should play a number of games equal to its level's `games_per_season` as defined in the config file.
9. 