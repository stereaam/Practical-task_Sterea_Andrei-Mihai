rom arrowhead_client.api import ArrowheadHttpClient

temp_consumer = ArrowheadHttpClient(
    'consumer_test',
    'localhost',
    '1338',
    '')


temp_consumer.add_orchestration_rule(service_definition='echo', method='GET')
temp_consumer.add_orchestration_rule(service_definition='cpu_temp', method='POST')
    
     
connected=False
if __name__ == '__main__':
  while not connected:
    try:
      echo_response = temp_consumer.consume_service('echo')
      cpu_temp_response = temp_consumer.consume_service('cpu_temp')
      print(echo_response)
      print(cpu_temp_response)
      print('Done')
      connected=True
    except Exception as e:
      print(e)
