# Articles Management System

A Python-based article management system that demonstrates relationships between authors, magazines, and articles using SQLite database and Object-Relational Mapping (ORM) patterns.

## Project Structure

```
project/
├── lib/
│   ├── db/
│   │   ├── connection.py      # Database connection utilities
│   │   ├── schema.sql         # Database table definitions
│   │   └── seed.py           # Initial data population
│   ├── models/
│   │   ├── author.py         # Author model with business logic
│   │   ├── magazine.py       # Magazine model with business logic
│   │   └── article.py        # Article model with business logic
│   └── debug.py              # Interactive CLI for testing
├── scripts/
│   └── setup_db.py           # Database initialization script
└── db/
    └── development.db        # SQLite database file (created after setup)
```

## Features

### Core Models
- **Author**: Manages author information and their articles
- **Magazine**: Handles magazine data including categories
- **Article**: Links authors to magazines with article titles

### Key Functionality
- Create and manage authors, magazines, and articles
- Find entities by ID, name, or title
- Track relationships between authors and magazines
- Identify top magazines by article count
- List contributing authors and topic areas

## Database Schema

The system uses three main tables with proper foreign key relationships:

- **authors**: `id`, `name`
- **magazines**: `id`, `name`, `category`
- **articles**: `id`, `title`, `author_id`, `magazine_id`

Includes optimized indexes for better query performance on foreign keys and categories.

## Setup Instructions

### Prerequisites
- Python 3.6+
- SQLite3 (usually included with Python)

### Installation

1. **Clone or download the project files**

2. **Set up the database**:
   ```bash
   python scripts/setup_db.py
   ```
   
   This command will:
   - Create the SQLite database at `db/development.db`
   - Set up all required tables with proper relationships
   - Populate the database with sample data (3 authors, 3 magazines, 7 articles)

3. **Verify installation**:
   ```bash
   python lib/debug.py
   ```

## Usage Examples

### Using the Interactive CLI

Run the debug CLI to interact with your data:

```bash
python lib/debug.py
```

Available commands:
- `1` - Show the magazine with the most articles
- `2 <author_name>` - List all articles by a specific author
- `3 <magazine_name>` - List all articles in a specific magazine
- `4` - Exit the program

Example session:
```
>>> 1
Top Magazine: Tech Weekly (Technology)

>>> 2 Alice Smith
Articles by Alice Smith:
 - AI in 2025
 - Tech for Good
 - Cultural Commentary

>>> 3 Health Monthly
Articles in Health Monthly:
 - Meditation Benefits
 - Healthy Eating
```

### Using the Models Programmatically

```python
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Find an author and their articles
author = Author.find_by_name("Alice Smith")
articles = author.articles()

# Find a magazine and its contributors
magazine = Magazine.find_by_name("Tech Weekly")
contributors = magazine.contributors()

# Create new content
new_author = Author("Jane Doe")
new_author.save()

tech_magazine = Magazine.find_by_name("Tech Weekly")
new_author.add_article(tech_magazine, "The Future of AI")
```

## Code Architecture Explanation

### Database Connection (`lib/db/connection.py`)
- **Purpose**: Centralized database connection management
- **Key Feature**: Uses `sqlite3.Row` factory for dictionary-like access to query results
- **Pattern**: Connection factory pattern for consistent database access

### Models (`lib/models/`)
Each model follows the Active Record pattern:

- **Constructor**: Initializes object properties (with optional ID for existing records)
- **save()**: Persists new objects to database and sets the ID
- **Static finders**: Class methods like `find_by_id()` and `find_by_name()`
- **Relationship methods**: Handle associations between models (e.g., `author.articles()`)

### Key Programming Concepts Demonstrated

1. **Object-Relational Mapping (ORM)**: Models represent database tables as Python classes
2. **Foreign Key Relationships**: Articles link to authors and magazines via IDs
3. **SQL Query Optimization**: Indexes on frequently queried columns
4. **Circular Import Prevention**: Models import each other only within methods when needed
5. **Database Transactions**: Proper commit/close patterns for data integrity

## Sample Data

The system comes pre-loaded with:

**Authors:**
- Alice Smith (writes about Technology and Art)
- Bob Johnson (writes about Health)
- Charlie Rose (writes about Art)

**Magazines:**
- Tech Weekly (Technology category)
- Health Monthly (Health category)  
- Art & Culture (Art category)

**Articles:**
- Various articles connecting authors to appropriate magazines

## Extending the System

To add new functionality:

1. **New Model**: Create a new class in `lib/models/` following the existing pattern
2. **Database Changes**: Update `schema.sql` and re-run setup
3. **Relationships**: Add methods to link your new model with existing ones
4. **CLI Commands**: Extend `debug.py` to test new features

## Troubleshooting

- **Database not found**: Run `python scripts/setup_db.py` to create it
- **Import errors**: Ensure you're running scripts from the project root directory
- **Empty results**: Check that the database was properly seeded with sample data

---

This project demonstrates fundamental database relationships and ORM patterns commonly used in web applications and data management systems.