Postmortem

Duration of the Outage: The outage started at 9:00 AM GMT on April 1, 2024, and ended at 11:00 AM GMT on the same day.
Impact: The web application was down, resulting in a complete service disruption. Approximately 80% of users were affected.
Root Cause: A misconfiguration in the Nginx server caused the outage.
Timeline

9:00 AM: The issue was detected through a monitoring alert indicating that the web application was not responding.
9:15 AM: Initial investigation began, focusing on potential network issues.
9:30 AM: The network was found to be functioning correctly, shifting the focus to server configuration.
10:00 AM: The incident was escalated to the senior DevOps team.
10:30 AM: The root cause was identified as a misconfiguration in the Nginx server.
11:00 AM: The issue was resolved by correcting the Nginx configuration and restarting the server.
Root Cause and Resolution

Root Cause: The issue was caused by an incorrect rewrite rule in the Nginx configuration file, which resulted in requests not being properly routed to the application.
Resolution: The incorrect rewrite rule was identified and corrected, and the Nginx server was restarted, resolving the issue.
Corrective and Preventative Measures

Improvements: Enhance monitoring to detect similar issues in the future, improve documentation related to server configuration, and provide additional training to the team on Nginx configuration.
Tasks: Patch the Nginx server, add more specific monitoring on server configuration, review and update the documentation related to server configuration, and schedule a training session on Nginx configuration for the team.