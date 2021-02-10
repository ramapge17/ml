## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks a lot
- thanks for the info
- got it
- got it thanks
- thanks for the list
- [thanks](affirm)
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- thanks
- thanks bye
- no thanks
- bye thanks

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- heyyy
- Hi
- Hello

## intent:stop
- sorry
- I do not understand

## intent:answering
- yes
- no
- [ys](answering)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [American](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- show me the restaurants in [Bombay]{"entity": "location", "value": "Mumbai"}
- tell me the restaurants
- [lucknow](location)
- Like to know some restaurants in [agra](location)
- cuisine variety
- some restaurants in [dhanbad](location)
- some restaurants in [kanchipuram](location)
- some restaurants in [thiruppur](location)
- some [korean](cuisine) restaurants in [chennai](location)
- some [chinese](cuisine) restaurants
- in [raipur](location)
- [noida](location)
- [jaipur](location)
- some restaurants
- [Mexican](cuisine)
- show some restaurants
- [raikot](location)
- show me some restaurants
- [kanchi](location)
- get some restaurants
- [salem](location)
- [korean](cuisine)
- I wld like to know some restaurants in [bhopal](location)
- can you pls tell me some restautants in [surat](location)
- This is my email id [ram@gmail.com](emailid)
- share some restaurants in [jammu](location)
- some restaurants in [pune](location)
- give me some restaurants in [bhopal](location)
- some restaurants in [delhi](location)
- get me some [chinese](cuisine) restaurants in [delhi](location)
- this is my email id [reek@gmail.com](emailid)
- some [south indian](cuisine) restaurants in [chennai](location)
- my id is [ram@gmail.com](emailid)
- restaurants in [madurai](location)
- [South Indian](cuisine)
- its my email id [rahul@yahoo.com](emailid)
- some [north indian](cuisine) restaurants in [chennai](location)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:Kolkata
- Calcutta

## synonym:Mumbai
- Bombay

## synonym:No
- no
- na

## synonym:Yes
- yes
- ys
- yess

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:thiruvananthapuram
- tiruvananthapuram

## synonym:thrissur
- trissur

## synonym:tiruchirappalli
- thiruchirappalli

## synonym:tiruppur
- thiruppur

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:restaurant_search
- ^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
- in[^\s]*
