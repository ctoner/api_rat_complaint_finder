#                               
#                        ,d     
#                        88     
#8b,dPPYba, ,adPPYYba, MM88MMM  
#88P'   "Y8 ""     `Y8   88     
#88         ,adPPPPP88   88     
#88         88,    ,88   88,    
#88         `"8bbdP"Y8   "Y888  
                               

import requests
import json
import os
import sys

# enter get() information

url = "http://311api.cityofchicago.org/open311/v2/requests.json"

#maximize the results per page, begin at page 1 on the API. page 0 repeats the same information as page 1

pageload = {'page_size': '500', 'page': 1}

headers = {'Accept': 'application/vnd.github.v3+json'}

rats = []

exist = False

# create loop that goes until a specified page in the API

print("Scanning for rat complaints...")
print("Looping through the API...\n")
while pageload['page'] < 51:
	response = requests.get(url, headers=headers, params=pageload)
	response_dict = response.json()

# isolate loop for rats
	for r in response_dict:
		if r['service_name'] == 'Rodent Baiting/Rat Complaint':
			rat = r
			rats.append(rat)
			rat_count = len(rats)

#show pagination
	print(f"\t----> Page loop: {pageload['page']}. {rat_count} …ᘛ⁐̤ᕐᐷ complaints found!")
		
#paginate by 1
	pageload['page'] += 1



#dump data into file if file is blank
readable_file = 'chicago_api_rats.jsonl'
with open(readable_file, 'a') as file:
	# If the file is empty
	if os.path.getsize(readable_file) == 0:
		print(f"\nNo existing file found. Creating new file with {rat_count} rat complaints!")
		for rat in rats:
			json_line = json.dumps(rat)
			file.write(json_line + '\n')
	else:
		print("\nExisting file found! Checking for new complaints.\n")
		#create trigger to cue next segment
		exist = True

#check if complaint exists, if so, load file, isolate service request ids

if exist:
	new_complaints = []
	rq_id = []
	with open(readable_file, 'r') as f:
		for line in f:
			existing_file = json.loads(line)
			request_id = existing_file.get('service_request_id')
			rq_id.append(request_id)

#filter dictionary by the list
	new_complaints = [d for d in rats if d['service_request_id'] not in rq_id]
	num_new_complaints = len(new_complaints)

#create language variable to differentiate 'one complaint identified' vs 'five complaints identified'

	if num_new_complaints == 1:
		lang_var = 'complaint'
	else:
		lang_var = 'complaints'
	
	print(f"{num_new_complaints} new rat {lang_var} identified.\n")

#kill switch if there are no complaints
	if not new_complaints:
		print("No new complaints were found, program shutting down.")
		exist = False


#identify that new_complaints has data in it
if exist:
#then write to file
	if len(new_complaints) != 0:
		with open(readable_file, 'a') as f:
			for new_complaint in new_complaints:
				json_line = json.dumps(new_complaint)
				f.write(json_line + '\n')
			print(f"New {lang_var} added successfully!")

