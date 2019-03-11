## What it is
### This project consists of basically a single python script to write the status of the São Paulo subway lines to a docs.google worksheet.

The sheets can be viewed (and freely used for any datascience project) [here](https://drive.google.com/open?id=1vXVWAJHnpvW9UaNSybqdEPZ8EaXIVYGF).

## How it works

Every 5 minutes the script fetches [the official subway company page](http://www.viaquatro.com.br/) using 'requests' module and extracts the operation status as shown in the column on the right-side of the page using 'beautiful soup' module. The last-update time shown is also stored and later on is associated with each subwat line.

Once everything is properly parsed, the information is stored in the worksheet using the 'gspread' module.

The script runs indefinately on [heroku](http://www.heroku.com).

## Unavailability or other issues

If for some reason the data points registered are empty, an e-mail is sent with the page attached so I can see the page and if necessary the logs to find out what happend.

**If this data is ever useful to you, let me know. Enjoy!**
🍻

## Data Analysis
An analysis of the data was made by [Paulo](https://github.com/pmhaddad)! You can read it [here](https://github.com/pmhaddad/ds_subway_analysis/blob/master/subway_analysis.md)
