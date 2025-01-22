# tests/test_database.py
import pytest
import sqlite3
import os
from website2docset import db_connection, init_db, update_db

def test_db_connection(temp_dir):
    """Test database connection creation."""
    db_path = os.path.join(temp_dir, "test.db")
    
    with db_connection(db_path) as db:
        assert isinstance(db, sqlite3.Connection)
    
    assert  os.path.exists(db_path) 
    

def test_init_db(temp_dir):
    """Test database initialization."""
    db_path = os.path.join(temp_dir, "test.db")
    
    
    with db_connection(db_path) as db:
        init_db(db)
        
        # Verify table exists
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='searchIndex';")
        assert cursor.fetchone() is not None
        
        # Verify table structure
        cursor.execute("PRAGMA table_info(searchIndex);")
        columns = cursor.fetchall()
        assert len(columns) == 4
        assert any(col[1] == 'id' for col in columns)
        assert any(col[1] == 'name' for col in columns)
        assert any(col[1] == 'type' for col in columns)
        assert any(col[1] == 'path' for col in columns)
        

def test_update_db(temp_dir):
    """Test database record updating."""
    db_path = os.path.join(temp_dir, "test.db")
    
    with db_connection(db_path) as db:
        init_db(db)
        
         # Test inserting new record
        update_db(db, "Test Function", "Function", "test.html")
        
        cursor = db.cursor()
        cursor.execute("SELECT * FROM searchIndex WHERE name=?", ("Test Function",))
        record = cursor.fetchone()
        
        assert record is not None
        assert record[1] == "Test Function"
        assert record[2] == "Function"
        assert record[3] == "test.html"
        
        # Test duplicate insertion
        update_db(db, "Test Function", "Function", "test.html")
        cursor.execute("SELECT COUNT(*) FROM searchIndex WHERE name=?", ("Test Function",))
        count = cursor.fetchone()[0]
        assert count == 1  # Should still only be one record