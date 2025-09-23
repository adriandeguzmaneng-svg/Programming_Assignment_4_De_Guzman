# Programming_Assignment_4_De_Guzman
This programing assignment contains the codes for the given problems in python. These problems tackles Data Wrangling and Visualization.
___
## Problem #1
### Overview
For this problem, we are tasked to create a data frame based on the format provided in which there are 2 formats provided meaning we need to create 2 data frames. 
For data frame a, the format is: Filename: Instru = [“Name”, “GEAS”, “Electronics >70”]; where track is constant as Instrumentation and hometown Luzon
For data frame b, the format is: Filename: Mindy = [ “Name”, “Track”, “Electronics”, “Average >=55”]; where hometown is
constant as Mindanao and gender Female
### Code
Data Frame a
<img width="775" height="93" alt="image" src="https://github.com/user-attachments/assets/f6ce2ded-6e60-4ca6-9e02-707ea835f02b" />

Data Frame b
<img width="1181" height="92" alt="image" src="https://github.com/user-attachments/assets/d7a58f27-5962-47bc-961e-78e83f359d9c" />

### How i made it
I first loaded the panda library for the Data Frames using the code "import pandas as pd" then loaded the given .csv file to the IDE then storing it to the variable df = creating the code "df = pd.read_csv('board2.csv')"
#### Data Frame a
For data frame a, i used the syntax ".loc" to look through the data frame through the columns of the "Hometown" for any Luzons since it is constant, to also look for the "Track" column to look for any "Instrumentation", and to look for any value in "Electronics" that is greater than 70. All of this while using the logic operator "&" for all three, symbolizing "and" meaning all 3 of the conditions must be satisfied for it to be true. Thus creating the syntax, "Instru = df.loc[(df['Hometown'] == 'Luzon') & (df['Track'] == 'Instrumentation') & (df['Electronics'] > 70)]". Then using the ".DataFrame" syntax, i was able to pick specific colums that was only required to display or save and that is the "Name", "GEAS" and "Electronics", producing the code Instru = pd.DataFrame(Instru, columns = ("Name", "GEAS", "Electronics")). Next, i saved the data frame into a csv through the syntax ".to_csv()" thus if the whole line makes "Instru.to_csv('Instru.csv')". Lastly i displayed the data frame for checking.
#### Data Frame b
For data frame b, it is just like the data frame a but with a few modification. I first got the average of them all by using the function ".mean(axis=1)" to get the average of the columns "Math", "Electronics", "GEAS" and "Communication" then stored it while creating a new column in the data frame using the syntax "mindy["Average"]=". Meaning the whole line of code would be mindy["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1). Then, I used the syntax ".loc" to look through the data frame through the columns of the "Hometown" for any "Mindanao" since it is constant, to also look for the "Gender" column to look for any "Female", and to look for any value in "Average" that is greater than or equal to 55. All of this while using the logic operator "&" for all three, symbolizing "and" meaning all 3 of the conditions must be satisfied for it to be true. Thus creating the syntax, "Mindy = mindy.loc[(mindy['Hometown'] == 'Mindanao') & (mindy['Gender'] == 'Female') & (mindy['Average'] >= 55)]". Then using the ".DataFrame" syntax, i was able to pick specific colums that was only required to display or save and that is the "Name", "Track", "Electronics" and "Average", producing the code "Mindy = pd.DataFrame(Mindy, columns = ("Name", "Track", "Electronics", "Average"))". Next, i saved the data frame into a csv through the syntax ".to_csv()" thus if the whole line makes "Instru.to_csv('Instru.csv')". Lastly i displayed the data frame for checking.
### Output 
Data Frame a
<img width="440" height="187" alt="image" src="https://github.com/user-attachments/assets/6938f80b-279d-489c-8733-41ee18d3fd54" />
Data Frame b
<img width="305" height="185" alt="image" src="https://github.com/user-attachments/assets/5a1887fe-3bee-47fc-888e-253f81e4c896" />
### Lesson Learned
Through this problem, Although it is not visible on the code itself, i learned to be efficient on my codes. Produce the same amount and quality of output while using the least amount of lines of codes as possible. Through this, my codes would be able to be presentable as well as help a program faster in the future as i mean running on lesser lines of codes.

## Problem #2
### Overview
For this problem, we are tasked to create Create a visualization that shows how the different features contributes to average grade and to answer "Does chosen track in college, gender, or hometown contributes to a higher average score?".
### Code 



