from aws_cdk import (
   core as cdk,
   aws_lambda as lambda_,
   aws_events as events_,
   aws_events_targets as targets_,
   aws_iam
)

class AminaArshadWebHealthStackStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #webhealth lambda funcion
        lambda_role = self.create_lambda_role()
        helloLambda = self.create_lambda('HelloLambdaFunction', './Resources', 'web_Health_lambda.lambda_handler', lambda_role)
        
        #invoke lambda for every minute
        lambda_schedule= events_.Schedule.rate(cdk.Duration.minutes(1))
        lambda_target= targets_.LambdaFunction(handler=helloLambda)
        rule = events_.Rule(self, "Web Health Invocation - Amina", description="Periodic Lambda", enabled=True, schedule=lambda_schedule, targets=[lambda_target])
        
    
    def create_lambda_role(self):
        lambdaRole = aws_iam.Role(self, "lambda-role",
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'), 
            managed_policies=[
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('CloudwatchFullAccess')
                            ])
        return lambdaRole
            

            
            
    def create_lambda(self, id, asset, handler, role):
        return lambda_.Function(self, id,
        code=lambda_.Code.from_asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6,
        role=role
        )
