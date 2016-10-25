# Explore Messages

1. To explore your messages download your Facebook data by going to https://www.facebook.com/settings and exporting your data.
![Download Facebook Data](/facebookdata.png)

2. You will recieve a zip file called `facebook-<username>`.
   Unzip that file to create a new folder of the same name: `facebook-<username>`

3. Navigate inside that folder.

   If you type `ls` 
   You should see folders called html, photos, and videos as well as a file called index.html

4. Download this repository.

   `git clone https://github.com/markdawson/explore-messages.git`

5. Create a virtualenv running *python 2*

   `virtualenv -p /usr/bin/python2.7 venv`

6. Activate it

   `source venv/bin/activate`

7. Now start up the script:

   `source start.sh`

   It will install dependencies.

8. Now you can use any of the following commands:

|Command             |Description   |
|--------------------|--------------|
|`people()`          |Gives a list of all the people you've had conversations wtih
|`convosWith(name)`  |Input a string, and for all names matching your srting, you will see all the conversations you've had with people matching the string
|`messagesWith(name)`|input a persons name and view all messages just between you and that person, also creates a new html file with all messages with that person. Note: if there are multiple matches for your input - say two people with the same first name - it will just pick one.
|`negativeWith(name)`|View negative messages with someone|
|`positiveWith(name)`|View position message with someone|

Run `python -i soup.py` if you exit the python shell and want to re-enter it 
