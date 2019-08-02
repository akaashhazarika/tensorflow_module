def get_keywords_and_impressions(client, customer_id, page_size):
  """Get keywords, impressions and cost in micros, from customers account
     where ad_group_status is enabled and ad_group_criterion is
     either enabled or paused. 

  Args:
    client: An instance of the google.ads.google_ads.client.GoogleAdsClient class.
    campaign_id: (str) The ID of the campaign under which to create a new ad group.
    page_size: (int) Maximum Page size. Response will be chunked if it is more than
    the page size.

  Returns:
    (list) List of Responses along with a list of clumn names. 
  """
  ga_service = client.get_service('GoogleAdsService', version='v2')
  results = []

  query = ('SELECT ad_group_criterion.keyword.text, '
            'metrics.impressions, metrics.clicks, metrics.cost_micros '
            'FROM keyword_view WHERE segments.date DURING LAST_7_DAYS '
            'AND ad_group.status = \'ENABLED\' '
            'AND ad_group_criterion.status IN (\'ENABLED\', \'PAUSED\') '
            'ORDER BY metrics.impressions DESC '
            'LIMIT 100')
  response = ga_service.search(customer_id, query, page_size=page_size)
  try:
    for row in response:
        criterion = row.ad_group_criterion
        metrics = row.metrics
        results+= [criterion.keyword.text.value,
                  metrics.impressions.value,
                  metrics.cost_micros.value],
    return [[results],['Keyword', 'Impressions', 'Cost_Micros']]
  except GoogleAdsException as ex:
    print('Request with ID {} failed with status {} and includes the '
            'following errors:'.format(ex.request_id, ex.error.code().name))
    return None



def grpc_iterator(client, customer_id, page_size):
  """Get keywords, impressions and cost in micros, from customers account
     where ad_group_status is enabled and ad_group_criterion is
     either enabled or paused. 

  Args:
    client: An instance of the google.ads.google_ads.client.GoogleAdsClient class.
    campaign_id: (str) The ID of the campaign under which to create a new ad group.
    page_size: (int) Maximum Page size. Response will be chunked if it is more than
    the page size.

  Returns:
    (GRPC Iterator) An iterator for the response received. 
  """
    ga_service = client.get_service('GoogleAdsService', version='v2')
    results = []

    query = ('SELECT ad_group_criterion.keyword.text, '
        'metrics.impressions, metrics.clicks, metrics.cost_micros '
        'FROM keyword_view WHERE segments.date DURING LAST_7_DAYS '
        'AND ad_group.status = \'ENABLED\' '
        'AND ad_group_criterion.status IN (\'ENABLED\', \'PAUSED\') '
        'ORDER BY metrics.impressions DESC '
        'LIMIT 100')
    response = ga_service.search(customer_id, query, page_size=page_size)
    return response
