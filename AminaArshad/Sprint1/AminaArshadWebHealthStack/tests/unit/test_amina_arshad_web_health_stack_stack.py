import aws_cdk as core
import aws_cdk.assertions as assertions

from amina_arshad_web_health_stack.amina_arshad_web_health_stack_stack import AminaArshadWebHealthStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in amina_arshad_web_health_stack/amina_arshad_web_health_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AminaArshadWebHealthStackStack(app, "amina-arshad-web-health-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
