# Rod-Corp Innovation Directory

## 🚀 New Project Development Guidelines

**All new projects and experimental features must be developed in this `/innovation` directory to maintain system stability.**

## 📋 Innovation Policy

### Why Innovation Directory?
- **System Stability**: Keep experimental code separate from production systems
- **Risk Management**: Prevent new projects from breaking existing functionality
- **Clear Organization**: Distinguish between stable services and experimental features
- **Easy Migration**: Graduate successful projects to main system when ready

### Project Structure Requirements

Each new project must follow this structure:

```
/innovation/project-name/
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
├── main.py or start.sh         # Entry point
├── config/                     # Configuration files
├── docs/                       # Project-specific documentation
├── tests/                      # Unit and integration tests
└── .gitignore                 # Git ignore rules
```

## 📝 Project Creation Process

### 1. Create Project Directory
```bash
mkdir -p /home/rod/rod-corp/innovation/your-project-name
cd /home/rod/rod-corp/innovation/your-project-name
```

### 2. Initialize Project Structure
```bash
# Create required files
touch README.md requirements.txt main.py
mkdir -p config docs tests

# Create basic README
cat > README.md << 'EOF'
# Your Project Name

## Description
Brief description of what this project does.

## Dependencies
- Python 3.8+
- List other requirements

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Status
- [x] Initial implementation
- [ ] Testing
- [ ] Documentation
- [ ] Ready for production migration
EOF

# Create basic requirements.txt
echo "# Add your dependencies here" > requirements.txt

# Create basic main.py
cat > main.py << 'EOF'
#!/usr/bin/env python3
"""
Your Project Name
Description of the project
"""

def main():
    print("Your project is ready to start!")

if __name__ == "__main__":
    main()
EOF

chmod +x main.py
```

### 3. Document in Main README
After creating your project, update `/home/rod/rod-corp/README.md` with:
- Add project to Innovation section
- Document what the project does
- Add any special requirements or notes

## 🎯 Current Innovation Projects

### Example Template
- **Project**: example-project
- **Status**: Development
- **Purpose**: Template for new projects
- **Lead**: System
- **Dependencies**: Python 3.8+

## 🔄 Graduation Process

When a project is ready for production:

1. **Testing Complete**: All tests pass, no critical bugs
2. **Documentation Complete**: Full README and docs
3. **Integration Tested**: Works with existing Rod-Corp services
4. **Security Review**: Code reviewed for security issues
5. **Performance Validated**: Meets performance requirements

### Migration Steps:
1. Move from `/innovation` to appropriate `/services` directory
2. Update main README.md with service information
3. Add to service startup scripts
4. Update RODCORP_CONTEXT.md with new capabilities
5. Create service audit entry

## 🚫 What NOT to Put Here

- **Configuration changes** to existing services
- **Bug fixes** to production code
- **Documentation updates** to existing features
- **Security patches** (these go directly to main system)

## 🛠️ Available Resources

### Rod-Corp Integration
Projects in innovation can access:
- Database connections (MSSQL + SQLite fallback)
- Service discovery system
- Agent context and communication
- Port registry for service coordination

### Development Tools
- All AI agents (claude-full, qwen-full, etc.)
- System management utilities
- Testing frameworks
- Documentation generation

## 📊 Innovation Metrics

Track your project progress:
- Development start date
- Key milestones achieved
- Testing status
- Documentation completion
- Performance benchmarks
- User feedback (if applicable)

## 🔍 Review Process

Innovation projects are reviewed:
- **Weekly**: Progress check and blocker identification
- **Monthly**: Comprehensive review and graduation assessment
- **On-demand**: When requesting graduation to production

## 💡 Innovation Ideas

Potential projects for development:
- Advanced monitoring dashboards
- New AI agent capabilities
- Integration with external services
- Performance optimization tools
- Security enhancement features
- User interface improvements

## 📞 Support

For innovation project support:
1. Check existing Rod-Corp documentation
2. Use AI agents for development assistance
3. Test integration with existing services
4. Document issues and solutions

---

**Remember**: Innovation is about experimenting safely while maintaining system stability. Follow the guidelines, document everything, and don't be afraid to try new ideas!