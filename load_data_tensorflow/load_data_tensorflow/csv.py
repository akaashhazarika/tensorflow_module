import numpy as np
import pandas as pd
class csv_creator(object):

  def __init__(self, curr_file):
    """Instanstiate class variables with the ad's response data. 
    
    Args: 
      curr_file: (list) A multimensional list consisting of response_data
      along with names of attributes extracted. 
    """
    self.curr_file = curr_file
    self.df = None

  def extract_column_names(self):
    """Extract the names of the data attributes consisting in the response 
    data. 
    
    Returns:
      A list of attribute names coming in the response. 
    """
    return self.curr_file[1]

  def extract_data(self):
    """Extract the raw data populated inside the class variable. It internally
    calls multiple methods to reshape the response so that it becomes two 
    dimension while returning. 
    
    Returns:
      A list of raw data. Each row of response is in a list consisting of all
      data attributes. 
    """
    np_repr = np.asarray(self.curr_file[0])
    np_repr = self.flatten_numpy_array(np_repr)
    data = list(np_repr)
    return data

  def flatten_numpy_array(self, np_arr):
    """Converts the numpy array to 2 dimensions from 3 dimensions. 
    
    Args:
      np_arr: (numpy) A numpy ndarray consisting of data collected through the 
      API call. 
    
    Returns:
      A numpy array flattening the first dimension of the input attribute. 
    """
    curr_shape = np_arr.shape
    required_shape = curr_shape[1:]
    np_arr = np.reshape(np_arr, required_shape)
    return np_arr

  def create_dataframe(self):
    """Creates a pandas dataframe from the data and column names associated 
    with the class variable.
    
    Returns:
      A pandas dataframe of the data extracted through the API.
    """
    data = self.extract_data()
    col_names = self.extract_column_names()
    self.df = pd.DataFrame(data, columns = col_names) 
    return self.df

  def get_data_frame(self):
    """A getter method to get the pandas dataframe.
    
    Returns:
      Pandas Dataframe of the data extracted through the API.
    """
    self.create_dataframe()
    return self.df

  def save_to_csv(self,file_name):
    """Saves the pandas dataframe to a csv. 
    
    Args:
      file_name: (str) File name to be used while saving the csv. 
    """
    if self.df is None:
      print('Data Frame hasnt been created')
      return 
      
    if self.check_file_name(file_name):
      self.df.to_csv(file_name, index=False)
    else:
      print('Incorrect File name. Follow *.csv naming convention')

  def check_file_name(self, file_name):
    """A validator function to check if file_name is a csv.
    
    Returns:
      (bool) True or False depending on whether the file_name is a csv. 
    """
    res = file_name.split('.')
    return str(res[-1])=='csv' 
  
  def generate_streaming_data(self):
    """A demonstrator function that is used further in loaading data in a 
    streaming fashion in tensoflow. It uses generators to yield the ith indexed
    keyword for demonstration purposes. 
    
    Returns:
      A generator for the ith indexed keyword value.    
    """
    value = self.extract_data()
    for i in range(len(value)):
      yield value[i][0]
