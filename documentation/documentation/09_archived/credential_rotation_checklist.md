# 🔐 Critical Credential Rotation Checklist

## ⚠️ IMMEDIATE ACTIONS REQUIRED

### 1. Crypto Trading APIs (CRITICAL - DO FIRST)
- [ ] **Kraken**: Login to Kraken → API → Revoke existing keys → Generate new keys
- [ ] **Binance**: Login to Binance → API Management → Delete old keys → Create new keys
- [ ] **Coinbase**: Check for any Coinbase Pro API keys and rotate

### 2. Database Credentials
- [ ] **MSSQL Server**: Change password for 'rdai' user
- [ ] **Backup Systems**: Update backup job credentials
- [ ] **Connection Strings**: Update all service connection strings

### 3. Service Authentication
- [ ] **API Gateway**: Update JWT secret keys
- [ ] **RAG System**: Regenerate authentication tokens
- [ ] **AI Orchestration**: Update service-to-service auth

### 4. External Service Integration
- [ ] **N8N**: Update webhook secrets and encryption keys
- [ ] **Home Assistant**: Generate new long-lived access tokens
- [ ] **Claude Code**: Verify API key security

### 5. AI Model APIs
- [ ] **OpenAI**: Rotate API keys if exposed
- [ ] **Anthropic**: Verify Claude API key security
- [ ] **Google**: Check Gemini API key exposure

## 🛡️ SECURITY HARDENING STEPS

### Network Security
- [ ] Implement network segmentation for crypto trading
- [ ] Setup VPN access for financial systems
- [ ] Configure firewall rules for service isolation

### Access Control
- [ ] Implement multi-factor authentication
- [ ] Setup role-based access control
- [ ] Create service accounts with minimal privileges

### Monitoring
- [ ] Setup security monitoring alerts
- [ ] Implement audit logging
- [ ] Configure intrusion detection

## 📊 VERIFICATION STEPS

### After Rotation
- [ ] Test all service connections with new credentials
- [ ] Verify crypto trading API connectivity
- [ ] Confirm database access with new passwords
- [ ] Test N8N webhook integrations
- [ ] Validate Home Assistant connectivity

### Security Validation
- [ ] Run vulnerability scans
- [ ] Verify encryption at rest
- [ ] Test backup and recovery procedures
- [ ] Confirm monitoring and alerting

## 🚨 EMERGENCY CONTACTS

If issues arise during rotation:
1. Database Admin: [Contact Info]
2. Network Security: [Contact Info]
3. API Support: [Contact Info]

## ⏰ TIMELINE

- **Hour 1**: Crypto API rotation (CRITICAL)
- **Hour 2**: Database credential updates
- **Hour 3**: Service authentication updates
- **Hour 4**: External service integration
- **Hour 5**: Testing and validation

