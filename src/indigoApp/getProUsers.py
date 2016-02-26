#from keywordScrape import KeywordProvider
from models import CategoryCustomerMap
from models import Customers
from django.shortcuts import get_object_or_404

class ProUsers:

    def getUsers(self, category, keyword):
        if category:
            return self.getUsersFromCategory(category)

        if keyword:
            #keywords = KeywordProvider.getKeywords(KeywordProvider, keyword)
            return self.getUsersFromKeyword(keyword)

    def getUserByName(self, name):
        return Customers.objects.get(CompanyName=name, IsPro=1)

    def getUsersFromCategory(self, categoryInput):
        customers = []
        categoryCustomers = CategoryCustomerMap.objects.filter(Category=categoryInput)
        for categoryCustomer in categoryCustomers:
            try:
                customer = Customers.objects.get(id=categoryCustomer.CustomerId, IsAvailable=1, IsPro=1)
                if customer:
                    customers.append(customer)
            except:
                continue

        customers.sort(key=lambda x: x.Rating, reverse=True)
        return customers


    def getUsersFromKeyword(self, keyword):
        return



# ProUsers.getUsers(ProUsers, "Appliances", None)

