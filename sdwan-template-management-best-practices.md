# Cisco SD-WAN Template Management Best Practices

## Overview

Cisco SD-WAN templates provide centralized and consistent device configuration using vManage. Proper template management reduces configuration drift and simplifies large-scale deployments.

## Template Types

- Feature Templates
- Device Templates
- CLI Templates

## Deployment Workflow

1. Create feature templates.
2. Build a device template.
3. Attach feature templates.
4. Validate variable mappings.
5. Preview the generated configuration.
6. Attach the template to target devices.
7. Verify successful deployment.

## Common Issues

- Missing required variables
- Incorrect VPN interface mappings
- Template attachment failures
- Configuration conflicts
- Device out of sync with vManage

## Validation

- Verify template status in vManage.
- Check configuration preview before deployment.
- Confirm device synchronization.
- Validate routing and tunnel connectivity after deployment.

## Best Practices

- Use reusable feature templates.
- Keep naming conventions consistent.
- Test templates in a lab before production.
- Document template versions and changes.
- Back up device configurations before major updates.