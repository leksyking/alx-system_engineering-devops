Postmortem: Service Outage Incident
By Ogundipe Felix Oluwagbemileke (gbemilekeogundipe@gmail.com)

![](https://t3.ftcdn.net/jpg/04/92/09/72/240_F_492097246_yagE8x9Uk8M9IekPy7GBuE0x1Uoa7esD.jpg)

Issue Summary:
- Duration: May 29, 2023, 10:00 AM to May 30, 2023, 2:00 PM (WAT)
- Impact: Car Rental Website was completely inaccessible during the outage, affecting 100% of the users.

![](https://iq.opengenus.org/content/images/2020/06/loadcreatedbalancer.png)

Timeline:
- Issue Detected: May 29, 2023, 10:00 AM (WAT)
    - The issue was detected through monitoring alerts triggered by the sudden spike in error rates and the  
      inability to establish database connections.
- Actions Taken:
    - Initially, the focus was on the database layer, assuming it was the root cause of the issue.
    - The database server logs were examined, but no unusual activities or errors were found.
    - Network connectivity was checked, and all connections appeared to be functioning properly.
    - As the issue persisted, the investigation expanded to other system components, including the application server and web server configurations.
- Misleading Investigation/Debugging Paths:
    - Initially, it was suspected that a database query bottleneck was causing the high error rates. However, further analysis revealed that the database was not the primary cause.
    - Network connectivity was investigated extensively, even though it turned out to be functioning correctly.
- Escalation:
    - The incident was escalated to the DevOps team for further investigation and resolution.
- Incident Resolution:
    - After extensive analysis, the root cause was identified as a misconfiguration in the web server's load balancer settings.
    - The load balancer was not distributing traffic evenly, causing certain servers to be overloaded while others remained underutilized.
    - The issue was resolved by adjusting the load balancer settings to ensure proper distribution of traffic among the application servers.

Root Cause and Resolution:
- Root Cause:
    - The misconfiguration in the load balancer resulted in uneven distribution of traffic, leading to server overload and subsequent service unavailability.
- Resolution:
    - The load balancer settings were updated to evenly distribute incoming requests among the available application servers.
    - A thorough testing process was conducted to validate the load balancer configuration changes.
    - Additional monitoring was implemented to ensure that any future load balancing issues are promptly identified and resolved.

Corrective and Preventative Measures:
- Improvement/Fixes:
    - Implement a regular audit process to review and verify load balancer configurations.
    - Enhance monitoring and alerting systems to promptly detect any load balancing issues.
- Tasks:
    - Conduct a comprehensive review of the load balancer configuration across all environments and ensure consistency.
    - Implement automated tests to validate load balancer functionality and distribution.
    - Set up proactive monitoring for load balancer performance and traffic distribution.
Establish incident response procedures for load balancer-related issues, including proper escalation and communication channels.

By addressing the root cause and implementing corrective measures, we aim to prevent similar service outages in the future and ensure a more reliable and resilient Car Rental Website for our users.

