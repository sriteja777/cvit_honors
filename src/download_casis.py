import requests
import bs4
from humanize import naturalsize

sess = requests.session()
login_url = "http://biometrics.idealtest.org/public/user/index.jsp"
pg = sess.get(login_url)
sp  = bs4.BeautifulSoup(pg.text, 'lxml')

host = "http://biometrics.idealtest.org"
vc_url = host + sp.find('img', {'id': 'img'}).get('src')
img = sess.get(vc_url)

im_f = open('vc.jpeg', 'wb')

im_f.write(img.content)

im_f.close()

vc_code = input("String: ")
data = {"tblUserEmail": "sriteja.sugoor@students.iiit.ac.in", "tblUserPassword": "vit.2d.xy", "validateCode": vc_code}

p = sess.post("http://biometrics.idealtest.org/login.do", data=data)

head = sess.get("http://biometrics.idealtest.org/downloadDB.do?id=4",stream=True)

f=open('casis.zip','wb')

dld = 0
for chunk in head.iter_content(2048):
	if chunk:
		dld += f.write(chunk)
	print('\r', naturalsize(dld), dld,end='')

f.close()