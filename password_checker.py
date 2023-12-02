import requests
import hashlib
import sys



def request_api_data (query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching {res.status_code}, check the api and try again')
	return res

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5] , sha1password[5:]
	response = request_api_data(first5_char).text
	return get_password_leaks_count( response, tail)
	

def get_password_leaks_count(hash, hash_to_check):
	hashlist = hash.splitlines()
	for i in hashlist :
		hashcode = i.split(':')[0]
		hashnumber = i.split (':')[1]
		if hashcode == hash_to_check:
			print ("This password leaked to internet " + hashnumber + " times")
			return 0
	print ('no match')
	
while True:
	pwned_api_check(input ("\nwrite the password\n"))


