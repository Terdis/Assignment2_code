import logging

import azure.functions as func
from utils import integral


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    min_max = req.params.get('min_max')

    if not min_max:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            min_max = req_body.get('min_max')

    if min_max:
        min_x, max_x=min_max.split("_")
        values=integral.sinIntegral(float(min_x), float(max_x))
        return func.HttpResponse(f"I got the values {values}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
