def a():
	import requests

	headers = {
	    'Authorization': 'Bearer N5YCDHEO7WS2YCXMNN4RY6ELE6P4X75M',
	}

	params = (
	    ('v', '20190210'),
	    ('q', 'hello'),
	)

	response = requests.get('https://api.wit.ai/message', headers=headers, params=params)

	#NB. Original query string below. It seems impossible to parse and
	#reproduce query strings 100% accurately so the one below is given
	#in case the reproduced version is not "correct".
	# response = requests.get('https://api.wit.ai/message?v=20190210&q=temp', headers=headers)
	return (response.json()["entities"]["intent"][0]["value"])