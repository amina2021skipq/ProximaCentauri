import boto3
import constant as constants

class cloudWatchPutMatric:
    def __init__(self):
        self.client = boto3.client('cloudwatch')
        
    def put_data(self, nameSpace, metricName, dimensions, value):
        response = self.client.put(
            Namespace= nameSpace,
            MatricData=[
                {
                    'MetricName':metricName,
                    'Dimensions':dimensions,
                    'Value':value
                    
                    
                }]
            )