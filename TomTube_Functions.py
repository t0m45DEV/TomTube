import random
import pafy


niceanswers = ["I'm downloading your video...",
		"You can breathe in and out while i'm working.",
		"I found what you want to ilegally download."]

erroranswers = ["I can't work with that...",
		"That doesn't look like a youtube link to me...",
		"You have to write a youtube link, you know?"]


print("Please, write below the video link adress:\n")

link = input()


try:
	video = pafy.new(link)
	video.getbestaudio(preftype="m4a").download(filepath="/home/t0m45/Downloads", quiet=True)
	
	print(random.choice(niceanswers))


except ValueError or OSError:
	print("\n" + random.choice(erroranswers))


