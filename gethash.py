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
keyword = input("enter keyword to create hashtags : ")
url = f"http://hashmeapi-stage.us-west-2.elasticbeanstalk.com/search?q={keyword}"
r = requests.get(url)
hashtags = r.json()
if len(hashtags) > 1:
	print(len(hashtags))
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
			with open("ATAGS.txt","a") as f:
				f.write(f"#{hash}"+"\n")
else:
	print("try another keyword #f09l")
