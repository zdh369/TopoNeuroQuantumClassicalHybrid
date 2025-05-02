<<<<<<< HEAD
# Contributing to QuantumOmniCrypt

We welcome contributions from the community! This document provides guidelines and instructions for contributing to the QuantumOmniCrypt project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a new branch for your feature
4. Make your changes
5. Submit a pull request

## Development Environment

### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/your-username/quantum-omni-crypt.git

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Coding Standards

### Style Guide
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all public functions
- Keep functions focused and small

### Testing
- Write unit tests for new features
- Ensure all tests pass
- Maintain test coverage
- Use pytest for testing

### Documentation
- Update README.md for significant changes
- Document new features
- Keep comments clear and concise
- Update API documentation

## Pull Request Process

We welcome contributions from the community! To ensure a smooth process, please follow these guidelines:

1. **Fork the repository**: Create a personal copy of the repository on your GitHub account.
2. **Clone your fork**: Clone the forked repository to your local machine.
3. **Create a new branch**: Create a new branch for your feature or bug fix.
4. **Make your changes**: Implement your changes in the new branch.
5. **Submit a pull request**: Once your changes are ready, submit a pull request to the main repository.

### Guidelines for Handling Pull Requests

- **Review**: All pull requests will be reviewed by maintainers.
- **Feedback**: Feedback will be provided, and changes may be requested.
- **Testing**: Ensure that all tests pass before submitting a pull request.
- **Documentation**: Update documentation if necessary.
- **Merge**: Once approved, the pull request will be merged into the main branch.

### Need to Merge and Finish Pull Requests

It is important to regularly merge and finish pull requests to keep the repository up-to-date and maintain a smooth workflow. Please ensure that all pending pull requests are reviewed and merged in a timely manner.

### Automated Merging of Pull Requests

To streamline the process, we have implemented automated merging of pull requests. If all tests pass and the pull request meets the required criteria, it will be automatically merged. This helps in maintaining an up-to-date repository and reduces manual intervention.

## Review Process

1. Pull requests will be reviewed by maintainers
2. Feedback will be provided
3. Changes may be requested
4. Once approved, changes will be merged

## Feature Requests

1. Open an issue
2. Describe the feature
3. Provide use cases
4. Discuss implementation

## Bug Reports

1. Open an issue
2. Describe the bug
3. Provide steps to reproduce
4. Include error messages
5. Add system information

## Security Issues

Please report security issues to security@quantum-omni-crypt.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
=======
# Contributing to Ollama

Thank you for your interest in contributing to Ollama! Here are a few guidelines to help get you started.

## Set up

See the [development documentation](./docs/development.md) for instructions on how to build and run Ollama locally.

### Ideal issues

* [Bugs](https://github.com/ollama/ollama/issues?q=is%3Aissue+is%3Aopen+label%3Abug): issues where Ollama stops working or where it results in an unexpected error.
* [Performance](https://github.com/ollama/ollama/issues?q=is%3Aissue+is%3Aopen+label%3Aperformance): issues to make Ollama faster at model inference, downloading or uploading.
* [Security](https://github.com/ollama/ollama/blob/main/SECURITY.md): issues that could lead to a security vulnerability. As mentioned in [SECURITY.md](https://github.com/ollama/ollama/blob/main/SECURITY.md), please do not disclose security vulnerabilities publicly.

### Issues that are harder to review

* New features: new features (e.g. API fields, environment variables) add surface area to Ollama and make it harder to maintain in the long run as they cannot be removed without potentially breaking users in the future.
* Refactoring: large code improvements are important, but can be harder or take longer to review and merge.
* Documentation: small updates to fill in or correct missing documentation is helpful, however large documentation additions can be hard to maintain over time.

### Issues that may not be accepted

* Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API)
* Changes that add significant friction to the user experience
* Changes that create a large future maintenance burden for maintainers and contributors

## Proposing a (non-trivial) change

> By "non-trivial", we mean a change that is not a bug fix or small
> documentation update. If you are unsure, please ask us on our [Discord
> server](https://discord.gg/ollama).

Before opening a non-trivial Pull Request, please open an issue to discuss the change and
get feedback from the maintainers. This helps us understand the context of the
change and how it fits into Ollama's roadmap and prevents us from duplicating
work or you from spending time on a change that we may not be able to accept.

Tips for proposals:

* Explain the problem you are trying to solve, not what you are trying to do.
* Explain why the change is important.
* Explain how the change will be used.
* Explain how the change will be tested.

Additionally, for bonus points: Provide draft documentation you would expect to
see if the change were accepted.

## Pull requests

**Commit messages**

The title should look like:

    <package>: <short description>

The package is the most affected Go package. If the change does not affect Go
code, then use the directory name instead. Changes to a single well-known
file in the root directory may use the file name.

The short description should start with a lowercase letter and be a
continuation of the sentence:

      "This changes Ollama to..."

Examples:

      llm/backend/mlx: support the llama architecture
      CONTRIBUTING: provide clairity on good commit messages, and bad

Bad Examples:

      feat: add more emoji
      fix: was not using famous web framework
      chore: generify code

**Tests**

Please include tests. Strive to test behavior, not implementation.

**New dependencies**

Dependencies should be added sparingly. If you are adding a new dependency,
please explain why it is necessary and what other ways you attempted that
did not work without it.

## Need help?

If you need help with anything, feel free to reach out to us on our [Discord server](https://discord.gg/ollama).
>>>>>>> gitea/main
