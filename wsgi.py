# import newrelic.agent
# newrelic.agent.initialize('/home/ec2-user/flask_api_example/newrelic.ini')

import os

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(debug=True)
