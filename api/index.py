def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": "<h1>Hello from Python on Vercel 🚀</h1>"
    }