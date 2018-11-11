# Cannabis Family Tree
A family-tree-style data visualization of cannabis strain lineage with accompanying information. Made by Michael 
Wheeler for BostonHacks 2018.

## To set up the virtualenv:
1. `pip install virtualenvwrapper`
2. `mkvirtualenv --python=python3.6 cannabisfamilytree`
3. `workon cannabisfamilytree`
4. `python -m pip install -f requirements.txt`
5. `deactivate  (to exit virtualenv)`

## To run the web scraper:
1. `workon cannabisfamilytree`
2. `scrapy crawl scrape-leafly`