from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
import re 

class InfoForm(FormAction):
    def name(self):
        return "info_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "standard",
            ]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        standard = tracker.get_slot("standard")
        output="All done! You clicked {}, which is of price 10000".format(standard)
        dispatcher.utter_message(output) 
        return []