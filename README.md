# Website2Docset
[![pytest python](https://github.com/Var7600/website2docset/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Var7600/website2docset/actions/workflows/python-app.yml)

Convert HTML documentation to Dash/Zeal docsets easily. This tool helps you transform your HTML documentation into a format compatible with documentation browsers like Dash and Zeal.

## Features

- Convert HTML documentation to Dash/Zeal compatible docsets
- Automatic index generation for quick searching
- Support for custom icons
- Configurable metadata
- Support for different entry types (Function, Class, Section, etc.)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

## Installing

```bash
git clone https://github.com/Var7600/website2docset.git
cd website2docset
pip install -e .
```

## Usage

### Basic Usage

Convert a documentation directory to a docset:

```bash
website2docset.py  -n MyDocs -v 1.0 path/to/docs
```

### Command Line Options

```bash
 options:
  -n, --name          Name of the docset
  -v, --version       Version of the docset (default: 0.0)
  -i, --icon          Path to PNG icon (16x16 pixels)
  -d, --destination   Output directory
```

### Examples

1. **Create a basic docset:**
   
   ```bash
   website2docset.py -n Python3 -v 1.0 ./python-docs
   ```

2. **Include a custom icon:**
   
   ```bash
   website2docset.py -n Python3 -v 1.0 -i icon.png ./python-docs
   ```

3. **Specify output directory:**
   
   ```bash
   website2docset.py -n Python -v 1.0 -d ~/Docsets ./python-docs
   ```

## Documentation Structure

Your HTML documentation should follow this structure:

```
documentation/
├── index.html
├── page1.html
├── page2.html
└── assets/
    ├── css/
    └── js/
```

The `index.html`**file should contain links/href references to all documentation pages with appropriate class attributes for indexing.**

## Configuration

### Entry Types

The following entry types are supported in your HTML:

- Function

- Class

- Section

- Guide

- Library

- Type

- Variable

- Macro
  
  for more about supported entry types see https://kapeli.com/docsets#supportedentrytypes

Add them as class attributes to your links(**entry types  should be first in your class attributes**):

```html
<a href="function.html" class="Function">My Function</a>
```

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/Var7600/website2docset.git
cd website2docset

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

This project follows PEP 8 guidelines. To check your code:

```bash
flake8 website2docset.py
```

static analyzer mypy. To check your code:

```bash
mypy website2docset.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/Develop`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/Develop`)
5. Open a Pull Request

### Guidelines for contributing:

- Write tests for new features
- Update documentation as needed
- Follow the existing code style
- Write meaningful commit messages

## License

 MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [GitHub - zealdocs/zeal: Offline documentation browser inspired by Dash](https://github.com/zealdocs/zeal/)

- [Dash Documentation](https://kapeli.com/docsets#dashDocset)

## Support

**If you find any bugs or have feature requests, please create an issue on GitHub.**
