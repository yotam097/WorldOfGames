from selenium import webdriver
import docker

# Defining app_url as Score's Web URL
app_url = 'http://192.168.99.100:8777/'


# A test function that validates if the element "score" exists,and if it's between 0 to 1000
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


# A test function that validates if MySQL service is up
def test_mysql_service():
    try:
        client = docker.from_env()
        for container in client.containers.list():
            container_list = str(container.image)
            if 'mysql:5.7' in container_list:
                return "MySQL service is fully up"
            else:
                return "NO"
    except Exception as e:
        return "MySQL is not running", e


# Main function that runs the test's function and checks if failed or succeeded
def main():
    print(test_mysql_service())
    try:
        test_scores_service(app_url)
        print(0)
    except Exception as e:
        print(-1, e)


if __name__ == '__main__':
    main()
