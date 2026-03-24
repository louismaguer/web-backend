import requests

response = requests.get("https://api64.ipify.org?format=json")
public_ip = response.json()["ip"]

print("Public IP:", public_ip)
