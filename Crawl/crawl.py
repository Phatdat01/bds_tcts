from crawling import open_web, login, access
def crawl():
    driver, cre = open_web()
    login(driver=driver,cre=cre)
    files = access(driver=driver, cre= cre)
    print(files)
    driver.quit()
crawl()