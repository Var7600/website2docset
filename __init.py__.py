"""
website2docset - A tool to convert HTML documentation to Dash/Zeal docsets
"""

from website2docset import db_connection, init_db, update_db, add_urls

__version__ = '0.0'
__author__ = 'DOUDOU DIAWARA'
__email__ = 'zeta2@duck.com'

# Export the main functions that users will need
__all__ = [
    'db_connection',
    'init_db',
    'update_db',
    'add_urls',
    'add_infoplist',
    'add_meta',
    'check_icon_size',
    'copy_docs'
]