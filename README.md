# Large Flask App Structure Demo
This web app demonstrates how I would structure a large web app using Flask.
I employ Flask Blueprints to bring modularity to routes and functionality.

Visual Structure:
```
.
├── app
│   ├── __init__.py
│   ├── index
│   │   ├── templates
│   │   │   └── index.html
│   │   └── routes.py
│   └── api
│       ├── templates
│       │   └── index.html
│       └── routes.py
└── run.py
```
Each folder within the app directory holds a blueprint along with its associated routes. This in turns makes the app more modular and re-usable.
