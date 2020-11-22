# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
##from firebase import firebase

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
##from rasa_sdk.events import  UserUtteranceReverted
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


cred = credentials.Certificate(r"C:\Users\HP\Desktop\chatbot\actions\chat-bot-387a1-firebase-adminsdk-vowk7-55176916c1.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chat-bot-387a1.firebaseio.com/'
})

org = ''
des = ''

res = db.reference('/')
a=res.get()
event=a['collegeEvents']

ref = db.reference('events')
events=ref.get()

def PROD():
    myurl = 'http://frcrce.ac.in/index.php/crce-department/prodengg/faculty-prod'

    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    filename = "prod_faculty.csv"
    f = open(filename, "w")

    headers = "designation, name\n"

    f.write(headers)

    faculty_info = page_soup.findAll("div", {"class":"sppb-person-information"})

    designation = []
    name = []

    for faculty in faculty_info:
        d = faculty.find("span", {"class":"sppb-person-designation"})
        designation.append(d.text)

        n = faculty.find("span", {"class":"sppb-person-name"})
        name.append(n.text)

	
    f.close()
    return designation, name

def IT():
    myurl = 'http://frcrce.ac.in/index.php/crce-department/infotech/faculty-it'

    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    filename = "it_faculty.csv"
    f = open(filename, "w")

    headers = "designation, name\n"

    f.write(headers)

    faculty_info = page_soup.findAll("div", {"class":"sppb-person-information"})

    designation = []
    name = []

    for faculty in faculty_info:
        d = faculty.find("span", {"class":"sppb-person-designation"})
        designation.append(d.text)

        n = faculty.find("span", {"class":"sppb-person-name"})
        name.append(n.text)

	
    f.close()
    return designation, name

def SCI():
    myurl = 'http://frcrce.ac.in/index.php/crce-department/science-humanities/faculty-scihum'

    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    filename = "scihum_faculty.csv"
    f = open(filename, "w")

    headers = "designation, name\n"

    f.write(headers)

    faculty_info = page_soup.findAll("div", {"class":"sppb-person-information"})

    designation = []
    name = []

    for faculty in faculty_info:
        d = faculty.find("span", {"class":"sppb-person-designation"})
        designation.append(d.text)

        n = faculty.find("span", {"class":"sppb-person-name"})
        name.append(n.text)

	
    f.close()
    return designation, name


def COMPS():
    myurl = 'http://frcrce.ac.in/index.php/crce-department/comp-engg/faculty-compengg'

    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    faculty_info = page_soup.findAll("div", {"class":"sppb-person-information"})

    filename = "comps_faculty.csv"
    f = open(filename, "w")

    headers = "designation, name, degree\n"

    f.write(headers)

    designation = []
    name = []

    for faculty in faculty_info:
        d = faculty.find("span", {"class":"sppb-person-designation"})
        designation.append(d.text)

        n = faculty.find("span", {"class":"sppb-person-name"})
        name.append(n.text)

	
    f.close()
    return designation, name

def ELEX():
    myurl = 'http://frcrce.ac.in/index.php/crce-department/elex-compsci/faculty-elex-compsci'

    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    filename = "elex_compsci_faculty.csv"
    f = open(filename, "w")

    headers = "designation, name\n"

    f.write(headers)

    faculty_info = page_soup.findAll("div", {"class":"sppb-person-information"})

    designation = []
    name = []

    for faculty in faculty_info:
        d = faculty.find("span", {"class":"sppb-person-designation"})
        designation.append(d.text)

        n = faculty.find("span", {"class":"sppb-person-name"})
        name.append(n.text)

    f.close()
    return designation, name




def get_news():

    myurl = 'http://frcrce.ac.in'

    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    # get the news
    news = page_soup.findAll("div",{"class":"latestnews"})
    n = news[0]
    articles = n.findAll("a")
        
    h, l = [], []
    for article in articles:
        
        news_headline = article.span.text.strip()
        news_link = myurl + article["href"]
        h.append(news_headline)
        l.append(news_link)
    return h,l
#
class Action_Notice(Action):
    
#
	def name(self) -> Text:
		return "action_aws"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = get_news()
		full_news = "http://www.frcrce.ac.in/index.php/students/crce-notices"
		
		for i, k in zip(h, l):
			o = ''
			o = i
			o += '\n'
			o += k
			o += '\n'
			dispatcher.utter_message(o)
		dispatcher.utter_message("Full news: " + full_news)

			

		return []

class Action_HOD_COMPS(Action):
    
#
	def name(self) -> Text:
		return "action_COMPS"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = COMPS()
		#full_news = "http://www.frcrce.ac.in/index.php/students/crce-notices"
		
		
		dispatcher.utter_message(l[0] +" "+ h[0])
		#dispatcher.utter_message("Full news: " + full_news)

			

		return []

class Action_HOD_IT(Action):
#
	def name(self) -> Text:
		return "action_IT"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = IT()
		#full_news = "http://www.frcrce.ac.in/index.php/students/crce-notices"
		
		
		dispatcher.utter_message(l[0] +" "+ h[0])
		#dispatcher.utter_message("Full news: " + fu

		return []

class Action_HOD_ELEX(Action):
#
	def name(self) -> Text:
		return "action_Elex"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = ELEX()
		#full_news = "http://www.frcrce.ac.in/index.php/students/crce-notices"
		
		
		dispatcher.utter_message(l[0] +" "+ h[0])
		#dispatcher.utter_message("Full news: " + fu
			

		return []
class Action_HOD_SCI(Action):
#
	def name(self) -> Text:
		return "action_SCI"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = SCI()
		#full_news = "http://www.frcrce.ac.in/index.php/students/crce-notices"
		
		
		dispatcher.utter_message(l[0] +" "+ h[0])
		#dispatcher.utter_message("Full news: " + fus)

			

		return []

class Action_HOD_PROD(Action):
#
	def name(self) -> Text:
		return "action_PROD"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = PROD()
		#full_news = "http://www.frcrce.ac.in/index.php/students/crce-notices"
		
		
		dispatcher.utter_message(l[0] +" "+ h[0])
		#dispatcher.utter_message("Full news: " + fu

			

		return []

class action_COMPS(Action):
#
	def name(self) -> Text:
		return "action_COMPS_F"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = COMPS()
		full_details = "http://frcrce.ac.in/index.php/crce-department/prodengg/faculty-prod"
		
		for i, k in zip(l, h):
			o = ''
			o = i
			o += '\t'
			o += k
			o += '\n'
			dispatcher.utter_message(o)
		dispatcher.utter_message("Full details: " + full_details)

			

		return []

class action_IT(Action):
#
	def name(self) -> Text:
		return "action_IT_F"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = IT()
		full_details = "http://frcrce.ac.in/index.php/crce-department/infotech/faculty-it"
		
		for i, k in zip(l, h):
			o = ''
			o = i
			o += '\t'
			o += k
			o += '\n'
			dispatcher.utter_message(o)
		dispatcher.utter_message("Full details: " + full_details)

			

		return []

class action_Elex(Action):
#
	def name(self) -> Text:
		return "action_Elex_F"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = ELEX()
		full_details = "http://frcrce.ac.in/index.php/crce-department/elex-compsci/faculty-elex-compsci"
		
		for i, k in zip(l, h):
			o = ''
			o = i
			o += '\t'
			o += k
			o += '\n'
			dispatcher.utter_message(o)
		dispatcher.utter_message("Full details: " + full_details)

			

		return []

class action_PROD(Action):
#
	def name(self) -> Text:
		return "action_PROD_F"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = PROD()
		full_details = "http://frcrce.ac.in/index.php/crce-department/prodengg/faculty-prod"
		
		for i, k in zip(l, h):
			o = ''
			o = i
			o += '\t'
			o += k
			o += '\n'
			dispatcher.utter_message(o)
		dispatcher.utter_message("Full details: " + full_details)

			

		return []

class action_SCI(Action):
#
	def name(self) -> Text:
		return "action_SCI_F"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		h , l = SCI()
		full_details = "http://frcrce.ac.in/index.php/crce-department/science-humanities/faculty-scihum"
		
		for i, k in zip(l, h):
			o = ''
			o = i
			o += '\t'
			o += k
			o += '\n'
			dispatcher.utter_message(o)
		dispatcher.utter_message("Full details: " + full_details)

			

		return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for key in events:
            dispatcher.utter_message(str(key)+" on "+str(events[key]))

        return []

class FacilityForm(FormAction):
    def name(self) -> Text:
        return "facility_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """Database of supported cuisines"""

        return ["colevents"]
    
    def slot_mappings(self)-> Dict[Text, Any]:
        return{"colevents": self.from_entity(entity = "colevents", intent=["college_events"])}
    
        
    
    ##slot_value: Any,
    def submit(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
        ) -> List[Dict]:
        """Validate cuisine value."""
        
        
        my_events = tracker.get_slot("colevents")
        
        
        
        
        for i in event:
            if(i==my_events):
                for j in event[i]:
                    org = j
                    des = event[i][j]

        dispatcher.utter_message(org+"\n"+des)
        
        
        return []
        