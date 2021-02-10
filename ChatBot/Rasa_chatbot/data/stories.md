## Complete path
* greet
    - utter_greet
* restaurant_search{"location": "madurai"}
    - slot{"location": "madurai"}
    - action_check_location
    - slot{"location": "madurai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"location": "madurai"}
    - utter_ask_budgetoption
* answering
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_budget_search_restaurant
    - slot{"location": "madurai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email_id
* answering
    - utter_ask_email_option
* restaurant_search{"emailid": "rahul@yahoo.com"}
    - slot{"emailid": "rahul@yahoo.com"}
    - action_validate_email
    - slot{"emailid": "rahul@yahoo.com"}
    - slot{"email_ok": true}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye


## interactive_story_1 Scenario 3 wrong cuisine and corrected
* greet
    - utter_greet
* restaurant_search{"cuisine": "korean", "location": "chennai"}
    - slot{"cuisine": "korean"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "chennai"}
* goodbye
    - utter_goodbye

## interactive_story_1 Scenario 4 without location and validating
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_check_location
    - slot{"location": "raipur"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - slot{"location": "raipur"}
* goodbye
    - utter_goodbye

## interactive_story_1 Scenario 5 location not given and proceed with correct location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_check_location
    - slot{"location": "raipur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"location": "raipur"}
* goodbye
    - utter_goodbye

## interactive_story_1 Scenario 6 location not given and proceed with incorrect location negative scenario
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raikot"}
    - slot{"location": "raikot"}
    - action_check_location
    - slot{"location": "raikot"}
    - slot{"location_ok": false}
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye

## interactive_story_1 location negative scenario
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanchi"}
    - slot{"location": "kanchi"}
    - action_check_location
    - slot{"location": "kanchi"}
    - slot{"location_ok": false}
    - utter_ask_howcanhelp
    - utter_default
* affirm
    - utter_goodbye

## interactive_story_1 correct location & tested with cuisine
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "salem"}
    - slot{"location": "salem"}
    - action_check_location
    - slot{"location": "salem"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "korean"}
    - slot{"cuisine": "korean"}
    - action_validate_cuisine
    - slot{"cuisine": "korean"}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"location": "salem"}
* affirm
    - utter_goodbye

## interactive_story_1 Not using budget and email option
* greet
    - utter_greet
* restaurant_search{"location": "jammu"}
    - slot{"location": "jammu"}
    - action_check_location
    - slot{"location": "jammu"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"location": "jammu"}
    - utter_ask_budgetoption
* answering
    - utter_ask_email_id
* answering
    - utter_goodbye
* goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budgetoption
* answering
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_budget_search_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* answering
    - utter_ask_email_option
* answering{"answering": "ys"}
* restaurant_search{"emailid": "reek@gmail.com"}
    - action_validate_email
    - slot{"emailid": null}
    - slot{"email_ok": false}
* goodbye
    - utter_goodbye

