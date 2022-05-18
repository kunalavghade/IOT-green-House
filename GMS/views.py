from django.shortcuts import render
import requests
from json import dumps

def index(request):

	data = requests.get("https://api.thingspeak.com/channels/1699059/feeds.json?api_key=8J0UBF269PG0OSKH&results=10")
	data = data.json()

	hue = []
	moist = []
	tmp = []
	x = []
	count = 0

	for i in data['feeds']:
		x.append(str(count))
		hue.append(int(i['field1']))
		moist.append(int(i['field2']))
		tmp.append(int(i['field3']))
		count+=1

	data = {
		'hue' : hue,
		'moist' : moist,
		"tmp" : tmp,
		'x' : x
	}

	print(data)

	data = dumps(data)

	if request.method == "POST":
		if request.POST['btn'] == "OFF":
			requests.post(f'https://api.thingspeak.com/update?api_key=6UZ2I520Z4TJB1EK&field1={hue[-1]}&field2={moist[-1]}&field3={tmp[-1]}&field4=0')
		else:
			requests.post(f'https://api.thingspeak.com/update?api_key=6UZ2I520Z4TJB1EK&field1={hue[-1]}&field2={moist[-1]}&field3={tmp[-1]}&field4=1')	

	return render(request,'index.html',{'data':data})