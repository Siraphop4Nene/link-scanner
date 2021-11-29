import sys
import requests
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_links(given_url):
    """Find all links on page at the given url.
    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser = webdriver.Chrome()
    browser.get(given_url)
    get_link = browser.find_elements(By.TAG_NAME, 'a')
    link_list = []
    for each_link in get_link:
        each_link = each_link.get_attribute('href')
        if each_link is not None:
            if '#' in each_link:
                each_link = each_link.split('#')[0]
            if '?' in each_link:
                each_link = each_link.split('?')[0]
            link_list.append(each_link)
    return link_list


def is_valid_url(urls: str):
    """Check that url is valid.
    """
    return requests.head(urls).ok


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    invalid_urls_list = []
    for url in urllist:
        if not is_valid_url(url):
            invalid_urls_list.append(url)
    return invalid_urls_list


if __name__ == "__main__":
    url = sys.argv[1]
    links = get_links(url)
    print("All links: ")
    for each_url in links:
        print(each_url)
    print()
    print("Bad Links:")
    for bad_link in invalid_urls(links):
        print(bad_link)
    print()
