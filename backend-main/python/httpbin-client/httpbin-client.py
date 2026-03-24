import requests

input(" -- press return to send request get")
get_out = requests.get("http://httpbin.org/get")
print( get_out.content.decode())

input(" -- press return to send request get with parameters a and b")
get_out = requests.get("http://httpbin.org/get?a=10&b=100")
print( get_out.content.decode())

input(" -- press return to send request post - payload is a dict with 'name' and 'mail' keys")
post_out = requests.post(
    "http://httpbin.org/post", 
    data={"name": "Basile Marchand", "mail": "basile.marchand@mines-paristech.fr"})
print(post_out.content.decode())


input(" -- press return to send request delete")
delete_out = requests.delete("http://httpbin.org/delete")
print(delete_out.content.decode())