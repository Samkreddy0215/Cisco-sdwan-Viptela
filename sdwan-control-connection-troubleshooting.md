# Cisco SD-WAN Control Connection Troubleshooting

## Overview

Cisco Catalyst SD-WAN uses secure control connections between WAN Edge routers and SD-WAN controllers. Control-connection failures can prevent devices from receiving routes, policies, and centralized configuration.

This guide provides a structured workflow for troubleshooting control-plane connectivity.

## Main SD-WAN Components

- Cisco Catalyst SD-WAN Manager
- Cisco Catalyst SD-WAN Controller
- Cisco Catalyst SD-WAN Validator
- WAN Edge routers

## Control Connection Troubleshooting Workflow

1. Verify WAN interface connectivity.
2. Confirm DNS resolution if controller hostnames are used.
3. Validate system IP and site ID.
4. Verify organization name.
5. Check device certificates.
6. Confirm system clock and NTP synchronization.
7. Inspect active control connections.
8. Review connection-history failures.
9. Validate firewall and NAT traversal.
10. Confirm controller reachability.

## Important Verification Commands

```bash
show sdwan control connections
show sdwan control connections-history
show sdwan control local-properties
show sdwan system status
show sdwan bfd sessions
show clock
```

## Check Active Control Connections

Run:

```bash
show sdwan control connections
```

Verify that expected controller connections are established.

Review:

- Peer type
- Peer system IP
- Site ID
- Local color
- Remote color
- Connection state
- Uptime

## Check Connection History

Run:

```bash
show sdwan control connections-history
```

Use connection history to identify repeated authentication, certificate, reachability, or transport failures.

## Validate Local Properties

Run:

```bash
show sdwan control local-properties
```

Confirm:

- Organization name
- System IP
- Site ID
- Certificate status
- WAN transport interfaces
- Public and private IP information

## Common Failure Scenarios

### Controller Unreachable

Verify:

- Default route
- Underlay routing
- DNS
- Firewall rules
- NAT
- Internet/MPLS connectivity

### Organization Name Mismatch

The organization name must match the SD-WAN controller environment.

### Certificate Problems

Validate certificate status and ensure the WAN Edge router is authorized correctly.

### Incorrect System Time

Certificate validation can fail when device time is incorrect.

Configure and verify reliable NTP synchronization.

### Transport Interface Problem

Confirm that the WAN interface has:

- Correct IP addressing
- Proper tunnel configuration
- Required transport color
- Working underlay connectivity

## Validation Checklist

- WAN interface is operational.
- Underlay routing works.
- Controllers are reachable.
- DNS resolution works where required.
- System IP is correct.
- Site ID is correct.
- Organization name matches.
- Certificates are valid.
- NTP synchronization is working.
- Expected control connections are established.
- No recurring failures appear in connection history.

## Operational Best Practices

- Monitor control-connection availability.
- Maintain redundant transports where required.
- Configure reliable NTP sources.
- Document site IDs and system IP assignments.
- Monitor certificate expiration.
- Baseline normal controller connectivity.
- Review connection history during incidents.
- Validate control connections after WAN changes.

## Troubleshooting Sequence

Follow this order during an incident:

```text
WAN Interface
      ↓
Underlay Routing
      ↓
DNS / Controller Reachability
      ↓
NAT / Firewall
      ↓
Identity Parameters
      ↓
Certificates / NTP
      ↓
Control Connections
      ↓
Connection History
      ↓
Policy and Overlay Validation
```

Following a consistent troubleshooting sequence helps isolate whether an SD-WAN outage originates from the transport network, device identity, security establishment, or SD-WAN control plane.
