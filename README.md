## What it is
### This project consists of basically a single python script to write the status of the São Paulo subway lines to a docs.google worksheet.

The sheet can be viewed (and freely used for any datascience project) (https://docs.google.com/spreadsheets/d/19vBtt1j64Au01vJaVjyiNB5CiCqSlG7juUc6_VSALbg/edit?usp=sharing)[here].

## How it works

Every 5 minutes the script fetches [the official subway company page](http://www.viaquatro.com.br/) using 'requests' module and extracts the operation status as shown in the column on the right-side of the page using 'beautiful soup' module. The last-update time shown is also stored and later on is associated with each subwat line.

Once everything is properly parsed, the information is stored in the worksheet using the 'gspread' module.

The script runs indefinately on [heroku](http://www.heroku.com).

## Unkown variables:

I am not sure what will be shown in the website when line 4 (yellow / amarela) status is not normal. Some pre-processing may be required, as the scraper.py script does not try to match the yellow line status with the status from the other ones. Check values for 'amarela' line.

## If this data is ever useful to you, let me know. Enjoy! 🍻