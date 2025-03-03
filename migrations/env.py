import sys
import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Add the path to the models module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base  # Ensure this import works
target_metadata = Base.metadata

# Other necessary configurations for Alembic
config = context.config

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    ...

def run_migrations_online():
    """Run migrations in 'online' mode."""
    ...

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
