from selenium import webdriver
import pprint,os,json,time

a=webdriver.Chrome('chromedriver_linux64/chromedriver')
main_list=[]
def zomato_details():
	for page in range(1,10):
		a.get(f'https://www.zomato.com/ncr/restaurants?page={page}')
		hotels_list=[]
		address_list=[]
		main_div=a.find_elements_by_xpath("//div[@class='card  search-snippet-card     search-card  ']")

		details={}

		hotel_name=a.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
		for name in hotel_name:
			hotels_list.append(name.text)

		address=a.find_elements_by_xpath("//div[@class='col-m-16 search-result-address grey-text nowrap ln22']")
		for i in address:
			address_list.append(i.text)


		name_of=0
		for each_div in main_div:
			details={"hotel_name":"","address":"","cuisines_available":"","cost_per_two":"","timing":"","feautred_in":""}

			details["hotel_name"]=hotels_list[name_of]
			details["address"]=address_list[name_of]
			name_of+=1
			lists=(each_div.text).split("\n")
			if 'HOURS:' in lists:
				j=0
				for i in lists:
					j+=1
					if i=='HOURS:':
						break
				details["timing"]=lists[j]

			if 'FEATURED IN:' in lists:
				j=0
				for i in lists:
					j+=1
					if i=='FEATURED IN:':
						break
				details["feautred_in"]=lists[j].split(",")

			if 'COST FOR TWO:' in lists:
				j=0
				for i in lists:
					j+=1
					if i=='COST FOR TWO:':
						break
				details["cost_per_two"]=lists[j]

			if 'CUISINES:' in lists:
				j=0
				for i in lists:
					j+=1
					if i=='CUISINES:':
						break
				details["cuisines_available"]=lists[j].split(",")
			main_list.append(details.copy())
	return main_list



python_data=zomato_details()
if os.path.exists("zomato_details.json"):
	pass
else:
	with open("zomato_details.json","w+") as naik:
		json_data=json.dump(python_data,naik,indent=2) 