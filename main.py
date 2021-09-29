from logging import debug
from app import create_app

app = create_app()

if __name__ == '__main__':
  app.run(host='localhost', port=55505, debug=True)
