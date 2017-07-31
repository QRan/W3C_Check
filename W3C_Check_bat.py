import requests
import os
from bs4 import BeautifulSoup


def w3c_check(check_file):
    url = 'https://validator.w3.org/check'
    post_files = {
        'fragment': (None, open(check_file, encoding='utf-8')),
        'prefill': (None, '0'), 'doctype': (None, 'Inline'), 'prefill_doctype': (None, 'html401'),
        'group': (None, '0')}
    response = requests.post(url, files=post_files)
    soup = BeautifulSoup(response.text, 'lxml')
    check_result = soup.find('td', colspan="2").text
    result.write("========================================================================================" + "<br />")
    if 'Passed' in check_result:
        result.write(check_file + "<br />" + check_result + "<br />")
    else:
        result.write(check_file + "<br />")
        result.write(soup.find('div', id='result').prettify(formatter="html") + "\n")


items = os.listdir(".")
result_dir = os.path.join(os.path.dirname(__file__), "result")
if os.path.isdir(result_dir):
    if "result.html" in os.listdir(result_dir):
        os.remove(os.path.join(result_dir, "result.html"))
else:
    os.makedirs(result_dir)
result = open(os.path.join(result_dir, "result.html"), 'a', encoding='utf-8')
for file in items:
    if os.path.splitext(file)[1] == ".html":
        w3c_check(file)
