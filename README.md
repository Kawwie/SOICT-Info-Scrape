- Database result is written inside db.sqlite
- Docx outputs are are written inside /output

To run the program
- Scrape data from Soict
```
scrapy crawl soict
```
- Scrape data from GoogleScholar
```
scrapy crawl GS
```
- To test the program on one one profile, without writing to database
```
scrapy crawl test
```
- This test output is a docx file and will be written into /testoutput