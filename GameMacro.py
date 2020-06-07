from selenium import webdriver
driver = webdriver.Chrome('/Users/dudhk/OneDrive/바탕 화면/chromedriver_win32/chromedriver.exe')
driver.get('https://zzzscore.com/1to50/')

count = 1       # 50개의 숫자를 세기 위한 count
while count <= 50:
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[@*]')
    for btn in btns:
        if btn.text == str(count):  # 버튼의 text가 순서와 같다면
            btn.click()             # 해당 버튼을 누르고
            count += 1              # count를 증가시키고
            break                   # for문 탈출
