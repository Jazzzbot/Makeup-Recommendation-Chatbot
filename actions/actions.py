import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text

# Load dataset once globally
df = pd.read_csv("cosmetics.csv")  # Adjust path if needed

class ActionFindMainIngredient(Action):
    def name(self) -> Text:
        return "action_find_main_ingredient"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = next(tracker.get_latest_entity_values("product"), None)
        if product:
            result = df[df["Name"].str.contains(product, case=False, na=False)]
            if not result.empty:
                ingredients = result.iloc[0]["Ingredients"]
                main = ingredients.split(",")[0] if isinstance(ingredients, str) else "unknown"
                dispatcher.utter_message(text=f"The main ingredient in {product} is {main}.")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't find that product.")
        return []

class ActionFindProductsWithIngredient(Action):
    def name(self) -> Text:
        return "action_find_products_with_ingredient"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ingredient = next(tracker.get_latest_entity_values("ingredient"), None)
        if ingredient:
            matches = df[df["Ingredients"].str.contains(ingredient, case=False, na=False)]
            products = matches["Name"].head(5).tolist()
            if products:
                dispatcher.utter_message(text="Products with " + ingredient + ": " + ", ".join(products))
            else:
                dispatcher.utter_message(text="No products found with that ingredient.")
        return []

class ActionFindProductsForSkinType(Action):
    def name(self) -> Text:
        return "action_find_products_for_skin_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        skin_type = next(tracker.get_latest_entity_values("skin_type"), None)
        if skin_type and skin_type.capitalize() in df.columns:
            matches = df[df[skin_type.capitalize()] == 1]
            products = matches["Name"].head(5).tolist()
            dispatcher.utter_message(text=f"Top products for {skin_type} skin: {', '.join(products)}")
        else:
            dispatcher.utter_message(text="Couldn't find any matches. Try dry, oily, sensitive, or normal.")
        return []


