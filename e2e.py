from selenium import webdriver

# app_url = input("Please enter the application URL: ")
app_url = 'http://localhost:8777/'


def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get(app_url)
    score = driver.find_element_by_id('score')
    if int(score.text) >= 0:
        if int(score.text) <= 1000:
            return True
    else:
        return False


def main():
    try:
        test_scores_service(app_url)
        return 0
    except:
        return -1


if __name__ == '__main__':
    print(main())
