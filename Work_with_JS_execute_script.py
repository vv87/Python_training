from selenium import webdriver
browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';")
# browser.execute_script("alert('Robots at work');")
# browser.execute_script('document.title="Script executing";')
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
#  заставить браузер дополнительно проскролить нужный элемент, чтобы он точно стал видимым:
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
# появится ошибка (из-за того что точка клика перекрыта другим окном (блоком), при отсутствии скрипта: browser.execute_script("return arguments[0].scrollIntoView(true);", button)
assert True
