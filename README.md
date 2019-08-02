Python package to load Google Ad's API request directly into Tensorflow. 
It supports two functionalities:
1. Download all of the API requests into a CSV. Use the the CSV to load data into tensorflow. 


Clone Repo:
Install requirements to be imported locally : pip install -e . 


Usage:
  1. Put the Google ads yaml file in the same directory as readme.
  2. from load_data_tensorflow import standalone_streaming 
		  : standalone_streaming.main()   
		 :: This calls the streaming tensorflow code.
  3. from load_data_tensorflow import csv_data_load  
		 : csv_data_load.main()  
		 :: This builds up the CSV package after loading all data and then loads into tensorflow. 
