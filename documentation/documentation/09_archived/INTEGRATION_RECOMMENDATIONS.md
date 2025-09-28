# n8n Workflow Integration Recommendations

This review focuses on templates that complement the Rod-Corp multi-agent stack and existing LibroSynth pipelines. Each item includes the template path, the main trigger/destinations, third-party requirements, and suggested integration options.

## High-Priority Candidates

- **AI_ML/customer_sentiment_analysis.json**  
  - **What it does:** Webhook-triggered pipeline that batches customer text, runs Cohere embeddings, stores context in Pinecone, and routes tone analysis through Claude.  
  - **Integration idea:** Pair with the AI Interaction Server to auto-tag incoming support tickets before dispatching them to `ticket_urgency_classification`. Update Rod-Corp dashboards with sentiment KPIs.
- **AI_ML/ticket_urgency_classification.json**  
  - **What it does:** Cron/Webhook triggered triage using Cohere embeddings + Claude to score urgency and assign severity labels.  
  - **Integration idea:** Feed results into MSSQL (`RodSanchez_PersonalData`) via the existing agent loader pattern. Use severity to trigger LibroSynth specialists.
- **Data_Analytics/competitor_price_scraper.json**  
  - **What it does:** Scheduled HTTP scrapes + CSV normalization + Slack digest.  
  - **Integration idea:** Replace Slack step with AI Interaction Server notification and push normalized price data into the Rod-Corp analytics warehouse.
- **Productivity/morning_briefing_email.json**  
  - **What it does:** Cron job that fetches RSS, merges with calendar tasks, and delivers formatted summary via email.  
  - **Integration idea:** Re-route compiled summary into `librosynth_repo_training_automation` notification so agents start the day with aligned context.
- **Email_Automation/daily_email_digest.json**  
  - **What it does:** Polls shared inbox, dedupes threads, and produces daily digest.  
  - **Integration idea:** Combine with `customer_sentiment_analysis` output to give human handlers a consolidated view.

## Secondary Opportunities

- **AI_ML/resume_screening.json** – Works with Cohere + Claude to shortlist candidates. Could enrich HR dashboards but overlaps with existing recruitment automation.  
- **AI_ML/voice_note_transcription.json** – Transcribes audio via OpenAI, viable for call summaries if privacy reviewed.  
- **Email_Automation/follow-up_emails.json** – Good template for post-ticket follow-ups once support severity workflow is live.

## Items to Revisit Later

- **Misc/** (48 files) – Many are promotional demos; keep archived until specific use cases emerge.  
- **Finance_Accounting/** – Several rely on QuickBooks and banking APIs we don’t expose today.  
- **Social_Media/** – Useful for marketing teams but out-of-scope for current agent objectives.

### Next Steps
1. Import the five high-priority templates into n8n and map them to Rod-Corp credentials.  
2. Replace notification nodes with AI Interaction Server webhooks so agents receive consistent updates.  
3. Capture metrics (execution counts, error rates) using LibroSynth dashboards once pilots run for one week.
