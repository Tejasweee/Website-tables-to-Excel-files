import os
import sys
import subprocess
import urllib.request

try:
    import pandas as pd
except:
    subprocess.call([sys.executable, "-m", "pip", "install", 'pandas'])
finally:
    import pandas as pd

def extractor(sites):
    '''Extract tables from a single or a list of urls or html filenames passed.'''
    if_file=os.getcwd()
    os.makedirs('SiteToExcel', exist_ok=True)
    os.chdir('SiteToExcel')
    return_dir= os.getcwd()
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"}

    for i in range(len(sites)):
        site = sites[i].strip()
        isAFile=False

        if (len(site.split('.'))==2) and ('.html' in site):
            isAFile=True
            os.chdir(if_file)
            try:
                with open(site, 'r', encoding='utf8') as f:
                    content= f.read()
            except Exception as e:
                print(e)
                print('Place file: ' + site + ' in ' + os.getcwd())
        
        if len(site.split('//'))>1:
            fname = site.split('//')[1]
        else:
            fname = site
            site = 'http://'+site
        
        print('Extracting tables from: ' + site)
        
        try:
            if isAFile==False:
                req=urllib.request.Request(site, headers=header)
                content = urllib.request.urlopen(req).read()
                df1= pd.read_html(content)
            else:
                df1= pd.read_html(content)
        except Exception as e:
            df1=[]
            print(e)
            
        os.chdir(return_dir)
        os.makedirs(fname, exist_ok=True)
        os.chdir(fname)
        os.makedirs('CSV', exist_ok=True)

        j=0
        for j in range(len(df1)):
            filename= 'Table'+ str(j+1) + '.xlsx'
            df1[j].to_excel(filename)
            print(filename, 'extracted...')
        print(str(j) + ' xlsx tables extraced from ' + site+ ' at '+ os.getcwd())
        
        os.chdir('CSV')
        for j in range(len(df1)):
            csvfile = 'Csv' + str(j+1) + '.csv'
            df1[j].to_csv(csvfile)
            print(csvfile, 'extracted...')

    
if len(sys.argv)>1:
    sites = sys.argv[1:]
else:
    print('Enter URL (you can also pass list of urls using comma as seperator) OR You can also give filename of htmlfile: ' )
    sites=input()
    sites= sites.split(',')

if __name__ == '__main__':
    extractor(sites)
