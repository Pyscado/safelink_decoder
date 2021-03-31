import urllib.parse
url = input("Enter SafeLink URL: ")
url = url.split("&data=04")
url = url[0]
url = url.lstrip("https://nam11.safelinks,protection.outlook.com/?")
url = url.lstrip("=")
url = urllib.parse.unquote(url)
print("\n",url,"\n")
url = url.replace(".", "[.]")
url = url.replace("http", "hxxp")
print(url, "\n")
input("Press ENTER to quit")