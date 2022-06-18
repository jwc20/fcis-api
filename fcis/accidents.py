from .core import *


class Accidents(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def is_a_keyword(keywords):
        """
        Validates a list of words to see if they are in the keyword list
        """
        for keyword in keywords:
            if (keyword in self.get_keywords(keyword[0])):
                return True
            else:
                return False

        return

    def _make_accidents_search_url(self):
        return

    def _load_accidents_search_page(self):
        r = requests.get(BASE_URL + ACCIDENT_SEARCH_URL)
        html = r.text
        return BeautifulSoup(html, "lxml")

    def _load_accidents_keywords_page(self, first_letter):
        """
        For loading the list of keywords page by letters.
        """
        r = requests.get(BASE_URL + ACCIDENT_KEYWORD_LETTER_URL + first_letter)
        html = r.text
        return BeautifulSoup(html, "lxml")

    # def _load_accidents_search_form_page(self):
    #     r = requests.get(BASE_URL + ACCIDENT_SEARCH_FORM_URL)
    #     html = r.text
    #     return BeautifulSoup(html, "lxml")

    def _extract_accidents_0(self):
        return

    def _extract_accidents_1(self):
        return

    def _extract_accidents_2(self):
        return

    def _transform_accidents(self):
        return

    def get_keywords(self, first_letter):
        if len(first_letter) != 1:
            print("Must input a letter.")
        else:
            keyword_list = []
            page = self._load_accidents_keywords_page(first_letter)
            # TODO: scrape the keywords
            # must return a list
            a_hrefs = page.find("div", {"class": "well"}).find_all("a")
            for a_href in a_hrefs:
                keyword_list.append(a_href.text)
            return keyword_list

    def get_accidents(self):
        return
