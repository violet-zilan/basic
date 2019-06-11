#coding = gbk
import urllib.request
import re
def save_file(file_name,txt):
	with open(file_name, 'a') as f:
		f.write("\n"+txt+"\n")
		f.write('------------------------------------------------')
		f.close()
def getHtml(url):
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	headers = {'User_Agent':user_agent}
	req = urllib.request.Request(url,headers = headers)
	page = urllib.request.urlopen(url)
	html = page.read()
	return html
html = getHtml("https://www.qiushibaike.com/text/") 
print(html)
