#from keywordScrape import KeywordProvider
from indigoApp.models import KeywordCategoryUrlMap
from django.db.models import Q

class DiyLinks:

    def getDiyLinks(self, keyword):
        return self.getDiyLinksFromKeyword(keyword)


    def getDiyLinksFromKeyword(self, keyword):
        urls = []
        categoryUrls = []
        categories = []
        keywordUrls = KeywordCategoryUrlMap.objects.filter(Q(Keyword__contains=keyword.lower()))
        for url in keywordUrls:
            urls.append(url.Url)
            categories.append(url.Category)
        # for category in categories:
        #     categoryRelatedUrls = KeywordCategoryUrlMap.objects.filter(Category=category)
        #     for categoryRelatedUrl in categoryRelatedUrls:
        #         categoryUrls.append(categoryRelatedUrl.Url)
        urls.extend(categoryUrls)

        if len(urls) is None:
            urls.append("http://www.homedepot.com/s/"+keyword)
        return list(set(urls))

