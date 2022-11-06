from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginator(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_query_param = "page"
    page_size_query_param = "limit"

    def get_paginated_response(self, data):
        return Response({
            'status': 'success',
            'data': {
                'count': self.page.paginator.count,
                'page_current': self.page.number,
                'page_max': self.page.paginator.num_pages,
                'page_limit': self.page.paginator.per_page,
                'posts': data
            },
            'message': ''
        })
