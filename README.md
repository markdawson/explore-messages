# Messages Explorer

To explore your messages download your Facebook data by going to https://www.facebook.com/settings and exporting your data.

![Download Facebook Data](/facebookdata.png)

You will recieve a zip file called `facebook-<username>`.
Unzip that file to create a new folder of the same name: `facebook-<username>`

Navigate inside that folder.
If you type `ls`
You should see folders called html, photos, and videos as well as a file called index.html

Now start up the script:

`source start.sh`

It will install dependencies.
Now you can use any of the following commands:

|Command             |Description   |
|--------------------|--------------|
|`convosWith(name)`  |input a string and view all the conversations you've had with that person
|`messagesWith(name)`|input a persons name and view all messages just between you and that person, also creates a new html file with all messages with that person. Note: if there are multiple matches for your input - say two people with the same first name - it will just pick one.
