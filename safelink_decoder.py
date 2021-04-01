import urllib.parse
url = input("Enter SafeLink URL: ")
index = url.find("?url=")
url = url[index:].lstrip("?url=")
index = url.find("&data=04%C01%7C")
url = url[:index]
url = urllib.parse.unquote(url)
print("\n",url,"\n")
url = url.replace(".", "[.]")
url = url.replace("http", "hxxp")
print(url.lstrip("k[.]com/?url="), "\n")
input("Press ENTER to quit")
