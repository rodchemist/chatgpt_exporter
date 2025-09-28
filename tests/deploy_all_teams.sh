#!/bin/bash
# deploy_all_teams.sh - Deploy documentation system test to all agent teams

echo "🚀 Deploying Universal Documentation System Test to All Agent Teams"
echo "================================================================="

TEAMS=(
    "codex_team_1" "codex_team_2" "codex_team_3"
    "gemini_team_1" "gemini_team_2" "gemini_team_3"
    "qwen_team_1" "qwen_team_2" "qwen_team_3"
)

BASE_DIR="/mnt/c/_rod/Documentation_Center"

for team in "${TEAMS[@]}"; do
    echo ""
    echo "🔧 Setting up $team..."

    # Create team directory if it doesn't exist
    mkdir -p "$BASE_DIR/tests/$team"
    cd "$BASE_DIR/tests/$team"

    # Copy required files
    echo "  📁 Copying source files..."
    cp "$BASE_DIR/AI_Chats_Exporter.zip" .
    cp "$BASE_DIR/UNIVERSAL_DOCUMENTATION_SYSTEM_README.md" .
    cp "$BASE_DIR/AGENT_EVALUATION_FRAMEWORK.md" .

    # Create deployment log
    cat > deployment_log.txt << EOF
Team: $team
Deployed: $(date)
Status: Ready for agent deployment

Files Provided:
- AI_Chats_Exporter.zip (source codebase to transform)
- UNIVERSAL_DOCUMENTATION_SYSTEM_README.md (complete instructions)
- AGENT_EVALUATION_FRAMEWORK.md (evaluation criteria)

Mission:
Transform AI_Chats_Exporter into a self-documenting, self-maintaining system
following the Universal Documentation System specifications.

Success Criteria:
- 100% verification score
- All required directories and files created
- Documentation engine fully functional
- Quality score ≥80%
- Continuous monitoring active
EOF

    # Create evaluation script for this team
    cat > evaluate.sh << 'EOF'
#!/bin/bash
# Evaluation script for this team

echo "🔍 Evaluating implementation..."

# Initialize scores
TOTAL_SCORE=0
ISSUES=()

# Test 1: Directory Structure
echo "Testing directory structure..."
REQUIRED_DIRS=(
    ".documentation/templates"
    ".documentation/cache"
    ".documentation/logs"
    "docs/api"
    "docs/guides"
    "docs/architecture"
    "docs/procedures"
    "docs/quality"
    "records/audits"
    "records/reviews"
    "records/corrective_actions"
    "records/training"
    "src"
    "tests"
    "agents/config"
    "agents/scripts"
    "agents/outputs"
)

DIR_COUNT=0
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        ((DIR_COUNT++))
    else
        ISSUES+=("Missing directory: $dir")
    fi
done

DIR_SCORE=$(( DIR_COUNT * 10 / ${#REQUIRED_DIRS[@]} ))
echo "  Directory Score: $DIR_SCORE/10 ($DIR_COUNT/${#REQUIRED_DIRS[@]} directories)"

# Test 2: Required Files
echo "Testing required files..."
REQUIRED_FILES=(
    "README.md"
    "CHANGELOG.md"
    "ARCHITECTURE.md"
    "API_REFERENCE.md"
    "DEPLOYMENT.md"
    "TROUBLESHOOTING.md"
    "CONTRIBUTING.md"
    "SECURITY.md"
    "LICENSE"
)

FILE_COUNT=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        ((FILE_COUNT++))
    else
        ISSUES+=("Missing file: $file")
    fi
done

FILE_SCORE=$(( FILE_COUNT * 10 / ${#REQUIRED_FILES[@]} ))
echo "  File Score: $FILE_SCORE/10 ($FILE_COUNT/${#REQUIRED_FILES[@]} files)"

# Test 3: Core Engine
echo "Testing documentation engine..."
ENGINE_SCORE=0
if [ -f "agents/scripts/documentation_engine.py" ]; then
    if python3 -m py_compile agents/scripts/documentation_engine.py 2>/dev/null; then
        echo "  ✅ Engine compiles successfully"
        ENGINE_SCORE=10

        # Test functionality
        if python3 agents/scripts/documentation_engine.py --verify 2>/dev/null | grep -q "100%"; then
            echo "  ✅ Engine verification: 100%"
            ENGINE_SCORE=20
        elif python3 agents/scripts/documentation_engine.py --verify 2>/dev/null | grep -q "Score:"; then
            SCORE=$(python3 agents/scripts/documentation_engine.py --verify 2>/dev/null | grep -o 'Score: [0-9]*' | cut -d' ' -f2)
            echo "  📊 Engine verification: $SCORE%"
            ENGINE_SCORE=$(( SCORE * 20 / 100 ))
        fi
    else
        echo "  ❌ Engine has syntax errors"
        ISSUES+=("Documentation engine has syntax errors")
    fi
else
    echo "  ❌ Documentation engine not found"
    ISSUES+=("Documentation engine missing: agents/scripts/documentation_engine.py")
fi

echo "  Engine Score: $ENGINE_SCORE/20"

# Test 4: Database
echo "Testing database..."
DB_SCORE=0
if [ -f ".documentation/tracking.db" ]; then
    echo "  ✅ Database file exists"
    DB_SCORE=8

    # Test database schema
    TABLES=$(sqlite3 .documentation/tracking.db ".tables" 2>/dev/null | wc -w)
    if [ $TABLES -ge 4 ]; then
        echo "  ✅ Database schema complete ($TABLES tables)"
    else
        echo "  ⚠️  Database schema incomplete ($TABLES tables)"
        ISSUES+=("Database schema incomplete")
    fi
else
    echo "  ❌ Database file missing"
    ISSUES+=("Database file missing: .documentation/tracking.db")
fi

echo "  Database Score: $DB_SCORE/8"

# Test 5: Templates
echo "Testing templates..."
TEMPLATE_SCORE=0
if [ -d ".documentation/templates" ]; then
    TEMPLATE_COUNT=$(find .documentation/templates -name "*.md" 2>/dev/null | wc -l)
    if [ $TEMPLATE_COUNT -ge 5 ]; then
        echo "  ✅ Templates complete ($TEMPLATE_COUNT templates)"
        TEMPLATE_SCORE=8
    elif [ $TEMPLATE_COUNT -ge 3 ]; then
        echo "  📊 Templates partial ($TEMPLATE_COUNT templates)"
        TEMPLATE_SCORE=6
        ISSUES+=("Templates incomplete: only $TEMPLATE_COUNT found, need 5+")
    elif [ $TEMPLATE_COUNT -ge 1 ]; then
        echo "  ⚠️  Templates minimal ($TEMPLATE_COUNT templates)"
        TEMPLATE_SCORE=4
        ISSUES+=("Templates minimal: only $TEMPLATE_COUNT found, need 5+")
    else
        echo "  ❌ No templates found"
        ISSUES+=("No templates found in .documentation/templates")
    fi
else
    echo "  ❌ Templates directory missing"
    ISSUES+=("Templates directory missing: .documentation/templates")
fi

echo "  Template Score: $TEMPLATE_SCORE/8"

# Calculate total score
IMPLEMENTATION_SCORE=$(( DIR_SCORE + FILE_SCORE + ENGINE_SCORE ))
FUNCTIONALITY_SCORE=$(( DB_SCORE + TEMPLATE_SCORE ))
TOTAL_SCORE=$(( IMPLEMENTATION_SCORE + FUNCTIONALITY_SCORE ))

# Determine grade
if [ $TOTAL_SCORE -ge 54 ]; then    # 90% of 60 points tested
    GRADE="A"
elif [ $TOTAL_SCORE -ge 48 ]; then  # 80%
    GRADE="B"
elif [ $TOTAL_SCORE -ge 42 ]; then  # 70%
    GRADE="C"
elif [ $TOTAL_SCORE -ge 36 ]; then  # 60%
    GRADE="D"
else
    GRADE="F"
fi

# Generate report
cat > evaluation_report.txt << EOR
==================================================
AGENT EVALUATION REPORT
==================================================
Team: $(basename $(pwd))
Date: $(date)
Evaluator: Automated System

SCORES:
-------
Implementation (40 points tested):
  - Directory Structure: $DIR_SCORE/10
  - Required Files: $FILE_SCORE/10
  - Core Engine: $ENGINE_SCORE/20

Functionality (20 points tested):
  - Database: $DB_SCORE/8
  - Templates: $TEMPLATE_SCORE/8

TOTAL SCORE: $TOTAL_SCORE/60 (subset of full evaluation)
ESTIMATED GRADE: $GRADE

DIRECTORY STATUS: $DIR_COUNT/${#REQUIRED_DIRS[@]} created
FILE STATUS: $FILE_COUNT/${#REQUIRED_FILES[@]} created
ENGINE STATUS: $([ -f "agents/scripts/documentation_engine.py" ] && echo "Present" || echo "Missing")
DATABASE STATUS: $([ -f ".documentation/tracking.db" ] && echo "Present" || echo "Missing")

ISSUES FOUND:
$(printf '%s\n' "${ISSUES[@]}")

NEXT STEPS:
- Address missing components
- Run full verification: python3 agents/scripts/documentation_engine.py --verify
- Check quality metrics: python3 agents/scripts/documentation_engine.py --metrics
- Start monitoring: python3 agents/scripts/documentation_engine.py --monitor

Report generated: $(date)
==================================================
EOr

echo ""
echo "📋 Evaluation Results:"
echo "  🏆 Score: $TOTAL_SCORE/60 (Grade: $GRADE)"
echo "  📁 Directories: $DIR_COUNT/${#REQUIRED_DIRS[@]}"
echo "  📄 Files: $FILE_COUNT/${#REQUIRED_FILES[@]}"
echo "  ⚙️  Engine: $([ -f "agents/scripts/documentation_engine.py" ] && echo "✅" || echo "❌")"
echo "  🗄️  Database: $([ -f ".documentation/tracking.db" ] && echo "✅" || echo "❌")"

if [ ${#ISSUES[@]} -gt 0 ]; then
    echo ""
    echo "⚠️  Issues Found:"
    printf '  - %s\n' "${ISSUES[@]}"
fi

echo ""
echo "📄 Full report saved to: evaluation_report.txt"
EOF

    chmod +x evaluate.sh

    echo "  ✅ $team setup complete"
done

echo ""
echo "🎯 All teams deployed successfully!"
echo ""
echo "Next steps:"
echo "1. Deploy agents to each team directory"
echo "2. Run evaluation: cd tests/[team_name] && ./evaluate.sh"
echo "3. Compare results across teams"
echo ""
echo "Teams ready:"
for team in "${TEAMS[@]}"; do
    echo "  - tests/$team"
done