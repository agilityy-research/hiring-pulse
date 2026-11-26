---
title: "Privacy"
description: >-
  What the Hiring Pulse website does and does not collect: no cookies, one cookieless page-view counter, no advertising code; what the hosting provider logs.
permalink: /privacy/
---
# Privacy

**This site sets no cookies.** One script, Cloudflare Web Analytics, counts page views without cookies, fingerprinting or
cross-site tracking, under the [Cloudflare privacy policy](https://www.cloudflare.com/privacypolicy/). Nothing else is
loaded from third parties; there is no advertising code.

- **Hosting.** The site is served by GitHub Pages. GitHub may log requests (IP address, user agent, page) for security
  and operations under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
- **Company search.** The search box on the front page runs entirely in your browser; it downloads one public data
  file from this site and sends nothing anywhere.
{%- if site.beta_signup_action != "" %}
- **The free beta e-mail.** The signup form sends your e-mail address, your role and your one-line answer directly to
  [Kit](https://kit.com), the e-mail service that sends the daily files, under the
  [Kit privacy policy](https://kit.com/privacy). We use them only to send you the files, to understand who uses the
  data and why, and to write to you about the end of the beta. Kit records whether an e-mail was opened and which links
  were clicked; we use that only to see which files are used. Every e-mail has a one-click unsubscribe link, after
  which nothing more is sent; to have your details deleted, reply to any of the e-mails and say so. The files
  themselves come from a private storage bucket at Amazon Web Services through links that expire after 7 days, under
  the [AWS privacy notice](https://aws.amazon.com/privacy/). We never sell or share the list.
{%- endif %}
- **E-mail subscription.** If a signup box is shown, submitting it sends your address directly to the named
  mailing-list provider, which processes it under its own policy. We see the address only as a subscriber of that list.
- **Requests and purchases.** Data requests go through GitHub issues; purchases of the daily data go through the Apify
  Store. Both are governed by those services' policies, and we see only what they show us.
- **The data we publish** is about companies and their job postings, taken from public job boards. It contains no
  personal data about candidates. If a posting contains personal data and you want it removed from our files, use the
  [request form](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml).

Agilityy Research, publisher of Hiring Pulse. Last updated {% if site.beta_signup_action != "" %}2026-11-25{% else %}2026-11-24{% endif %}. Questions about this page: see
[About]({{ '/about/' | relative_url }}) for how to reach us.
