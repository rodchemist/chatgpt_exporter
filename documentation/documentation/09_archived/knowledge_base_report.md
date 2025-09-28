# Knowledge Base Status Report

**Report Date:** {{ report_date }}
**Knowledge Base Version:** {{ kb_version }}
**Agent:** {{ agent_id }}
**Report Type:** {{ report_type }}

## Executive Summary

{{ executive_summary }}

### Key Statistics
- **Total Documents:** {{ total_documents }}
- **Total Collections:** {{ total_collections }}
- **Vector Embeddings:** {{ total_embeddings }}
- **Knowledge Base Size:** {{ kb_size_mb }} MB
- **Last Update:** {{ last_update }}

## Collection Overview

{% for collection in collections %}
### {{ collection.name|title }} Collection

**Description:** {{ collection.description }}

#### Statistics
- **Documents:** {{ collection.document_count }}
- **Embeddings:** {{ collection.embedding_count }}
- **Average Quality Score:** {{ collection.avg_quality_score }}/10
- **Last Updated:** {{ collection.last_updated }}
- **Storage Size:** {{ collection.size_mb }} MB

#### Content Distribution
{% for content_type, count in collection.content_distribution.items() %}
- **{{ content_type|title }}:** {{ count }} documents ({{ collection.content_percentages[content_type] }}%)
{% endfor %}

#### Quality Metrics
- **Completeness:** {{ collection.quality_metrics.completeness }}/10
- **Accuracy:** {{ collection.quality_metrics.accuracy }}/10
- **Relevance:** {{ collection.quality_metrics.relevance }}/10
- **Freshness:** {{ collection.quality_metrics.freshness }}/10

#### Recent Updates
{% for update in collection.recent_updates %}
- **{{ update.date }}:** {{ update.description }} ({{ update.documents_affected }} documents)
{% endfor %}

{% endfor %}

## Vector Database Performance

### Query Performance Metrics
- **Average Query Time:** {{ performance.avg_query_time_ms }} ms
- **95th Percentile:** {{ performance.p95_query_time_ms }} ms
- **99th Percentile:** {{ performance.p99_query_time_ms }} ms
- **Slowest Queries:** {{ performance.slowest_query_time_ms }} ms

### Index Statistics
{% for index in indices %}
#### {{ index.name }} Index
- **Type:** {{ index.type }}
- **Size:** {{ index.size_mb }} MB
- **Build Time:** {{ index.last_build_time }} seconds
- **Efficiency Score:** {{ index.efficiency_score }}/10
- **Last Optimized:** {{ index.last_optimized }}
{% endfor %}

### Memory Usage
- **RAM Usage:** {{ memory.ram_usage_mb }} MB
- **Index Cache:** {{ memory.index_cache_mb }} MB
- **Query Cache:** {{ memory.query_cache_mb }} MB
- **Available Memory:** {{ memory.available_mb }} MB

## Content Analysis

### Document Quality Distribution
{% for quality_range, count in quality_distribution.items() %}
- **{{ quality_range }}:** {{ count }} documents ({{ quality_percentages[quality_range] }}%)
{% endfor %}

### Content Freshness
{% for freshness_category, stats in freshness_analysis.items() %}
#### {{ freshness_category|title }}
- **Document Count:** {{ stats.count }}
- **Average Age:** {{ stats.avg_age_days }} days
- **Oldest Document:** {{ stats.oldest_days }} days
- **Newest Document:** {{ stats.newest_days }} days
{% endfor %}

### Language and Format Analysis
{% for format, stats in format_analysis.items() %}
#### {{ format|upper }} Documents
- **Count:** {{ stats.count }}
- **Total Size:** {{ stats.total_size_mb }} MB
- **Average Quality:** {{ stats.avg_quality }}/10
- **Processing Success Rate:** {{ stats.success_rate }}%
{% endfor %}

## Semantic Analysis

### Topic Modeling Results
{% for topic in topics %}
#### Topic {{ loop.index }}: {{ topic.name }}
- **Documents:** {{ topic.document_count }}
- **Coherence Score:** {{ topic.coherence_score }}
- **Top Keywords:** {{ topic.keywords|join(', ') }}
- **Representative Documents:**
{% for doc in topic.representative_docs %}
  - {{ doc.title }} ({{ doc.relevance_score }})
{% endfor %}
{% endfor %}

### Knowledge Graph Insights
- **Entities Identified:** {{ knowledge_graph.entity_count }}
- **Relationships Mapped:** {{ knowledge_graph.relationship_count }}
- **Concept Clusters:** {{ knowledge_graph.cluster_count }}
- **Orphaned Concepts:** {{ knowledge_graph.orphaned_count }}

#### Top Entities
{% for entity in knowledge_graph.top_entities %}
- **{{ entity.name }}:** {{ entity.mention_count }} mentions, {{ entity.connection_count }} connections
{% endfor %}

#### Key Relationships
{% for relationship in knowledge_graph.key_relationships %}
- **{{ relationship.source }} → {{ relationship.target }}:** {{ relationship.strength }} ({{ relationship.type }})
{% endfor %}

## Usage Analytics

### Query Patterns
{% for period in usage_analytics.periods %}
#### {{ period.name }}
- **Total Queries:** {{ period.total_queries }}
- **Unique Users:** {{ period.unique_users }}
- **Average Response Time:** {{ period.avg_response_time_ms }} ms
- **Success Rate:** {{ period.success_rate }}%
{% endfor %}

### Popular Query Types
{% for query_type, stats in usage_analytics.query_types.items() %}
- **{{ query_type|title }}:** {{ stats.count }} queries ({{ stats.percentage }}%)
  - Avg Response Time: {{ stats.avg_response_time_ms }} ms
  - Success Rate: {{ stats.success_rate }}%
{% endfor %}

### Top Search Terms
{% for term in usage_analytics.top_search_terms %}
{{ loop.index }}. **{{ term.term }}** ({{ term.frequency }} searches)
{% endfor %}

### User Satisfaction Metrics
- **Average Rating:** {{ user_satisfaction.avg_rating }}/5
- **Response Relevance:** {{ user_satisfaction.relevance_score }}/10
- **Result Completeness:** {{ user_satisfaction.completeness_score }}/10
- **User Feedback Count:** {{ user_satisfaction.feedback_count }}

## Data Quality Assessment

### Duplicate Detection
- **Exact Duplicates:** {{ data_quality.exact_duplicates }}
- **Near Duplicates:** {{ data_quality.near_duplicates }}
- **Similarity Threshold:** {{ data_quality.similarity_threshold }}
- **Deduplication Recommendations:** {{ data_quality.dedup_recommendations }}

### Content Integrity
{% for check in data_quality.integrity_checks %}
#### {{ check.name }}
- **Status:** {{ check.status }}
- **Issues Found:** {{ check.issues_count }}
- **Last Checked:** {{ check.last_checked }}
- **Recommendations:** {{ check.recommendations|join(', ') }}
{% endfor %}

### Embedding Quality
- **Average Embedding Norm:** {{ embedding_quality.avg_norm }}
- **Dimensionality:** {{ embedding_quality.dimensions }}
- **Variance Score:** {{ embedding_quality.variance_score }}
- **Outlier Count:** {{ embedding_quality.outlier_count }}

## System Health

### Database Health Checks
{% for check in health_checks %}
#### {{ check.component }}
- **Status:** {% if check.status == 'healthy' %}✅ Healthy{% elif check.status == 'warning' %}⚠️ Warning{% else %}❌ Critical{% endif %}
- **Last Check:** {{ check.last_check }}
- **Response Time:** {{ check.response_time_ms }} ms
- **Issues:** {{ check.issues|join(', ') }}
{% endfor %}

### Backup Status
- **Last Backup:** {{ backup_status.last_backup_date }}
- **Backup Size:** {{ backup_status.backup_size_mb }} MB
- **Backup Integrity:** {{ backup_status.integrity_status }}
- **Recovery Time Estimate:** {{ backup_status.recovery_time_estimate }}

### Resource Utilization
- **CPU Usage:** {{ resources.cpu_usage_percent }}%
- **Memory Usage:** {{ resources.memory_usage_percent }}%
- **Disk Usage:** {{ resources.disk_usage_percent }}%
- **Network I/O:** {{ resources.network_io_mbps }} Mbps

## Update and Maintenance Log

### Recent Updates
{% for update in recent_updates %}
#### {{ update.date }} - {{ update.type|title }}
- **Description:** {{ update.description }}
- **Documents Affected:** {{ update.documents_affected }}
- **Processing Time:** {{ update.processing_time }} minutes
- **Status:** {{ update.status }}
- **Notes:** {{ update.notes }}
{% endfor %}

### Maintenance Schedule
{% for maintenance in scheduled_maintenance %}
#### {{ maintenance.date }} - {{ maintenance.type }}
- **Duration:** {{ maintenance.estimated_duration }}
- **Impact:** {{ maintenance.impact_level }}
- **Description:** {{ maintenance.description }}
- **Preparation Required:** {{ maintenance.preparation|join(', ') }}
{% endfor %}

### Failed Operations
{% for failure in failed_operations %}
#### {{ failure.date }} - {{ failure.operation }}
- **Error:** {{ failure.error_message }}
- **Impact:** {{ failure.impact }}
- **Resolution:** {{ failure.resolution_status }}
- **Follow-up Required:** {{ failure.followup_required|yesno:"Yes,No" }}
{% endfor %}

## Optimization Recommendations

### Performance Optimizations
{% for optimization in performance_optimizations %}
#### {{ optimization.category }}
- **Issue:** {{ optimization.issue_description }}
- **Recommendation:** {{ optimization.recommendation }}
- **Expected Improvement:** {{ optimization.expected_improvement }}
- **Implementation Effort:** {{ optimization.effort_level }}
- **Priority:** {{ optimization.priority }}
{% endfor %}

### Content Improvements
{% for improvement in content_improvements %}
#### {{ improvement.area }}
- **Current State:** {{ improvement.current_state }}
- **Target State:** {{ improvement.target_state }}
- **Action Items:**
{% for action in improvement.action_items %}
  - {{ action }}
{% endfor %}
- **Success Metrics:** {{ improvement.success_metrics|join(', ') }}
{% endfor %}

### Infrastructure Scaling
{% for scaling in scaling_recommendations %}
#### {{ scaling.component }}
- **Current Capacity:** {{ scaling.current_capacity }}
- **Projected Need:** {{ scaling.projected_need }}
- **Scaling Strategy:** {{ scaling.strategy }}
- **Timeline:** {{ scaling.timeline }}
- **Cost Estimate:** {{ scaling.cost_estimate }}
{% endfor %}

## Future Roadmap

### Short-term Goals (Next 30 Days)
{% for goal in short_term_goals %}
- [ ] **{{ goal.title }}**
  - Description: {{ goal.description }}
  - Owner: {{ goal.owner }}
  - Success Criteria: {{ goal.success_criteria }}
{% endfor %}

### Medium-term Objectives (Next 90 Days)
{% for objective in medium_term_objectives %}
- [ ] **{{ objective.title }}**
  - Description: {{ objective.description }}
  - Dependencies: {{ objective.dependencies|join(', ') }}
  - Resources Required: {{ objective.resources }}
{% endfor %}

### Long-term Vision (Next Year)
{% for vision in long_term_vision %}
- **{{ vision.area }}:** {{ vision.description }}
  - Key Milestones: {{ vision.milestones|join(', ') }}
  - Success Metrics: {{ vision.metrics|join(', ') }}
{% endfor %}

## Alerts and Notifications

### Active Alerts
{% for alert in active_alerts %}
#### {{ alert.severity|upper }}: {{ alert.title }}
- **Triggered:** {{ alert.trigger_time }}
- **Description:** {{ alert.description }}
- **Impact:** {{ alert.impact }}
- **Action Required:** {{ alert.action_required }}
- **Owner:** {{ alert.assigned_to }}
{% endfor %}

### Resolved Issues
{% for issue in resolved_issues %}
- **{{ issue.date }}:** {{ issue.title }} - {{ issue.resolution_summary }}
{% endfor %}

## Configuration Summary

### Current Configuration
```yaml
{{ current_configuration }}
```

### Configuration Changes
{% for change in config_changes %}
- **{{ change.date }}:** {{ change.parameter }} changed from `{{ change.old_value }}` to `{{ change.new_value }}`
  - Reason: {{ change.reason }}
  - Impact: {{ change.impact }}
{% endfor %}

---

## Appendices

### Appendix A: Detailed Query Performance
{% for query in detailed_queries %}
#### Query: {{ query.query_text[:50] }}...
- **Execution Time:** {{ query.execution_time_ms }} ms
- **Results Returned:** {{ query.results_count }}
- **Collections Searched:** {{ query.collections|join(', ') }}
- **Cache Hit:** {{ query.cache_hit|yesno:"Yes,No" }}
{% endfor %}

### Appendix B: Error Log Summary
{% for error in error_summary %}
- **{{ error.date }}:** {{ error.error_type }} - {{ error.count }} occurrences
{% endfor %}

### Appendix C: API Usage Statistics
- **Total API Calls:** {{ api_stats.total_calls }}
- **Successful Calls:** {{ api_stats.successful_calls }}
- **Error Rate:** {{ api_stats.error_rate }}%
- **Average Response Size:** {{ api_stats.avg_response_size_kb }} KB

---
*Report generated by RAG Documentation Specialist Agent*
*Next report scheduled: {{ next_report_date }}*