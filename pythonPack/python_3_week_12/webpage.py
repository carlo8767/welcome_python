# Import the urllib.request module
import urllib.request

def main():
	url = "https://google.com"
    # Open a connection to google.com
	req = urllib.request.urlopen(url)
    # Download the webpage's contents
	response = req.read().decode(errors='ignore')

	print(response)

main()
