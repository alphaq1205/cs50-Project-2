# Project 2

This is a web application on which one login with any nick name. user can chat with random people who alredy have registered on this web application. A user can also create a new channel or can choose to chat in a particular channel created by other users. This web application is built on flask and javascript.

The sections of this website are:-

### Front Page
This is sort of a welcome page which contain signIn navigation buttons which will take user to registration page.

### Registration
- Users is able to register on this website by providing a nick name, as a user enters name user will be taken to homepage.
- Registered name will be associated with every message the user sends. If a user closes the page and returns to your app later, the display name will still be remembered.

### Logout
User is able to logout from the website once user is loged in by click the logout button on homepage. 

* NOTE: User can login anytime to the website with the same name user registered and can continue from where he left.

### Homepage
This is the maine page of the application where a user can do following things :-
1. Create channel:
- Once user enter the website he can see the list of channel created by other users and can choose to select the particular channel he wants to chat in.
- A user can also create it's own channel according to his own intrest in which other users can also chat.
- A user is able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.
- If a user is on a channel page, closes the web browser window, and goes back to your web application, application will remember what channel the user was on previously and take the user back to that channel.

2. Chat:
- Once a channel is selected, the user will see any messages that have already been sent in that channel, up to a maximum of 100 messages. App will only store the 100 most recent messages per channel in server-side memory.
- Once in a channel, users will be able to send text messages to others the channel. When a user sends a message, their display name and the timestamp of the message will be associated with the message. All users in the channel will then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages will NOT require reloading the page.

3. Personal Touch:
- A user is able to differentiate between his own messages and other messages in a chat room.
