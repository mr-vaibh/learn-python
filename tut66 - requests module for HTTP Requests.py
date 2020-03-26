import requests

'''Creating simple GET request'''
# r = requests.get('https://mrvaibh.herokuapp.com')
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")

print(r)
print(r.text)
print(r.status_code)

'''Creating simple POST request'''
url = 'http://dummy.restapiexample.com/api/v1/create'
data = {
    'name': 'test',
    'salary': '123',
    'age': '23',
}
r = requests.post(url=url, data=data)
print(r)
print(r.text)
print(r.status_code)