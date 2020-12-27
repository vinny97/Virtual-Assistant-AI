# Virtual-Assistant-AI
Your virtual assistant, created using python and can answer a range of questions

![image](http://static.businessworld.in/article/article_extra_large_image/1502431470_PZSaUZ_RPA.jpg)


The ReadMe file includes the Process, Packages and other helpful information that went into creating this program

Wolframalpha api
import wolframalpha
https://pypi.org/project/wolframalpha/#description

Python Simple GUI
need a simple GUI
so search for a python gui 
we want a nice window to pop up rather than using command line or terminal

using pysimpleGUI
in order to install this use:
    pip install pysimplegui

now onto the loop
while true loop, the window will stay open until the user clicks ‘Cancel’
instead of getting the temperature of washington, it will return whatever the user enters
which is value 0 , the first element in the values list

use the print (next(res.results).text line 
use sg.popup to have a another window popup and show the answer instead of terminal

Wikipedia
now time to use wikipedia as well
don’t need an api key to use wikipedia
 
pip install wikipedia
then import wikipedia

wolframalpha can answer most questions, but wikipedia may give a longer more distinct answer
set wiki_result to values since that’s what we are going to be inputting into the program
and in the popup set it to wiki_result so it will print out wiki_result by default

as wikipedia is faster see if wikipedia can return  result, if not, it will go to wolfram
- use the try
- The try block lets you test a block of code for errors.
The except block lets you handle the error.

our code now, it firstly tests the block of code of wikipedia and if there is an error the except block of code will run wolfram

however that didn’t work
so now we will try the other way around
where try run it through wolfram first and if that doesn’t return anything or throws error it will redirect to wikipedia

need a sg.popup for both results
- for try and except
test: rhode island

wolfram ran rhode island and retrived name, population and joined union
however we want the info from wikipedia, which states , the name and then where its based and other useful info rather than bunch of stats
- possible solution
    - the user will ask questions and well from that decide if categorises that wikipedia should handle or wolfram should handle
    - or have both pop up, give the user as much as info as possible

the second solution of having both pieces of information from the two sources has worked

text to speech
pip install pyttsx3

use import in your code to import this package
- follow the usage code on the python package website
once it has been installed 
we want the the text to appear first and then the text to speech to start reading 
    - however it didn’t start text to speech until we clicked Ok button which closed the text and then it started the text to speech
- so it either it says it first and then the pop of the text appears, vice versa
- we want it to do both at the same time
- possible solutions
        - use popupNonBlocking to concurrently run both the text to speech and the popup text

then using one try and two except statements
where it first sold of tried the wiki result and saw the user warning and except that and went to the except code which is wolfram
- but we were using the except statement for the user warning error
- there is also another error that appears the disambiguation error
therefore use two seperate except statements for both errors


summary
- Firstly our try and except block of code will try wikipedia and try wolfram
- if wikipedia throws disambiguation error or a page error it will try wolfram
- if it throws another error not related to those two errors, then going to throw just wikipedia at us because going to assume if its not those two errors, then its wolfram that is wrong and just ask for wikipedia
- so now if i type in something random like “ssdfdsxdfded” 
    - it will return nothing and no need for an error message to pop up
 - the text to speech works concurrently with the text
