# AWS Retail Store Sample Application - Interview Preparation Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Resume Entry](#resume-entry)
3. [LinkedIn Post](#linkedin-post)
4. [Interview Questions & Answers](#interview-questions--answers)
5. [Technical Deep Dive](#technical-deep-dive)
6. [Preparation Checklist](#preparation-checklist)

---

## Project Overview

### Cloud-Native Retail Platform | AWS, Kubernetes, Terraform
*Personal Project demonstrating enterprise microservices architecture*

This project is a **production-grade, polyglot microservices application** deployed on AWS using modern cloud-native practices. It demonstrates enterprise-level architecture patterns including service mesh, GitOps, observability, security, and chaos engineering.

### Key Technologies Used
- **Cloud Platform**: AWS (EKS, ECS, Lambda, DynamoDB, RDS, SQS, etc.)
- **Orchestration**: Kubernetes, Istio Service Mesh
- **Languages**: Java 21 (Spring Boot), Go (Gin), Node.js (NestJS)
- **Databases**: DynamoDB, PostgreSQL, MySQL, Redis, OpenSearch
- **DevOps**: Terraform, ArgoCD, GitHub Actions
- **Observability**: Prometheus, Grafana, Jaeger, OpenTelemetry
- **Security**: OPA Gatekeeper, Network Policies, mTLS
- **Reliability**: Chaos Mesh, Velero Backup

---

## Resume Entry

### Option 1: Project Section (Recommended)

```markdown
### Cloud-Native Retail Platform | AWS, Kubernetes, Terraform
*Personal Project demonstrating enterprise microservices architecture*

• Architected 5-service polyglot microservices application on AWS EKS using Java/Spring Boot, 
  Go/Gin, and Node.js/NestJS with Istio service mesh for mTLS and intelligent traffic routing
  
• Implemented GitOps-based CI/CD with ArgoCD and automated canary deployments using 
  Argo Rollouts, achieving zero-downtime releases with automated rollback capabilities

• Designed comprehensive observability stack with Prometheus, Grafana, and OpenTelemetry, 
  including custom SLO-based alerting (99% availability target) and business metrics tracking

• Established security-first infrastructure using OPA Gatekeeper policies, Kubernetes Network 
  Policies, RBAC, and Pod Security Standards implementing zero-trust architecture

• Deployed multi-database polyglot persistence layer utilizing DynamoDB, PostgreSQL, MySQL, 
  Redis, and OpenSearch with event-driven architecture via RabbitMQ and AWS SQS

• Implemented chaos engineering practices with Chaos Mesh for automated resilience testing, 
  and Velero-based disaster recovery with S3 storage and automated scheduling
```

### Option 2: Experience Section

```markdown
**Cloud Infrastructure Engineer** | Personal Project
*AWS Retail Store Sample Application - Open Source*

• Built production-grade microservices platform on AWS EKS with 5 services handling 
  1000+ concurrent connections, utilizing Terraform for Infrastructure as Code
  
• Configured Istio service mesh with circuit breakers, outlier detection, and 
  weighted traffic routing for A/B testing and blue-green deployments
  
• Developed automated CI/CD pipelines using GitHub Actions with Trivy security 
  scanning, OPA policy validation, and multi-environment deployments
  
• Created custom Grafana dashboards and Prometheus alerting rules for service 
  mesh metrics, application performance, and business KPIs
```

---

## LinkedIn Post

### Post Template 1: Project Announcement

```
🚀 Excited to share my latest project: A Cloud-Native Retail Platform built on AWS!

I've been working on architecting a production-grade microservices application that demonstrates enterprise-level cloud-native patterns. Here's what I built:

🔹 5 microservices in Java, Go, and Node.js
🔹 Kubernetes + Istio service mesh with mTLS
🔹 GitOps with ArgoCD & automated canary deployments
🔹 Full observability stack (Prometheus, Grafana, OpenTelemetry)
🔹 Zero-trust security with OPA Gatekeeper
🔹 Chaos engineering & disaster recovery

This project taught me:
• How to design resilient distributed systems
• The importance of observability in microservices
• Security-first architecture from day one
• Modern deployment strategies beyond basic CI/CD

Technical deep dive coming soon! 💻

#CloudNative #AWS #Kubernetes #DevOps #Microservices #Istio #GitOps #OpenSource
```

### Post Template 2: Technical Deep Dive

```
💡 Lessons from building a Cloud-Native Retail Platform on AWS

After months of work, here are my key takeaways from implementing a polyglot microservices architecture:

1️⃣ Service Mesh is a Game Changer
Istio's mTLS, circuit breakers, and traffic routing solved so many cross-cutting concerns. No more handling retries in application code!

2️⃣ GitOps > Traditional CI/CD
ArgoCD's declarative approach made deployments predictable. The ability to rollback by reverting a git commit? Priceless.

3️⃣ Observability Can't Be an Afterthought
Building in Prometheus metrics and distributed tracing from the start saved countless debugging hours later.

4️⃣ Polyglot Persistence is Real
Each service used the right database: DynamoDB for carts (fast writes), PostgreSQL for orders (ACID), Redis for sessions.

5️⃣ Security Should Be Default
OPA Gatekeeper policies prevented non-compliant resources from even being deployed. Shift-left security in action.

The code is open source - happy to discuss implementation details!

#SRE #PlatformEngineering #CloudArchitecture #AWS #Kubernetes #LearnInPublic
```

### Post Template 3: Achievement Focus

```
🏆 Project Milestone: Complete Cloud-Native Platform

Just deployed a fully-featured retail platform with:
✅ 5 polyglot microservices (Java, Go, Node.js)
✅ Istio service mesh with traffic management
✅ GitOps pipelines with canary deployments
✅ Custom observability dashboards
✅ Zero-trust security model
✅ Chaos engineering experiments
✅ Automated disaster recovery

This project represents 200+ hours of learning and implementation.

Check it out: [GitHub Link]

#CloudEngineering #DevOps #AWS #Microservices #ProjectShowcase
```

---

## Interview Questions & Answers

### Section 1: Architecture & Design

#### Q1: Why did you choose microservices over a monolith for this project?
**Answer:**
"I chose microservices because this retail platform has distinct business domains (catalog, cart, orders, checkout) with different scaling needs and technology requirements. For example:

- The catalog service needs heavy read optimization with OpenSearch
- The cart service requires high-throughput writes to DynamoDB
- The orders service needs ACID compliance with PostgreSQL
- The checkout service needs fast session storage with Redis

Microservices allowed me to use polyglot persistence - choosing the right database for each use case. Additionally, services can scale independently. During Black Friday, the cart service might need 10x the instances while catalog remains steady."

**Follow-up:** How do you handle the complexity trade-offs?
"Great question. I mitigated complexity by using a service mesh (Istio) to handle cross-cutting concerns like mTLS, retries, and observability. This prevents having to implement these in each service."

---

#### Q2: Explain your service mesh implementation. Why Istio?
**Answer:**
"I implemented Istio as the service mesh layer for several key capabilities:

**1. Security:** Automatic mTLS between services means all inter-service communication is encrypted without code changes. I also implemented AuthorizationPolicies for fine-grained access control.

**2. Traffic Management:** I configured VirtualServices with:
   - Canary deployments (gradual traffic shifting)
   - Circuit breakers (automatic unhealthy host ejection)
   - Retries and timeouts per route
   - A/B testing capabilities

**3. Observability:** Istio automatically collects metrics, logs, and traces for all service-to-service calls.

**Why Istio:** It's the most mature service mesh with excellent AWS integration, comprehensive feature set, and strong community support. The Envoy proxy provides high performance without application changes."

---

#### Q3: How did you implement zero-trust security?
**Answer:**
"I implemented a defense-in-depth zero-trust architecture:

**Network Layer:**
- NetworkPolicies for pod-to-pod traffic control
- Default deny-all ingress/egress
- Explicit allow rules only for required communication

**Identity Layer:**
- mTLS via Istio (SPIFFE identities)
- JWT-based authentication with RequestAuthentication
- Service-to-service authorization policies

**Policy Layer:**
- OPA Gatekeeper for admission control
- Deny privileged containers
- Enforce resource limits
- Require specific labels
- Image digest verification

**RBAC:**
- Principle of least privilege
- Dedicated service accounts per component
- ClusterRoles for different personas (readonly, developer, platform)

**Pod Security:**
- Security Contexts (read-only root filesystems)
- Non-root containers
- Dropped unnecessary capabilities"

---

### Section 2: DevOps & CI/CD

#### Q4: Walk me through your GitOps pipeline.
**Answer:**
"I implemented GitOps using ArgoCD with the following flow:

**1. Git Repository Structure:**
```
repo/
├── apps/                 # ArgoCD Application manifests
├── environments/         # staging/, production/
├── helm-charts/         # Service charts
└── kustomize/           # Environment overlays
```

**2. Developer Workflow:**
- Developer pushes code → GitHub Actions triggers
- CI runs: tests, linting, security scanning (Trivy), build
- If successful, image pushed to ECR with git SHA tag
- PR merged to main → ArgoCD detects change
- ArgoCD automatically syncs desired state to cluster

**3. Progressive Delivery with Argo Rollouts:**
```yaml
strategy:
  canary:
    steps:
    - setWeight: 20
    - pause: {duration: 10m}
    - analysis:
        templates:
        - templateName: success-rate
        args:
        - name: service-name
          value: catalog-service
    - setWeight: 50
    - setWeight: 100
```

**4. Automated Analysis:**
- Prometheus queries check error rate < 1%
- Latency p99 < 500ms
- If analysis fails, automatic rollback

**Benefits:**
- Single source of truth (Git)
- Drift detection (ArgoCD alerts if cluster diverges)
- Easy rollbacks (revert git commit)
- Audit trail (all changes in Git history)"

---

#### Q5: How do you handle database migrations in a microservices architecture?
**Answer:**
"I used the **Database per Service** pattern with these strategies:

**Schema Migrations:**
- Each service owns its database schema
- Used Flyway (Java services) and golang-migrate (Go service)
- Migrations run as Kubernetes Jobs before deployment
- Version-controlled in service repo

**Backward Compatibility:**
- Never delete columns in same PR as code changes
- Expand-contract pattern:
  1. Add new column (backward compatible)
  2. Deploy code to write to both old and new
  3. Backfill data
  4. Switch reads to new column
  5. Remove old column

**Event Sourcing for Complex Changes:**
- Orders service publishes events to RabbitMQ
- Consumers handle eventual consistency
- Saga pattern for distributed transactions

**Database per Service Enforcement:**
- OPA policy ensures services only access their own databases
- Network policies prevent cross-service DB access
- Connection pooling per service (HikariCP, pgx)"

---

### Section 3: Observability

#### Q6: How did you implement observability? What metrics matter?
**Answer:**
"I implemented the **Three Pillars of Observability**:

**1. Metrics (Prometheus + Grafana):**

Application Metrics:
- Request rate, error rate, duration (RED method)
- Business metrics: order rate, cart abandonment, checkout success
- JVM metrics (heap, GC, threads) for Java services

Infrastructure Metrics:
- Node CPU, memory, disk
- Pod restart count, resource utilization
- HPA scaling events

Service Mesh Metrics:
- Request volume per destination
- mTLS certificate expiration
- Circuit breaker state changes

**2. Logs (Loki + Promtail):**
- Structured JSON logging
- Correlation IDs propagated across services
- Service mesh access logs
- Application error logs

**3. Traces (Jaeger + OpenTelemetry):**
- Distributed tracing across all services
- Span tags for business context (user_id, order_id)
- Istio automatically generates spans
- Custom spans for critical operations

**Alerting Rules (Examples):**
```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.01
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "High error rate detected"
```

**SLO-Based Alerting:**
- 99% availability target
- Error budget burn rate alerts
- Latency SLO: p99 < 500ms"

---

#### Q7: What's your approach to distributed tracing?
**Answer:**
"I implemented distributed tracing using OpenTelemetry and Jaeger:

**Propagation:**
- W3C Trace Context headers (traceparent, tracestate)
- Istio automatically injects/extracts trace headers
- Services forward headers without modification

**Instrumentation:**
- Java: OpenTelemetry Java Agent (auto-instrumentation)
- Go: OpenTelemetry SDK with Gin middleware
- Node.js: OpenTelemetry auto-instrumentation

**Critical Spans I Added:**
- Database queries (PostgreSQL, DynamoDB)
- External API calls
- Message publishing/consuming (RabbitMQ)
- Cache operations (Redis)

**Trace Structure Example:**
```
UI Request
├── HTTP GET /products
│   └── Catalog Service
│       ├── SELECT * FROM products
│       └── OpenSearch query
├── HTTP POST /cart
│   └── Cart Service
│       └── DynamoDB PutItem
└── HTTP POST /checkout
    └── Checkout Service
        ├── Redis GET session
        ├── Publish order.created
        └── Orders Service (async)
```

**Sampling Strategy:**
- Head-based sampling: 10% of requests traced in production
- Tail-based sampling for error scenarios: 100% of errors
- Debug mode: 100% for specific users/sessions"

---

### Section 4: Scalability & Performance

#### Q8: How does your system handle high traffic? What's your scaling strategy?
**Answer:**
"I implemented multi-layer scaling:

**1. Horizontal Pod Autoscaling (HPA):**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: catalog-service
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "100"
```

**2. Cluster Autoscaling:**
- AWS Cluster Autoscaler adds nodes when pending pods exist
- Mixed instance types (on-demand + spot for cost savings)
- Node affinity rules for service placement

**3. Database Scaling:**
- DynamoDB: On-demand capacity mode (auto-scales)
- RDS: Read replicas for read-heavy workloads
- Redis: Cluster mode for horizontal scaling

**4. Caching Strategy:**
- Application-level caching (Caffeine for Java)
- Redis for distributed session storage
- CDN for static assets (CloudFront)
- Result caching for expensive queries

**5. Circuit Breakers:**
```yaml
trafficPolicy:
  connectionPool:
    tcp:
      maxConnections: 100
    http:
      http1MaxPendingRequests: 50
  outlierDetection:
    consecutiveErrors: 5
    interval: 30s
    baseEjectionTime: 30s
```

**Load Testing:**
- Used Locust to simulate 1000 concurrent users
- Identified bottlenecks at 800 RPS
- Optimized database connection pooling
- Added caching layer for hot data"

---

#### Q9: How do you handle service-to-service communication failures?
**Answer:**
"I implemented multiple resilience patterns:

**1. Circuit Breaker (Istio):**
```yaml
outlierDetection:
  consecutiveErrors: 5
  interval: 10s
  baseEjectionTime: 30s
  maxEjectionPercent: 50
```
- After 5 consecutive errors, host ejected for 30s
- Gradual recovery with exponential backoff
- Prevents cascading failures

**2. Retries with Exponential Backoff:**
```yaml
retries:
  attempts: 3
  perTryTimeout: 2s
  retryOn: gateway-error,connect-failure,refused-stream
```
- Only retry on idempotent operations (GET)
- Max 3 attempts with 2s timeout each

**3. Timeouts:**
```yaml
timeout: 5s
```
- Fail fast instead of hanging
- Custom timeouts per route

**4. Fallback Responses:**
- UI service returns cached catalog if catalog service fails
- Graceful degradation (show generic recommendations)

**5. Bulkhead Pattern:**
```yaml
connectionPool:
  http:
    http1MaxPendingRequests: 100
    maxRequestsPerConnection: 10
```
- Limits concurrent connections per service
- Prevents resource exhaustion

**6. Health Checks:**
- Kubernetes liveness/readiness probes
- Istio health checks for upstream services
- Custom health endpoints (/health, /ready)

**Monitoring:**
- Alert on circuit breaker trips
- Track retry rates
- Monitor 5xx error patterns"

---

### Section 5: Security

#### Q10: Explain your security architecture. How do you prevent common vulnerabilities?
**Answer:**
"I implemented defense-in-depth security:

**Network Security:**
- VPC with private subnets for workloads
- Security Groups: least privilege (only required ports)
- Network Policies: pod-level firewall rules
- WAF: AWS WAF for common attack patterns (SQL injection, XSS)

**Application Security:**
- Input validation on all endpoints
- Parameterized queries (prevent SQL injection)
- Content Security Policy headers
- Rate limiting per IP and user

**Identity & Access:**
- IRSA (IAM Roles for Service Accounts): No long-term credentials
- RBAC: Principle of least privilege
- Service-to-service mTLS via Istio
- JWT authentication for external requests

**Container Security:**
- Non-root containers
- Read-only root filesystems
- Dropped Linux capabilities
- Distroless images where possible
- Container image scanning with Trivy

**Secrets Management:**
- AWS Secrets Manager for database credentials
- External Secrets Operator syncs to Kubernetes
- No secrets in Git (Sealed Secrets or SOPS)
- Automatic secret rotation

**Policy Enforcement:**
- OPA Gatekeeper admission controller
- Deny privileged containers
- Enforce resource limits
- Require security labels
- Image digest verification (prevent tag mutation attacks)

**Audit & Compliance:**
- Kubernetes audit logs to CloudWatch
- AWS CloudTrail for API calls
- Falco for runtime security monitoring"

---

#### Q11: How do you handle secrets in your infrastructure?
**Answer:**
"I used a multi-layer approach for secrets management:

**1. AWS Secrets Manager:**
- Stores database credentials, API keys
- Automatic rotation configured
- Fine-grained IAM policies

**2. External Secrets Operator:**
```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: ClusterSecretStore
    name: aws-secrets-manager
  target:
    name: db-credentials
  data:
  - secretKey: password
    remoteRef:
      key: prod/catalog-db-password
```
- Syncs AWS secrets to Kubernetes Secrets
- Automatic rotation support
- Access controlled via IRSA

**3. Sealed Secrets (Alternative):**
- Encrypt secrets with cluster-specific key
- Safe to commit to Git
- Decrypted only by Sealed Secrets controller

**4. Pod Identity:**
- IRSA eliminates need for AWS credentials
- Each service account has specific IAM role
- No static credentials in pods

**5. Runtime Protection:**
- Secrets mounted as files (not env vars)
- tmpfs volumes (memory only, never disk)
- Automatic unmount on termination
- No shell access to production pods"

---

### Section 6: Chaos Engineering

#### Q12: Why did you implement chaos engineering? Give me an example.
**Answer:**
"I implemented chaos engineering to proactively identify weaknesses before they cause outages. Here's my approach:

**Chaos Mesh Integration:**

**1. Pod Failure Experiment:**
```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: catalog-pod-failure
spec:
  action: pod-failure
  mode: one
  duration: "5m"
  selector:
    labelSelectors:
      app: catalog-service
```
- Randomly kills catalog service pods
- Verifies Kubernetes reschedules pods correctly
- Checks client retry logic works

**2. Network Latency Injection:**
```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: orders-latency
spec:
  action: delay
  mode: all
  selector:
    labelSelectors:
      app: orders-service
  delay:
    latency: "100ms"
    correlation: "100"
```
- Adds 100ms latency to orders service
- Tests timeout configurations
- Validates circuit breaker trips

**3. Automated Canary Analysis:**
- Deploy canary version
- Inject chaos during rollout
- If success rate stays above threshold, promote
- If not, automatic rollback

**4. Scheduled Experiments:**
```yaml
kind: Schedule
spec:
  schedule: "0 2 * * 0"  # Weekly on Sunday 2 AM
  type: PodChaos
```
- Run chaos experiments in staging regularly
- Automated safety checks (never in production without approval)

**Benefits Discovered:**
- Found missing health check in cart service
- Discovered circuit breaker wasn't triggering
- Identified insufficient retry logic in UI service
- Fixed connection pool exhaustion issue"

---

### Section 7: Disaster Recovery

#### Q13: What's your disaster recovery strategy?
**Answer:**
"I implemented multi-layer disaster recovery:

**1. Backup Strategy with Velero:**

**Cluster Backup:**
```yaml
apiVersion: velero.io/v1
kind: Schedule
metadata:
  name: daily-backup
spec:
  schedule: 0 2 * * *
  template:
    includedNamespaces:
    - catalog
    - cart
    - orders
    - checkout
    - monitoring
    storageLocation: aws-s3
    ttl: 720h  # 30 days retention
```

**Application Data:**
- RDS: Automated daily backups with 35-day retention
- DynamoDB: Point-in-time recovery (35 days)
- S3: Cross-region replication for artifacts

**2. Multi-AZ Deployment:**
- EKS worker nodes across 3 AZs
- RDS Multi-AZ for automatic failover
- Load balancer cross-zone enabled

**3. Recovery Objectives:**
- RPO (Recovery Point Objective): 1 hour
- RTO (Recovery Time Objective): 30 minutes

**4. DR Testing:**
- Quarterly DR drills
- Restore to separate test cluster
- Verify application functionality
- Document and improve procedures

**5. Runbook Documentation:**
```markdown
## Cluster Recovery Procedure
1. Restore EKS cluster: terraform apply
2. Restore applications: velero restore
3. Verify RDS connectivity
4. Run smoke tests
5. Update DNS (if needed)
```

**6. GitOps Advantage:**
- All infrastructure in Git
- Can recreate entire environment from scratch
- State stored in S3 with versioning
- ArgoCD apps automatically sync after restore"

---

### Section 8: Cost Optimization

#### Q14: How do you optimize costs in your AWS infrastructure?
**Answer:**
"I implemented several cost optimization strategies:

**1. Right-Sizing:**
- Started with larger instances, monitored utilization
- Reduced from t3.large to t3.medium for UI service
- Used AWS Compute Optimizer recommendations

**2. Spot Instances:**
```yaml
spec:
  template:
    spec:
      containers:
      - name: cart-service
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
      nodeSelector:
        node-type: spot
      tolerations:
      - key: "spot"
        operator: "Equal"
        value: "true"
        effect: "NoSchedule"
```
- Spot instances for stateless workloads (70% savings)
- On-demand for critical services (orders, checkout)

**3. Autoscaling:**
- HPA prevents over-provisioning
- Cluster Autoscaler removes unused nodes
- Scale to zero for dev environments

**4. Reserved Capacity:**
- Reserved Instances for predictable baseline
- Savings Plans for compute
- 1-year commitment for 40% savings

**5. Storage Optimization:**
- S3 lifecycle policies (transition to Glacier)
- EBS gp3 volumes (20% cheaper than gp2)
- RDS storage auto-scaling

**6. Database:**
- DynamoDB on-demand for unpredictable traffic
- RDS Graviton instances (20% cheaper)
- Read replicas for read-heavy workloads

**7. Monitoring:**
- AWS Cost Explorer dashboards
- Set budget alerts at 80% of expected spend
- Tagging strategy for cost allocation
- Monthly cost reviews

**8. Container Optimization:**
- Distroless images (smaller size)
- Multi-stage builds
- Image caching
- Resource limits prevent runaway costs"

---

### Section 9: Troubleshooting

#### Q15: Walk me through debugging a production issue.
**Answer:**
"Here's my systematic approach using the example of a latency spike:

**Scenario:** P99 latency jumped from 200ms to 2s

**1. Initial Triage (2 minutes):**
```bash
# Check alerts
kubectl get alerts -n monitoring

# View recent events
kubectl get events --sort-by=.metadata.creationTimestamp

# Check pod status
kubectl get pods -n production --field-selector=status.phase!=Running
```

**2. Metrics Investigation (5 minutes):**
```promql
# Check error rate
rate(http_requests_total{status=~"5.."}[5m])

# Latency by service
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# Database connection pool
java_sql_connections_active / java_sql_connections_max
```

**3. Log Analysis:**
```bash
# Search for errors
kubectl logs -l app=catalog-service | grep ERROR

# Distributed trace
jaeger-ui: Trace for high-latency request
# Found: 1.8s spent in database query
```

**4. Root Cause:**
- Missing database index on product_search table
- Query doing full table scan
- Only affected search endpoint

**5. Immediate Mitigation:**
```sql
-- Add index (applied via Flyway migration)
CREATE INDEX CONCURRENTLY idx_product_search_name 
ON product_search(name);
```

**6. Verification:**
```promql
# Confirm latency return to normal
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

**7. Prevention:**
- Added query performance monitoring
- SLO alerts for p99 latency
- Load testing with database profiling
- Documentation in runbook

**Tools Used:**
- Prometheus + Grafana for metrics
- Jaeger for distributed tracing
- Loki for log aggregation
- kubectl for pod investigation"

---

### Section 10: Behavioral & Soft Skills

#### Q16: What was the biggest challenge you faced in this project?
**Answer:**
"The biggest challenge was implementing the service mesh without disrupting existing services.

**Challenge:** Adding Istio required sidecar injection, which changed network behavior and caused initial connectivity issues.

**Solution Process:**

1. **Research Phase:**
   - Read Istio documentation thoroughly
   - Reviewed community best practices
   - Set up test environment

2. **Incremental Rollout:**
   - Started with non-critical service (recommendations)
   - Used Istio's permissive mTLS mode initially
   - Monitored for issues

3. **Troubleshooting:**
   - Discovered application was doing pod IP calls (bypassed service mesh)
   - Fixed to use Kubernetes service names
   - Adjusted connection pool settings

4. **Lessons Learned:**
   - Test in staging extensively first
   - Have rollback plan ready
   - Monitor everything during rollout
   - Document all configuration changes

**Outcome:**
- Successful Istio deployment across all services
- mTLS encryption without code changes
- Improved observability
- Zero downtime migration

**What I'd Do Differently:**
- Start with canary namespace approach
- Better documentation of network assumptions
- More extensive load testing before production"

---

#### Q17: How do you keep up with new technologies?
**Answer:**
"I have a multi-channel approach to continuous learning:

**1. Hands-On Projects:**
- This retail platform project taught me Istio, ArgoCD, OPA
- Document everything I learn in GitHub
- Build proof-of-concepts for new tools

**2. Official Sources:**
- AWS newsletters and blogs
- Kubernetes release notes
- CNCF project updates

**3. Community:**
- Reddit r/kubernetes, r/devops
- LinkedIn technical posts
- Discord communities (Kubernetes, Argo)

**4. Certifications:**
- AWS Solutions Architect Associate
- Kubernetes CKA (planned)
- Terraform Associate (planned)

**5. Practical Application:**
- Apply new concepts to personal projects
- Experiment in home lab
- Share knowledge through blog posts

**Recent Learnings:**
- eBPF for observability (Cilium, Pixie)
- Platform engineering concepts
- Cost optimization strategies"

---

## Technical Deep Dive

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         AWS Cloud                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Route 53   │  │ CloudFront   │  │     WAF      │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         │                 │                 │                │
│         └─────────────────┴─────────────────┘                │
│                           │                                  │
│  ┌────────────────────────▼────────────────────────┐         │
│  │              AWS Load Balancer                 │         │
│  └────────────────────────┬────────────────────────┘         │
│                           │                                  │
│  ┌────────────────────────▼────────────────────────┐         │
│  │                  EKS Cluster                    │         │
│  │  ┌─────────────────────────────────────────┐    │         │
│  │  │           Istio Ingress Gateway        │    │         │
│  │  └──────────────────┬────────────────────┘    │         │
│  │                     │                         │         │
│  │  ┌──────────────────┼────────────────────┐   │         │
│  │  │     Istio Service Mesh (mTLS)        │   │         │
│  │  │                                         │   │         │
│  │  │  ┌─────────┐ ┌─────────┐ ┌──────────┐  │   │         │
│  │  │  │   UI    │ │ Catalog │ │   Cart   │  │   │         │
│  │  │  │ (Java)  │ │  (Go)   │ │ (Java)   │  │   │         │
│  │  │  └────┬────┘ └────┬────┘ └────┬─────┘  │   │         │
│  │  │       │          │          │        │   │         │
│  │  │  ┌────▼────┐ ┌───▼────┐ ┌───▼─────┐  │   │         │
│  │  │  │ Orders  │ │Checkout│ │Recommend│  │   │         │
│  │  │  │ (Java)  │ │(Node)  │ │  (Go)   │  │   │         │
│  │  │  └────┬────┘ └────┬───┘ └────┬────┘  │   │         │
│  │  └───────┼──────────┼──────────┼───────┘   │         │
│  │          │          │          │           │         │
│  └──────────┼──────────┼──────────┼───────────┘         │
│               │          │          │                     │
│  ┌────────────┼──────────┼──────────┼─────────────────┐   │
│  │    Data Layer        │          │                 │   │
│  │  ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌────────┐│   │
│  │  │DynamoDB │ │PostgreSQL│ │  MySQL  │ │ Redis  ││   │
│  │  │  (Cart) │ │ (Orders) │ │(Catalog)│ │(Session)│   │
│  │  └─────────┘ └──────────┘ └─────────┘ └────────┘│   │
│  │  ┌───────────────────────────────────────────┐   │   │
│  │  │     OpenSearch (Product Search)          │   │   │
│  │  └───────────────────────────────────────────┘   │   │
│  └────────────────────────────────────────────────────┘   │
│                                                            │
│  ┌────────────────────────────────────────────────────┐   │
│  │              Message Queue Layer                    │   │
│  │  ┌──────────────┐      ┌──────────────┐          │   │
│  │  │   RabbitMQ   │      │     SQS      │          │   │
│  │  └──────────────┘      └──────────────┘          │   │
│  └────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

### Service Communication Flow

```
User Request Flow:

1. Client → Route 53 → CloudFront → WAF → ALB
2. ALB → Istio Ingress Gateway
3. Ingress Gateway → UI Service (Spring Boot)
4. UI Service → Catalog Service (Go)
   - Via Istio proxy (mTLS)
   - Circuit breaker active
   - Retry policy applied
5. Catalog Service → MySQL (via RDS)
   - Connection pooling
   - Query metrics collected
6. Response flows back through Istio
   - Distributed trace collected
   - Metrics recorded
   - Access log written
```

---

### GitOps Deployment Flow

```
Developer Workflow:

┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   Git    │────▶│   CI     │────▶│   ECR    │────▶│ ArgoCD   │
│   Push   │     │ Pipeline │     │  Push    │     │  Sync    │
└──────────┘     └──────────┘     └──────────┘     └────┬─────┘
                                                          │
                                    ┌─────────────────────▼──────────┐
                                    │         EKS Cluster          │
                                    │  ┌──────────────────────────┐  │
                                    │  │    Argo Rollouts         │  │
                                    │  │  ┌────────────────────┐  │  │
                                    │  │  │  Canary: 20%       │  │  │
                                    │  │  │  Analysis: 10 min  │  │  │
                                    │  │  │  Promote: 100%     │  │  │
                                    │  │  └────────────────────┘  │  │
                                    │  └──────────────────────────┘  │
                                    └────────────────────────────────┘
```

---

## Preparation Checklist

### Technical Knowledge

#### Kubernetes
- [ ] Understand Pods, Deployments, Services, Ingress
- [ ] Know Horizontal Pod Autoscaler (HPA)
- [ ] Understand Cluster Autoscaler
- [ ] Familiar with ConfigMaps and Secrets
- [ ] Know kubectl commands by heart
- [ ] Understand RBAC (Roles, RoleBindings, ClusterRoles)
- [ ] Familiar with Network Policies

#### Istio Service Mesh
- [ ] Understand mTLS and how it works
- [ ] Know VirtualService, DestinationRule, Gateway resources
- [ ] Can explain circuit breakers and retries
- [ ] Understand traffic splitting (canary, blue-green)
- [ ] Know how observability works (metrics, traces)

#### AWS Services
- [ ] EKS architecture and components
- [ ] RDS (Multi-AZ, read replicas)
- [ ] DynamoDB (capacity modes, indexes)
- [ ] SQS vs SNS
- [ ] ALB vs NLB
- [ ] IAM roles and policies
- [ ] VPC basics (subnets, security groups)

#### Observability
- [ ] Prometheus metrics and PromQL
- [ ] Grafana dashboards
- [ ] Distributed tracing concepts
- [ ] Jaeger or Zipkin basics
- [ ] Structured logging

#### Security
- [ ] Zero-trust architecture principles
- [ ] mTLS implementation
- [ ] Network policies
- [ ] RBAC best practices
- [ ] OPA Gatekeeper concepts

#### DevOps
- [ ] GitOps principles
- [ ] ArgoCD/Flux concepts
- [ ] Canary deployments
- [ ] CI/CD pipeline design
- [ ] Infrastructure as Code (Terraform)

### Communication Skills

- [ ] Practice explaining technical concepts simply
- [ ] Prepare stories using STAR method (Situation, Task, Action, Result)
- [ ] Have specific metrics ready (performance improvements, cost savings)
- [ ] Prepare questions to ask interviewers

### Questions to Ask Interviewers

1. "What does a typical day look like for this role?"
2. "What's the biggest technical challenge the team is facing?"
3. "How does the team handle on-call rotations?"
4. "What's your cloud infrastructure roadmap for the next year?"
5. "How do you approach technical debt?"

---

## Additional Resources

### Documentation
- [Project README](../README.md)
- [Architecture Decision Records](../docs/adr/)
- [Runbooks](../docs/runbooks/)

### External Links
- [Istio Documentation](https://istio.io/latest/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [AWS EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/)
- [CNCF Trail Map](https://landscape.cncf.io/)

### Practice
- [Killer.sh CKA Practice](https://killer.sh/)
- [AWS Free Tier Hands-on](https://aws.amazon.com/free/)

---

## Final Tips

1. **Be Honest**: If you don't know something, say so. Show how you'd learn it.

2. **Show Passion**: Your enthusiasm for cloud-native tech should come through.

3. **Use Specifics**: Instead of "I improved performance," say "I reduced P99 latency from 2s to 200ms."

4. **Demonstrate Trade-off Thinking**: "I chose Istio over Linkerd because..."

5. **Ask Clarifying Questions**: Make sure you understand the question before answering.

6. **Draw Diagrams**: If virtual/whiteboard, draw the architecture. Shows clear thinking.

7. **Stay Calm Under Pressure**: Take a breath before answering complex questions.

8. **Follow Up**: Send a thank-you email mentioning something specific from the interview.

---

## Good Luck! 🚀

Remember: This project demonstrates enterprise-grade skills. Be confident and showcase your knowledge!

Last Updated: 2026
