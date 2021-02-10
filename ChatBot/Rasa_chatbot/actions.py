from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from collections import OrderedDict
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from email.message import EmailMessage
d_email_rest = []

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		list_loc = ["ahmedabad", "bangalore", "chennai", "delhi", "hyderabad", "kolkata", "mumbai", "pune", "agra", "ajmer", "aligarh", "amravati", "amritsar", "asansol", "aurangabad", "bareilly", "belgaum", "bhavnagar", "bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bilaspur", "bokaro steel city", "chandigarh", "coimbatore", "cuttack", "dehradun", "dhanbad", "bhilai", "durgapur", "erode", "faridabad", "firozabad", "ghaziabad", "gorakhpur", "gulbarga", "guntur", "gwalior", "gurgaon", "guwahati", "hamirpur", "hubli–dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar", "jamshedpur", "jhansi", "jodhpur", "kakinada", "kannur", "kanpur", "kochi", "kolhapur", "kollam", "kozhikode", "kurnool", "ludhiana", "lucknow", "madurai", "malappuram", "mathura", "goa", "mangalore", "meerut", "moradabad", "mysore", "nagpur", "nanded", "nashik", "nellore", "noida", "patna", "pondicherry", "purulia", "prayagraj", "raipur", "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli", "shimla", "siliguri", "solapur", "srinagar", "surat", "thiruvananthapuram", "thrissur", "tiruchirappalli", "tiruppur", "ujjain", "bijapur", "vadodara", "varanasi", "vasai-virar city", "vijayawada", "visakhapatnam", "vellore", "warangal"]
 
		loc = tracker.get_slot('location')
		if loc is not None:
			if loc.lower() in list_loc:
				return[SlotSet('location',loc),SlotSet('location_ok', True)]
			else:
				dispatcher.utter_message("We do not operate in that area yet.")
				return[SlotSet('location',None),SlotSet('location_ok', False)]
		else:
			dispatcher.utter_message("We do not operate in that area yet.")
			return[SlotSet('location', None),SlotSet('location_ok', False)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		list_cuisine = ["chinese","mexican","italian","american","south indian","north indian"]
		cuisine = tracker.get_slot('cuisine')
		if cuisine is not None:
			if cuisine.lower() in list_cuisine:
				return[SlotSet('cuisine',cuisine),SlotSet('cuisine_ok', True)]
			else:
				dispatcher.utter_message("Sorry We do not have such cuisine. please select from any one of Cuisine: chinese,mexican,italian,american,south indian,north indian")
				return[SlotSet('cuisine',None),SlotSet('cuisine_ok', False)]
		else:
			dispatcher.utter_message("Sorry We do not have such cuisine. please select from any one of Cuisine: chinese,mexican,italian,american,south indian,north indian")
			return[SlotSet('cuisine', None),SlotSet('cuisine_ok', False)]	

class VerifyBudget(Action):

    def name(self):
        return 'action_validate_budget'

    def run(self, dispatcher, tracker, domain):
        budgetmin = None
        budgetmax = None
        error_msg = "Sorry!! price range not supported, please re-enter."
        try:
            budgetmin = int(tracker.get_slot('budgetmin'))
            budgetmax = int(tracker.get_slot('budgetmax'))
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
            return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]

            
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"769453aee87a12a77d04d4af5c91247a"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		#print(location_detail)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ ">> " +restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated " +restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
		
		dispatcher.utter_message("Here are the restaurants for you:"+"\n" + response)
		return [SlotSet('location',loc)]
        
class ActionbudgetSearchRestaurants(Action):

    config = {"user_key": "769453aee87a12a77d04d4af5c91247a"}

    def name(self):
        return 'action_budget_search_restaurant'

    def run(self, dispatcher, tracker, domain):
        zomato = zomatopy.initialize_app(self.config)
        # Get location from slot
        loc = tracker.get_slot('location')

        # Get cuisine from slot
        cuisine = tracker.get_slot('cuisine')
        cost_min = tracker.get_slot('budgetmin')
        cost_max = tracker.get_slot('budgetmax')
        results, lat, lon = self.get_location_suggestions(loc,zomato)

        if (results != 0):
            # Zomato API could not find suggestions for this location.
            restaurant_exist = True
            d_rest = self.get_restaurants(lat, lon, cost_min, cost_max, cuisine)

            # Filter the results based on budget
            d_budget = [d_rest_single for d_rest_single in d_rest if ((d_rest_single['restaurant']['average_cost_for_two'] > cost_min) & (
                d_rest_single['restaurant']['average_cost_for_two'] < cost_max))]
            # Sort the results according to the restaurant's rating
            d_budget_rating_sorted = sorted(d_budget, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)
                
        else:
            dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")

            # Build the response
            response = ""
            restaurant_exist = True
            if len(d_budget_rating_sorted) != 0:
                # Pick the top 5
                d_budget_rating_top5 = d_budget_rating_sorted[:5]
                global d_email_rest
                d_email_rest = d_budget_rating_sorted[:10]
                if(d_email_rest and len(d_email_rest) > 0):
                    restaurant_exist = True
                for restaurant in d_budget_rating_top5:
                    response = response+ ">> " +restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated " +restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
                dispatcher.utter_message("Here are the restaurants for you:"+"\n" + response)
                
            else:
                dispatcher.utter_message("Sorry, no results found :("+ "\n")
        return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]

    def get_location_suggestions(self, loc, zomato):
        # Get location details including latitude and longitude
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(d1["location_suggestions"])
        if (results > 0):
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
        return results, lat, lon

    def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        d_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
        executor.shutdown()
        return d_rest
        

class ActionValidateEmail(Action):
	def name(self):
		return 'action_validate_email'
		
	def run(self, dispatcher, tracker, domain):
		pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		email_check = tracker.get_slot('emailid')
		if email_check is not None:
			if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email_check):
				return[SlotSet('emailid',email_check),SlotSet('email_ok', True)]
			else:
				dispatcher.utter_message("Sorry this is not a valid email. please resend the emailid")
				return[SlotSet('emailid',None),SlotSet('email_ok', False)]
		else:
			dispatcher.utter_message("Sorry this is not a valid email. please resend the emailid")
			return[SlotSet('emailid', None),SlotSet('email_ok', False)]			
	

	
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
       
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global d_email_rest
        email_rest_count = len(d_email_rest)
        # Construct the email 'subject' and the contents.
        d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
        for restaurant in d_email_rest:
            d_email_msg = d_email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("asaupgrad.chatbot@gmail.com", "pgdmlaiupgrad")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "asaupgrad.chatbot@gmail.com"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
        return []

        
def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '769453aee87a12a77d04d4af5c91247a'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])