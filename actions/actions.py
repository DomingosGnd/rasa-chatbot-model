# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from rasa_sdk import Action

class ActionDietAdvice(Action):
    def name(self):
        return "action_diet_advice"

    def run(self, dispatcher, tracker, domain):
        trimester = tracker.get_slot('trimester')
        if trimester == 'primeiro':
            response = "No primeiro trimestre, concentre-se em uma dieta equilibrada com proteínas e ácido fólico."
        elif trimester == 'segundo':
            response = "No segundo trimestre, continue com uma alimentação rica em ferro e cálcio."
        else:
            response = "Mantenha uma dieta saudável rica em nutrientes durante toda a gravidez."
        dispatcher.utter_message(text=response)
        return []
