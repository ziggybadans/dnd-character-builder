# D&D Character Builder
A web application that will be deployed to players for creating and managing Dungeons & Dragons 5th Edition characters.

## Current Features
- Beautiful and clean user interface with modern design and D&D-style theming
- Ability to create and manage multiple characters
- Ability to import sourcebook content from a JSON file
- Custom game system support

### Stage 1: Character Creation
- Create characters with comprehensive D&D 5E data integration:
  - Race and subrace selection with traits and abilities
  - Class and subclass selection
  - Background integration
  - Ability scores with automatic modifier calculation
  - Proficiency bonus calculation
  - Hit points and hit dice tracking
  - Skills and proficiencies
- Test by using mock data

### Stage 2: Character Sheet
- View interactive character sheets with:
  - Well laid out sheet info
  - Automatically calculated ability modifiers and skills
  - Proficiency bonus
  - Current and maximum hit points and death saves
  - Character traits and features
  - Dice roller with nice visuals

### Stage 3: Character Progression
- Equipment and inventory management with encumbrance tracking
- Level-based progression with class features
- Spell management
- Multiclassing

### Stage 4: Character Management
- Character export to PDF
- Save characters to files
- Load existing characters
- User accounts and online character storage
- Colours and backgrounds
- Customisable character sheet UI

### Beyond Stage 4
- DM tools
 - Campaign management
 - Encounter creation and tracking
 - DM screen with customisable UI
 - Soundboard
- Homebrew content support
- World wiki

## Setup
### Backend

1. Create and activate virtual environment:
```bash
python3.12 -m venv .venv
source .venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

### Frontend

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:5173

### API Documentation
Once the backend is running, you can access:
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc

## Technology Stack
- Backend:
  - Python 3.12
  - FastAPI
  - SQLite (for data storage)
  - pytest (for testing)

- Frontend:
  - React + TypeScript
  - Vite
  - Material-UI
  - Jest + React Testing Library