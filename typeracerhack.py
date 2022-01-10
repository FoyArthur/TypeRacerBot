# Arthur Foy
# 2021
# Hack For Type Racer

def execute(link="https://play.typeracer.com/"):
    from selenium import webdriver
    from time import sleep
    from webdriver_manager.chrome import ChromeDriverManager

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])



    x = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if link == "":
        link = "https://play.typeracer.com/"
        
    x.get(link)


    WebDriverWait(x, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Join race"))).click()

    wait = WebDriverWait(x, 200)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.gameStatusLabel"), "The race is on! Type the text below:"))
    string = ""

    try: 
        z = x.find_element_by_xpath('//*[@id="gwt-uid-22"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]').text
        print("FOUND")
        string += z
        
    except:
        pass 

    try:
        y = x.find_element_by_xpath('//*[@id="gwt-uid-22"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]').text
        if string == "I" and len(y) > 3:
            string += " " + y
        else:
            string += y
    
    except:
        pass
    try: 
        xx = x.find_element_by_xpath('//*[@id="gwt-uid-22"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text
        string += (" " + xx)
    except:
        pass




    
    text = x.find_element_by_css_selector('input.txtInput')
    for i in string:
         for j in i:
            text.send_keys(j)

    text.send_keys(string)

    time.sleep(30)
    #x.close()

if __name__ == "__main__":
    execute()