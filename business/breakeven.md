# breakeven.md  

## 1. Cost per Active User (monthly)

| Cost Component | Assumptions | Unit Cost | Cost per Active User |
|----------------|-------------|-----------|----------------------|
| **Compute (CPU)** | 1 vCPU‑core‑hour per active user for inference & background jobs (AWS t3.medium @ $0.0416 / hr) | $0.0416 / hr | **$0.08** |
| **Memory / RAM** | 1 GiB‑hour per user (t3.medium includes 4 GiB, amortised) | $0.005 / GiB‑hr | **$0.01** |
| **Storage** | 100 MiB of persistent user data (S3 Standard @ $0.023 / GB‑mo) | $0.0023 / GB‑mo | **$0.02** |
| **Bandwidth (egress)** | 200 MiB of API responses per user (AWS Data Transfer @ $0.09 / GB) | $0.09 / GB | **$0.02** |
| **Total Variable Cost** | — | — | **≈ $0.13 / active user / month** |

> **Why it matters** – The variable cost is tiny compared to any realistic SaaS price point, giving us ample margin to cover fixed overhead and generate profit.

---

## 2. Pricing Tiers (monthly)

| Tier | Price (USD) | Core Features | Target Segment |
|------|-------------|---------------|----------------|
| **Starter** | **$9** | • 5,000 task executions / mo  <br>• 99.9 % SLA <br>• Email support <br>• Community forum | Hobbyist developers, indie tool‑makers |
| **Professional** | **$29** | • 25,000 task executions / mo  <br>• 99.99 % SLA <br>• Priority email & Slack support <br>• Role‑based access control (RBAC) <br>• Audit logs | Small‑to‑medium SaaS teams, CI/CD pipelines |
| **Enterprise** | **$99** | • Unlimited task executions <br>• 99.999 % SLA <br>• Dedicated account manager <br>• SSO / SAML <br>• On‑prem / VPC‑peered deployment option <br>• Custom compliance reports | Large organisations, regulated industries |

*All tiers include the core “precision engine” that guarantees < 0.1 % task‑failure rate (validated internally).*

---

## 3. Customer‑Acquisition Cost (CAC)

| Acquisition Channel | Typical Spend per Lead | Conversion Rate (Lead → Paying) | CAC Range |
|---------------------|------------------------|----------------------------------|-----------|
| Content & SEO (blog, tutorials) | $0.50 | 2 % | **$25 – $30** |
| Paid Search / Social Ads | $2.00 | 5 % | **$40 – $50** |
| Developer Conferences / Sponsorships | $5.00 | 8 % | **$60 – $70** |
| **Weighted Average** (mix of above) | — | — | **≈ $45** |

*We budget a **$30–$60** CAC range to stay profitable given our LTV (see below).*

---

## 4. Lifetime Value (LTV)

Assumptions per tier  

| Tier | Monthly churn | Monthly Revenue per User (ARPU) | LTV (months) = 1 / churn | LTV (USD) = ARPU × LTV |
|------|---------------|--------------------------------|--------------------------|------------------------|
| Starter | 5 % | $9 | 20 mo | **$180** |
| Professional | 3 % | $29 | 33.3 mo | **≈ $970** |
| Enterprise | 1 % | $99 | 100 mo | **≈ $9,900** |

**Result:** Even the low‑end Starter tier yields an LTV ~4× the high‑end CAC, satisfying the classic SaaS rule of thumb (LTV ≥ 3 × CAC).

---

## 5. Break‑Even Users Count (monthly)

### Fixed Monthly Overhead (estimated)

| Cost Item | Monthly Cost (USD) |
|-----------|--------------------|
| Engineering (2 senior devs) | $12,000 |
| DevOps / Cloud Ops | $2,000 |
| Product & Design | $3,000 |
| Marketing & Sales (ads, events) | $2,000 |
| General & Administrative | $1,000 |
| **Total Fixed** | **$20,000** |

### Variable cost per user = $0.13 (see §1)

**Break‑Even Revenue Needed** = Fixed + Variable = $20,000 + $0.13 × N  

Revenue = Σ (price_i × users_i)

To simplify, assume an **average revenue per user (ARPU)** of **$30** (mix of tiers weighted 40 % Starter, 45 % Professional, 15 % Enterprise).  

Break‑Even equation:  

```
30 × N  = 20,000 + 0.13 × N
=> (30 – 0.13) × N = 20,000
=> 29.87 × N = 20,000
=> N ≈ 670 users
```

**≈ 670 active paying users** (with the above mix) are required to cover all costs and reach cash‑flow neutrality.

---

## 6. Path to $10 K MRR

| Desired MRR | Tier Mix (Starter / Professional / Enterprise) | Required Users |
|-------------|-----------------------------------------------|----------------|
| **$10,000** | 50 % Starter, 40 % Professional, 10 % Enterprise | 112 Starter + 86 Professional + 10 Enterprise = **208 users** |
| **$20,000** | 40 % Starter, 45 % Professional, 15 % Enterprise | 160 Starter + 135 Professional + 30 Enterprise = **325 users** |
| **$30,000** | 30 % Starter, 50 % Professional, 20 % Enterprise | 210 Starter + 250 Professional + 60 Enterprise = **520 users** |

**Interpretation:**  
- Hitting **$10 K MRR** only needs ~200 paying users, far below the 670‑user break‑even point.  
- Therefore the **first financial milestone** is to acquire ~200 users (mix above) while keeping CAC ≤ $45.  
- Once the 670‑user threshold is crossed, the business becomes cash‑neutral; any additional users directly contribute to profit.

---

## 7. Quick‑Start Financial Roadmap

| Milestone | Target | Timeline | Key Levers |
|-----------|--------|----------|------------|
| **MVP launch** | 20 Starter beta users | Month 0‑1 | Community outreach, Reddit / Hacker News posts |
| **First paying cohort** | 50 Starter + 20 Professional | Month 2‑3 | Early‑bird pricing (15 % discount) + referral bonus |
| **$10 K MRR** | 208 total users (mix) | Month 4‑6 | Paid ads (CPC ≈ $0.80), SEO content, dev‑conference sponsorship |
| **Break‑Even** | 670 users | Month 9‑12 | Upsell to Professional/Enterprise, add on “Compliance Pack” ($49/mo) |
| **$30 K MRR** | 520 users (mix) | Month 12‑18 | Enterprise sales team, channel partners, API marketplace listings |

---

### Bottom Line
- **Variable cost per user is negligible ($0.13/mo).**  
- **Pricing tiers** give a healthy **ARPU (~$30)**.  
- **CAC (~$45)** is comfortably covered by **LTV (≥ $180)**.  
- **Break‑even** occurs around **670 paying users**.  
- **$10 K MRR** is reachable with **≈ 200 users**, providing a clear early‑stage growth target.  

Proceed to validate CAC assumptions with a small paid‑ad pilot and refine the tier mix based on early adopter feedback.