from app import app

# This line ensures that Flask will work with Vercel's serverless platform.
def handler(event, context):
    return app(event, context)
