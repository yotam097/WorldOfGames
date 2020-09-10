from selenium import webdriver

app_url = input("Please enter the application URL: ")


def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(app_url)
    score = driver.find_element_by_id('score')
    if 0 >= score <= 1000:
        return True
    else:
        return False


def main():
    try:
        test_scores_service(app_url)
        print(0)
    except:
        print(-1)


if __name__ == '__main__':
    main()
