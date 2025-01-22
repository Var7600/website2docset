# tests/conftest.py - 
import pytest
import os
import tempfile
import shutil

@pytest.fixture
def temp_dir():
    """create a temporary directory for testing."""
    test_dir = tempfile.mkdtemp()
    yield test_dir
    shutil.rmtree(test_dir)
    

@pytest.fixture
def sample_html_dir(temp_dir):
    """create a sample HTML directory structure for testing."""
    # Create test HTML content
    index_content = """
    <html>
        <body>
            <a href="page1.html" class="Function">Test Function</a>
            <a href="page2.html" class="Section">Test Section</a>
        </body>
    </html>
    """
    
    # Create directory structure
    os.makedirs(os.path.join(temp_dir, "test_docs"))
    
    #write index file
    with open(os.path.join(temp_dir, "test_docs", "index.html"), "w") as file:
        file.write(index_content)
        
    # wrtie sample pages
    with open(os.path.join(temp_dir, "test_docs", "page1.html"), "w") as file:
        file.write("<html><body>Test Page 1</body></html>")
        
    with open(os.path.join(temp_dir, "test_docs", "page2.html"), "w") as file:
        file.write("<html><body>Test Page 2</body></html>")
    
    return os.path.join(temp_dir, "test_docs")