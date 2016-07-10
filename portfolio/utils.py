import xml.etree.ElementTree as ET
from random import randint

bad_words = ["beeyotch", "biatch", "bitch", "chinaman", "chinamen", "chink", "crip", "cunt", "dago", "daygo", "dego", "dick",  "douchebag", "dyke", "fag", "fatass","fatso", "fuck", "gash", "gimp", "golliwog", "gook", "gyp",  "homo", "hooker",  "jap", "kike", "kraut", "lame", "lardass", "lesbo", "negro", "nigga", "nigger", "paki", "pussy", "raghead", "retard",    "shemale", "skank", "slut", "spic", "spook", "tard", "tits", "titt", "trannies", "tranny", "twat", "wetback", "whore", "wop"]
image_links = ["https://www.dropbox.com/s/5e1stwwqmfhk4oa/Cat.png?raw=1", "https://www.dropbox.com/s/qyi8nl2qx4rk5wc/Cow.png?raw=1", "https://www.dropbox.com/s/hcktbevx049kiwx/Elephant.png?raw=1", "https://www.dropbox.com/s/jnaoc5epkh8s889/Fox.png?raw=1", "https://www.dropbox.com/s/8lq2660btjcagnq/Monkey.png?raw=1", "https://www.dropbox.com/s/jt5q6t42n0he672/Owl.png?raw=1", "https://www.dropbox.com/s/f4sahg3oyrnve7z/Sheep.png?raw=1"]
adjectives = ["Beige", "Blue", "Brown", "Dark", "Emerald", "Sapphire", "Magenta", "Maroon", "Purple", "Violet", "Lavender", "Gold"]
nouns = ["Apple", "Mango", "Watermelon", "Honeydew", "Pineapple", "Peach", "Plum", "Cherry", "Lychee"]

def filter_comment(comment):
	for i in bad_words:
		if comment.find(i)!=-1:
			comment = comment.replace(i, "---")
		if comment.find(i.capitalize())!=-1:
			comment = comment.replace(i.capitalize(), "---")
		if comment.find(i.upper())!=-1:
			comment = comment.replace(i.upper(), "---")
	return comment

def generate_profile_image():
	index = randint(0, len(image_links)-1)
	return image_links[index]

def generate_username():
	adj_index = randint(0, len(adjectives)-1)
	noun_index = randint(0, len(nouns)-1)
	return adjectives[adj_index] + " " + nouns[noun_index]
	# return random.sample(adjectives,1)[0]+" "+random.sample(nouns,1)[0]

def get_data():
		# Parse 'svn_log.xml'
	# logs = []    # A list of log entries as dictionaries
	# tree = ET.parse('svn_log.xml')
	# root = tree.getroot()

	# for child in root:
	# 	log_entry = {}
	# 	log_entry['revision'] = child.attrib['revision']
	# 	for grandchild in child:
	# 		if grandchild.tag == 'author':
	# 			log_entry['author'] = grandchild.text
	# 		elif grandchild.tag == 'msg':
	# 			log_entry['message'] = grandchild.text
	# 		elif grandchild.tag == 'date':
	# 			log_entry['date'] = grandchild.text
	# 		elif grandchild.tag == 'paths':
	# 			log_entry['paths'] = []
	# 			for path in grandchild:
	# 				path_dict = {}
	# 				path_dict['kind'] = path.attrib['kind']
	# 				path_dict['action'] = path.attrib['action']
	# 				path_dict['link'] = path.text
	# 				log_entry['paths'].append(path_dict)
	# 	logs.append(log_entry)
	# return logs

	lists = []	# A list of entries
	tree = ET.parse('svn_list.xml')
	root = tree.getroot()

	for child in root:
		for grandchild in child:
			entry = {}
			entry['kind'] = grandchild.attrib['kind']
			for item in grandchild:
				if item.tag == 'name':
					entry['name'] = item.text
				elif item.tag == 'size':
					entry['size'] = item.text
				elif item.tag == 'commit':
					entry['revision'] = item.attrib['revision']
					for subitem in item:
						if subitem.tag == 'author':
							entry['author'] = subitem.text
						elif subitem.tag == 'date':
							entry['date'] = subitem.text
			lists.append(entry)

	project_dict = {'Assignment0': {'files':dict(), 'version': None, 'date': None, 'title': "Getting Started", 'summary': "Uploading my codes"}, 
	'Assignment1': {'files':dict(), 'version': None, 'date': None, 'title': "Chess", 
	'summary': "Updating game interface"},
	'Assignment2': {'files':dict(), 'version': None, 'date': None, 'title': "CSAir", 'summary': "Adding editing route features"},
	'Assignment3': {'files':dict(), 'version': None, 'date': None, 'title': "Web Portfolio", 'summary': "Creating Assignment3 Folder"}}

	for item in lists:
		name = item['name'].split('/')
		if name[0].startswith('Assignment'):
			project_name = name[0][:11]
			file_name = name[-1]
			# file_dict = project_dict[project_name]['files']
			if file_name in project_dict[project_name]['files'] or 'size' not in item:
				pass
			else:
				project_dict[project_name]['files'][file_name] = {}
				project_dict[project_name]['files'][file_name]['size'] = item['size']
				project_dict[project_name]['files'][file_name]['author'] = item['author']
				project_dict[project_name]['files'][file_name]['revision'] = item['revision']
				project_dict[project_name]['files'][file_name]['date'] = item['date']
				# Set filetype
				if file_name.endswith('.java') or file_name.endswith('.py') or file_name.endswith('.swift'):
					project_dict[project_name]['files'][file_name]['type'] = 'code'
				elif file_name.endswith('.json'):
					project_dict[project_name]['files'][file_name]['type'] = 'data'
				elif file_name.endswith('.png') or file_name.endswith('.jpg'):
					project_dict[project_name]['files'][file_name]['type'] = 'image'
				else:
					project_dict[project_name]['files'][file_name]['type'] = 'others'
				#Update project information
				if not project_dict[project_name]['version'] or project_dict[project_name]['version']<item['revision']:
					project_dict[project_name]['version'] = item['revision']
					project_dict[project_name]['date'] = item['date']

	return project_dict