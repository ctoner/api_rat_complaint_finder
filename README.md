# api_rat_complaint_finder
Grab rat complaints off Chicago's 311 API

This program grabs rat complaints off Chicago's API and writes them to a Jsonline file, showing users how many complaints are grabbed as each page in the API loops through.

If no Jsonline file exists, the program will create one with the identified complaints. New complaints pulled off the API will check against what's already in the Jsonfile and amend the file with only new items.

**api_rat_complaint_finder.py** - the program

**chicago_api_rats.jsonl** - Jsonline file containing rat complaints from the first 50 pages of the Chicago 311 API, as of 5:22 p.m. on 2024-09-17.
