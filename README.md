### PYTHON WEEK 8 ASSIGNMENT

Question 1:
Create nine empty text files with pathnames day1.txt, day2.txt, ……., day9.txt . 

Question 2:
Create a file “numbers.txt” and write the numbers 1 to 10 into the file.. 

Question 3:
Write the following city names sequentially to the file “sehir.txt” with plate sign belong to each.
cities=['Kayseri' ,'Istanbul', 'Izmir', 'Konya','Kars', 'Kastamonu',  'Kirklareli','Icel', 'Kirsehir', 'Kocaeli' ]

Sample output in the file:
Sehir.txt
____________________________________________________________
33 Icel
34 Istanbul
.
.
.
41 Kocaeli
42 Konya


Question 4:
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data:  regex_sum_259427.txt(There are 85 values and the sum ends with 556)
Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. 
The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

Turn in Assignment
Enter the sum from the actual data and your Python code below:
Sum:    
 (ends with 556) 
