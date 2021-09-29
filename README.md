# Large Flask App Structure Demo
This web app demonstrates how I would structure a large web app using Flask.
I employ Flask Blueprints to bring modularity to routes and functionality.

Visual Structure:

.

├── __init__.py

├── app

│   ├── __init__.py
│   ├── index
│   │   ├── __init__.py
│   │   └── routes.py
│   └── api
│       ├── __init__.py
│       └── routes.py
└── run.py
