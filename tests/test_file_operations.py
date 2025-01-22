# tests/test_file_operations.py
import pytest
import os
from website2docset import add_urls, db_connection

def test_add_urls(sample_html_dir, temp_dir):
    """Test URL extraction and database population."""
    db_path = os.path.join(temp_dir, "test.db")
    path = os.path.join(temp_dir, "test_docs")
    
    # Run the URL addition
    add_urls(db_path, path)
    
    # Verify database contents
    with db_connection(db_path) as db:
        cursor = db.cursor()
        
        # Check first entry
        cursor.execute("SELECT * FROM searchIndex WHERE path=?", ("page1.html",))
        record = cursor.fetchone()
        assert record is not None
        assert record[1] == "Test Function"
        assert record[2] == "Function"
        
        # Check second entry
        cursor.execute("SELECT * FROM searchIndex WHERE path=?", ("page2.html",))
        record = cursor.fetchone()
        assert record is not None
        assert record[1] == "Test Section"
        assert record[2] == "Section"