import re
from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        first_name = tracker.get_slot("first_name")
        # If the name is super short, it might be wrong.
        print(f"First name given =" + first_name + "length = {len(slot_value)}")
        if len(first_name) <= 2:
            dispatcher.utter_message(text="That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": first_name}

# class ValidateEmail(Action):
#     def name(self) -> Text:
#         return "validate_email_form"
#
#     def validate_email(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `email` value."""
#
#         email = tracker.get_slot("email")
#         # If the name is super short, it might be wrong.
#         print(f"email given =" + email + "length = {len(slot_value)}")
#         if re.Match(r"[a-zA-Z0-9_.±]+@[a-zA-Z]+.[^@]+", str(email)):
#             return {"email": email}
#         else:
#             dispatcher.utter_message(text="Invalid email")
#             return {"email": None}

# class SayName(Action):
#     def name(self) -> Text:
#         return "reply_name"
#
#     def reply_name(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#
#         first_name = tracker.get_slot("first_name")
#
#         if len(first_name) <= 0:
#             dispatcher.utter_message(text=f"You haven't given me your name yet.")
#         else:
#             dispatcher.utter_message(text=f"Your name is {first_name}")