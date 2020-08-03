# Combat Log Parser

# Requires 

 - python3

 - pandas


# Installation
Clone or download the zip file by clicking the "Code" button near the top of the page.
```bash

python -m pip install pandas
```

# Usage
use the following command 
```bash
python parse.py -path C:\\\path\\to\\your\\log\\file
```

The default location of this log file is near your interface/addons on a path like this:
"C:\\Program Files (x86)\World of Warcraft\_classic_\Logs\WoWCombatLog.txt"

You can also just put the log file in the same directory as this file and simply call

```bash
python parse.py -path ./WoWCombatLogs.txt
```

or whatever the name of your file is.

This outputs two files called `wbuffs.txt` and `consumes.txt`

You should have no problems loading them int excel or google sheets.


If you want to add more types of consumes or buffs to the list, you need to edit the parse.py 
and add in the names you want. There are comments there to help guide you!


# Test

If you want to use the test file located in the test/ folder, you can use the following command:

```bash
python parse.py -path ./test/WoWCombatLog.txt
```

Good Will Hunting!

