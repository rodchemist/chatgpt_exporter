# Repository Migration Mapping Plan

## Directory Structure Successfully Created

The following development-phase based directory structure has been created in `/mnt/c/_rod/Organized_Repos/`:

```
/mnt/c/_rod/Organized_Repos/
├── PRODUCTION/
│   ├── AI_ML/                    # Production AI/ML applications
│   ├── CRYPTO_TRADING/           # Production crypto trading systems
│   ├── INDUSTRIAL_AUTOMATION/    # Production industrial systems
│   ├── WEB_APPLICATIONS/         # Production web apps
│   └── DATA_PROCESSING/          # Production data processing tools
├── DEVELOPMENT/
│   ├── AI_FRAMEWORKS/            # AI frameworks in development
│   ├── AUTOMATION_TOOLS/         # Development automation tools
│   ├── WEB_PROJECTS/             # Web projects in development
│   └── UTILITIES/                # Utility tools being developed
├── PROTOTYPE/
│   ├── AI_EXPERIMENTS/           # AI prototypes and experiments
│   ├── PROOF_OF_CONCEPTS/        # Early stage POCs
│   └── TESTING_FRAMEWORKS/       # Testing framework prototypes
├── RESEARCH/
│   ├── DATA_ANALYSIS/            # Research data analysis projects
│   ├── ACADEMIC_PROJECTS/        # Academic/research projects
│   └── DOCUMENTATION/            # Research documentation
├── ARCHIVE/
│   ├── COMPLETED_PROJECTS/       # Finished historical projects
│   ├── LEGACY_CODE/              # Legacy codebases
│   └── DEPRECATED/               # Deprecated projects
└── MODEL_COLLECTIONS/
    ├── ML_MODELS/                # Individual ML model repositories
    ├── AI_BENCHMARKS/            # AI benchmarking collections
    └── TRAINING_DATASETS/        # Training data repositories
```

## Repository Mapping Analysis

### Current Repository Inventory

**GIT_REPOS Directory:**
- 01_Projects
- AI-LLM-LOCAL
- AI_Notebooks
- ARCHIVE (existing)
- ByCoin
- DEVELOPMENT (existing)
- PRODUCTION (existing)
- PROTOTYPE (existing)
- Plots_Manufacturing
- RESEARCH (existing)
- RodChem_Crypto_Predictor
- RodChem_Crypto_Predictor 2
- SQL-AI-samples
- _Empiric_repos
- _Ideas_repos
- _Repos_Dare
- _adhd_repos
- _automation
- _backups_agents
- ai_conductor
- ai_repos
- ai_trainer_v01
- best_scripts
- guidelines
- ircc_recurren

**NON_GIT_REPOS Directory:**
- 03_outputs
- BOOK_MAnufacturing
- ChaoChile
- PR_Citizenship
- STANDBY
- _Integrated_System
- _repos
- ai-orchestration
- n8n_server

## Detailed Migration Mapping

### PRODUCTION Destinations

#### PRODUCTION/CRYPTO_TRADING/
- **ByCoin** (Production-ready cryptocurrency backtesting dashboard with MSSQL support)
- **RodChem_Crypto_Predictor** (Main production crypto prediction system)

#### PRODUCTION/AI_ML/
- **ai_conductor** (Production AI orchestration system)

#### PRODUCTION/WEB_APPLICATIONS/
- **NON_GIT_REPOS/n8n_server** (Production automation server)

#### PRODUCTION/DATA_PROCESSING/
- **best_scripts** (Production-ready data processing scripts)

#### PRODUCTION/INDUSTRIAL_AUTOMATION/
- **Plots_Manufacturing** (Manufacturing automation systems)

### DEVELOPMENT Destinations

#### DEVELOPMENT/AI_FRAMEWORKS/
- **ai_trainer_v01** (AI training framework in development)
- **ai_repos** (AI development repositories)

#### DEVELOPMENT/AUTOMATION_TOOLS/
- **_automation** (Contains multiple automation projects in development)

#### DEVELOPMENT/WEB_PROJECTS/
- **NON_GIT_REPOS/ai-orchestration** (Web-based AI orchestration in development)

#### DEVELOPMENT/UTILITIES/
- **SQL-AI-samples** (SQL and AI utility samples)
- **_backups_agents** (Backup automation utilities)

### PROTOTYPE Destinations

#### PROTOTYPE/AI_EXPERIMENTS/
- **AI_Notebooks** (Experimental AI notebooks and prototypes)
- **RodChem_Crypto_Predictor 2** (Experimental version)

#### PROTOTYPE/PROOF_OF_CONCEPTS/
- **_Ideas_repos** (Early stage idea repositories)
- **_Repos_Dare** (Experimental/dare projects)
- **_adhd_repos** (ADHD-related prototype projects)

#### PROTOTYPE/TESTING_FRAMEWORKS/
- **(No current repositories identified - ready for future testing frameworks)**

### RESEARCH Destinations

#### RESEARCH/ACADEMIC_PROJECTS/
- **NON_GIT_REPOS/BOOK_MAnufacturing** (Manufacturing research book project)
- **NON_GIT_REPOS/PR_Citizenship** (Puerto Rico citizenship research)
- **NON_GIT_REPOS/ChaoChile** (Chile-related research)

#### RESEARCH/DATA_ANALYSIS/
- **_Empiric_repos** (Empirical data analysis projects)

#### RESEARCH/DOCUMENTATION/
- **guidelines** (Research and development guidelines)

### ARCHIVE Destinations

#### ARCHIVE/COMPLETED_PROJECTS/
- **01_Projects** (Historical work from 2023)
- **ircc_recurren** (Completed immigration-related project)

#### ARCHIVE/LEGACY_CODE/
- **(To be populated with legacy versions when repositories are updated)**

#### ARCHIVE/DEPRECATED/
- **NON_GIT_REPOS/STANDBY** (Projects on standby/deprecated)

### MODEL_COLLECTIONS Destinations

#### MODEL_COLLECTIONS/ML_MODELS/
- **AI-LLM-LOCAL** (GGUF model artifacts collection)

#### MODEL_COLLECTIONS/AI_BENCHMARKS/
- **(Ready for AI benchmarking repositories)**

#### MODEL_COLLECTIONS/TRAINING_DATASETS/
- **(Ready for training dataset repositories)**

### Special Handling Required

#### Repositories Needing Extraction:
1. **_automation** - Contains multiple projects that should be separated:
   - adhd-books-website → DEVELOPMENT/WEB_PROJECTS/
   - adhd_business → DEVELOPMENT/AUTOMATION_TOOLS/
   - generic_automation_system → DEVELOPMENT/AUTOMATION_TOOLS/
   - images_generation → PROTOTYPE/AI_EXPERIMENTS/
   - video_generation → PROTOTYPE/AI_EXPERIMENTS/

2. **_Empiric_repos** - Contains multiple projects that may need separation

3. **NON_GIT_REPOS/_repos** - Needs analysis for proper categorization

#### Directories Already Existing (Need Merge Strategy):
- **GIT_REPOS/ARCHIVE** → Merge with new **ARCHIVE/**
- **GIT_REPOS/DEVELOPMENT** → Merge with new **DEVELOPMENT/**
- **GIT_REPOS/PRODUCTION** → Merge with new **PRODUCTION/**
- **GIT_REPOS/PROTOTYPE** → Merge with new **PROTOTYPE/**
- **GIT_REPOS/RESEARCH** → Merge with new **RESEARCH/**

## Migration Priority Order

### Phase 1: High Priority (Production Systems)
1. **ByCoin** → **PRODUCTION/CRYPTO_TRADING/**
2. **RodChem_Crypto_Predictor** → **PRODUCTION/CRYPTO_TRADING/**
3. **ai_conductor** → **PRODUCTION/AI_ML/**
4. **Plots_Manufacturing** → **PRODUCTION/INDUSTRIAL_AUTOMATION/**
5. **best_scripts** → **PRODUCTION/DATA_PROCESSING/**

### Phase 2: Medium Priority (Development Projects)
1. **ai_trainer_v01** → **DEVELOPMENT/AI_FRAMEWORKS/**
2. **ai_repos** → **DEVELOPMENT/AI_FRAMEWORKS/**
3. **SQL-AI-samples** → **DEVELOPMENT/UTILITIES/**
4. **_backups_agents** → **DEVELOPMENT/UTILITIES/**

### Phase 3: Research and Documentation
1. **guidelines** → **RESEARCH/DOCUMENTATION/**
2. **_Empiric_repos** → **RESEARCH/DATA_ANALYSIS/**
3. **NON_GIT_REPOS/BOOK_MAnufacturing** → **RESEARCH/ACADEMIC_PROJECTS/**

### Phase 4: Model Collections
1. **AI-LLM-LOCAL** → **MODEL_COLLECTIONS/ML_MODELS/**

### Phase 5: Prototypes and Experiments
1. **AI_Notebooks** → **PROTOTYPE/AI_EXPERIMENTS/**
2. **_Ideas_repos** → **PROTOTYPE/PROOF_OF_CONCEPTS/**
3. **_adhd_repos** → **PROTOTYPE/PROOF_OF_CONCEPTS/**

### Phase 6: Archive and Legacy
1. **01_Projects** → **ARCHIVE/COMPLETED_PROJECTS/**
2. **ircc_recurren** → **ARCHIVE/COMPLETED_PROJECTS/**

### Phase 7: Complex Extractions
1. Extract and organize **_automation** subdirectories
2. Analyze and organize **NON_GIT_REPOS/_repos**
3. Merge existing category directories

## Post-Migration Tasks

1. **Verify Git Repository Integrity**: Ensure all `.git` directories are properly maintained
2. **Update Documentation**: Update README files with new locations
3. **Create Symbolic Links**: For backward compatibility if needed
4. **Validate Dependencies**: Ensure inter-repository dependencies still work
5. **Update CI/CD Pipelines**: If any exist, update paths in automation scripts
6. **Archive Original Structure**: Keep a backup of the original organization

## Notes

- All Git repositories will maintain their full history
- Non-Git directories will be moved as-is
- Dependencies between repositories should be documented before migration
- Consider creating a master index of all repositories and their new locations
- Some repositories may benefit from being split or combined during migration

This mapping provides a clear roadmap for transitioning from the current mixed organization to a development-phase based structure that will improve project management and reduce cognitive overhead.