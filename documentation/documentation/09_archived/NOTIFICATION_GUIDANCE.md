# GitHub Actions Notification Guidance

## Slack Integration
- Create an incoming webhook or use Slack App with OAuth; store credentials in GitHub repository or organization secrets (e.g., `SLACK_WEBHOOK_URL`).
- Example step (to add to `.github/workflows/ci.yml` after validation job):
  ```yaml
  - name: Notify Slack on failure
    if: failure()
    uses: slackapi/slack-github-action@f209303ecf5dd7fe15d1a31ee06dd91c47edceb1
    with:
      payload: |
        {"text": "CI failed for ${{ github.repository }}@${{ github.ref }}"}
    env:
      SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
  ```
  - Pin to commit SHA (`f209303ecf5dd7fe15d1a31ee06dd91c47edceb1` as of 2025-09-22).
  - Use `protected` environments with approval for production notifications when needed.

## GitHub Approval for Forked Workflows
- Navigate to repository settings → Actions → General → Fork pull request workflows.
- Select "Require approval for all outside collaborators" to ensure manual review before execution.
- Document responsible approvers (DevOps Lead or delegate).

## Teams / Email (Optional)
- Use GitHub Actions OIDC with Microsoft Graph (requires enterprise app) or `actions/github-script` to send emails.
- For simple email notifications, configure a self-hosted relay and expose credentials via secrets, keeping policy restrictions in mind.

## Operational Notes
- Notification configuration updates require review by DevOps Lead and Quality Lead.
- Track notification health during monthly workflow review as per RC-QMS-014.
