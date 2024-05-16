class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0

    def __call__(self, request):
        # Increment the request count for each request
        self.request_count += 1

        # Pass the request to the next middleware or view
        response = self.get_response(request)

        return response
        