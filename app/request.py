import urllib.request,json
from .models import Qoutes

def get_quote():
    qoute_api='http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(qoute_api) as url:
        qoutes = url.read()
        qoutess = json.loads(qoutes)


        if qoutess:
            id = qoutess.get('id')
            author = qoutess.get('author')
            quote= qoutess.get('quote')

            allquotes =Qoutes(id,author,quote)

    return allquotes