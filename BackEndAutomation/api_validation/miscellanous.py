import requests

# httpbin.org

url = 'https://rahulshettyacademy.com'
cookie_visit = {'visit-month': 'November'}
response = requests.get(url, allow_redirects=False, cookies=cookie_visit, timeout=1)
print(response.history)     # To check redirection status_code=301
print(response.status_code)



se = requests.session()
se.cookies.update({'visit-month': 'November'})

response2 = se.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(response2.headers)
print(response2.cookies)
print(response2.text)