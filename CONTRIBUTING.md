# Contributing to Free Web Hosting Gems

Thank you for contributing to **Free Web Hosting Gems**.

This repository is a curated list of free web hosting, cloud, PaaS, serverless, VPS, and no-code/low-code platforms. The goal is to keep the list useful, accurate, structured, and easy for developers to compare.

The repository currently organizes services into these categories:

- 🌐 Static Site Hosting
- 🔧 Full-Stack Platforms
- ⚡ Serverless & Edge
- ☁️ VPS & Cloud Infrastructure
- 🎨 No-Code & Low-Code Builders

The README uses a fixed table structure for every category, and contributors are expected to follow that structure exactly.

---

## 📋 Before You Contribute

Please read this entire document before opening a Pull Request.

A contribution should be:

- Relevant to web hosting, application hosting, deployment, cloud infrastructure, serverless, or related developer hosting.
- Based on a genuinely usable free tier.
- Accurate at the time of submission.
- Supported by the service's official website or documentation.
- Added to the correct category.
- Formatted exactly like the existing README tables.
- Free of duplicate entries.
- Free of misleading, exaggerated, or promotional claims.

Pull Requests that do not follow the repository structure may be closed or requested for changes.

---

## 🧭 What You Can Contribute

You can contribute in several ways:

### 1. Add a New Hosting Service

Add a hosting platform that is not already listed.

Examples include:

- Static hosting
- Full-stack application hosting
- PaaS
- Serverless platforms
- Edge compute
- VPS/cloud infrastructure
- No-code or low-code hosting/builders
- Developer-focused hosting platforms

### 2. Update an Existing Service

You can update:

- Free-tier limits
- Storage limits
- Bandwidth limits
- Compute limits
- Project/application limits
- Runtime availability
- Database availability
- Domain support
- Deployment methods
- Service descriptions
- Official URLs

### 3. Report an Inaccurate Listing

If a service no longer provides the listed free tier, has changed its limits, shut down, or has incorrect information, submit a Pull Request with the corrected information.

### 4. Remove an Invalid Service

A service may be removed if:

- Its free tier has been discontinued.
- The service has permanently shut down.
- The listed service is no longer usable.
- The listing is misleading.
- The service no longer fits the repository's scope.

Please provide evidence when requesting removal.

---

# 🚨 Contribution Rules

These rules are mandatory.

## Rule 1 — Follow the Existing Table Structure

Every hosting service must use exactly this structure:

```md
| # | Service | Description | Free Tier Highlights | Link |
|---|--------|-------------|----------------------|------|
| 1 | Service Name | Short description. | Free-tier details. | https://example.com |
```

Do not create a different table format.

Do not add additional columns.

Do not remove existing columns.

Do not use HTML tables for individual service listings.

---

## Rule 2 — Keep One Service Per Row

Each service must occupy exactly one row.

Correct:

```md
| 28 | Example Hosting | Static hosting platform. | 1 GB storage. | https://example.com |
| 29 | Another Host | Full-stack hosting. | 512 MB RAM. | https://another.example |
```

Incorrect:

```md
| 28 | Example Hosting |
| 29 | Another Host | Full-stack hosting. |
```

Do not split one service across multiple rows.

Do not combine multiple services into one row.

---

## Rule 3 — Keep Numbering Sequential

The `#` column must remain sequential within each category.

For example:

```md
| 1 | Service A | ... |
| 2 | Service B | ... |
| 3 | Service C | ... |
```

If you add a new service between entries 10 and 11, update the numbering accordingly.

Do not use:

```md
| 10 | Service A | ... |
| 15 | Service B | ... |
| 27 | Service C | ... |
```

The category numbering should always be continuous.

---

## Rule 4 — Use the Official Service URL

The `Link` column must point to the official website of the service.

Correct:

```md
| 28 | Example Host | Static hosting. | 1 GB storage. | https://example.com |
```

Avoid:

- Affiliate links
- Referral links
- Tracking-heavy URLs
- Blog posts
- Review websites
- Third-party directories
- Unofficial mirrors

If the official URL contains an unavoidable campaign or attribution parameter, explain why it is necessary in your Pull Request.

---

## Rule 5 — Do Not Add Services Without a Genuine Free Tier

The repository is specifically focused on free hosting options.

A service should have a usable free offering.

Examples of acceptable free tiers may include:

- Permanently free hosting
- Free developer tier
- Free project
- Free application
- Free static site hosting
- Free compute allocation
- Free serverless requests
- Free storage allocation
- Free trial only when the repository explicitly supports that type of offering

A service that requires payment immediately to deploy should not be presented as a free hosting service.

Do not describe a paid trial as "free forever."

Do not describe promotional credits as permanent free hosting.

---

## Rule 6 — Verify Free-Tier Limits

Before submitting a service, verify its current free-tier information from the official service website or official documentation.

Check as many of these as applicable:

- Storage
- Bandwidth
- CPU
- RAM
- Build minutes
- Runtime hours
- Requests
- Function invocations
- Database limits
- Number of projects
- Number of applications
- Custom domains
- Deployment limits
- Sleep behavior
- Expiration
- Credit-card requirements
- Geographic restrictions
- Verification requirements

If a free tier has important restrictions, include the restriction in `Free Tier Highlights`.

Do not hide important limitations.

---

# 🧱 Required Entry Format

Every entry has exactly five fields:

```text
# | Service | Description | Free Tier Highlights | Link
```

## 1. Number

The number identifies the service within its category.

Example:

```md
| 28 | Example Host | ... | ... | https://example.com |
```

## 2. Service

Use the official product/service name.

Do not add unnecessary marketing text.

Good:

```md
| 28 | Example Host | ... |
```

Avoid:

```md
| 28 | Example Host - THE BEST FREE HOSTING EVER | ... |
```

## 3. Description

Keep the description short and factual.

Recommended style:

```text
Static site hosting.
Git-based deployment.
Serverless backend platform.
Docker-based PaaS.
VPS infrastructure.
No-code application builder.
```

The description should tell the reader what the service is.

Do not turn the description into an advertisement.

## 4. Free Tier Highlights

This field should contain the most useful free-tier limits.

Examples:

```text
1 GB storage.
```

```text
100k requests/day.
```

```text
3 projects, custom domains.
```

```text
750 hrs/month.
```

When there are several important limits:

```text
1 GB RAM, 5 GB storage, 100 GB bandwidth.
```

Use concise values.

## 5. Link

Use the official service URL:

```text
https://example.com
```

---

# 🗂️ Choosing the Correct Category

Place each service in the category that best represents its primary hosting capability.

## 🌐 Static Site Hosting

Use this category for services primarily focused on:

- HTML
- CSS
- JavaScript
- Static site deployment
- Static site generators
- Documentation sites
- JAMstack
- Git-based static deployment
- CDN-backed static hosting

Examples already represented in the repository include Netlify, Vercel, Cloudflare Pages, GitHub Pages, GitLab Pages, and Neocities.

## 🔧 Full-Stack Platforms

Use this category for services that can host application backends or complete applications.

Examples include:

- PHP hosting
- Node.js hosting
- Python applications
- Databases
- Docker applications
- PaaS
- Forums
- Backend applications
- Full-stack web applications

## ⚡ Serverless & Edge

Use this category for:

- Serverless functions
- Edge functions
- Edge compute
- Function-as-a-service platforms
- Request-based backend execution

## ☁️ VPS & Cloud Infrastructure

Use this category for infrastructure-level services such as:

- VPS
- Virtual machines
- Cloud compute
- Infrastructure instances
- Cloud servers

## 🎨 No-Code & Low-Code Builders

Use this category for platforms primarily focused on building applications or websites with little or no traditional coding.

Examples include:

- Visual website builders
- No-code application platforms
- Low-code application platforms
- Visual page builders

If a service clearly fits multiple categories, choose the category that best represents its primary free hosting capability.

---

# 🔍 Check for Duplicates Before Adding

Before adding a service, search the entire README.

Check for:

- Exact service name
- Product name
- Parent company
- Alternate spelling
- Previous name
- Same platform listed in another category

Do not add the same service twice simply because it provides multiple features.

For example, if a platform already exists in the repository, update its existing entry instead of creating a second entry.

---

# ✍️ Writing Style

Keep every entry concise.

### Use

- Sentence case
- Clear technical language
- Short descriptions
- Specific limits
- Consistent units
- Factual wording

### Avoid

- "Best"
- "Amazing"
- "Awesome"
- "World's #1"
- "Perfect"
- "Insane"
- "Unlimited everything"
- Unverified claims
- Marketing slogans

The repository is a curated technical resource, not an advertising directory.

---

# 📊 Category Statistics

The README contains an automatically maintained category statistics section.

It is surrounded by:

```md
<!-- CATEGORY_STATS_START -->
...
<!-- CATEGORY_STATS_END -->
```

Do not manually edit the generated statistics.

Do not change:

- Category counts
- Total count
- Generated table structure
- Generated category links

The statistics are intended to be updated automatically based on the service tables.

When you add or remove a service, update the actual category table. The automated statistics workflow should handle the counts.

---

# ⚠️ Do Not Break the README Structure

The README contains important structural elements, including:

- Repository header
- Badges
- Category statistics
- Category headings
- Service tables
- Contributors section
- Promotion section
- Contact information

Do not remove or modify these unless your Pull Request specifically addresses that section.

In particular, do not remove:

```md
<!-- CATEGORY_STATS_START -->
```

or:

```md
<!-- CATEGORY_STATS_END -->
```

These markers are used by the automated statistics process.

---

# ➕ Adding a New Service

Follow this process exactly.

## Step 1 — Search the README

Confirm that the service is not already listed.

## Step 2 — Verify the Official Website

Open the service's official website.

Confirm that the service actually provides hosting or a relevant developer platform.

## Step 3 — Verify the Free Tier

Confirm the current free-tier limits.

Record the important limits before editing the README.

## Step 4 — Choose the Category

Place the service in the most appropriate category.

## Step 5 — Add the Row

Use the exact five-column format:

```md
| 28 | Example Host | Static hosting platform. | 1 GB storage, custom domains. | https://example.com |
```

## Step 6 — Fix Numbering

Make sure every row in that category is sequential.

## Step 7 — Check Markdown

Make sure:

- Every row has five columns.
- Every URL is valid.
- No `|` characters accidentally break a cell.
- No row is missing a value.
- The table separator is unchanged.

## Step 8 — Review Your Diff

Before opening the Pull Request, review the complete Git diff.

Your PR should contain only the changes necessary for your contribution.

---

# 🔄 Updating an Existing Service

When updating an existing listing:

1. Find the existing service.
2. Verify the current information from the official source.
3. Change only the outdated fields.
4. Preserve the existing table format.
5. Do not create a duplicate row.
6. Explain the change in your Pull Request.

For example, if a service changes from:

```md
| 10 | Example Host | Static hosting. | 1 GB storage. | https://example.com |
```

to:

```md
| 10 | Example Host | Static hosting. | 5 GB storage, 100 GB bandwidth. | https://example.com |
```

mention the source and reason for the change in your PR.

---

# 🗑️ Removing a Service

Do not remove a service without a reason.

A removal Pull Request should explain:

- What changed?
- Why should the service be removed?
- When was the change observed?
- What official source supports the change?

Examples:

```text
The service no longer provides a free tier.
```

```text
The service has shut down.
```

```text
The previously listed free tier has been discontinued.
```

If possible, provide the official announcement or pricing page in the Pull Request description.

---

# 🧪 Pull Request Checklist

Before submitting your Pull Request, verify every item below.

### Service

- [ ] The service is relevant to this repository.
- [ ] The service is not already listed.
- [ ] The official website is provided.
- [ ] The service has a genuine free offering.
- [ ] The free-tier limits were verified.
- [ ] Important restrictions are mentioned.

### Formatting

- [ ] I used the existing five-column table structure.
- [ ] I added exactly one service per row.
- [ ] I used the correct category.
- [ ] Numbering is sequential.
- [ ] The description is concise.
- [ ] Free-tier information is factual.
- [ ] The official URL is used.
- [ ] I did not add unnecessary marketing language.

### Repository Integrity

- [ ] I did not modify unrelated services.
- [ ] I did not break any Markdown tables.
- [ ] I did not remove category statistics markers.
- [ ] I did not manually modify generated statistics.
- [ ] I reviewed my Git diff.
- [ ] I checked that all changed links work.

---

# 📝 Pull Request Template

Use this structure when opening a Pull Request:

```md
## What changed?

Briefly describe the change.

## Type of contribution

- [ ] New hosting service
- [ ] Update existing service
- [ ] Correct inaccurate information
- [ ] Remove unavailable service
- [ ] Documentation
- [ ] Other

## Service

**Name:** Example Host

**Category:** Static Site Hosting

**Official URL:** https://example.com

## Free Tier

- Storage:
- Bandwidth:
- Projects:
- Runtime:
- Other relevant limits:

## Verification

Explain where you verified the information.

## Checklist

- [ ] Service is not already listed
- [ ] Official URL verified
- [ ] Free tier verified
- [ ] Correct category selected
- [ ] Table format followed
- [ ] Numbering checked
- [ ] No unrelated changes
- [ ] README reviewed
```

---

# 🚫 Contributions That May Be Rejected

A Pull Request may be rejected or requested for changes when it contains:

- Duplicate services
- Incorrect free-tier information
- Unverified claims
- Paid-only services presented as free
- Expired promotional credits presented as permanent free hosting
- Affiliate links
- Referral links
- Unofficial URLs
- Broken Markdown
- Incorrect table structure
- Incorrect numbering
- Excessive marketing language
- Unrelated README changes
- Bulk submissions without adequate verification
- Changes to automated statistics
- Changes that make the repository harder to maintain

---

# 🤝 Service Owners and Representatives

If you own or represent a listed service, you are welcome to submit updates.

However, being a service owner does not guarantee inclusion.

Service information must still be:

- Relevant
- Accurate
- Verifiable
- Consistent with the repository format
- Transparent about limitations

Do not submit promotional copy in place of factual free-tier information.

If your service has changed its pricing or free tier, provide the official pricing or documentation source in the Pull Request.

---

# 🔐 Transparency

This repository aims to remain useful and developer-focused.

A service should not receive preferential treatment because of:

- Sponsorship
- Partnership
- Personal relationship
- Referral program
- Affiliate program
- Promotional offer

Free-tier information should be presented consistently across all services.

If a service has an important limitation, disclose it.

---

# 📦 Multiple Contributions

If you are adding multiple services:

- Verify every service individually.
- Check every service for duplicates.
- Use the correct category for each.
- Keep all rows consistent.
- Explain the additions in the Pull Request.
- Avoid adding large numbers of poorly verified services in a single PR.

For substantial changes, consider separating unrelated changes into separate Pull Requests.

---

# 🧹 Keep the Repository Maintainable

This project is designed to be a long-term curated resource.

Contributors should prioritize:

1. Accuracy
2. Consistency
3. Verifiability
4. Clarity
5. Maintainability

Do not optimize for the number of services added.

A smaller number of accurate listings is more useful than a large number of inaccurate or outdated listings.

---

# 🌟 Thank You

Every useful contribution helps developers discover hosting options that may fit their projects.

Before submitting, make sure your contribution follows the repository's existing structure and all requirements in this document.

**If you are unsure whether a service belongs in the repository, open an issue first and describe the service, its free tier, and why it fits the project.**
