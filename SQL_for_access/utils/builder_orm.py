from models.model import TotalRequests, RequestsByType, TopURL, Top_4XX, Top_5XX

class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client

    def create_total_requests(self, Count=None):
        if Count is None:
            Count = 0

        totalrequests = TotalRequests(
            Count=Count,
        )

        self.client.session.add(totalrequests)
        self.client.session.commit()
        return totalrequests

    def create_requests_by_type(self, Request=None, Count=None):
        if Request is None:
            Request = 'No data'
        if Count is None:
            Count = 0

        requestsbytype = RequestsByType(
            Request=Request,
            Count=Count,
        )

        self.client.session.add(requestsbytype)
        self.client.session.commit()
        return requestsbytype

    def create_top_URL(self, URL=None, Count=None):
        if URL is None:
            URL = 'No data'
        if Count is None:
            Count = 0

        topurl = TopURL(
            URL=URL,
            Count=Count
        )

        self.client.session.add(topurl)
        self.client.session.commit()
        return topurl

    def create_top_4XX(self, URL=None, Response=None, Size=None, IP=None):
        if URL is None:
            URL = 'No data'
        if Response is None:
            Response = 0
        if Size is None:
            Size = 0
        if IP is None:
            IP='No data'

        top_4xx = Top_4XX(
            URL=URL,
            Response=Response,
            Size=Size,
            IP=IP
        )

        self.client.session.add(top_4xx)
        self.client.session.commit()
        return top_4xx

    def create_top_5XX(self, IP=None, Count=None):
        if IP is None:
            IP = 'No data'
        if Count is None:
            Count = 0

        top_5xx = Top_5XX(
            IP=IP,
            Count=Count,
        )

        self.client.session.add(top_5xx)
        self.client.session.commit()
        return top_5xx