---
title: "Contact Agilityy Research"
description: >-
  Data requests, corrections, press and research questions about Hiring Pulse. We answer within two working days.
permalink: /contact/
---
# Contact

Data requests (the whole history, a custom cut, a feed into your systems), corrections, press and research questions.
We answer within two working days. Journalists and researchers usually get a cut of the history free, with attribution.
{% if site.beta_signup_action != "" %}Beta subscribers can also reply to any of the daily e-mails.{% endif %}

{% if site.contact_form_action != "" -%}
<div class="beta card" id="contact-form">
<p id="contact-sent" class="beta-thanks card"><b>Sent.</b> Thank you; we reply within two working days.</p>
<form action="{{ site.contact_form_action }}" method="post" id="contact">
<label><span>Work e-mail</span><input type="email" name="email" autocomplete="email" required></label>
<label><span>Organisation</span><input type="text" name="organisation" maxlength="120" autocomplete="organization"></label>
<label><span>What is it about?</span><select name="topic" required><option value="">Choose one</option><option>A data request: history, a custom cut or a feed</option><option>A correction or a question about a figure</option><option>Press or research</option><option>Something else</option></select></label>
<label class="wide"><span>Your message</span><textarea name="message" rows="5" maxlength="3000" required placeholder="For a data request: which companies, days or tables, and what for."></textarea></label>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">
<input type="hidden" name="_subject" value="Hiring Pulse: contact">
<button type="submit" class="btn">Send</button>
</form>
<p class="muted small">Your message and address go to the form service and from there to us; nothing else is collected. <a href="{{ '/privacy/' | relative_url }}">Privacy</a>.</p>
</div>
<script>
(function () {
  var f = document.getElementById("contact"), ok = document.getElementById("contact-sent"); if (!f || !window.fetch) return;
  f.addEventListener("submit", function (ev) {
    ev.preventDefault(); var b = f.querySelector("button"); b.disabled = true; b.textContent = "Sending…";
    fetch(f.action, {method: "POST", body: new FormData(f), headers: {"Accept": "application/json"}}).then(function (r) {
      if (!r.ok) throw new Error("status " + r.status);
      f.reset(); ok.style.display = "block"; b.textContent = "Sent"; ok.scrollIntoView({block: "nearest"});
    }).catch(function () { b.disabled = false; b.textContent = "Send"; f.removeEventListener("submit", arguments.callee); f.submit(); });
  });
})();
</script>
{%- else -%}
<p class="card" id="contact-address"><b>Write to us:</b> <span id="contact-mail" data-u="data" data-d="agilityy.com">the address appears here when scripts run</span>.
<noscript>data [at] agilityy [dot] com</noscript></p>
<script>(function(){var e=document.getElementById("contact-mail");if(!e)return;var a=e.getAttribute("data-u")+"@"+e.getAttribute("data-d");var l=document.createElement("a");l.href="mailto:"+a+"?subject=Hiring%20Pulse";l.textContent=a;e.replaceWith(l);})();</script>
{%- endif %}

## Before you write

- **The daily data** is free by e-mail during the beta: [get the data]({{ '/get-the-data/' | relative_url }}).
- **How every figure is measured**, and the checks that run each morning: [methodology]({{ '/methodology/' | relative_url }}).
- **Columns, a free sample and loading notes**: [for data teams]({{ '/for-data-teams/' | relative_url }}).
