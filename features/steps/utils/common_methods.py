def subscription_post(context):
    context.payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    context.url = "https://api.restful-api.dev/objects"
    context.headers = {"Content-Type": "application/json"}
    return context.payload, context.url, context.headers