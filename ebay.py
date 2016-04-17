import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
import secrets

def deals(keyword):
    try:
        api = Connection(appid=secrets.ebay, config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': keyword})

        assert(response.reply.ack == 'Success')
        assert(type(response.reply.timestamp) == datetime.datetime)
        assert(type(response.reply.searchResult.item) == list)

        item = response.reply.searchResult.item[0]
        assert(type(item.listingInfo.endTime) == datetime.datetime)
        assert(type(response.dict()) == dict)
        return response.dict()

    except ConnectionError as e:
        print(e)
        print(e.response.dict())
