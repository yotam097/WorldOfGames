from selenium import webdriver

# Defining app_url as Score's Web URL
# app_url = input("Please enter the application URL: ")
app_url = 'http://localhost:8777/'


# A test function that validates if the element "score" exists,and if it's between 0 to 1000
def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get(app_url)
    score = driver.find_element_by_id('score')
    if int(score) >= 0 and int(score) <= 1000:
        return True
    else:
        return False


# Main function that runs the test's function and checks if failed or succeeded
def main():
    try:
        test_scores_service(app_url)
        return 0
    except Exception as e:
        print(e)
        return -1


if __name__ == '__main__':
    print(main())
