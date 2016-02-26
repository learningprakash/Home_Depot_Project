from lxml import html
import requests
#from fuzzydict import FuzzyDict

import difflib



class FuzzyDict(dict):
    "Provides a dictionary that performs fuzzy lookup"
    def __init__(self, items = None, cutoff = .5):
        """Construct a new FuzzyDict instance
        items is an dictionary to copy items from (optional)
        cutoff is the match ratio below which mathes should not be considered
        cutoff needs to be a float between 0 and 1 (where zero is no match
        and 1 is a perfect match)"""
        super(FuzzyDict, self).__init__()

        if items:
            self.update(items)
        self.cutoff =  cutoff

        # short wrapper around some super (dict) methods
        self._dict_contains = lambda key: \
            super(FuzzyDict,self).__contains__(key)

        self._dict_getitem = lambda key: \
            super(FuzzyDict,self).__getitem__(key)

    def _search(self, lookfor, stop_on_first = False):
        """Returns the value whose key best matches lookfor
        if stop_on_first is True then the method returns as soon
        as it finds the first item
        """

        # if the item is in the dictionary then just return it
        if self._dict_contains(lookfor):
            return True, lookfor, self._dict_getitem(lookfor), 1

        # set up the fuzzy matching tool
        ratio_calc = difflib.SequenceMatcher()
        ratio_calc.set_seq1(lookfor)

        # test each key in the dictionary
        best_ratio = 0
        best_match = None
        best_key = None
        matches = []
        iterate = 0
        for key in self:

            # if the current key is not a string
            # then we just skip it
            try:
                # set up the SequenceMatcher with other text
                ratio_calc.set_seq2(key)
            except TypeError:
                continue

            # we get an error here if the item to look for is not a
            # string - if it cannot be fuzzy matched and we are here
            # this it is defintely not in the dictionary
            try:
            # calculate the match value
                ratio = ratio_calc.ratio()
            except TypeError:
                break

            # if this is the best ratio so far - save it and the value
            if ratio > best_ratio:
                best_ratio = ratio
                best_key = key
                best_match = self._dict_getitem(key)

                if ratio >= self.cutoff:
                    matches.append(best_match)
            if stop_on_first and ratio >= self.cutoff:
                break
        print matches


        return (
            best_ratio >= self.cutoff,
            best_key,
            matches,
            best_ratio)


    def __contains__(self, item):
        "Overides Dictionary __contains__ to use fuzzy matching"
        if self._search(item, True)[0]:
            return True
        else:
            return False

    def __getitem__(self, lookfor):
        "Overides Dictionary __getitem__ to use fuzzy matching"
        matched, key, item, ratio = self._search(lookfor)

        if not matched:
            raise KeyError(
                "'%s'. closest match: '%s' with ratio %.3f"%
                    (str(lookfor), str(key), ratio))

        return item



## SEarching in HomeDepot Website
#http://www.homedepot.com/s/diy%20project?NCNI-5
# dict = {'Appliance': 'http://www.homedepot.com/c/Appliance_Upgrades',
#         'Bath':'http://www.homedepot.com/c/bathroom_ideas',
#         'Building Materials': 'http://www.homedepot.com/c/project_how_to_project_guides_building_materials',
#         'Decor':'http://www.homedepot.com/c/project_how_to_project_guides_decor',
#         'Doors and Windows':'http://www.homedepot.com/c/project_how_to_project_guides_doors_windows',
#         'Electrical':'http://www.homedepot.com/c/project_how_to_project_guides_electrical',
#         'Flooring':'http://www.homedepot.com/c/flooring_upgrades',
#         'Heating and Cooling':'http://www.homedepot.com/c/project_how_to_project_guides_heating_cooling',
#         'Kitchen':'http://www.homedepot.com/c/kitchen_ideas',
#         'Lighting and Fans':'http://www.homedepot.com/c/project_how_to_project_guides_lighting_fans',
#         'Lumber':'http://www.homedepot.com/c/project_how_to_project_guides_lumber_composites',
#         'Home Maintenance':'http://www.homedepot.com/c/home_maintenance_diy_ideas',
#         'Outdoor':'http://www.homedepot.com/c/outdoor_diy_ideas',
#         'Plumbing':'http://www.homedepot.com/c/project_how_to_project_guides_plumbing',
#         'Seasonal':'http://www.homedepot.com/c/project_how_to_project_guides_seasonal',
#         'Storage':'http://www.homedepot.com/c/project_how_to_project_guides_storage_organization'};

# for category in dict.keys():
#     print dict.get(category)
# completeKeywords = []
# for key in dict:
#
#     page = requests.get(dict.get(key))
#     tree = html.fromstring(page.content)
#     diyLinks = tree.xpath('//a')
#
#     diyWebsite = []
#     text = '/c/how'
#     for link in diyLinks:
#         website = link.get("href")
#         if text in website or "HT_BG" in website:
#             if website.startswith("/c/"):
#                 diyWebsite.append("http://www.homedepot.com"+ website)
#             elif website.startswith("http://www.homedepot.com/"):
#                 diyWebsite.append(website)
#
#     websites = set(diyWebsite)
#     ##print websites
#
#
#     for web in websites:
#         page = requests.get(web)
#         tree = html.fromstring(page.content)
#         try:
#             keywords = tree.xpath( "//meta[@name='keywords']")[0].get("content")
#             completeKeywords[1:1] = filter(None, keywords.lower().split(","))
#             for keyword in keywords.split(","):
#                 if not keyword:
#                     print key.strip().lower() + "," + key.strip().lower() + "," + web
#                 else:
#                     print keyword.strip().lower() + "," + key.strip().lower() + "," + web
#         except:
#             print "Error getting keywords for" + web
#
#
#


#completeKeywords = ['organization ideas', 'Refrigerators', ' Energy Saving Refrigerators', ' Best Refrigerators', ' Electronic Refrigerators', ' Refrigerators Types', ' Appliances', 'privacy', 'security', 'personal information', 'shopping', 'installation services', 'tool rentals', 'call centers', 'online registration', 'contests', 'questions', 'surveys', 'financial products', 'extended warranty services', 'sale of business', 'legal', 'cookies', 'tracer tags', 'third party links', 'security measures', 'secure shopping', 'passwords', 'order information', 'contact', 'privacy protection', 'data security', 'Privacy Policy', 'Privacy Statement', 'garbage disposer', ' garbage disposer installation', ' installing a garbage disposer', ' Appliances', '', 'Replacing Dishwasher', ' How to replace dishwasher', ' How to install dishwasher', ' Appliances', '', 'project', 'how-to', 'buying guide', 'project guide', 'how-to video', 'kitchen', ' appliances', ' small kitchen appliances', ' coffee maker', ' bean grinder', ' toasters', ' food processors', ' Kitchen Storage', ' Storage Innovation', ' Smart Kitchen Storage Solutions', ' Cabinet Storage and Innovation', ' Kitchen Storage Solutions', '', 'Ice Makers', ' Types of Ice Makers', ' Freezer Ice Makers', ' Portable Ice Makers', ' Free-standing Ice Makers', ' Appliances', 'Freezer', ' chest freezer', ' upright freezer', ' manual defrost freezer', ' Frost-free freezer', ' auto-defrost', 'appliances', 'Email', 'The Home Depot', 'customer service', 'customer support', 'phone numbers', '', 'return policy', 'returns', 'online purchase', 'homedepot.com', 'UPS deliveries', 'UPS return', 'customer care', 'merchandise', 'receipt', 'RGA', 'refund', 'credit card', 'return instructions', 'damaged items', 'shortage claims', 'flammable', 'liquids', 'gases', 'gift cards', 'cash', 'check', 'store credit', 'gift certificate', 'credit account', 'special order', 'Evaporative Coolers', ' Swamp Coolers', ' Portable Coolers', ' Mobile Coolers', ' Window or Through-the-Wall units', ' Down Discharge coolers', ' Side Discharge units', ' Evaporative Coolers CFM Ratings', ' Evaporative Coolers Maintenance', ' Appliances', ' Summer', ' Heating Cooling', 'washer', ' wash', ' stackable', ' dryer combination', ' compact', ' portable', ' rinse', ' top-load', ' front-load', ' stain detergent', ' wash clean', ' clean', ' wash cycle', ' energy', ' washing machines', 'appliances', 'Installing a Dryer Vent', ' How to install dryer vent', ' Install dryer vent in wall', ' Install dryer vent vinyl siding', ' Appliances', ' HVAC', 'recalls', 'product recalls', 'consumer product safety commission', 'CPSC', 'safety', 'hazards', 'recall details', 'Recalled products', '', 'GIFTCARD', 'water dispenser', ' dispenser', ' hot water dispenser', ' water heater', ' electric water heater', ' Appliances', 'Changing Dryer Cord', ' Dryer Cord', ' 3-prong cord', ' 4-prong cord', ' Appliances', 'Air Conditioner', ' Window Units', ' Portable units', ' Installing an air conditioner', ' Appliances', 'Range Hood', ' Installing a Range Hood', ' Range Hood Installation', ' kitchen ventilation', ' Appliances', ' HVAC', 'Customer Support', 'Customer Care', 'FAQ', 'privacy', 'security', 'returns', 'contact us', 'product recalls', 'Dishwasher', ' types of dishwashers', ' modern dishwashers', ' dishwasher technology', ' dishwasher models', '', 'Microwaves', ' Over-the-Range Microwaves', ' Microwave types', ' Countertop Microwaves', ' Built-In Microwaves', ' How to select microwave', ' Choosing Microwave', ' Appliances', '', '', 'Kitchen Ideas', 'Kitchen', 'Kitchens', 'Kitchen Design Ideas', 'garbage disposers', ' unclogging garbage disposers', ' unclog garbage disposers', ' unclog disposals', ' Appliances', 'home delivery appliances installation Home Depot', 'privacy preferences', 'privacy', 'manage privacy preferences', 'Range Hood', ' Types of Range Hood', ' Range Hood for your Kitchen', ' Ventilation System', ' Range Hood Installation Tips', ' Range Hood Maintenance', ' Appliances', 'dishwasher installation', ' install dish washer', 'installing a dishwasher', ' Appliances', 'About Your Online Order', 'Order Tracking', 'Order Status', 'Order Detaills', 'Questions about my order', 'Shipping', 'Delivery', 'Return Policy', 'bathroom remodel', 'bathroom remodel ideas', 'bathroom decorating ideas', 'bathroom design ideas', '', 'project calculator', ' how-to calculator', ' roofing calculator', ' tile calculator', ' insulation calculator', ' the home depot', 'Wall Oven', ' Gas Wall Oven', ' Electric Wall Oven', ' Types of Wall Oven', ' Appliances', '', '', 'privacy', 'security', 'personal information', 'shopping', 'installation services', 'tool rentals', 'call centers', 'online registration', 'contests', 'questions', 'surveys', 'financial products', 'extended warranty services', 'sale of business', 'legal', 'cookies', 'tracer tags', 'third party links', 'security measures', 'secure shopping', 'passwords', 'order information', 'contact', 'privacy protection', 'data security', 'Privacy Policy', 'Privacy Statement', '', 'home depot android', 'home depot android app', 'home depot app', 'home depot iphone', 'home depot iphone app', 'home depot mobile app', 'mobile', 'iphone', 'apps', 'android', 'windows phone', 'home depot affiliate program', 'home depot affiliate', 'affiliate marketing', 'online marketing program', 'commission junction', 'online affiliate programs', 'affiliate network', 'The Home Depot', '', 'Pedestal', ' stack kit', ' washer', ' dryer', ' washer pedestal', ' dryer pedestal', ' pedestal system', ' dryer pedestals', ' washer and dryer pedestals', ' washer and dryer pedestal', ' stacking kit', ' stack dryer', ' stack washer and dryer', ' stacking kits', 'appliances', '', 'Installing an Icemaker', ' Install copper tubing', ' Install copper tubing for icemaker', ' Install copper tubing refrigerator', ' Appliances', 'Dryers Electric', ' Reliable Electric Dryer', ' Energy Efficient Electric Dryer', ' Types of Electric Dryer', ' Features of Electric Dryer', ' Appliances', 'Installing new water heater', ' old water heater', ' Electric heater', ' Gas heater', ' Replace old water heater', ' Install the Water Lines and Pressure Relief Line', ' Appliances', '', '', 'Vacuum Cleaners', ' Best Vacuum Cleaners', ' Steam Cleaners', ' Type of Vacuum Cleaners', ' Uses of Vacuum Cleaner', ' Appliances', '', '', 'Installing a Flue Hat', ' How to Install a Flue hat', ' Removing harmful fumes', ' Flue Hat', ' heating', ' cooling', ' flue hats', ' Appliances', ' HVAC', 'Ranges', ' Types of Range', ' Gas Range', ' Electric Range', ' Cooking Ranges', ' appliances', '', 'Cooktops', ' Gas Cooktops', ' Electric Cooktops', ' Induction Cooktops', ' Selection of Cooktops', ' Appliances', '', 'storage ideas']

#
# page = requests.get('http://www.homedepot.com/c/how_to_install_water_heater_HT_PG_AP')
# tree = html.fromstring(page.content)
#
# keywords = tree.xpath( "//meta[@name='keywords']" )[0].get("content")



