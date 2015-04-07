# Simple Olark AppEngine Webhook 
A quick example of how to process an Olark webhook using Google App Engine.  See:  https://www.olark.com/help/webhooks to better understand Olark webhooks.

# Getting started
1. Create a new cloud application in google appengine (make note of the PROJECT_ID)
2. Configure Google AppEngine on your local machine.

# To Test locally

Run the app engine dev server:
```
dev_appserver.py olarkwebhook/
```

Use curl to generate a fake request.
```
curl -X POST -d '{"kind": "Conversation", "tags": ["olark", "customer"], "items": [{"body": "Hi there. Need any help?", "timestamp": "1307116657.1", "kind": "OfflineMessage", "nickname": "John", "operatorId": "1234"}, {"body": "Yes, please help me with billing.", "timestamp": "1307116661.25", "kind": "MessageToOperator", "nickname": "Bob"}], "operators": {"1234": {"username": "jdoe", "emailAddress": "john@example.com", "kind": "Operator", "nickname": "John", "id": "1234"}}, "visitor": {"ip": "123.4.56.78", "city": "Palo Alto", "kind": "Visitor", "conversationBeginPage": "http://www.example.com/path", "countryCode": "US", "country": "United State", "region": "CA", "chat_feedback": {"overall_chat": 5, "responsiveness": 5, "friendliness": 5, "knowledge": 5, "comments": "Very helpful, thanks"}, "operatingSystem": "Windows", "emailAddress": "bob@example.com", "organization": "Widgets Inc.", "phoneNumber": "(555) 555-5555", "fullName": "Bob Doe", "customFields": {"favoriteColor": "blue", "myInternalCustomerId": "12341234"}, "id": "9QRF9YWM5XW3ZSU7P9CGWRU89944341", "browser": "Chrome 12.1"}, "id": "EV695BI2930A6XMO32886MPT899443414"}' http://localhost:8080
```

# To deploy to AppEngine
```
appcfg.py -A PROJECT_ID --oauth2 update olarkwebhook/
```
