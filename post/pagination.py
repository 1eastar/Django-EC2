from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class EssayPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        # return super().get_paginated_response(data)
        return Response({
            'links':{
                'prev':self.get_previous_link(),
                'next':self.get_next_link()
            },
            'count':self.page.paginator.count,
            'result':data
        })