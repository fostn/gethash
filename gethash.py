import os
try:
	import requests
except ModuleNotFoundError:
	os.system("pip install requests")
print("""
 +-+-+-+-+-+-+-+
 |g|e|t|h|a|s|h|
 +-+-+-+-+-+-+-+
#hashtags generator
    iG : f09l
""")
print("-"*40)
print("enter keyword to create hashtags\nfor example : code ")
print("-"*40)
keyword = input("enter keyword : ")

url = f"http://hashmeapi-stage.us-west-2.elasticbeanstalk.com/search?q={keyword}"
r = requests.get(url)
hashtags = r.json()
if len(hashtags) > 1:
	print("-"*40)
	for i in range(len(hashtags)):
		if hashtags[i] == "HashmeApp":
			hashtags[i] = "f09l"
		print(f"#{hashtags[i]}")
	print("-"*40)
	save = input("Save hashtags y/n : ")
	if save == "y":
		for i in range(len(hashtags)):
			hash = hashtags[i]
			with open("gethash.txt","a") as f:
				f.write(f"#{hash}"+"\n")
		print("file saved as gethash.txt")
else:
	print("try another keyword #f09l")
