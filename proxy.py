import requests

# Your proxy settings
proxy = {
    "http": "http://38.55.73.47:31280"
}

# Make a request using the proxy
try:
    response = requests.get("http://httpbin.org/ip", proxies=proxy, timeout=10)
    if response.status_code == 200:
        print("Proxy is working!")
        print("Response:", response.json())
    else:
        print(f"Failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
