#!/usr/bin/env python3

import subprocess, sys, json, re


d = json.load(subprocess.Popen([
	"youtube-dl",
	"https://www.youtube.com/playlist?list=PLfu8OwqMlN0T1kSHj3WKwK2H6iDQXUJQU",
	"--playlist-reverse",
	"--playlist-items", "1-12",
	"-J"
], universal_newlines=True, stdout=subprocess.PIPE).stdout)

all_videos = []

for month in d["entries"]:
	monthabbr = month["title"].split(" ")[6][:3]
	
	m = re.search("(https://www.youtube.com/playlist\\?list=.+?)\\s", month["description"])
	monthplaylist = m.group(1)
	
	monthd = json.load(subprocess.Popen([
		"youtube-dl",
		"--playlist-items", "1-10",
		monthplaylist,
		"-J"
	], universal_newlines=True, stdout=subprocess.PIPE).stdout)
	
	for i,video in enumerate(monthd["entries"]):
		print('<a href="%s">%s</a> by %s (%s #%d)' % (
			video["webpage_url"],
			video["title"],
			video["uploader"],
			monthabbr,
			(i+1),
		))
	
