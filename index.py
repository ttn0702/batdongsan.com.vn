from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from File_Class import *

list_data = File_Interact('config.txt').read_file_list()
so_trang = int(list_data[0].split('=')[-1])
print('so_trang: ',so_trang)

list_title = []
list_phone = []
list_price = []
list_content = []
list_link = []

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)

for index in range(1,so_trang+1):
    url = 'https://batdongsan.com.vn/nha-dat-cho-thue-go-vap'
    if index > 1:
        url = f'{url}/p{index}'
    driver.get(url)
    
    try:
        WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="re__main-content"]')))
    except:
        try:
            WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3[class="re__card-title"]')))
        except:
            pass
    js = '''return document.querySelectorAll('h3[class="re__card-title"]').length'''
    len_job = driver.execute_script(js)

    for i in range(len_job):
        #get title
        try:
            js_title = f'''return document.querySelectorAll('h3[class="re__card-title"]')[{i}].innerText'''
            title = driver.execute_script(js_title)
        except:
            title = ''
        list_title.append(title)
        # get phone 
        try:
            js_phone = f'''return document.querySelectorAll('h3[class="re__card-title"]')[{i}].querySelectorAll('span')[1].getAttribute('raw')'''
            phone = driver.execute_script(js_phone)
        except:
            #cach 2
            # document.querySelectorAll('div[class="re__card-contact-button"]')[3].querySelectorAll('span')[0].getAttribute('raw')
            try:
                js_phone = f'''return document.querySelectorAll('div[class="re__card-contact-button"]')[{i}].querySelectorAll('span')[0].getAttribute('raw')'''
                phone = driver.execute_script(js_phone)
            except:
                phone = ''
        list_phone.append(phone)

        #get price
        try:
            js_price = f'''return document.querySelectorAll('span[class="re__card-config-price"]')[{i}].innerText'''
            price = driver.execute_script(js_price)
        except:
            price = ''
        list_price.append(price)

        # get content
        try:
            js_content = f'''return document.querySelectorAll('div[class="re__card-description js__card-description"]')[{i}].innerText'''
            content = driver.execute_script(js_content)
        except:
            content = ''
        list_content.append(content)

        # link
        try:
            js_link = f'''return document.querySelectorAll('a[class="js__product-link-for-product-id"]')[{i}].href'''
            link = driver.execute_script(js_link)
        except:
            link = ''
        list_link.append(link)
driver.quit()

File_Excel1 = File_Excel('data.xlsx')
sheet_name = 'Sheet1'
File_Excel1.update_cell(sheet_name,'A1','STT')
File_Excel1.update_cell(sheet_name,'B1',"Title")
File_Excel1.update_cell(sheet_name,'C1',"Số Điện Thoại")
File_Excel1.update_cell(sheet_name,'D1',"Giá")
File_Excel1.update_cell(sheet_name,'E1',"Nội Dung")
File_Excel1.update_cell(sheet_name,'F1',"Link")

for index in range(len(list_title)):
    stt = index+1
    title = list_title[index]
    phone = list_phone[index]
    price = list_price[index]
    content = list_content[index]
    link = list_link[index]

    cell_name_stt ="A%s"%(index+2)
    cell_name_title ="B%s"%(index+2)
    cell_name_phone ="C%s"%(index+2)
    cell_name_price ="D%s"%(index+2)
    cell_name_content ="E%s"%(index+2)
    cell_name_link ="F%s"%(index+2)

    File_Excel1.update_cell(sheet_name,cell_name_stt,stt)
    File_Excel1.update_cell(sheet_name,cell_name_title,title)
    File_Excel1.update_cell(sheet_name,cell_name_phone,phone)
    File_Excel1.update_cell(sheet_name,cell_name_price,price)
    File_Excel1.update_cell(sheet_name,cell_name_content,content)
    File_Excel1.update_cell(sheet_name,cell_name_link,link)

print('===========================================================')
print('                     ĐÃ CHẠY XONG')
print('===========================================================')