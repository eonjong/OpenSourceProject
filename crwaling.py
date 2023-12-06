from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By


class CRAWLING:
    def __init__(self) -> None:
        self.init_driver()

    def init_driver(self):
        self.chrome_service = Service(ChromeDriverManager().install())
        self.driver = None

    def main(self):
        self.driver = webdriver.Chrome(service=self.chrome_service)
        self.driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%A0%84%EB%82%A8%EB%8C%80")
       
    def search(self, breed) :
        s_input = self.driver.find_element(By.XPATH, "//input[@id='nx_query']")
        s_input.clear()

        if breed == 'cat-Abyssinian' :
            s_input.send_keys("아비니시안 고양이")
        elif breed == 'cat-Bengal' :
            s_input.send_keys("벵갈 고양이")
        elif breed == 'cat-Birman' :
            s_input.send_keys("버먼 고양이")
        elif breed == 'cat-Bombay' :
            s_input.send_keys("봄베이 고양이")
        elif breed == 'cat-British_Shorthair' :
            s_input.send_keys("브리티시 쇼트헤어 고양이")
        elif breed == 'cat-Egyptian_Mau' :
            s_input.send_keys("이집션 마우 고양이")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        elif breed == '3' :
            s_input.send_keys("3")
        
        else :
            print("검색할 수 없는 품종입니다.")
            return

        s_input.send_keys(Keys.ENTER)
        news_titles = self.driver.find_elements(By.XPATH, "//a[@class='news_tit']")
        for index, value in enumerate(news_titles):
            print(f"{index+1} : {value.text} [link : {value.get_attribute('href')}]")
            if index == 4:
                break
        pass
    


    




if __name__ == "__main__":
    c = CRAWLING()
    c.main()
    #while True:    #반복문 사용하려면 input~~ 줄과 c.search~~줄을 while문에 맞출 것
    input_data = input("원하는 품종을 입력해 주세요. : ")
    c.search(input_data)
