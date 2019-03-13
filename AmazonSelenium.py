from selenium import webdriver
import time
mail="mail@mail.com"
mailPassword="yourpassword"


driver=webdriver.Chrome("C:\\Python\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
#driver.fullscreen_window()
driver.get("https://www.amazon.com")

if "Amazon" in driver.title:
    print("Home page loaded successfully")
else:
    print("error: homepage was not loaded")

driver.find_element_by_id("nav-link-accountList").click()
driver.find_element_by_id("ap_email").send_keys(mail)
driver.find_element_by_id("ap_password").send_keys(mailPassword)
driver.find_element_by_id("signInSubmit").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung")

driver.find_element_by_id("twotabsearchtextbox").send_keys(u'\ue007')# search butonun id'sini bulamadım ve enter tuşuna basar gibi eventi gönderdim
i=0
for elem in driver.find_elements_by_class_name("a-text-normal"):
    if "Samsung" in elem.text:# eğer sonuçlar içerisinde en az 2 tane Samsung texti varsa sonuçlar doğru listelenmiştir
        i+=1
    if i>1:
        print("search result is correct")
        break
if i<2:
    print("search result failed")

driver.find_element_by_class_name("a-pagination").find_element_by_link_text("2").click()

if "page=2" in str(driver.current_url):#eğer 2. sayfadaysa url içinde page=2 vardır
    print("you are in 2. result page")

driver.find_element_by_xpath("//span[@data-component-type='s-search-results']/div[1]/div[3]").find_element_by_tag_name("a").click()

driver.find_element_by_id("add-to-wishlist-button-submit").click()
while 1<2:
    time.sleep(1)
    if driver.find_element_by_id("WLHUC_viewlist")!=None:
        break
driver.find_element_by_id("WLHUC_viewlist").click()
while 1<2:
    time.sleep(1)
    if driver.find_element_by_id("g-items")!=None:
        break
wishListCount=len(driver.find_element_by_id("g-items").find_elements_by_tag_name("li"))
print("there are " +str(wishListCount)+" elemnt(s) in your wishlist")

driver.find_element_by_id("g-items").find_element_by_tag_name("li").find_element_by_link_text("Delete item").click()
while 1<2:
    time.sleep(1)
    if driver.find_element_by_id("g-items").find_element_by_link_text("Undo")!=None:
        print("item was deleted successfully")
        break
