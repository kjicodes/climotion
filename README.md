# Climotion API

A weather-aware workout planner for registered users. Enter a city to get current weather conditions and a recommendation on whether to work out indoors or outdoors. Create an account to get personalized exercise recommendations and save workouts with reflection notes.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework, PostgreSQL, JWT (Simple JWT)
- **Frontend:** React, Tailwind CSS — see [climotion-frontend](https://github.com/kjicodes/climotion-frontend)
- **APIs:** OpenWeatherMap API, API Ninjas Exercises API, Google Gemini API
- **Testing:** Postman

## Features

- City-based weather lookup with current conditions, temperature, and daily high/low
- AI-generated weather description and indoor/outdoor workout recommendation powered by Google Gemini, cached per unique weather condition and temperature combination
- User registration and login with JWT authentication
- Personalized exercise recommendations based on workout type, difficulty, and target muscle groups (authenticated users only)                                                                  
- Save, view, update, and delete workouts with before and after reflection notes (authenticated users only)
- Previously searched cities saved for quick access

## Local Setup

1. Install dependencies: `pip install -r requirements.txt`

2. Create a `.env` file in the project root:
   ```
   SECRET_KEY=
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://localhost:5432/climotion
   OPENWEATHER_API_KEY=
   OPENWEATHER_BASE_URL=https://api.openweathermap.org/data/2.5/weather
   GEOCODING_BASE_URL=http://api.openweathermap.org/geo/1.0/direct
   EXERCISES_API_KEY=
   EXERCISES_BASE_URL=https://api.api-ninjas.com/v1/exercises
   GOOGLE_GEMINI_API_KEY=
   ```

3. Create a local PostgreSQL database named `climotion`, then run:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## API Endpoints

   **Public**
   - `GET /api/weather/?city=London` - retrieves current weather conditions for a given city
   - `GET /api/searched-cities/` - retrieves a list of previously searched cities
   - `POST /api/users/` - registers a new user
   - `POST /api/token/` - authenticates a user and receives a JWT access token
   
   **Authenticated**
   - `GET /api/workouts/?exercise-type=strength&difficulty=beginner&muscle-group=upper` - retrieves a list of exercises filtered by type, difficulty, and target muscle group
   - `GET/POST /api/saved-workouts/` - retrieves saved workouts or saves a new one with before/after workout reflection notes
   - `GET/PATCH/DELETE /api/saved-workouts/<id>/` - retrieves, updates, or deletes a specific saved workout

## Roadmap

- [x] City-based weather lookup and indoor/outdoor workout recommendation
- [x] Exercise recommendations by workout type and difficulty level
- [x] Muscle group selector for strength training
- [x] Migrate backend to Django REST Framework
- [x] Searched Cities - save frequently searched cities
- [x] Saved Workouts - save and revisit previously generated workouts
- [x] User authentication
- [x] Replaced hard-coded weather descriptions with AI-generated descriptions via Google Gemini
- [ ] React frontend — in progress, see [climotion-frontend](https://github.com/kjicodes/climotion-frontend)
