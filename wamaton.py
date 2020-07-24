from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
while True:
	driver.get('https://web.whatsapp.com/')
	name=input('User to send: ')
	msg=input('Message to send: ')
	n=int(input('Enter no of repeatations: '))
	input('')
	user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#print(str(user))
#actions=ActionChains(driver)
#actions.click(user).perform()
	user.click()
#else:
#	print('No such elements')
#print(len(user))
	msgbox=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
	for i in range(n):
		print(str(i+1))
		msgbox.send_keys(msg)
		button=driver.find_element_by_class_name('_1U1xa')
		button.click()