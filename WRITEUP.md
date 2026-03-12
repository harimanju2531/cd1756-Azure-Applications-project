# Deployment Analysis: VM vs App Service

## Virtual Machine Analysis
- **Costs**: VMs require paying for compute time even when idle. Free tier B1ls is available but limited to 750 hours/month.
- **Scalability**: Manual scaling requiring configuration of load balancers and VM scale sets. Not automatic.
- **Availability**: Need to manually configure availability sets/zones. VM maintenance (updates, patches) required.
- **Workflow**: Full control over environment, can install any software, but requires manual setup of web server (Nginx), SSL certificates, and deployment pipelines.

## App Service Analysis
- **Costs**: Free F1 tier available with 1 GB disk space. Auto-sleep after 20 minutes of inactivity saves costs [citation:5].
- **Scalability**: Built-in auto-scaling capabilities. Easy vertical/horizontal scaling with configuration changes.
- **Availability**: Built-in load balancing, automatic patching, and 99.95% SLA guarantee.
- **Workflow**: Simplified deployment via GitHub Actions or direct upload. Built-in SSL, easy configuration through portal [citation:1].

## Justification
I chose **App Service** for deployment because: [Write 2-3 sentences explaining your choice]

## Scenario Changes
If the application required specific OS configurations, custom software installations, or needed to run background processes that aren't supported by App Service, I would choose a VM.
