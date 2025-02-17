# D&D Character Builder - Development Guidelines

This document outlines the development practices and guidelines for the D&D Character Builder project. While this is currently a solo project, these guidelines ensure consistent code quality and maintainable development practices.

## Branch Strategy

The project uses a multi-branch workflow:

- `main`: Production-ready code
- `staging`: Pre-production testing
- `develop`: Active development branch

### Branch Naming Convention

- Features: `feature/feature-name`
- Bug fixes: `fix/bug-name`
- Documentation: `docs/change-description`
- Releases: `release/version-number`

## Development Workflow

1. Create a new branch from `develop`
2. Make changes following the code style guidelines
3. Run tests and ensure all checks pass
4. Merge changes back to `develop`
5. When ready for release, merge to `staging` for testing
6. After testing, merge to `main` for production

### Before Merging

- [ ] Update documentation if needed
- [ ] Add/update tests as needed
- [ ] Run the test suite
- [ ] Run linting and formatting tools
- [ ] Ensure all pre-commit hooks pass
- [ ] Review your own code critically

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
- Run black and isort before commits

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
- Run the full test suite before merging to `staging`

## Documentation

- Keep README.md up to date
- Document new features as they're implemented
- Maintain API documentation
- Include JSDoc for frontend components
- Add docstrings for Python functions
- Document any complex logic or algorithms

## Version Control Best Practices

1. Keep commits focused and atomic
2. Write clear commit messages
3. Regularly push changes to remote
4. Create meaningful branch names
5. Clean up branches after merging

## Project Organization

- Keep the project structure clean and organized
- Follow the established directory structure
- Use meaningful file names
- Group related functionality together
- Maintain separation of concerns

## Performance Considerations

- Optimize database queries
- Implement caching where appropriate
- Minimize frontend bundle size
- Use lazy loading for components
- Monitor and optimize API response times

## Security Best Practices

- Keep dependencies up to date
- Never commit sensitive data
- Use environment variables for secrets
- Implement proper input validation
- Follow security best practices for authentication

## Future Collaboration Considerations

While this is currently a solo project, the following practices are maintained to facilitate potential future collaboration:

- Clear documentation
- Consistent coding style
- Comprehensive test coverage
- Well-structured project organization
- Detailed commit history

## License

This project is licensed under [LICENSE]. All contributions must be compatible with this license.

## Code Style Workflow

Before committing any Python code changes:

```bash
# From the backend directory
black --check .
isort --check-only .
mypy .
pytest
```
