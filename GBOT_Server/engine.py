##dict of response for each type of intent
intent_response_dict = {
    "intro": ["This is a GST FAQ bot. One stop-shop to all your GST related queries"],
    "greet":["Hey","Hello","Hi"],
    "goodbye":["Bye","It was nice talking to you","See you","ttyl"],
    "affirm":["Cool","I know you would like it"]

}

gstinfo_response_dict = {
    "GST": " Goods and Service Tax (GST) is a destination based tax on consumption of goods and services.",
    "gst": " Goods and Service Tax (GST) is a destination based tax on consumption of goods and services.",
    "benefits":"GST consumes more than a dozen taxes, thus making it hassle free and efficient.",
    "dual":"Both the levels of Government have distinct responsibilities toperform according to the division of powers prescribed in the Constitution for which they need to raise resources. A dual GST will, therefore, be in keeping with the Constitutional requirement of fiscal federalism.",
    "faq_link":'You can check all the answers <a href="http://www.cbic.gov.in/resources//htdocs-cbec/gst/faq-gst-2018.pdf">here</a>',
    "rate":{"grains":"The GST on grains is 5%","tobacco":"The GST rates on tobacco products are 28%"}
}

gst_query_value_dict = {
    "12":"Non-AC hotels, business class air ticket, frozen meat products, butter, cheese, ghee, dry fruits in packaged form, animal fat, sausage, fruit juices, namkeen and ketchup",
    "5":"railways, air travel, branded paneer, frozen vegetables, coffee, tea, spices, kerosene, coal, medicines",
    "18":"AC hotels that serve liquor, telecom services, IT services, flavored refined sugar, pasta, cornflakes, pastries and cakes",
    "28":"5-star hotels, race club betting,wafers coated with chocolate, pan masala and aerated water",
    "exempt":"education, milk, butter milk, curd, natural honey, fresh fruits and vegetables, flour, besan"
}

def gst_info(entities):
	if entities == []:
		return "Could not find out specific information about this ..." +  gstinfo_response_dict["faq_link"]
	if len(entities) >= 1:
			return gstinfo_response_dict[entities[0]['value']]
	else:
		return "Sorry.." + gstinfo_response_dict["faq_link"]

def gst_query(entities):
    if entities == []:
        return "Could not query this ..." + gstinfo_response_dict["faq_link"]
    for ent in entities:
        qtype = ent["entity"]
        qval = ent["value"]
        if qtype == "gst-query-value":
            return gst_query_value_dict[qval]

        return gstinfo_response_dict[entities[0]['value']][entities[1]['value']]
    return "Sorry.." + gstinfo_response_dict["faq_link"]