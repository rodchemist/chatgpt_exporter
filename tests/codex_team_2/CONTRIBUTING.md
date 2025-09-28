# Contributing Guidelines

## Overview
We welcome contributions to the Universal Documentation System! This guide outlines the process for contributing code, documentation, and improvements to the project.

## Installation for Development
Set up your development environment:

```bash
# Clone and setup
git clone <repository>
cd <project>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Initialize system
python agents/scripts/documentation_engine.py --init
```

## How to Contribute

### 1. Fork and Clone
```bash
# Fork the repository on GitHub
git clone https://github.com/yourusername/project.git
cd project
```

### 2. Create Feature Branch
```bash
git checkout -b feature/AmazingFeature
```

### 3. Implement Changes
- Write clean, documented code
- Add tests for new functionality
- Update documentation as needed

### 4. Test Your Changes
```bash
# Run verification
python agents/scripts/documentation_engine.py --verify

# Check quality metrics
python agents/scripts/documentation_engine.py --metrics

# Run tests if available
pytest tests/
```

### 5. Commit and Push
```bash
git add .
git commit -m 'Add AmazingFeature: description of changes'
git push origin feature/AmazingFeature
```

### 6. Open Pull Request
Submit a pull request with:
- Clear description of changes
- Reference to related issues
- Screenshots if applicable

## Code Standards

### Python Style Guide
- Follow PEP 8 for Python code formatting
- Use type hints where appropriate
- Add comprehensive docstrings to all functions and classes
- Include unit tests for new functionality
- Maintain backward compatibility

### Example Code Style
```python
def calculate_quality_score(self, doc_path: Path) -> float:
    """
    Calculate documentation quality score based on content analysis.

    Args:
        doc_path: Path to the documentation file

    Returns:
        Quality score from 0.0 to 100.0
    """
    # Implementation here
    pass
```

## Documentation Standards

### Markdown Guidelines
- Use clear, descriptive headings
- Include code examples with syntax highlighting
- Add installation and usage sections
- Keep language clear and concise
- Update CHANGELOG.md for all changes

### API Documentation
```python
# Document all public methods
def scan_project(self) -> Dict[str, Any]:
    """
    Comprehensive project scan for documentation needs.

    Returns:
        Dictionary containing scan results with keys:
        - source_files: List of discovered source files
        - documentation_files: List of existing documentation
        - missing_docs: List of missing required documentation
        - services: List of discovered services
    """
```

## Usage Examples

### Testing Contributions
```bash
# Verify implementation completeness
python agents/scripts/documentation_engine.py --verify

# Generate and test documentation
python agents/scripts/documentation_engine.py --generate
python agents/scripts/documentation_engine.py --metrics
```

## License
By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---
*Contributing Guidelines v1.0.0*
