import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    log.info("hello cloudwatch logs!! body: {}".format(json.dumps(body)))

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
