# Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Both are really similar and very useful, but where they distinguish is that Python is more of a multi-threaded language where you can use for more of the backend, and Javascript is more single threaded and can be more used for front-end.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.
  Without the programming crashing we can use get(key,def_val) because this method will try to look for c, and if c is not present it will return the def_val. The second way it is to use setdefault(key, def_value) which works the same but the difference is that because c is absent, a new key will be created with the def_value associated with the key passed in arguments.

- What is a unit test?
  A unit test is that the amount that your testing is small. Meaning that it test the individual components.

- What is an integration test?
  An integration test is that the amount that your testing is multiple. Meaning that it test if the indivual componets go well together.

- What is the role of web application framework, like Flask?
  The role of web application framework, like Flask is that it enables the user to create web applications, which allows us to to divide the content into routes and start a server which comes with the GET and POST request.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Well, depending on the application, the /foods/pretzel would already be predefined or could be another type of food. And foods?type=pretzel can be more of a search based routing of the user.

- How do you collect data from a URL placeholder parameter using Flask?
  The way that one collect data from a URL placeholder parameter using Flask is by request.args[]

- How do you collect data from the query string using Flask?
  The way that one collect data from the query string using using Flask is by request.url[]

- How do you collect data from the body of the request using Flask?
  The way that one collect data from the body of the request using Flask is by request.args.get[]

- What is a cookie and what kinds of things are they commonly used for?
  Cookies are pieces of data that are tied to a user that will be used whenever the user visits the website again. They are commonly used for search history, user preferences, and for buying items.

- What is the session object in Flask?
  A session object in Flask is that it tracks the session data of the user and stores it.

- What does Flask's `jsonify()` do?
  It will return flask data that need to be turned into the JSON format for frontend API's to received.
