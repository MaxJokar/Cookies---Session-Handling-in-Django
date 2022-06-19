# Cookies---Session-Handling-in-Django
sometimes you might want to store some data on a per-site-visitor basisi as per the requirements of your web applicaiton .Cookies are saved on the client side and 
depend on your client browser security level, setting cookies can at times work and at times might not.
Session:Django has a session framwork , They are used to abstract the reciving and sending of cookies , data is saved on sever side like in db:
by adding some lines to the MIDDLEWARE_CLASSES  & INSTALED_APPS
