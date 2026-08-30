# Contributing to AI-Powered Multi-Agent Data Pipeline Orchestrator

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

---

## 🎯 How to Contribute

We welcome contributions in the following areas:

### 1. **Code Contributions**

- Bug fixes
- Feature enhancements
- Performance optimizations
- Code refactoring

### 2. **Documentation**

- README improvements
- Setup guide enhancements
- Code comments and docstrings
- Troubleshooting guides

### 3. **Testing**

- Unit tests
- Integration tests
- Test dataset creation
- Edge case validation

### 4. **Infrastructure**

- Docker support
- Kubernetes deployment configs
- GitHub Actions CI/CD
- Cloud deployment guides

### 5. **Features (Roadmap)**

- [ ] Streaming CSV support
- [ ] Real-time monitoring dashboard
- [ ] Additional validation rules (email, date, phone formats)
- [ ] More LLM integrations (OpenAI, Claude, etc.)
- [ ] Performance optimization & caching
- [ ] Audit logging system
- [ ] Notification system (email, Slack)
- [ ] Business Insights Agent
- [ ] Root Cause Analysis Agent

---

## 🚀 Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub
```

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator.git
cd AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/bug-description
```

### 4. Set Up Development Environment

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Optional: Install development tools
pip install pytest pytest-cov black flake8
```

### 5. Make Your Changes

- Keep commits atomic and well-described
- Follow PEP 8 style guide
- Add docstrings to functions
- Write tests for new features

### 6. Test Your Changes

```bash
# Run unit tests
pytest

# Check code style
flake8 app/
black --check app/

# Run the application locally
uvicorn app.main:app --reload
```

### 7. Commit and Push

```bash
git add .
git commit -m "Brief description of changes"
git push origin feature/your-feature-name
```

### 8. Create a Pull Request

- Go to GitHub and click "Compare & pull request"
- Write a clear description of changes
- Reference any related issues (#123)
- Wait for review and feedback

---

## 📋 Code Style Guidelines

### Python Formatting

- Use **PEP 8** style guide
- Max line length: 100 characters
- Use type hints for functions
- Write docstrings for classes and functions

### Example:

```python
def process_data(data: pd.DataFrame, threshold: float = 0.8) -> dict:
    """
    Process input data and return quality metrics.

    Args:
        data: Input DataFrame
        threshold: Quality threshold (0-1)

    Returns:
        Dictionary with quality metrics

    Raises:
        ValueError: If threshold is invalid
    """
    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be between 0 and 1")

    # Implementation here
    return {}
```

### Naming Conventions

- Variables: `snake_case` (e.g., `pipeline_status`)
- Classes: `PascalCase` (e.g., `IngestAgent`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
- Private methods: `_leading_underscore` (e.g., `_validate_input`)

---

## 🧪 Testing

### Add Tests for New Features

```bash
# Tests directory structure
app/
├── agents/
│   └── __pycache__/
├── tests/
│   ├── test_agents.py
│   ├── test_workflow.py
│   └── test_validation.py
```

### Example Test:

```python
import pytest
from app.agents import IngestAgent

def test_ingest_agent_metadata():
    """Test metadata collection in ingest agent."""
    agent = IngestAgent()
    metadata = agent.collect_metadata("data/raw/sales.csv")

    assert metadata is not None
    assert "file_hash" in metadata
    assert "row_count" in metadata
```

### Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest app/tests/test_agents.py

# Run with coverage
pytest --cov=app
```

---

## 📝 Commit Message Guidelines

Use clear, descriptive commit messages:

```
# Good
git commit -m "Add streaming CSV support to ingest agent"
git commit -m "Fix null value detection in validator agent"
git commit -m "Optimize silver layer transformation performance"

# Avoid
git commit -m "Fix bug"
git commit -m "Update code"
git commit -m "WIP"
```

---

## 🐛 Reporting Bugs

### Before Reporting

- Check existing issues
- Verify you're using latest version
- Test with included datasets

### Create an Issue with:

1. **Title**: Clear, concise description
2. **Description**: What's the problem?
3. **Steps to Reproduce**:
   ```
   1. Run command X
   2. Load file Y
   3. Observe behavior Z
   ```
4. **Expected vs Actual**: What should happen vs what happened
5. **Environment**: Python version, OS, Databricks version
6. **Logs/Screenshots**: Error messages and relevant output

---

## 📚 Documentation

### Update README if you:

- Add new features
- Change API endpoints
- Modify setup instructions
- Fix known issues

### Create CHANGELOG entry:

- Add entry under `[Unreleased]`
- Follow [Keep a Changelog](https://keepachangelog.com/) format
- Include: Added, Changed, Fixed, Removed sections

---

## 🔒 Security

- Never commit `.env` files or secrets
- Don't include personal credentials
- Sanitize sensitive data in logs
- Use environment variables for config

---

## 📋 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] All tests pass locally
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] No sensitive data in commits
- [ ] Commit messages are clear
- [ ] Branch is up-to-date with main
- [ ] No merge conflicts

---

## 🏆 Recognition

All contributors will be recognized in:

- Project README
- Release notes
- GitHub contributors page

---

## ❓ Questions?

- Check [SETUP_AND_RUNBOOK.md](SETUP_AND_RUNBOOK.md) for setup help
- Open an issue for discussions
- Comment on PRs with questions
- Reach out to maintainers

---

## 📜 License

By contributing, you agree your code will be licensed under the MIT License.

---

**Thank you for contributing! 🚀**

Together we're building the future of AI-powered data engineering.
