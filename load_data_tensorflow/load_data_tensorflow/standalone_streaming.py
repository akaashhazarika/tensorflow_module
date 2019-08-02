import six
import tensorflow as tf
import tensorflow_datasets as tfds
from load_data_tensorflow import CUSTOMER_ID
from load_data_tensorflow import __DEFAULT_PAGE_SIZE
from load_data_tensorflow import query
from load_data_tensorflow import csv
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException 

def main():
    """
        Calls query.py to get the GRPC iterator for the above mentioned query. 
        Iterates through the query and loads data into tensorflow at the same time. 
        It makes uses of a nested helper function to yield the retuslt for the particular row.
        Steps:
            1. Populate result variable after reading through the iterator.
            2. Call ds.take() to consume that variable.

    """
    client = GoogleAdsClient.load_from_storage("./google-ads.yaml")
    response = query.grpc_iterator(client, six.text_type(CUSTOMER_ID),
                                       __DEFAULT_PAGE_SIZE)
    
    result = None
    #Implicit Generator on the global result variable
    #to load data into tensorflow. 
    def yielder():
        yield result
    ds = tf.data.Dataset.from_generator(
    yielder, output_types=(tf.string))

    try:
        for row in response:
            criterion = row.ad_group_criterion
            result = criterion.keyword.text.value
            for value in ds.take(1):
              print(value)

    except GoogleAdsException as ex:
        print('Request with ID {} failed with status {} and includes the '
                'following errors:'.format(ex.request_id, ex.error.code().name))
    return None
