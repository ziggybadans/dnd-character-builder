# Contributing to D&D Character Builder

Thank you for your interest in contributing to the D&D Character Builder project! This document provides guidelines and instructions for contributing.

## Branch Strategy

We use a multi-branch workflow:
- `main`: Production-ready code
- `staging`: Pre-production testing
- `develop`: Main development branch

### Branch Naming Convention
- Feature branches: `feature/feature-name`
- Bug fixes: `fix/bug-name`
- Documentation: `docs/change-description`
- Releases: `release/version-number`

## Development Workflow

1. Fork the repository (if you're not a team member)
2. Create a new branch from `develop`
3. Make your changes
4. Run tests and ensure all checks pass
5. Submit a pull request

### Before Submitting a Pull Request

- [ ] Update documentation if needed
- [ ] Add/update tests as needed
- [ ] Run the test suite
- [ ] Run linting and formatting tools
- [ ] Ensure all pre-commit hooks pass
- [ ] Rebase on the latest `develop` branch

## Commit Messages

Follow the conventional commits specification:
```
<type>: <subject>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style/formatting
- `refactor`: Code refactoring
- `test`: Adding/modifying tests
- `chore`: Build process/auxiliary tool changes

Example:
```
feat: Add character creation wizard

Implement step-by-step character creation process with validation.
Includes race, class, and background selection.

Closes #123
```

## Code Style

### Python
- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use docstrings for functions and classes

### TypeScript/JavaScript
- Use ESLint configuration
- Use Prettier for formatting
- Follow React best practices
- Document components with JSDoc

## Testing

- Write unit tests for new features
- Update existing tests when modifying features
- Aim for 80%+ coverage
- Include integration tests where appropriate

## Documentation

- Update README.md if needed
- Document new features
- Update API documentation
- Include JSDoc for frontend components
- Add docstrings for Python functions

## Review Process

1. Submit PR with clear description
2. Address review comments
3. Ensure CI checks pass
4. Get required approvals
5. Maintainer will merge

## Getting Help

- Open an issue for bugs
- Use discussions for questions
- Tag relevant team members
- Join our development channel

## Code of Conduct

Please follow our code of conduct:
- Be respectful and inclusive
- No harassment or discrimination
- Constructive feedback only
- Follow project conventions

## License

By contributing, you agree that your contributions will be licensed under the project's license. 