from typing import Dict
import arrowhead_client.api as ar

cpu_temp_provider = ar.ArrowheadHttpClient('cpu_temp_provider','localhost',1337,'')

def echo(request) -> Dict[str, str]:
    return {'cpu_temp': str(check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True))[7:11]}
                                       
def cpu_temp():
    return {'cpu_temp': str(check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True))[7:11]}
    
    
if __name__ == '__main__':

    
    cpu_temp_provider.provided_service( 
            service_definition='echo', 
            service_uri='echo', 
            protocol='HTTP-SECURE-JSON', 
            method='GET',
            payload_format='JSON',
            access_policy='') 
     
    cpu_temp_provider.provided_service( 
            service_definition='cpu_temp', 
            service_uri='/cpu_temp', 
            protocol='HTTP-SECURE-JSON', 
            method='GET',
            payload_format='JSON',
            access_policy='')
    
    print(cpu_temp_provider.certfile)
    print('OK')
    cpu_temp_provider.run_forever()
