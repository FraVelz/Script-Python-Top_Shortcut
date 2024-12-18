# Top shortcut
Project #5 with Python. Control your own shortcuts.

Python program in which you can create keyboard shortcuts
and configure them to perform certain actions, open web pages,
open applications, turn off PC hacker mode.

In the file directory there is a file called,
secrets-words.json is a .json file in which you can modify
so that when the program runs the top_shortcut.pyw file it reads the
.json program, and you can configure your keyboard shortcuts.

> Note: so far only the shortcuts with one word per shortcut have been tested,
> if you do not follow this recommendation the file may not work.

# How to add shortcuts or keywords
in the .json file it comes in the following format:

````json
{
    "shortcuts": [
        ["local", "fravelz", "turnOff.bat"],
        ["web", "youtube", "https:youtube.com/"],
    ]
}
`````

**shortcut:** is where you should add the information which is structured in the following way:

````json
["web", "youtube", "https:youtube.com/"],
`````

* **"web"**: It is where you specify the function of the file, that is, it specifies if it runs a file that is located in the same directory as the program **(local)**, or opens a web page **(web)**, or opens a PC application **(cmd)**.

* **"youtube"** Then it is separated and comes q indicates the keyword or keyboard shortcut, while the program is running, write in this case youtube anywhere and execute the function.

* "https:youtube.com/" And finally the code or route to execute, that is, for example, this will open the youtube page.

That is, with that previous code it says, open a **website**, when you write the word **youtube**, that web address will be **https:youtube.com**

````json
["web", "youtube", "https:youtube.com/"],
`````

Every time you want to add more commands and shortcuts, just put a comma at the end (**,**) to the last list of the shortcut and continue writing with the same writing.

> **Recommendations:**

> The shortcuts should preferably be only lowercase words and numbers, if this is not followed, the shortcuts may not work.

> For a better experience, it is recommended that you move the shortcut (Top Shortcut) to the user's startup folder so that you can access the shortcuts every time you start the PC and thus increase productivity.

````
C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
`````
Best regards!!!

Author: Francisco Vélez