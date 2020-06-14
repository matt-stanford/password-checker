import requests
import hashlib
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    context = {}
    return render(request, 'index.html', context)

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	return get_password_leaks_count(response, tail)

def password_check(request):
    if request.method == 'POST':
        password = request.POST['password']
        count = pwned_api_check(password)
        if count:
            message = f'{password} has been seen {count} times before!'
        else:
            message = f'{password} was NOT found :)'
        messages.success(request, message)
        return redirect('index')