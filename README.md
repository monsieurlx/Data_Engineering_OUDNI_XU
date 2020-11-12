# Data_Engineering_OUDNI_XU

To test it locally you first need to install :

flask,
nltk,
vaderSentiment

To start the application :

-python3 app.py

To start the testing :

-python3 test_app.py


In order to use docker you need to first build it with :

docker build -t <name> .
  
And then you can run it by using :

docker run -p 5000:5000 <name>
