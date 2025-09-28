# Repository Documentation Analysis Report

**Repository:** {{ repository_name }}
**Analysis Date:** {{ analysis_date }}
**Agent:** {{ agent_id }}
**Scan Duration:** {{ scan_duration }}

## Executive Summary

{{ executive_summary }}

### Key Metrics
- **Total Files Scanned:** {{ total_files_scanned }}
- **Documentation Coverage:** {{ documentation_coverage.percentage }}%
- **Quality Score:** {{ overall_quality_score }}/10
- **Missing Documentation Items:** {{ missing_documentation_count }}

## Documentation Coverage Analysis

### Overall Coverage
- **Documented Functions:** {{ documentation_coverage.documented_functions }}
- **Total Functions:** {{ documentation_coverage.total_functions }}
- **Coverage Percentage:** {{ documentation_coverage.percentage }}%

### Coverage by File Type
{% for file_type, coverage in coverage_by_type.items() %}
#### {{ file_type|upper }} Files
- **Files Analyzed:** {{ coverage.files_analyzed }}
- **Files with Documentation:** {{ coverage.documented_files }}
- **Coverage:** {{ coverage.percentage }}%
{% endfor %}

### Coverage by Directory
{% for directory, coverage in coverage_by_directory.items() %}
#### {{ directory }}
- **Files:** {{ coverage.total_files }}
- **Documented:** {{ coverage.documented_files }}
- **Coverage:** {{ coverage.percentage }}%
- **Priority:** {{ coverage.priority_level }}
{% endfor %}

## Missing Documentation Analysis

### Critical Missing Documentation
{% for item in critical_missing %}
#### {{ item.file_path }}
- **Type:** {{ item.type }}
- **Function/Class:** {{ item.name }}
- **Line:** {{ item.line_number }}
- **Complexity:** {{ item.complexity_score }}
- **Public API:** {{ item.is_public_api|yesno:"Yes,No" }}
- **Priority:** HIGH
{% endfor %}

### Standard Missing Documentation
{% for item in standard_missing %}
#### {{ item.file_path }}
- **Type:** {{ item.type }}
- **Function/Class:** {{ item.name }}
- **Line:** {{ item.line_number }}
- **Priority:** MEDIUM
{% endfor %}

### Documentation Gaps by Category
{% for category, items in missing_by_category.items() %}
#### {{ category|title }}
- **Count:** {{ items|length }}
- **Examples:**
{% for item in items[:3] %}
  - {{ item.file_path }}:{{ item.line_number }} - {{ item.name }}
{% endfor %}
{% if items|length > 3 %}
  - ... and {{ items|length|add:"-3" }} more
{% endif %}
{% endfor %}

## Code Quality Assessment

### Complexity Analysis
{% for file in complex_files %}
#### {{ file.path }}
- **Cyclomatic Complexity:** {{ file.complexity }}
- **Lines of Code:** {{ file.loc }}
- **Documentation Ratio:** {{ file.doc_ratio }}%
- **Recommendations:** {{ file.recommendations|join(', ') }}
{% endfor %}

### API Documentation Status
{% for api in api_analysis %}
#### {{ api.module_name }}
- **Public Functions:** {{ api.public_functions }}
- **Documented Functions:** {{ api.documented_functions }}
- **API Completeness:** {{ api.completeness_percentage }}%
- **Quality Score:** {{ api.quality_score }}/10
{% endfor %}

## Documentation Quality Issues

### Broken Links
{% for link in broken_links %}
- **File:** {{ link.file_path }}
- **Line:** {{ link.line_number }}
- **Broken Link:** {{ link.url }}
- **Link Type:** {{ link.link_type }}
{% endfor %}

### Outdated Documentation
{% for doc in outdated_docs %}
#### {{ doc.file_path }}
- **Last Modified:** {{ doc.last_modified }}
- **Referenced Code Modified:** {{ doc.code_last_modified }}
- **Age Gap:** {{ doc.age_gap_days }} days
- **Confidence:** {{ doc.outdated_confidence }}%
{% endfor %}

### Style Inconsistencies
{% for issue in style_issues %}
#### {{ issue.category }}
- **Files Affected:** {{ issue.file_count }}
- **Description:** {{ issue.description }}
- **Examples:**
{% for example in issue.examples %}
  - {{ example.file }}:{{ example.line }} - {{ example.issue }}
{% endfor %}
{% endfor %}

## Repository Structure Analysis

### Directory Structure
```
{{ directory_tree }}
```

### Documentation Distribution
{% for location in doc_locations %}
#### {{ location.path }}
- **Type:** {{ location.type }}
- **File Count:** {{ location.file_count }}
- **Total Size:** {{ location.total_size }}
- **Last Updated:** {{ location.last_updated }}
{% endfor %}

## Technology Stack Documentation

### Languages Detected
{% for language in languages %}
#### {{ language.name }}
- **Files:** {{ language.file_count }}
- **Lines of Code:** {{ language.loc }}
- **Documentation Standards:** {{ language.doc_standards }}
- **Coverage:** {{ language.coverage_percentage }}%
{% endfor %}

### Frameworks and Libraries
{% for framework in frameworks %}
#### {{ framework.name }}
- **Version:** {{ framework.version }}
- **Usage:** {{ framework.usage_description }}
- **Documentation Status:** {{ framework.doc_status }}
- **Official Docs:** {{ framework.official_docs_url }}
{% endfor %}

## Recommendations

### High Priority Actions
{% for action in high_priority_actions %}
{{ loop.index }}. **{{ action.title }}**
   - **Impact:** {{ action.impact }}
   - **Effort:** {{ action.effort_estimate }}
   - **Description:** {{ action.description }}
   - **Steps:**
{% for step in action.steps %}
     - {{ step }}
{% endfor %}
{% endfor %}

### Medium Priority Improvements
{% for improvement in medium_priority_improvements %}
- **{{ improvement.title }}:** {{ improvement.description }}
  - Estimated Effort: {{ improvement.effort }}
  - Expected Benefit: {{ improvement.benefit }}
{% endfor %}

### Long-term Enhancements
{% for enhancement in long_term_enhancements %}
- **{{ enhancement.title }}:** {{ enhancement.description }}
  - Timeline: {{ enhancement.timeline }}
  - Dependencies: {{ enhancement.dependencies|join(', ') }}
{% endfor %}

## Documentation Automation Opportunities

### Auto-Generation Candidates
{% for candidate in auto_generation_candidates %}
#### {{ candidate.type }}
- **Files Suitable:** {{ candidate.file_count }}
- **Automation Potential:** {{ candidate.automation_score }}%
- **Template Requirements:** {{ candidate.template_needs }}
- **Implementation Effort:** {{ candidate.implementation_effort }}
{% endfor %}

### Template Standardization
{% for template in template_opportunities %}
#### {{ template.name }}
- **Current Variations:** {{ template.variation_count }}
- **Standardization Benefit:** {{ template.benefit_score }}
- **Migration Effort:** {{ template.migration_effort }}
{% endfor %}

## Knowledge Base Integration

### Content Categorization
{% for category in content_categories %}
#### {{ category.name }}
- **Document Count:** {{ category.document_count }}
- **Quality Score:** {{ category.avg_quality_score }}
- **Update Frequency:** {{ category.update_frequency }}
- **RAG Suitability:** {{ category.rag_suitability }}
{% endfor %}

### Semantic Analysis Results
- **Unique Concepts Identified:** {{ semantic_analysis.unique_concepts }}
- **Knowledge Gaps:** {{ semantic_analysis.knowledge_gaps|length }}
- **Cross-Reference Opportunities:** {{ semantic_analysis.cross_reference_opportunities }}
- **Taxonomy Recommendations:** {{ semantic_analysis.taxonomy_recommendations|length }}

## Performance Metrics

### Analysis Performance
- **Files Processed per Second:** {{ performance.files_per_second }}
- **Memory Usage:** {{ performance.memory_usage_mb }} MB
- **Processing Time Breakdown:**
{% for phase, time in performance.phase_times.items() %}
  - {{ phase }}: {{ time }} seconds
{% endfor %}

### Knowledge Base Stats
- **Vector Embeddings Created:** {{ kb_stats.embeddings_created }}
- **Collections Updated:** {{ kb_stats.collections_updated }}
- **Index Size:** {{ kb_stats.index_size_mb }} MB
- **Query Performance:** {{ kb_stats.avg_query_time_ms }} ms

## Next Steps

### Immediate Actions (This Week)
{% for action in immediate_actions %}
- [ ] {{ action }}
{% endfor %}

### Short-term Goals (Next Month)
{% for goal in short_term_goals %}
- [ ] {{ goal }}
{% endfor %}

### Long-term Objectives (Next Quarter)
{% for objective in long_term_objectives %}
- [ ] {{ objective }}
{% endfor %}

## Historical Comparison

{% if previous_analysis %}
### Changes Since Last Analysis
- **Coverage Change:** {{ coverage_change }}%
- **Quality Improvement:** {{ quality_change }}
- **New Documentation:** {{ new_docs_count }} files
- **Resolved Issues:** {{ resolved_issues_count }}

### Trend Analysis
{% for trend in trends %}
- **{{ trend.metric }}:** {{ trend.direction }} ({{ trend.change_rate }})
{% endfor %}
{% endif %}

## Appendix

### Detailed File Inventory
{% for file in detailed_inventory %}
- **{{ file.path }}**
  - Type: {{ file.type }}
  - Size: {{ file.size }} bytes
  - Last Modified: {{ file.last_modified }}
  - Documentation Score: {{ file.doc_score }}/10
  - Issues: {{ file.issues|join(', ') }}
{% endfor %}

### Generated Queries for Knowledge Base
{% for query in suggested_queries %}
- {{ query.query }} (Expected Results: {{ query.expected_results }})
{% endfor %}

---
*Analysis completed by RAG Documentation Specialist Agent*
*Next scheduled analysis: {{ next_analysis_date }}*