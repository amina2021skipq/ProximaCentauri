import datetime
import urllib3
import constant
import boto3

    
def put_data(nameSpace, metricName, dimensions, value):
    
    client = boto3.client('cloudwatch')
    response = client.put_metric_data(
        Namespace= nameSpace,
        MetricData=[
            {
                'MetricName':metricName,
                'Dimensions':dimensions,
                'Value':value
            }]
        )
            
            
def lambda_handler(events, context):
    values=dict()
    
    avail =get_availability()
    
    dimensions=[
        {'Name': 'URL' , 'Value' : constant.URL_TO_MONITOR},
        {'Name': 'Region' , 'Value' : 'DUB'}
        ]
        
    put_data(constant.URL_MONITOR_NAMESPACE, constant.URL_MONITOR_AVAILABILITY, dimensions, avail)
        
    latency=get_latency()
    dimensions=[
        {'Name': 'URL' , 'Value' : constant.URL_TO_MONITOR},
        {'Name': 'Region' , 'Value' : 'DUB'}]
        
    put_data(constant.URL_MONITOR_NAMESPACE, constant.URL_MONITOR_LATENCY, dimensions, latency)
    
    values.update({"availability":avail, "latency":latency})
    return values
   

def get_availability():
    http = urllib3.PoolManager()
    response = http.request("GET", constant.URL_TO_MONITOR)
    if response.status==200:
        return 1.0
    else:
        return 0.0
    

def get_latency():
    http = urllib3.PoolManager()
    start =datetime.datetime.now()
    response = http.request("GET", constant.URL_TO_MONITOR)
    end = datetime.datetime.now()
    delta= end-start
    latencySec = round(delta.microseconds * .000001, 6)
    return latencySec
    