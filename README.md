# Django Chat

## The Task

### Implement a chat system:

This task would involve creating a real-time chat system for the application using Django and a web socket library such as Django Channels. The developer would be expected to design the chat interface, handle message sending and receiving, and implement user authentication and authorization for the chat feature.

They may also need to integrate the chat functionality with the rest of the application, such as displaying the chat history on user-specific pages or adding notifications for new messages.

---

## The Solution

The solution is based on the Django Channels tutorial:
https://channels.readthedocs.io/en/stable/tutorial/index.html

Additional resources used:

- Reconnecting websocket:
https://github.com/joewalnes/reconnecting-websocket

- User registration tutorial
https://ordinarycoders.com/blog/article/django-user-register-login-logout

- Django Bootstrap forms
https://ordinarycoders.com/blog/article/render-a-django-form-with-bootstrap

---

## Testing notes
- Before testing the solution, make sure you have Redis server on port 6379 (127.0.0.1:6379).
- Make sure Poetry dependency manager is installed in the testing environment.
- Clone the `dev` branch into a local directory.
- Install dependencies via `poetry install` .
- Navigate to the `src` folder and run Django server via `python manage.py runserver`.
- Open a browser and navigate to `127.0.0.1:8000` or `127.0.0.1:800/chat`.
- For a secondary user, open another browser window in a private mode or use a different browser.
- For admin access, navigate to `127.0.0.1:8000/admin`.
 
---
## TODO list:

- Add correct appearance of active/inactive users in the sidebar instead of using placeholders.
- Improve upon styling.
- Add unit/integration tests.

## Items for further consideration:

- Chat rooms alike Slack
- Settings for updating user profile, changing theme, etc.
- Integration with external resources such as social networks.
---

