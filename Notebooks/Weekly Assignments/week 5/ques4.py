import sys
import urllib.request
import urllib.error

if len(sys.argv) < 2:
    print("Error: No URL provided")
    sys.exit()

url = sys.argv[1]

try:
    response = urllib.request.urlopen(url)
    print("Website is working. Status code:", response.status)
except urllib.error.URLError:
    print("Website is not reachable")
