import requests

def get_horoscope(sign):
	url = f"https://ohmanda.com/api/horoscope/{sign}" 
	response = requests.get(url)
	result = response.json()
	    
	 # import pdb; pdb.set_trace()
	return result
print('VAMOS VER O QUE OS ASTROS TEM A DIZER HOJE?')
sign = input('Qual o seu signo?')

print(get_horoscope(sign))

    	
