def readable(name,*args):
    name_clear = name.__name__.capitalize().replace("_"," ")
    sum=""
    for arg in args:
        sum=sum+arg+" "
    print(f"{name_clear} {sum}")


def open_browser(browser_name):
    readable(open_browser, browser_name)

def go_to_company_name_homepage(page_url):
    readable(go_to_company_name_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    readable(find_registration_button_on_login_page, page_url, button_text)

open_browser("Chrome")
go_to_company_name_homepage("https://www.youtube.com/")
find_registration_button_on_login_page("https://www.youtube.com/", "SIGN IN")



