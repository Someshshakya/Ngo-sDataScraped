from pprint import pprint 
import csv
from csv import writer
from bs4 import BeautifulSoup
import requests,time,json,random ,os
g=open("ss.csv","w+")
si=writer(g)
si.writerow(["name","Email id","contact","url","Addres"])
def ngo():
	if os.path.exists("ngo.json"):
		# print("data	 from the json file")
		with open("ngo.json") as data:
			read_file = data.read()
			url_list = json.loads(read_file)
			data.close()
			return url_list
	else:
		# print("data from the web")
		page = requests.get("https://www.endslaverynow.org/connect?country=3353#filter")
		soup = BeautifulSoup(page.text,"html.parser")
		table = soup.find("table",id="responsiveTable")
		a = table.find_all("a")
		url_list = []
		for d in a:
			random_time = random.randint(1,3)
			time.sleep(random_time)
			url1 = "https://www.endslaverynow.org"+str(d["href"])
			url_list.append(url1)

		with open("ngo.json","w+") as data:
			dum = json.dumps(url_list)
			data.write(dum)
			data.close()
			return url_list

# pprint(ngo())

def detail(link):
	page = requests.get(link)
	soup = BeautifulSoup(page.text,"html.parser")
	dic_of_detail = {"name":""}

	data = soup.find("div",class_="right")
	# name 
	name = data.find("h2").get_text()
	dic_of_detail["name"] = name

	# link of the website
	url9 = data.find("a")["href"]
	dic_of_detail["url"] = url9
	# number
	data2 = soup.find("div",class_="left")
	span = data2.find_all("li",class_="")
	Email = 'No Email'
	cont = "No contact"
	for i in span:
		if "Tel:" in i.get_text().strip():
			cont = i.get_text().strip()[5:]
			dic_of_detail["contact_no. "] = cont
		if "Email:" in i.get_text().strip():
			Email = i.get_text().strip()[8:]
			dic_of_detail["Emai_id"] = Email

	ad = data2.find_all("ul",class_="")

	s = ad[0].get_text().strip()

	f=s[20:].strip()
	print(Email) 	
	si.writerow([name,Email,cont,url9,f])
	return dic_of_detail

# pprint(detail("https://www.endslaverynow.org/national-domestic-workers-movement"))

	
a = ngo()
for i in a:
	a = detail(i)
	pprint(a)

	


