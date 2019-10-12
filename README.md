# Site-to-Excel
This script allows to pass urls or html files and it extracts tables from html contents and saves them as Excel files and CSV files in .xlsx and .csv format.

# Using the Script:
- From Command Line Argument:
python site2excel.py, url
python site2excel.py, url1, url2, url3....

python site2excel.py, afile.html
python site2excel.py, afile1.html, afile2.html, afile3.html...

- Passing argument after running the script:
python site2excel.py
-- Now arguments can be passed in the input prompt

This script needs 'pandas' library to run. If pandas library is not installed this script will automatically try to install pandas first using pip.
