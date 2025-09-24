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
Using the code below, i was able to use the panda library as well as import the specified initial data frame into program
```python
import pandas as pd
df = pd.read_csv('board2.csv')
```
#### Data Frame a
```python
Instru = df.loc[(df['Hometown'] == 'Luzon') & (df['Track'] == 'Instrumentation') & (df['Electronics'] > 70)]
Instru = pd.DataFrame(Instru, columns = ("Name", "GEAS", "Electronics"))
Instru.to_csv('Instru.csv')
```
#### Data Frame b
```python
mindy = df.copy()
mindy["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)
Mindy = mindy.loc[(mindy['Hometown'] == 'Mindanao') & (mindy['Gender'] == 'Female') & (mindy['Average'] >= 55)]
Mindy = pd.DataFrame(Mindy, columns = ("Name", "Track", "Electronics", "Average"))
Mindy.to_csv('Mindy.csv')
Mindy
```
### How does it work
#### Data Frame a
This line analyzes through the data frame and checks the column for the given conditions such as the Hometown must be Luzon, Track must be instrumentation and score in electronics must be greater than 70 the store it to the variable "Instru"
```python
Instru = df.loc #puts all the value to the varible Instru
  [(df['Hometown'] == 'Luzon') & #Looks through the column "Hometown" and checks for the string "Luzon"
  (df['Track'] == 'Instrumentation') #Looks through the column "Track" and checks for the string "Instrumentation" 
  & #Logical operator that states all must be true for the statement to be true or in this case inlcuded.
  (df['Electronics'] > 70)] #Looks through the column "Electronics" and checks the value if they are more than 70
```
This lines would create a new data frame that only has the column "Name, "GEAS", and "Electronics" which were specified in task and save the data frame into a .csv file
```python
Instru = pd.DataFrame(Instru, columns = ("Name", "GEAS", "Electronics")) #Creates a new data frame that only has specific column
Instru.to_csv('Instru.csv') #Saves the data frame into a .csv file
```
#### Data Frame b
These lines copies the data frame and performs a function .mean() to get the average then put into a new column "Average"
```python
mindy = df.copy() #This line copies the data frame to prevent any errors in the code
mindy["Average"] #This line puts the value made from the function into a new column of an array
= df[["Math", "Electronics", "GEAS", "Communication"]] #gets the value within these columns
.mean(axis=1) #gets the mean or the average of the selected values, axis=1 for the rows
```
This line locates the specified parameters from the specified column
```python
Mindy = mindy.loc #puts all the located value to the variable Mindy
  [(mindy['Hometown'] == 'Mindanao') #locates in the column "Hometown" who's value has "Mindanao"
  & (mindy['Gender'] == 'Female') #locates in the column "Gender" who has the value of "Female"
  & (mindy['Average'] >= 55)] #locates in the column "Average" who has a value of greater than or equal to 55
```
this line puts all the specified and required columns and saves the data frame into a .csv file
```python
Mindy = pd.DataFrame(Mindy, columns = ("Name", "Track", "Electronics", "Average")) #creates a data frame in which only the columns Name, Track, Electronics and Average are ony written as well as all of the values inside that column
Mindy.to_csv('Mindy.csv') #saves the data frame into a .csv file
```
### Output

### Lesson Learned
Through this problem, Although it is not visible on the code itself, i learned to be efficient on my codes like using multiple amounts of funciton in a single line. Producing the same amount and quality of output while using the least amount of lines of codes as possible. Through this, my codes would be able to be presentable as well as help a program faster in the future as i mean running on lesser lines of codes.

## Problem #2
### Overview
For this problem, we are tasked to create Create a visualization that shows how the different features contributes to average grade and to answer "Does chosen track in college, gender, or hometown contributes to a higher average score?".
### Code 
Initial values and library
```python
df["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)
Average = df[["Track", "Gender", "Hometown", "Average"]]
import matplotlib.pyplot as plt
```
Average By Track
```python
ITrackAve = Average.loc[Average['Track'] == 'Instrumentation', "Average"].mean()
CTrackAve = Average.loc[Average['Track'] == 'Communication', "Average"].mean()
MTrackAve = Average.loc[Average['Track'] == 'Microelectronics', "Average"].mean()
plt.figure(figsize=(5, 6))
plt.bar(TrackAve['Track'], TrackAve['Average'])
plt.title("Average by Track")
```
Average By Gender 
```python
MGenderAve = Average.loc[Average['Gender'] == 'Male', "Average"].mean()
FGenderAve = Average.loc[Average['Gender'] == 'Female', "Average"].mean()
plt.figure(figsize=(5, 6))
plt.bar(GenderAve['Gender'], GenderAve['Average'])
plt.title("Average by Gender")
```
Average By Hometown
```python
LHomeAve = Average.loc[Average['Hometown'] == 'Luzon', "Average"].mean() #
VHomeAve = Average.loc[Average['Hometown'] == 'Visayas', "Average"].mean()
MHomeAve = Average.loc[Average['Hometown'] == 'Mindanao', "Average"].mean()
plt.figure(figsize=(5, 6))
plt.bar(HomeAve['Hometown'], HomeAve['Average'])
plt.title("Average by Hometown")
```
### How does it work
These lines were made for easier plotting since this lines creates an average for each student 
```python
df["Average"] #Creates a new column in the data frame named average
= df[["Math", "Electronics", "GEAS", "Communication"]] #only chooses the math, electronics, GEAS and communication column of the frame
.mean(axis=1) #gets the average of the column by rows throught the means of "Axis=1"
Average = df[["Track", "Gender", "Hometown", "Average"]] #plots the data frame with only the required columns
import matplotlib.pyplot as plt #imports the library for data plotting
```
Explaining a sample code from one of the visualization, these lines get the average of the rows
\n These lines gets the mean for the different track values such as instrumentation, communication, mircoelectronics
```python
ITrackAve = Average.loc[Average['Track'] == 'Instrumentation', "Average"].mean() #takes only the column track and row instrumentation and gets the mean of all their average
CTrackAve = Average.loc[Average['Track'] == 'Communication', "Average"].mean() #takes only the column track and row communication and gets the mean of all their average
MTrackAve = Average.loc[Average['Track'] == 'Microelectronics', "Average"].mean() #takes only the column track and row microelectronics and gets the mean of all their average
TrackAve
plt.figure(figsize=(5, 6))
plt.bar(TrackAve['Track'], TrackAve['Average'])
plt.title("Average by Track")
```
### Output
Average By Track

<img width="489" height="594" alt="image" src="https://github.com/user-attachments/assets/90059f65-595d-4431-895a-ffa6869d77d8" />

Average By Gender 

<img width="479" height="589" alt="image" src="https://github.com/user-attachments/assets/d72f115c-80fe-4bcb-b781-870b789bcfd3" />

Average By Hometown
<img width="483" height="594" alt="image" src="https://github.com/user-attachments/assets/2862867b-6a4b-4de7-a59c-6be75e1d33b2" />

### Lesson learned
Through this problem i am now able to visualize data to properly analyze problems. Using the problem given, i can use this knowledge in the future to analyze statistics using only python code. 
