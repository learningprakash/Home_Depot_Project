#from keywordScrape import KeywordProvider
from indigoApp.models import CategoryCustomerMap
from indigoApp.models import Customers
from django.shortcuts import get_object_or_404

class Associates:

    def getAssociates(self, category, keyword):
        if category:
            return self.getAssociatesFromCategory(category)

        if keyword:
            #keywords = KeywordProvider.getKeywords(KeywordProvider, keyword)
            return self.getAssociatesFromKeyword(keyword)

    def getAssociatesByName(self, name):
        return Customers.objects.get(CompanyName=name, IsPro=0)

    def getAssociatesFromCategory(self, categoryInput):
        customers = []
        categoryCustomers = CategoryCustomerMap.objects.filter(Category=categoryInput)
        for categoryCustomer in categoryCustomers:
            try:
                customer = Customers.objects.get(id=categoryCustomer.CustomerId, IsAvailable=1, IsPro=0)
                if customer:
                    customers.append(customer)
            except:
                continue

        customers.sort(key=lambda x: x.Rating, reverse=True)
        return customers


    def getAssociatesFromKeyword(self, keyword):
        return



# ProUsers.getUsers(ProUsers, "Appliances", None)

