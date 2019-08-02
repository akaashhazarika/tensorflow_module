Python package to load Google Ad's API request directly into Tensorflow. 
It supports two functionalities:
1. Download all of the API requests into a CSV. Use the the CSV to load data into tensorflow. 
2. Support data load in tensorflow in a streaming manner. Uses generators to achieve this. 



INSTALLATION STEPS: 
1. CLONE REPO in thes same directory of google-ads-python.
2. Make sure to be inside the virtual env inside which google-ads-python is installed. 
3. pip install -r requirements.txt   (INSTALL DEPENDENCIES)
4. pip install -e .  (INSTALL PACKAGE LOCALLY)
5. Put the Google ads yaml file in the home directory(Same directory as in README). 
6. INSIDE __init__.py method specify your CUSTOMER_ID (int) . 


Usage:

  1. from load_data_tensorflow import standalone_streaming 
		  : standalone_streaming.main()   
		 :: This calls the streaming tensorflow code.
  2. from load_data_tensorflow import csv_data_load  
		 : csv_data_load.main()  
		 :: This builds up the CSV package after loading all data and then loads into tensorflow. 
