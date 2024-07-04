"""
Checks password leak count using api call to pwned
"""
import hashlib
import sys
import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    return response


def get_password_leaks_count(hashes, hash_to_check):
    # splits hash & cnt form the recieved text dataset obj
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1[:5], sha1[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. Please change to a stonger one.')
        else:
            print(f'{password} was never leaked. Great! ')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
