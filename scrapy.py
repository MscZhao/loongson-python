import requests
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux loongarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 Safari/537.36"
}
ret = requests.get("https://www.loongson.cn", verify=False, headers=headers)
print(ret.text)