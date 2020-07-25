# -*- coding: utf-8 -*- #
"""Cloud SDK static completion CLI tree."""
# pylint: disable=line-too-long,bad-continuation
STATIC_COMPLETION_CLI_TREE = {
  "commands": {
    "alpha": {
      "commands": {
        "app": {
          "commands": {
            "domain-mappings": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--certificate-id": "value",
                    "--certificate-management": [
                      "automatic",
                      "manual"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--certificate-id": "value",
                    "--certificate-management": [
                      "automatic",
                      "manual"
                    ],
                    "--no-certificate-id": "bool"
                  }
                }
              },
              "flags": {}
            },
            "ssl-certificates": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--certificate": "value",
                    "--display-name": "value",
                    "--private-key": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--certificate": "value",
                    "--display-name": "value",
                    "--private-key": "value"
                  }
                }
              },
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--split-health-checks": "bool",
                "--use-container-optimized-os": "bool"
              }
            }
          },
          "flags": {}
        },
        "auth": {
          "commands": {
            "activate-service-account": {
              "commands": {},
              "flags": {
                "--key-file": "value",
                "--password-file": "value",
                "--prompt-for-password": "bool"
              }
            },
            "configure-docker": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--filter-account": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "login": {
              "commands": {},
              "flags": {
                "--activate": "bool",
                "--brief": "bool",
                "--enable-gdrive-access": "bool",
                "--force": "bool",
                "--launch-browser": "bool"
              }
            },
            "revoke": {
              "commands": {},
              "flags": {
                "--all": "bool"
              }
            }
          },
          "flags": {}
        },
        "billing": {
          "commands": {
            "accounts": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "projects": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "link": {
                      "commands": {},
                      "flags": {
                        "--account-id": "dynamic",
                        "--billing-account": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--billing-account": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    },
                    "unlink": {
                      "commands": {},
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "projects": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "link": {
                  "commands": {},
                  "flags": {
                    "--account-id": "dynamic",
                    "--billing-account": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "dynamic",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "unlink": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "builds": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--ongoing": "bool",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "log": {
              "commands": {},
              "flags": {
                "--stream": "bool"
              }
            },
            "submit": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--config": "value",
                "--disk-size": "value",
                "--gcs-log-dir": "value",
                "--gcs-source-staging-dir": "value",
                "--machine-type": [
                  "n1-highcpu-32",
                  "n1-highcpu-8"
                ],
                "--no-source": "bool",
                "--substitutions": "value",
                "--tag": "value",
                "--timeout": "value"
              }
            }
          },
          "flags": {}
        },
        "cloud-shell": {
          "commands": {
            "get-mount-command": {
              "commands": {},
              "flags": {
                "--force-key-file-overwrite": "bool",
                "--ssh-key-file": "bool"
              }
            },
            "scp": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--recurse": "bool",
                "--scp-flag": "value",
                "--ssh-key-file": "bool"
              }
            },
            "ssh": {
              "commands": {},
              "flags": {
                "--command": "value",
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--ssh-flag": "value",
                "--ssh-key-file": "bool"
              }
            }
          },
          "flags": {}
        },
        "compute": {
          "commands": {
            "accelerator-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "addresses": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--addresses": "value",
                    "--description": "value",
                    "--global": "bool",
                    "--ip-version": [
                      "IPV4",
                      "IPV6"
                    ],
                    "--network": "value",
                    "--network-tier": "value",
                    "--prefix-length": "value",
                    "--purpose": [
                      "GCE_ENDPOINT",
                      "VPC_PEERING"
                    ],
                    "--region": "dynamic",
                    "--subnet": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--global": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "backend-buckets": {
              "commands": {
                "add-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-file": "value",
                    "--key-name": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-cdn": "bool",
                    "--gcs-bucket-name": "dynamic",
                    "--signed-url-cache-max-age": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "delete-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-name": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-cdn": "bool",
                    "--gcs-bucket-name": "dynamic",
                    "--signed-url-cache-max-age": "value"
                  }
                }
              },
              "flags": {}
            },
            "backend-services": {
              "commands": {
                "add-backend": {
                  "commands": {},
                  "flags": {
                    "--balancing-mode": [
                      "CONNECTION",
                      "RATE",
                      "UTILIZATION"
                    ],
                    "--capacity-scaler": "value",
                    "--description": "value",
                    "--failover": "bool",
                    "--global": "bool",
                    "--instance-group": "dynamic",
                    "--instance-group-region": "dynamic",
                    "--instance-group-zone": "dynamic",
                    "--max-connections": "value",
                    "--max-connections-per-endpoint": "value",
                    "--max-connections-per-instance": "value",
                    "--max-rate": "value",
                    "--max-rate-per-endpoint": "value",
                    "--max-rate-per-instance": "value",
                    "--max-utilization": "value",
                    "--network-endpoint-group": "value",
                    "--network-endpoint-group-zone": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "add-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-file": "value",
                    "--key-name": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--affinity-cookie-ttl": "value",
                    "--cache-key-include-host": "bool",
                    "--cache-key-include-protocol": "bool",
                    "--cache-key-include-query-string": "bool",
                    "--cache-key-query-string-blacklist": "value",
                    "--cache-key-query-string-whitelist": "value",
                    "--connection-drain-on-failover": "bool",
                    "--connection-draining-timeout": "value",
                    "--custom-request-header": "value",
                    "--description": "value",
                    "--drop-traffic-if-unhealthy": "bool",
                    "--enable-cdn": "bool",
                    "--failover-ratio": "value",
                    "--global": "bool",
                    "--health-checks": "dynamic",
                    "--http-health-checks": "dynamic",
                    "--https-health-checks": "dynamic",
                    "--iap": "value",
                    "--load-balancing-scheme": [
                      "EXTERNAL",
                      "INTERNAL",
                      "INTERNAL_SELF_MANAGED"
                    ],
                    "--port-name": "value",
                    "--protocol": [
                      "HTTP",
                      "HTTP2",
                      "HTTPS",
                      "SSL",
                      "TCP",
                      "UDP"
                    ],
                    "--region": "dynamic",
                    "--session-affinity": [
                      "CLIENT_IP",
                      "CLIENT_IP_PORT_PROTO",
                      "CLIENT_IP_PROTO",
                      "GENERATED_COOKIE",
                      "NONE"
                    ],
                    "--signed-url-cache-max-age": "value",
                    "--timeout": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "delete-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-name": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "edit": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "get-health": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-backend": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--instance-group": "dynamic",
                    "--instance-group-region": "dynamic",
                    "--instance-group-zone": "dynamic",
                    "--network-endpoint-group": "value",
                    "--network-endpoint-group-zone": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "set-security-policy": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic",
                    "--security-policy": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--affinity-cookie-ttl": "value",
                    "--cache-key-include-host": "bool",
                    "--cache-key-include-protocol": "bool",
                    "--cache-key-include-query-string": "bool",
                    "--cache-key-query-string-blacklist": "value",
                    "--cache-key-query-string-whitelist": "value",
                    "--connection-drain-on-failover": "bool",
                    "--connection-draining-timeout": "value",
                    "--custom-request-header": "value",
                    "--description": "value",
                    "--drop-traffic-if-unhealthy": "bool",
                    "--enable-cdn": "bool",
                    "--failover-ratio": "value",
                    "--global": "bool",
                    "--health-checks": "dynamic",
                    "--http-health-checks": "dynamic",
                    "--https-health-checks": "dynamic",
                    "--iap": "value",
                    "--no-custom-request-headers": "bool",
                    "--port-name": "value",
                    "--protocol": [
                      "HTTP",
                      "HTTP2",
                      "HTTPS",
                      "SSL",
                      "TCP",
                      "UDP"
                    ],
                    "--region": "dynamic",
                    "--security-policy": "dynamic",
                    "--session-affinity": [
                      "CLIENT_IP",
                      "CLIENT_IP_PORT_PROTO",
                      "CLIENT_IP_PROTO",
                      "GENERATED_COOKIE",
                      "NONE"
                    ],
                    "--signed-url-cache-max-age": "value",
                    "--timeout": "value"
                  }
                },
                "update-backend": {
                  "commands": {},
                  "flags": {
                    "--balancing-mode": [
                      "CONNECTION",
                      "RATE",
                      "UTILIZATION"
                    ],
                    "--capacity-scaler": "value",
                    "--description": "value",
                    "--failover": "bool",
                    "--global": "bool",
                    "--instance-group": "dynamic",
                    "--instance-group-region": "dynamic",
                    "--instance-group-zone": "dynamic",
                    "--max-connections": "value",
                    "--max-connections-per-endpoint": "value",
                    "--max-connections-per-instance": "value",
                    "--max-rate": "value",
                    "--max-rate-per-endpoint": "value",
                    "--max-rate-per-instance": "value",
                    "--max-utilization": "value",
                    "--network-endpoint-group": "value",
                    "--network-endpoint-group-zone": "dynamic",
                    "--region": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "commitments": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--plan": [
                      "12-month",
                      "36-month"
                    ],
                    "--region": "dynamic",
                    "--resources": "value",
                    "--type": [
                      "general-purpose",
                      "memory-optimized"
                    ]
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "config-ssh": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--remove": "bool",
                "--ssh-config-file": "value",
                "--ssh-key-file": "value"
              }
            },
            "connect-to-serial-port": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--extra-args": "value",
                "--force-key-file-overwrite": "bool",
                "--port": "value",
                "--ssh-key-file": "value",
                "--zone": "dynamic"
              }
            },
            "copy-files": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--plain": "bool",
                "--ssh-key-file": "value",
                "--strict-host-key-checking": [
                  "ask",
                  "no",
                  "yes"
                ],
                "--zone": "value"
              }
            },
            "disk-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                }
              },
              "flags": {}
            },
            "disks": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "add-resource-policies": {
                  "commands": {},
                  "flags": {
                    "--resource-policies": "value",
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--csek-key-file": "value",
                    "--description": "value",
                    "--guest-os-features": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--kms-key": "dynamic",
                    "--kms-keyring": "dynamic",
                    "--kms-location": "dynamic",
                    "--kms-project": "dynamic",
                    "--labels": "value",
                    "--licenses": "value",
                    "--region": "dynamic",
                    "--replica-zones": "value",
                    "--require-csek-key-create": "bool",
                    "--resource-policies": "value",
                    "--size": "value",
                    "--source-snapshot": "dynamic",
                    "--type": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                },
                "move": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--destination-zone": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "remove-resource-policies": {
                  "commands": {},
                  "flags": {
                    "--resource-policies": "value",
                    "--zone": "dynamic"
                  }
                },
                "resize": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--size": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "snapshot": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--csek-key-file": "value",
                    "--description": "value",
                    "--guest-flush": "bool",
                    "--region": "dynamic",
                    "--snapshot-names": "value",
                    "--storage-location": "value",
                    "--zone": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "firewall-rules": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--action": [
                      "ALLOW",
                      "DENY"
                    ],
                    "--allow": "value",
                    "--description": "value",
                    "--destination-ranges": "value",
                    "--direction": [
                      "EGRESS",
                      "IN",
                      "INGRESS",
                      "OUT"
                    ],
                    "--disabled": "bool",
                    "--enable-logging": "bool",
                    "--network": "value",
                    "--priority": "value",
                    "--rules": "value",
                    "--source-ranges": "value",
                    "--source-service-accounts": "value",
                    "--source-tags": "value",
                    "--target-service-accounts": "value",
                    "--target-tags": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--allow": "value",
                    "--description": "value",
                    "--destination-ranges": "value",
                    "--disabled": "bool",
                    "--enable-logging": "bool",
                    "--priority": "value",
                    "--rules": "value",
                    "--source-ranges": "value",
                    "--source-service-accounts": "value",
                    "--source-tags": "value",
                    "--target-service-accounts": "value",
                    "--target-tags": "value"
                  }
                }
              },
              "flags": {}
            },
            "forwarding-rules": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--address": "dynamic",
                    "--address-region": "dynamic",
                    "--backend-service": "value",
                    "--backend-service-region": "dynamic",
                    "--description": "value",
                    "--global": "bool",
                    "--global-address": "bool",
                    "--global-backend-service": "bool",
                    "--ip-protocol": [
                      "AH",
                      "ESP",
                      "ICMP",
                      "SCTP",
                      "TCP",
                      "UDP"
                    ],
                    "--ip-version": [
                      "IPV4",
                      "IPV6"
                    ],
                    "--load-balancing-scheme": [
                      "EXTERNAL",
                      "INTERNAL",
                      "INTERNAL_SELF_MANAGED"
                    ],
                    "--network": "value",
                    "--network-tier": "value",
                    "--port-range": "value",
                    "--ports": "value",
                    "--region": "dynamic",
                    "--service-label": "value",
                    "--subnet": "value",
                    "--subnet-region": "dynamic",
                    "--target-http-proxy": "value",
                    "--target-https-proxy": "value",
                    "--target-instance": "value",
                    "--target-instance-zone": "dynamic",
                    "--target-pool": "value",
                    "--target-pool-region": "dynamic",
                    "--target-ssl-proxy": "value",
                    "--target-tcp-proxy": "value",
                    "--target-vpn-gateway": "value",
                    "--target-vpn-gateway-region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-target": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "value",
                    "--backend-service-region": "dynamic",
                    "--global": "bool",
                    "--global-backend-service": "bool",
                    "--load-balancing-scheme": [
                      "EXTERNAL",
                      "INTERNAL",
                      "INTERNAL_SELF_MANAGED"
                    ],
                    "--network": "value",
                    "--region": "dynamic",
                    "--subnet": "value",
                    "--subnet-region": "dynamic",
                    "--target-http-proxy": "value",
                    "--target-https-proxy": "value",
                    "--target-instance": "value",
                    "--target-instance-zone": "dynamic",
                    "--target-pool": "value",
                    "--target-pool-region": "dynamic",
                    "--target-ssl-proxy": "value",
                    "--target-tcp-proxy": "value",
                    "--target-vpn-gateway": "value",
                    "--target-vpn-gateway-region": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--global": "bool",
                    "--network-tier": "value",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "health-checks": {
              "commands": {
                "create": {
                  "commands": {
                    "http": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--port-specification": [
                          "use-fixed-port",
                          "use-named-port",
                          "use-serving-port"
                        ],
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "http2": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--port-specification": [
                          "use-fixed-port",
                          "use-named-port",
                          "use-serving-port"
                        ],
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "https": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--port-specification": [
                          "use-fixed-port",
                          "use-named-port",
                          "use-serving-port"
                        ],
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "ssl": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--port-specification": [
                          "use-fixed-port",
                          "use-named-port",
                          "use-serving-port"
                        ],
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "tcp": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--port-specification": [
                          "use-fixed-port",
                          "use-named-port",
                          "use-serving-port"
                        ],
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--protocol": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {
                    "http": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "http2": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "https": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "ssl": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "tcp": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "http-health-checks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                }
              },
              "flags": {}
            },
            "https-health-checks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                }
              },
              "flags": {}
            },
            "images": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--csek-key-file": "value",
                    "--description": "value",
                    "--family": "value",
                    "--force": "bool",
                    "--force-create": "bool",
                    "--guest-os-features": "value",
                    "--kms-key": "dynamic",
                    "--kms-keyring": "dynamic",
                    "--kms-location": "dynamic",
                    "--kms-project": "dynamic",
                    "--labels": "value",
                    "--licenses": "value",
                    "--require-csek-key-create": "bool",
                    "--source-disk": "dynamic",
                    "--source-disk-zone": "dynamic",
                    "--source-image": "value",
                    "--source-image-family": "value",
                    "--source-image-project": "value",
                    "--source-snapshot": "dynamic",
                    "--source-uri": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "deprecate": {
                  "commands": {},
                  "flags": {
                    "--delete-in": "value",
                    "--delete-on": "value",
                    "--obsolete-in": "value",
                    "--obsolete-on": "value",
                    "--replacement": "dynamic",
                    "--state": [
                      "ACTIVE",
                      "DELETED",
                      "DEPRECATED",
                      "OBSOLETE"
                    ]
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "describe-from-family": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--destination-uri": "value",
                    "--export-format": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--log-location": "value",
                    "--network": "value",
                    "--timeout": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--data-disk": "bool",
                    "--log-location": "value",
                    "--os": [
                      "centos-6",
                      "centos-7",
                      "debian-8",
                      "debian-9",
                      "rhel-6",
                      "rhel-6-byol",
                      "rhel-7",
                      "rhel-7-byol",
                      "ubuntu-1404",
                      "ubuntu-1604",
                      "windows-2008r2",
                      "windows-2012r2",
                      "windows-2016"
                    ],
                    "--source-file": "value",
                    "--source-image": "dynamic",
                    "--timeout": "value",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--preview-images": "bool",
                    "--regexp": "value",
                    "--show-deprecated": "bool",
                    "--sort-by": "value",
                    "--standard-images": "bool",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                },
                "vulnerabilities": {
                  "commands": {
                    "describe-note": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--image": "dynamic",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "instance-groups": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "get-named-ports": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                },
                "list-instances": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "managed": {
                  "commands": {
                    "abandon-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--base-instance-name": "value",
                        "--description": "value",
                        "--health-check": "dynamic",
                        "--http-health-check": "value",
                        "--https-health-check": "value",
                        "--initial-delay": "value",
                        "--instance-redistribution-type": [
                          "NONE",
                          "PROACTIVE"
                        ],
                        "--region": "dynamic",
                        "--size": "value",
                        "--stateful-disks": "value",
                        "--stateful-names": "bool",
                        "--target-pool": "value",
                        "--template": "value",
                        "--zone": "dynamic",
                        "--zones": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "delete-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "export-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--autoscaling-file": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "get-named-ports": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "instance-configs": {
                      "commands": {
                        "create": {
                          "commands": {},
                          "flags": {
                            "--force-instance-update": "bool",
                            "--instance": "value",
                            "--region": "dynamic",
                            "--stateful-disk": "value",
                            "--stateful-metadata": "value",
                            "--zone": "dynamic"
                          }
                        },
                        "delete": {
                          "commands": {},
                          "flags": {
                            "--force-instance-update": "bool",
                            "--instances": "value",
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--region": "dynamic",
                            "--sort-by": "value",
                            "--uri": "bool",
                            "--zone": "dynamic"
                          }
                        },
                        "update": {
                          "commands": {},
                          "flags": {
                            "--force-instance-update": "bool",
                            "--instance": "value",
                            "--region": "dynamic",
                            "--remove-stateful-disks": "value",
                            "--remove-stateful-metadata": "value",
                            "--update-stateful-disk": "value",
                            "--update-stateful-metadata": "value",
                            "--zone": "dynamic"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--regions": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zones": "value"
                      }
                    },
                    "list-instances": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "recreate-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "resize": {
                      "commands": {},
                      "flags": {
                        "--creation-retries": "bool",
                        "--region": "dynamic",
                        "--size": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "rolling-action": {
                      "commands": {
                        "replace": {
                          "commands": {},
                          "flags": {
                            "--max-surge": "value",
                            "--max-unavailable": "value",
                            "--min-ready": "value",
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        },
                        "restart": {
                          "commands": {},
                          "flags": {
                            "--max-unavailable": "value",
                            "--min-ready": "value",
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        },
                        "start-update": {
                          "commands": {},
                          "flags": {
                            "--canary-version": "value",
                            "--force": "bool",
                            "--max-surge": "value",
                            "--max-unavailable": "value",
                            "--min-ready": "value",
                            "--region": "dynamic",
                            "--type": [
                              "opportunistic",
                              "proactive"
                            ],
                            "--zone": "dynamic"
                          }
                        },
                        "stop-proactive-update": {
                          "commands": {},
                          "flags": {
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "set-autohealing": {
                      "commands": {},
                      "flags": {
                        "--health-check": "dynamic",
                        "--http-health-check": "value",
                        "--https-health-check": "value",
                        "--initial-delay": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "set-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--autoscaling-file": "value",
                        "--cool-down-period": "value",
                        "--custom-metric-utilization": "value",
                        "--description": "value",
                        "--max-num-replicas": "value",
                        "--min-num-replicas": "value",
                        "--mode": [
                          "off",
                          "on",
                          "only-down",
                          "only-up"
                        ],
                        "--queue-scaling-acceptable-backlog-per-instance": "value",
                        "--queue-scaling-cloud-pub-sub": "value",
                        "--queue-scaling-single-worker-throughput": "value",
                        "--region": "dynamic",
                        "--remove-stackdriver-metric": "value",
                        "--scale-based-on-cpu": "bool",
                        "--scale-based-on-load-balancing": "bool",
                        "--stackdriver-metric-filter": "value",
                        "--stackdriver-metric-single-instance-assignment": "value",
                        "--stackdriver-metric-utilization-target": "value",
                        "--stackdriver-metric-utilization-target-type": [
                          "delta-per-minute",
                          "delta-per-second",
                          "gauge"
                        ],
                        "--target-cpu-utilization": "value",
                        "--target-load-balancing-utilization": "value",
                        "--update-stackdriver-metric": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "set-instance-template": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--template": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "set-named-ports": {
                      "commands": {},
                      "flags": {
                        "--named-ports": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "set-target-pools": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--target-pools": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "stop-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--add-stateful-disks": "value",
                        "--instance-redistribution-type": [
                          "NONE",
                          "PROACTIVE"
                        ],
                        "--region": "dynamic",
                        "--remove-stateful-disks": "value",
                        "--stateful-names": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "update-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--mode": [
                          "off",
                          "on",
                          "only-down",
                          "only-up"
                        ],
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "wait-until-stable": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--timeout": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "set-named-ports": {
                  "commands": {},
                  "flags": {
                    "--named-ports": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "unmanaged": {
                  "commands": {
                    "add-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "get-named-ports": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zones": "dynamic"
                      }
                    },
                    "list-instances": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "remove-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "set-named-ports": {
                      "commands": {},
                      "flags": {
                        "--named-ports": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "instance-templates": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--address": "value",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-kms-key": "dynamic",
                    "--boot-disk-kms-keyring": "dynamic",
                    "--boot-disk-kms-location": "dynamic",
                    "--boot-disk-kms-project": "dynamic",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--configure-disk": "value",
                    "--create-disk": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--node": "value",
                    "--node-affinity-file": "value",
                    "--node-group": "value",
                    "--on-host-maintenance": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--preemptible": "bool",
                    "--region": "dynamic",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--shielded-vm-integrity-monitoring": "bool",
                    "--shielded-vm-secure-boot": "bool",
                    "--shielded-vm-vtpm": "bool",
                    "--source-instance": "dynamic",
                    "--source-instance-zone": "dynamic",
                    "--subnet": "value",
                    "--tags": "value"
                  }
                },
                "create-with-container": {
                  "commands": {},
                  "flags": {
                    "--address": "value",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--container-arg": "value",
                    "--container-command": "value",
                    "--container-env": "value",
                    "--container-env-file": "value",
                    "--container-image": "value",
                    "--container-mount-host-path": "value",
                    "--container-mount-tmpfs": "value",
                    "--container-privileged": "bool",
                    "--container-restart-policy": [
                      "always",
                      "never",
                      "on-failure"
                    ],
                    "--container-stdin": "bool",
                    "--container-tty": "bool",
                    "--create-disk": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--on-host-maintenance": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--preemptible": "bool",
                    "--region": "dynamic",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--subnet": "value",
                    "--tags": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "add-access-config": {
                  "commands": {},
                  "flags": {
                    "--access-config-name": "value",
                    "--address": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-public-dns": "bool",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--public-dns": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-metadata": {
                  "commands": {},
                  "flags": {
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-resource-policies": {
                  "commands": {},
                  "flags": {
                    "--resource-policies": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-tags": {
                  "commands": {},
                  "flags": {
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "attach-disk": {
                  "commands": {},
                  "flags": {
                    "--csek-key-file": "value",
                    "--device-name": "value",
                    "--disk": "value",
                    "--disk-scope": [
                      "regional",
                      "zonal"
                    ],
                    "--force-attach": "bool",
                    "--mode": [
                      "ro",
                      "rw"
                    ],
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--address": "value",
                    "--async": "bool",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-kms-key": "dynamic",
                    "--boot-disk-kms-keyring": "dynamic",
                    "--boot-disk-kms-location": "dynamic",
                    "--boot-disk-kms-project": "dynamic",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--create-disk": "value",
                    "--csek-key-file": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--deletion-protection": "bool",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-public-dns": "bool",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--node": "value",
                    "--node-affinity-file": "value",
                    "--node-group": "value",
                    "--on-host-maintenance": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--preemptible": "bool",
                    "--private-network-ip": "value",
                    "--public-dns": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--require-csek-key-create": "bool",
                    "--resource-policies": "value",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--shielded-vm-integrity-monitoring": "bool",
                    "--shielded-vm-secure-boot": "bool",
                    "--shielded-vm-vtpm": "bool",
                    "--source-instance-template": "dynamic",
                    "--subnet": "value",
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "create-with-container": {
                  "commands": {},
                  "flags": {
                    "--address": "value",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--container-arg": "value",
                    "--container-command": "value",
                    "--container-env": "value",
                    "--container-env-file": "value",
                    "--container-image": "value",
                    "--container-mount-host-path": "value",
                    "--container-mount-tmpfs": "value",
                    "--container-privileged": "bool",
                    "--container-restart-policy": [
                      "always",
                      "never",
                      "on-failure"
                    ],
                    "--container-stdin": "bool",
                    "--container-tty": "bool",
                    "--create-disk": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-public-dns": "bool",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--on-host-maintenance": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--preemptible": "bool",
                    "--private-network-ip": "value",
                    "--public-dns": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--source-instance-template": "dynamic",
                    "--subnet": "value",
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--delete-disks": [
                      "all",
                      "boot",
                      "data"
                    ],
                    "--keep-disks": [
                      "all",
                      "boot",
                      "data"
                    ],
                    "--zone": "dynamic"
                  }
                },
                "delete-access-config": {
                  "commands": {},
                  "flags": {
                    "--access-config-name": "value",
                    "--network-interface": "value",
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--guest-attributes": "value",
                    "--zone": "dynamic"
                  }
                },
                "detach-disk": {
                  "commands": {},
                  "flags": {
                    "--device-name": "value",
                    "--disk": "value",
                    "--disk-scope": [
                      "regional",
                      "zonal"
                    ],
                    "--zone": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--zone": "value"
                  }
                },
                "get-serial-port-output": {
                  "commands": {},
                  "flags": {
                    "--port": "value",
                    "--start": "value",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                },
                "move": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--destination-zone": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "network-interfaces": {
                  "commands": {
                    "update": {
                      "commands": {},
                      "flags": {
                        "--aliases": "value",
                        "--network-interface": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-metadata": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--keys": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-resource-policies": {
                  "commands": {},
                  "flags": {
                    "--resource-policies": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-tags": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "reset": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "resume": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--csek-key-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-disk-auto-delete": {
                  "commands": {},
                  "flags": {
                    "--auto-delete": "bool",
                    "--device-name": "value",
                    "--disk": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "set-machine-type": {
                  "commands": {},
                  "flags": {
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--machine-type": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "set-min-cpu-platform": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--min-cpu-platform": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-scheduling": {
                  "commands": {},
                  "flags": {
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--on-host-maintenance": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--restart-on-failure": "bool",
                    "--zone": "dynamic"
                  }
                },
                "set-scopes": {
                  "commands": {},
                  "flags": {
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--zone": "dynamic"
                  }
                },
                "simulate-maintenance-event": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "dynamic"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--csek-key-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--discard-local-ssd": "bool",
                    "--zone": "dynamic"
                  }
                },
                "suspend": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--discard-local-ssd": "bool",
                    "--zone": "dynamic"
                  }
                },
                "tail-serial-port-output": {
                  "commands": {},
                  "flags": {
                    "--port": "value",
                    "--zone": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--deletion-protection": "bool",
                    "--min-cpu-platform": "value",
                    "--remove-labels": "value",
                    "--shielded-vm-integrity-monitoring": "bool",
                    "--shielded-vm-learn-integrity-policy": "bool",
                    "--shielded-vm-secure-boot": "bool",
                    "--shielded-vm-vtpm": "bool",
                    "--update-labels": "value",
                    "--zone": "dynamic"
                  }
                },
                "update-access-config": {
                  "commands": {},
                  "flags": {
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-public-dns": "bool",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--public-dns": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--zone": "dynamic"
                  }
                },
                "update-container": {
                  "commands": {},
                  "flags": {
                    "--clear-container-args": "bool",
                    "--clear-container-command": "bool",
                    "--container-arg": "value",
                    "--container-command": "value",
                    "--container-env": "value",
                    "--container-env-file": "value",
                    "--container-image": "value",
                    "--container-mount-host-path": "value",
                    "--container-mount-tmpfs": "value",
                    "--container-privileged": "bool",
                    "--container-restart-policy": [
                      "always",
                      "never",
                      "on-failure"
                    ],
                    "--container-stdin": "bool",
                    "--container-tty": "bool",
                    "--remove-container-env": "value",
                    "--remove-container-mounts": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "interconnects": {
              "commands": {
                "attachments": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--interconnect": "dynamic",
                        "--region": "dynamic",
                        "--router": "dynamic"
                      }
                    },
                    "dedicated": {
                      "commands": {
                        "create": {
                          "commands": {},
                          "flags": {
                            "--candidate-subnets": "value",
                            "--description": "value",
                            "--enable-admin": "bool",
                            "--interconnect": "dynamic",
                            "--region": "dynamic",
                            "--router": "dynamic",
                            "--vlan": "value"
                          }
                        },
                        "update": {
                          "commands": {},
                          "flags": {
                            "--clear-labels": "bool",
                            "--description": "value",
                            "--enable-admin": "bool",
                            "--region": "dynamic",
                            "--remove-labels": "value",
                            "--update-labels": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "partner": {
                      "commands": {
                        "create": {
                          "commands": {},
                          "flags": {
                            "--description": "value",
                            "--edge-availability-domain": [
                              "any",
                              "availability-domain-1",
                              "availability-domain-2"
                            ],
                            "--enable-admin": "bool",
                            "--region": "dynamic",
                            "--router": "dynamic"
                          }
                        },
                        "update": {
                          "commands": {},
                          "flags": {
                            "--clear-labels": "bool",
                            "--description": "value",
                            "--enable-admin": "bool",
                            "--region": "dynamic",
                            "--remove-labels": "value",
                            "--update-labels": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--admin-enabled": "bool",
                    "--customer-name": "value",
                    "--description": "value",
                    "--interconnect-type": [
                      "DEDICATED",
                      "IT_PRIVATE",
                      "PARTNER"
                    ],
                    "--link-type": [
                      "LINK_TYPE_ETHERNET_10G_LR"
                    ],
                    "--location": "dynamic",
                    "--noc-contact-email": "value",
                    "--requested-link-count": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "locations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--admin-enabled": "bool",
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--noc-contact-email": "value",
                    "--remove-labels": "value",
                    "--requested-link-count": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "machine-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "network-endpoint-groups": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--default-port": "value",
                    "--network": "value",
                    "--subnet": "value",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-network-endpoints": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--zone": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-endpoint": "value",
                    "--remove-endpoint": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "networks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--bgp-routing-mode": [
                      "global",
                      "regional"
                    ],
                    "--description": "value",
                    "--mode": [
                      "auto",
                      "custom",
                      "legacy"
                    ],
                    "--range": "value",
                    "--subnet-mode": [
                      "auto",
                      "custom",
                      "legacy"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-ip-owners": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--ip-cidr-range": "value",
                    "--limit": "value",
                    "--owner-projects": "value",
                    "--owner-types": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--subnet-name": "value",
                    "--subnet-region": "value",
                    "--uri": "bool"
                  }
                },
                "peerings": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--auto-create-routes": "bool",
                        "--export-custom-routes": "bool",
                        "--import-custom-routes": "bool",
                        "--network": "value",
                        "--peer-network": "value",
                        "--peer-project": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--network": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--network": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "subnets": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--enable-flow-logs": "bool",
                        "--enable-private-ip-google-access": "bool",
                        "--network": "dynamic",
                        "--range": "value",
                        "--region": "dynamic",
                        "--secondary-range": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "expand-ip-range": {
                      "commands": {},
                      "flags": {
                        "--prefix-length": "value",
                        "--region": "dynamic"
                      }
                    },
                    "get-iam-policy": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "value",
                        "--sort-by": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--network": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--regions": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "list-usable": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "set-iam-policy": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--add-secondary-ranges": "value",
                        "--enable-flow-logs": "bool",
                        "--enable-private-ip-google-access": "bool",
                        "--region": "dynamic",
                        "--remove-secondary-ranges": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--bgp-routing-mode": [
                      "global",
                      "regional"
                    ],
                    "--switch-to-custom-subnet-mode": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                }
              },
              "flags": {}
            },
            "os-login": {
              "commands": {
                "describe-profile": {
                  "commands": {},
                  "flags": {}
                },
                "remove-profile": {
                  "commands": {},
                  "flags": {
                    "--operating-system": [
                      "linux",
                      "windows"
                    ]
                  }
                },
                "ssh-keys": {
                  "commands": {
                    "add": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value",
                        "--ttl": "value"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value",
                        "--ttl": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "project-info": {
              "commands": {
                "add-metadata": {
                  "commands": {},
                  "flags": {
                    "--metadata": "value",
                    "--metadata-from-file": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "remove-metadata": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--keys": "value"
                  }
                },
                "set-default-service-account": {
                  "commands": {},
                  "flags": {
                    "--no-service-account": "bool",
                    "--service-account": "value"
                  }
                },
                "set-usage-bucket": {
                  "commands": {},
                  "flags": {
                    "--bucket": "value",
                    "--no-bucket": "bool",
                    "--prefix": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--default-network-tier": [
                      "PREMIUM",
                      "STANDARD"
                    ]
                  }
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "reset-windows-password": {
              "commands": {},
              "flags": {
                "--user": "value",
                "--zone": "dynamic"
              }
            },
            "resource-policies": {
              "commands": {
                "create-backup-schedule": {
                  "commands": {},
                  "flags": {
                    "--daily-schedule": "bool",
                    "--description": "value",
                    "--guest-flush": "bool",
                    "--hourly-schedule": "value",
                    "--max-retention-days": "value",
                    "--region": "dynamic",
                    "--snapshot-labels": "value",
                    "--start-time": "value",
                    "--weekly-schedule": [
                      "friday",
                      "monday",
                      "saturday",
                      "sunday",
                      "thursday",
                      "tuesday",
                      "wednesday"
                    ],
                    "--weekly-schedule-from-file": "value"
                  }
                },
                "create-vm-maintenance": {
                  "commands": {},
                  "flags": {
                    "--daily-window": "bool",
                    "--description": "value",
                    "--region": "dynamic",
                    "--start-time": "value",
                    "--weekly-window": [
                      "friday",
                      "monday",
                      "saturday",
                      "sunday",
                      "thursday",
                      "tuesday",
                      "wednesday"
                    ],
                    "--weekly-window-from-file": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "rolling-updates": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--group": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "value"
                  }
                },
                "list-instance-updates": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "value"
                  }
                },
                "pause": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "resume": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "rollback": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--action": [
                      "RECREATE"
                    ],
                    "--auto-pause-after-instances": "value",
                    "--group": "value",
                    "--instance-startup-timeout": "value",
                    "--max-num-concurrent-instances": "value",
                    "--max-num-failed-instances": "value",
                    "--min-instance-update-time": "value",
                    "--template": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--zone": "value"
              }
            },
            "routers": {
              "commands": {
                "add-bgp-peer": {
                  "commands": {},
                  "flags": {
                    "--advertised-route-priority": "value",
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--async": "bool",
                    "--interface": "value",
                    "--peer-asn": "value",
                    "--peer-ip-address": "value",
                    "--peer-name": "value",
                    "--region": "dynamic",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "add-interface": {
                  "commands": {},
                  "flags": {
                    "--interconnect-attachment": "dynamic",
                    "--interconnect-attachment-region": "dynamic",
                    "--interface-name": "value",
                    "--ip-address": "value",
                    "--mask-length": "value",
                    "--region": "dynamic",
                    "--vpn-tunnel": "dynamic",
                    "--vpn-tunnel-region": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--asn": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--network": "dynamic",
                    "--region": "dynamic",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "get-status": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-bgp-peer": {
                  "commands": {},
                  "flags": {
                    "--peer-name": "value",
                    "--region": "dynamic"
                  }
                },
                "remove-interface": {
                  "commands": {},
                  "flags": {
                    "--interface-name": "value",
                    "--region": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-advertisement-groups": "value",
                    "--add-advertisement-ranges": "value",
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--async": "bool",
                    "--region": "dynamic",
                    "--remove-advertisement-groups": "value",
                    "--remove-advertisement-ranges": "value",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "update-bgp-peer": {
                  "commands": {},
                  "flags": {
                    "--add-advertisement-groups": "value",
                    "--add-advertisement-ranges": "value",
                    "--advertised-route-priority": "value",
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--async": "bool",
                    "--interface": "value",
                    "--ip-address": "value",
                    "--peer-asn": "value",
                    "--peer-ip-address": "value",
                    "--peer-name": "value",
                    "--region": "dynamic",
                    "--remove-advertisement-groups": "value",
                    "--remove-advertisement-ranges": "value",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "update-interface": {
                  "commands": {},
                  "flags": {
                    "--interconnect-attachment": "dynamic",
                    "--interconnect-attachment-region": "dynamic",
                    "--interface-name": "value",
                    "--ip-address": "value",
                    "--mask-length": "value",
                    "--region": "dynamic",
                    "--vpn-tunnel": "dynamic",
                    "--vpn-tunnel-region": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "routes": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--destination-range": "value",
                    "--network": "value",
                    "--next-hop-address": "value",
                    "--next-hop-gateway": "dynamic",
                    "--next-hop-ilb": "value",
                    "--next-hop-ilb-region": "value",
                    "--next-hop-instance": "value",
                    "--next-hop-instance-zone": "value",
                    "--next-hop-vpn-tunnel": "value",
                    "--next-hop-vpn-tunnel-region": "value",
                    "--priority": "value",
                    "--tags": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "scp": {
              "commands": {},
              "flags": {
                "--compress": "bool",
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--internal-ip": "bool",
                "--plain": "bool",
                "--port": "value",
                "--recurse": "bool",
                "--scp-flag": "value",
                "--ssh-key-file": "value",
                "--strict-host-key-checking": [
                  "ask",
                  "no",
                  "yes"
                ],
                "--zone": "value"
              }
            },
            "security-policies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--file-format": [
                      "json",
                      "yaml"
                    ],
                    "--file-name": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--file-format": [
                      "json",
                      "yaml"
                    ],
                    "--file-name": "value"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--file-format": [
                      "json",
                      "yaml"
                    ],
                    "--file-name": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-preconfigured-expression-sets": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "rules": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--action": [
                          "allow",
                          "deny-403",
                          "deny-404",
                          "deny-502"
                        ],
                        "--description": "value",
                        "--expression": "value",
                        "--preview": "bool",
                        "--security-policy": "dynamic",
                        "--src-ip-ranges": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--security-policy": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--security-policy": "dynamic"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--action": [
                          "allow",
                          "deny-403",
                          "deny-404",
                          "deny-502"
                        ],
                        "--description": "value",
                        "--expression": "value",
                        "--preview": "bool",
                        "--security-policy": "dynamic",
                        "--src-ip-ranges": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "shared-vpc": {
              "commands": {
                "associated-projects": {
                  "commands": {
                    "add": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "disable": {
                  "commands": {},
                  "flags": {}
                },
                "enable": {
                  "commands": {},
                  "flags": {}
                },
                "get-host-project": {
                  "commands": {},
                  "flags": {}
                },
                "list-associated-resources": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "organizations": {
                  "commands": {
                    "list-host-projects": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "sign-url": {
              "commands": {},
              "flags": {
                "--expires-in": "value",
                "--key-file": "value",
                "--key-name": "value",
                "--validate": "bool"
              }
            },
            "snapshots": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "ssh": {
              "commands": {},
              "flags": {
                "--command": "value",
                "--container": "value",
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--internal-ip": "bool",
                "--plain": "bool",
                "--ssh-flag": "value",
                "--ssh-key-file": "value",
                "--strict-host-key-checking": [
                  "ask",
                  "no",
                  "yes"
                ],
                "--zone": "dynamic"
              }
            },
            "ssl-certificates": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--certificate": "value",
                    "--description": "value",
                    "--domains": "value",
                    "--private-key": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "ssl-policies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--custom-features": "value",
                    "--description": "value",
                    "--min-tls-version": [
                      "1.0",
                      "1.1",
                      "1.2"
                    ],
                    "--profile": [
                      "COMPATIBLE",
                      "CUSTOM",
                      "MODERN",
                      "RESTRICTED"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-available-features": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--custom-features": "value",
                    "--min-tls-version": [
                      "1.0",
                      "1.1",
                      "1.2"
                    ],
                    "--profile": [
                      "COMPATIBLE",
                      "CUSTOM",
                      "MODERN",
                      "RESTRICTED"
                    ]
                  }
                }
              },
              "flags": {}
            },
            "target-http-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--url-map": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--url-map": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-https-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--quic-override": [
                      "DISABLE",
                      "ENABLE",
                      "NONE"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic",
                    "--url-map": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-ssl-policy": "bool",
                    "--quic-override": [
                      "DISABLE",
                      "ENABLE",
                      "NONE"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic",
                    "--url-map": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-instances": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--instance": "dynamic",
                    "--instance-zone": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-pools": {
              "commands": {
                "add-health-checks": {
                  "commands": {},
                  "flags": {
                    "--http-health-check": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "add-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "dynamic",
                    "--instances-zone": "dynamic",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--backup-pool": "value",
                    "--description": "value",
                    "--failover-ratio": "value",
                    "--health-check": "value",
                    "--http-health-check": "dynamic",
                    "--region": "dynamic",
                    "--session-affinity": [
                      "CLIENT_IP",
                      "CLIENT_IP_PROTO",
                      "GENERATED_COOKIE",
                      "NONE"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "get-health": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-health-checks": {
                  "commands": {},
                  "flags": {
                    "--http-health-check": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "remove-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "dynamic",
                    "--instances-zone": "dynamic",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "set-backup": {
                  "commands": {},
                  "flags": {
                    "--backup-pool": "dynamic",
                    "--failover-ratio": "value",
                    "--no-backup-pool": "bool",
                    "--region": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-ssl-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--description": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--clear-ssl-policy": "bool",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-tcp-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--description": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ]
                  }
                }
              },
              "flags": {}
            },
            "target-vpn-gateways": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--network": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "tpus": {
              "commands": {
                "accelerator-types": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator-type": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--network": "value",
                    "--preemptible": "bool",
                    "--range": "value",
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "locations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "reimage": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "versions": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "url-maps": {
              "commands": {
                "add-host-rule": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--hosts": "value",
                    "--path-matcher-name": "value"
                  }
                },
                "add-path-matcher": {
                  "commands": {},
                  "flags": {
                    "--backend-bucket-path-rules": "value",
                    "--backend-service-path-rules": "value",
                    "--default-backend-bucket": "value",
                    "--default-service": "value",
                    "--delete-orphaned-path-matcher": "bool",
                    "--description": "value",
                    "--existing-host": "value",
                    "--new-hosts": "value",
                    "--path-matcher-name": "value",
                    "--path-rules": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--default-backend-bucket": "value",
                    "--default-service": "value",
                    "--description": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "edit": {
                  "commands": {},
                  "flags": {}
                },
                "invalidate-cdn-cache": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--path": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-cdn-cache-invalidations": {
                  "commands": {},
                  "flags": {
                    "--limit": "value"
                  }
                },
                "remove-host-rule": {
                  "commands": {},
                  "flags": {
                    "--delete-orphaned-path-matcher": "bool",
                    "--host": "value"
                  }
                },
                "remove-path-matcher": {
                  "commands": {},
                  "flags": {
                    "--path-matcher-name": "value"
                  }
                },
                "set-default-service": {
                  "commands": {},
                  "flags": {
                    "--default-backend-bucket": "value",
                    "--default-service": "value"
                  }
                }
              },
              "flags": {}
            },
            "vpn-tunnels": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--ike-version": [
                      1,
                      2
                    ],
                    "--local-traffic-selector": "value",
                    "--peer-address": "value",
                    "--region": "dynamic",
                    "--remote-traffic-selector": "value",
                    "--router": "value",
                    "--shared-secret": "value",
                    "--target-vpn-gateway": "dynamic",
                    "--target-vpn-gateway-region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "xpn": {
              "commands": {
                "associated-projects": {
                  "commands": {
                    "add": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "disable": {
                  "commands": {},
                  "flags": {}
                },
                "enable": {
                  "commands": {},
                  "flags": {}
                },
                "get-host-project": {
                  "commands": {},
                  "flags": {}
                },
                "list-associated-resources": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "organizations": {
                  "commands": {
                    "list-host-projects": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "zones": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "config": {
          "commands": {
            "configurations": {
              "commands": {
                "activate": {
                  "commands": {},
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--activate": "bool"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--all": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            },
            "set": {
              "commands": {},
              "flags": {
                "--installation": "bool"
              }
            },
            "unset": {
              "commands": {},
              "flags": {
                "--installation": "bool"
              }
            }
          },
          "flags": {}
        },
        "container": {
          "commands": {
            "builds": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--ongoing": "bool",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "stream-logs": {
                  "commands": {},
                  "flags": {}
                },
                "submit": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "value",
                    "--disk-size": "value",
                    "--gcs-log-dir": "value",
                    "--gcs-source-staging-dir": "value",
                    "--machine-type": [
                      "n1-highcpu-32",
                      "n1-highcpu-8"
                    ],
                    "--no-source": "bool",
                    "--substitutions": "value",
                    "--tag": "value",
                    "--timeout": "value"
                  }
                }
              },
              "flags": {}
            },
            "clusters": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--additional-zones": "value",
                    "--addons": "value",
                    "--allow-route-overlap": "bool",
                    "--async": "bool",
                    "--cluster-ipv4-cidr": "value",
                    "--cluster-secondary-range-name": "value",
                    "--cluster-version": "value",
                    "--create-subnetwork": "value",
                    "--default-max-pods-per-node": "value",
                    "--disk-size": "value",
                    "--disk-type": [
                      "pd-ssd",
                      "pd-standard"
                    ],
                    "--enable-autoprovisioning": "bool",
                    "--enable-autorepair": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-autoupgrade": "bool",
                    "--enable-basic-auth": "bool",
                    "--enable-cloud-endpoints": "bool",
                    "--enable-cloud-logging": "bool",
                    "--enable-cloud-monitoring": "bool",
                    "--enable-ip-alias": "bool",
                    "--enable-kubernetes-alpha": "bool",
                    "--enable-legacy-authorization": "bool",
                    "--enable-main-authorized-networks": "bool",
                    "--enable-network-policy": "bool",
                    "--enable-pod-security-policy": "bool",
                    "--enable-stackdriver-kubernetes": "bool",
                    "--enable-tpu": "bool",
                    "--image-type": "value",
                    "--issue-client-certificate": "bool",
                    "--istio-config": "value",
                    "--labels": "value",
                    "--local-ssd-count": "value",
                    "--local-ssd-volumes": "value",
                    "--machine-type": "value",
                    "--maintenance-window": "value",
                    "--main-authorized-networks": "value",
                    "--main-ipv4-cidr": "value",
                    "--max-accelerator": "value",
                    "--max-cpu": "value",
                    "--max-memory": "value",
                    "--max-nodes": "value",
                    "--max-nodes-per-pool": "value",
                    "--min-accelerator": "value",
                    "--min-cpu": "value",
                    "--min-cpu-platform": "value",
                    "--min-memory": "value",
                    "--min-nodes": "value",
                    "--network": "value",
                    "--node-labels": "value",
                    "--node-locations": "value",
                    "--node-taints": "value",
                    "--node-version": "value",
                    "--num-nodes": "value",
                    "--password": "value",
                    "--preemptible": "bool",
                    "--private-cluster": "bool",
                    "--region": "value",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--services-ipv4-cidr": "value",
                    "--services-secondary-range-name": "value",
                    "--subnetwork": "value",
                    "--tags": "value",
                    "--tpu-ipv4-cidr": "value",
                    "--username": "value",
                    "--workload-metadata-from-node": [
                      "EXPOSED",
                      "SECURE",
                      "UNSPECIFIED"
                    ],
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "get-credentials": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "value"
                  }
                },
                "resize": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--node-pool": "value",
                    "--region": "value",
                    "--size": "value",
                    "--zone": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--additional-zones": "value",
                    "--async": "bool",
                    "--complete-credential-rotation": "bool",
                    "--complete-ip-rotation": "bool",
                    "--enable-autoprovisioning": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-basic-auth": "bool",
                    "--enable-legacy-authorization": "bool",
                    "--enable-main-authorized-networks": "bool",
                    "--enable-network-policy": "bool",
                    "--enable-pod-security-policy": "bool",
                    "--generate-password": "bool",
                    "--logging-service": "value",
                    "--maintenance-window": "value",
                    "--main-authorized-networks": "value",
                    "--max-accelerator": "value",
                    "--max-cpu": "value",
                    "--max-memory": "value",
                    "--max-nodes": "value",
                    "--min-accelerator": "value",
                    "--min-cpu": "value",
                    "--min-memory": "value",
                    "--min-nodes": "value",
                    "--monitoring-service": "value",
                    "--node-locations": "value",
                    "--node-pool": "value",
                    "--password": "value",
                    "--region": "value",
                    "--remove-labels": "value",
                    "--set-password": "bool",
                    "--start-credential-rotation": "bool",
                    "--start-ip-rotation": "bool",
                    "--update-addons": "value",
                    "--update-labels": "value",
                    "--username": "value",
                    "--zone": "value"
                  }
                },
                "upgrade": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster-version": "value",
                    "--concurrent-node-count": "value",
                    "--image-type": "value",
                    "--main": "bool",
                    "--node-pool": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "get-server-config": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "images": {
              "commands": {
                "add-tag": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--force-delete-tags": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--metadata-filter": "value",
                    "--show-all-metadata": "bool",
                    "--show-build-details": "bool",
                    "--show-deployment": "bool",
                    "--show-image-basis": "bool",
                    "--show-package-vulnerability": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--repository": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-tags": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--occurrence-filter": "value",
                    "--page-size": "value",
                    "--show-occurrences": "bool",
                    "--show-occurrences-from": "value",
                    "--sort-by": "value"
                  }
                },
                "untag": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "node-pools": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--cluster": "value",
                    "--disk-size": "value",
                    "--disk-type": [
                      "pd-ssd",
                      "pd-standard"
                    ],
                    "--enable-autorepair": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-autoupgrade": "bool",
                    "--enable-cloud-endpoints": "bool",
                    "--image-type": "value",
                    "--local-ssd-count": "value",
                    "--local-ssd-volumes": "value",
                    "--machine-type": "value",
                    "--max-nodes": "value",
                    "--max-pods-per-node": "value",
                    "--min-cpu-platform": "value",
                    "--min-nodes": "value",
                    "--node-labels": "value",
                    "--node-taints": "value",
                    "--node-version": "value",
                    "--num-nodes": "value",
                    "--preemptible": "bool",
                    "--region": "value",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--tags": "value",
                    "--workload-metadata-from-node": [
                      "EXPOSED",
                      "SECURE",
                      "UNSPECIFIED"
                    ],
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "value"
                  }
                },
                "rollback": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--enable-autorepair": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-autoupgrade": "bool",
                    "--max-nodes": "value",
                    "--min-nodes": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--zone": "value"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "subnets": {
              "commands": {
                "list-usable": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--network-project": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "dataflow": {
          "commands": {
            "jobs": {
              "commands": {
                "export-steps": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                }
              },
              "flags": {}
            },
            "logs": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--after": "value",
                    "--before": "value",
                    "--filter": "value",
                    "--importance": [
                      "debug",
                      "detailed",
                      "error",
                      "warning"
                    ],
                    "--limit": "value",
                    "--region": "value"
                  }
                }
              },
              "flags": {}
            },
            "metrics": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--changed-after": "value",
                    "--filter": "value",
                    "--hide-committed": "bool",
                    "--limit": "value",
                    "--region": "value",
                    "--source": [
                      "all",
                      "service",
                      "user"
                    ],
                    "--tentative": "bool",
                    "--transform": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "deployment-manager": {
          "commands": {
            "deployments": {
              "commands": {
                "cancel-preview": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--fingerprint": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--automatic-rollback-on-error": "bool",
                    "--composite-type": "value",
                    "--config": "value",
                    "--create-policy": [
                      "acquire",
                      "create",
                      "create-or-acquire"
                    ],
                    "--credential": "value",
                    "--description": "value",
                    "--labels": "value",
                    "--preview": "bool",
                    "--properties": "value",
                    "--template": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--delete-policy": [
                      "abandon",
                      "delete"
                    ]
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--fingerprint": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--composite-type": "value",
                    "--config": "value",
                    "--create-policy": [
                      "acquire",
                      "create",
                      "create-or-acquire"
                    ],
                    "--credential": "value",
                    "--delete-policy": [
                      "abandon",
                      "delete"
                    ],
                    "--description": "value",
                    "--fingerprint": "value",
                    "--manifest-id": "value",
                    "--preview": "bool",
                    "--properties": "value",
                    "--remove-labels": "value",
                    "--template": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "manifests": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "resources": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {
                "--deployment": "value"
              }
            },
            "type-providers": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--api-options-file": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--descriptor-url": "value",
                    "--labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--api-options-file": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--descriptor-url": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "types": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--labels": "value",
                    "--status": [
                      "DEPRECATED",
                      "EXPERIMENTAL",
                      "SUPPORTED"
                    ],
                    "--template": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--provider": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--provider": "value",
                    "--provider-project": "value",
                    "--sort-by": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--remove-labels": "value",
                    "--status": [
                      "DEPRECATED",
                      "EXPERIMENTAL",
                      "SUPPORTED"
                    ],
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "dlp": {
          "commands": {
            "datasources": {
              "commands": {
                "bigquery": {
                  "commands": {
                    "analyze": {
                      "commands": {},
                      "flags": {
                        "--categorical-stat-field": "value",
                        "--job-id": "value",
                        "--numerical-stat-field": "value",
                        "--output-tables": "value",
                        "--output-topics": "value",
                        "--quasi-ids": "value",
                        "--sensitive-attribute": "value"
                      }
                    },
                    "inspect": {
                      "commands": {},
                      "flags": {
                        "--exclude-info-types": "bool",
                        "--identifying-fields": "value",
                        "--include-quote": "bool",
                        "--info-types": "value",
                        "--job-id": "value",
                        "--max-findings": "value",
                        "--max-findings-per-item": "value",
                        "--max-time": "value",
                        "--min-likelihood": [
                          "likely",
                          "possible",
                          "unlikely",
                          "very-likely",
                          "very-unlikely"
                        ],
                        "--min-time": "value",
                        "--output-tables": "value",
                        "--output-topics": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "datastore": {
                  "commands": {
                    "inspect": {
                      "commands": {},
                      "flags": {
                        "--exclude-info-types": "bool",
                        "--include-quote": "bool",
                        "--info-types": "value",
                        "--job-id": "value",
                        "--max-findings": "value",
                        "--max-findings-per-item": "value",
                        "--max-time": "value",
                        "--min-likelihood": [
                          "likely",
                          "possible",
                          "unlikely",
                          "very-likely",
                          "very-unlikely"
                        ],
                        "--min-time": "value",
                        "--output-tables": "value",
                        "--output-topics": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "gcs": {
                  "commands": {
                    "inspect": {
                      "commands": {},
                      "flags": {
                        "--exclude-info-types": "bool",
                        "--file-size-limit": "value",
                        "--include-quote": "bool",
                        "--info-types": "value",
                        "--job-id": "value",
                        "--max-findings": "value",
                        "--max-findings-per-item": "value",
                        "--max-time": "value",
                        "--min-likelihood": [
                          "likely",
                          "possible",
                          "unlikely",
                          "very-likely",
                          "very-unlikely"
                        ],
                        "--min-time": "value",
                        "--output-tables": "value",
                        "--output-topics": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "images": {
              "commands": {
                "inspect": {
                  "commands": {},
                  "flags": {
                    "--exclude-info-types": "bool",
                    "--include-quote": "bool",
                    "--info-types": "value",
                    "--max-findings": "value",
                    "--min-likelihood": [
                      "likely",
                      "possible",
                      "unlikely",
                      "very-likely",
                      "very-unlikely"
                    ]
                  }
                },
                "redact": {
                  "commands": {},
                  "flags": {
                    "--include-quote": "bool",
                    "--info-types": "value",
                    "--min-likelihood": [
                      "likely",
                      "possible",
                      "unlikely",
                      "very-likely",
                      "very-unlikely"
                    ],
                    "--redact-all-text": "bool",
                    "--redact-color": "value"
                  }
                }
              },
              "flags": {}
            },
            "job-triggers": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--datastore-kind": "value",
                    "--description": "value",
                    "--display-name": "value",
                    "--exclude-info-types": "bool",
                    "--include-quote": "bool",
                    "--info-types": "value",
                    "--input-table": "value",
                    "--max-findings": "value",
                    "--max-findings-per-item": "value",
                    "--min-likelihood": [
                      "likely",
                      "possible",
                      "unlikely",
                      "very-likely",
                      "very-unlikely"
                    ],
                    "--output-tables": "value",
                    "--output-topics": "value",
                    "--path": "value",
                    "--trigger-schedule": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "jobs": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--job-type": [
                      "inspect",
                      "risk-analysis"
                    ],
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "text": {
              "commands": {
                "inspect": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--exclude-info-types": "bool",
                    "--include-quote": "bool",
                    "--info-types": "value",
                    "--max-findings": "value",
                    "--min-likelihood": [
                      "likely",
                      "possible",
                      "unlikely",
                      "very-likely",
                      "very-unlikely"
                    ]
                  }
                },
                "redact": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--info-types": "value",
                    "--min-likelihood": [
                      "likely",
                      "possible",
                      "unlikely",
                      "very-likely",
                      "very-unlikely"
                    ],
                    "--remove-findings": "bool",
                    "--replace-with-info-type": "bool",
                    "--replacement-text": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "emulators": {
          "commands": {
            "bigtable": {
              "commands": {
                "env-init": {
                  "commands": {},
                  "flags": {}
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--host-port": "value"
                  }
                }
              },
              "flags": {}
            },
            "datastore": {
              "commands": {
                "env-init": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value",
                    "--legacy": "bool"
                  }
                },
                "env-unset": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value",
                    "--legacy": "bool"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--consistency": "value",
                    "--data-dir": "value",
                    "--host-port": "value",
                    "--legacy": "bool",
                    "--store-on-disk": "bool"
                  }
                }
              },
              "flags": {
                "--data-dir": "value",
                "--legacy": "bool"
              }
            },
            "pubsub": {
              "commands": {
                "env-init": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value",
                    "--host-port": "value"
                  }
                }
              },
              "flags": {
                "--data-dir": "value"
              }
            },
            "start": {
              "commands": {},
              "flags": {
                "--emulators": "value",
                "--proxy-port": "value",
                "--route-to-public": "value"
              }
            }
          },
          "flags": {}
        },
        "endpoints": {
          "commands": {
            "configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--service": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--full": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "services": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "check-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "deploy": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--force": "bool",
                    "--validate-only": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "undelete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "filestore": {
          "commands": {
            "instances": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--file-share": "value",
                    "--labels": "value",
                    "--location": "value",
                    "--network": "value",
                    "--tier": [
                      "premium",
                      "standard"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--location": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "locations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "firebase": {
          "commands": {
            "test": {
              "commands": {
                "android": {
                  "commands": {
                    "locales": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "models": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "run": {
                      "commands": {},
                      "flags": {
                        "--additional-apks": "value",
                        "--app": "value",
                        "--app-initial-activity": "value",
                        "--app-package": "value",
                        "--async": "bool",
                        "--auto-google-login": "bool",
                        "--device": "value",
                        "--device-ids": "value",
                        "--directories-to-pull": "value",
                        "--environment-variables": "value",
                        "--filter": "value",
                        "--limit": "value",
                        "--locales": "value",
                        "--max-depth": "value",
                        "--max-steps": "value",
                        "--network-profile": "value",
                        "--obb-files": "value",
                        "--orientations": "dynamic",
                        "--os-version-ids": "value",
                        "--other-files": "value",
                        "--page-size": "value",
                        "--performance-metrics": "bool",
                        "--record-video": "bool",
                        "--results-bucket": "value",
                        "--results-dir": "value",
                        "--results-history-name": "value",
                        "--robo-directives": "value",
                        "--robo-script": "value",
                        "--scenario-labels": "value",
                        "--scenario-numbers": "value",
                        "--sort-by": "value",
                        "--test": "value",
                        "--test-package": "value",
                        "--test-runner-class": "value",
                        "--test-targets": "value",
                        "--timeout": "value",
                        "--type": [
                          "game-loop",
                          "instrumentation",
                          "robo"
                        ],
                        "--use-orchestrator": "bool"
                      }
                    },
                    "versions": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "ios": {
                  "commands": {
                    "models": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "run": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--device": "value",
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--record-video": "bool",
                        "--results-bucket": "value",
                        "--results-dir": "value",
                        "--results-history-name": "value",
                        "--sort-by": "value",
                        "--test": "value",
                        "--timeout": "value",
                        "--xctestrun-file": "value"
                      }
                    },
                    "versions": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "network-profiles": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "functions": {
          "commands": {
            "call": {
              "commands": {},
              "flags": {
                "--data": "value",
                "--region": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "deploy": {
              "commands": {},
              "flags": {
                "--clear-env-vars": "bool",
                "--clear-labels": "bool",
                "--entry-point": "value",
                "--env-vars-file": "value",
                "--memory": "value",
                "--region": "dynamic",
                "--remove-env-vars": "value",
                "--remove-labels": "value",
                "--retry": "bool",
                "--runtime": "value",
                "--set-env-vars": "value",
                "--source": "value",
                "--stage-bucket": "value",
                "--timeout": "value",
                "--trigger-bucket": "value",
                "--trigger-event": "value",
                "--trigger-http": "bool",
                "--trigger-resource": "value",
                "--trigger-topic": "value",
                "--update-env-vars": "value",
                "--update-labels": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "event-types": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "logs": {
              "commands": {
                "read": {
                  "commands": {},
                  "flags": {
                    "--end-time": "value",
                    "--execution-id": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--min-log-level": [
                      "debug",
                      "error",
                      "info"
                    ],
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--start-time": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "genomics": {
          "commands": {
            "callsets": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--name": "value",
                    "--variant-set-id": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--name": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--name": "value"
                  }
                }
              },
              "flags": {}
            },
            "datasets": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--name": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "restore": {
                  "commands": {},
                  "flags": {}
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--name": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--where": "value"
                  }
                }
              },
              "flags": {}
            },
            "pipelines": {
              "commands": {
                "run": {
                  "commands": {},
                  "flags": {
                    "--command-line": "value",
                    "--cpus": "value",
                    "--disk-size": "value",
                    "--docker-image": "value",
                    "--inputs": "value",
                    "--inputs-from-file": "value",
                    "--labels": "value",
                    "--logging": "value",
                    "--memory": "value",
                    "--outputs": "value",
                    "--pipeline-file": "value",
                    "--preemptible": "bool",
                    "--regions": "value",
                    "--service-account-email": "value",
                    "--service-account-scopes": "value",
                    "--zones": "value"
                  }
                }
              },
              "flags": {}
            },
            "readgroupsets": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--export-uri": "value",
                    "--reference-names": "value"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--dataset-id": "value",
                    "--partition-strategy": "value",
                    "--reference-set-id": "value",
                    "--source-uris": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--name": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--name": "value",
                    "--reference-set-id": "value"
                  }
                }
              },
              "flags": {}
            },
            "reads": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--end": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--reference-name": "value",
                    "--sort-by": "value",
                    "--start": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "references": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--accessions": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--md5checksums": "value",
                    "--page-size": "value",
                    "--reference-set-id": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "referencesets": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--accessions": "value",
                    "--assembly-id": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--md5checksums": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "variants": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--file-format": [
                      "complete-genomics",
                      "vcf"
                    ],
                    "--info-merge-config": "value",
                    "--normalize-reference-names": "bool",
                    "--source-uris": "value",
                    "--variantset-id": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--call-set-ids": "value",
                    "--end": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--limit-calls": "value",
                    "--page-size": "value",
                    "--reference-name": "value",
                    "--sort-by": "value",
                    "--start": "value",
                    "--uri": "bool",
                    "--variant-set-id": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--names": "value"
                  }
                }
              },
              "flags": {}
            },
            "variantsets": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--dataset-id": "value",
                    "--description": "value",
                    "--name": "value",
                    "--reference-set-id": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--bigquery-dataset": "value",
                    "--bigquery-project": "value",
                    "--call-set-ids": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--name": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "iam": {
          "commands": {
            "list-grantable-roles": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--page-size": "value"
              }
            },
            "list-testable-permissions": {
              "commands": {},
              "flags": {
                "--filter": "value"
              }
            },
            "roles": {
              "commands": {
                "copy": {
                  "commands": {},
                  "flags": {
                    "--dest-organization": "value",
                    "--dest-project": "value",
                    "--destination": "value",
                    "--source": "value",
                    "--source-organization": "value",
                    "--source-project": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--file": "value",
                    "--organization": "value",
                    "--permissions": "value",
                    "--stage": "value",
                    "--title": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--organization": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--organization": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--organization": "value",
                    "--show-deleted": "bool",
                    "--sort-by": "value"
                  }
                },
                "undelete": {
                  "commands": {},
                  "flags": {
                    "--organization": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-permissions": "value",
                    "--description": "value",
                    "--file": "value",
                    "--organization": "value",
                    "--permissions": "value",
                    "--remove-permissions": "value",
                    "--stage": "value",
                    "--title": "value"
                  }
                }
              },
              "flags": {}
            },
            "service-accounts": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--display-name": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "keys": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--iam-account": "value",
                        "--key-file-type": [
                          "json",
                          "p12"
                        ]
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--iam-account": "value"
                      }
                    },
                    "get-public-key": {
                      "commands": {},
                      "flags": {
                        "--iam-account": "value",
                        "--output-file": "value",
                        "--type": [
                          "pem",
                          "raw"
                        ]
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--created-before": "value",
                        "--filter": "value",
                        "--iam-account": "value",
                        "--limit": "value",
                        "--managed-by": [
                          "any",
                          "system",
                          "user"
                        ],
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "sign-blob": {
                  "commands": {},
                  "flags": {
                    "--iam-account": "value"
                  }
                },
                "sign-jwt": {
                  "commands": {},
                  "flags": {
                    "--iam-account": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--display-name": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "init": {
          "commands": {},
          "flags": {
            "--console-only": "bool",
            "--skip-diagnostics": "bool"
          }
        },
        "interactive": {
          "commands": {},
          "flags": {
            "--context": "value",
            "--update-cli-trees": "bool"
          }
        },
        "iot": {
          "commands": {
            "devices": {
              "commands": {
                "configs": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "get-value": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--config-data": "value",
                        "--config-file": "value",
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--version-to-update": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--blocked": "bool",
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--public-key": "value",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "credentials": {
                  "commands": {
                    "clear": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--expiration-time": "value",
                        "--path": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--type": [
                          "es256",
                          "es256-pem",
                          "es256-x509-pem",
                          "rs256",
                          "rsa-pem",
                          "rsa-x509-pem"
                        ]
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--expiration-time": "value",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--device-ids": "value",
                    "--device-num-ids": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "states": {
                  "commands": {
                    "list": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--blocked": "bool",
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "registries": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--region": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--enable-http-config": "bool",
                    "--enable-mqtt-config": "bool",
                    "--event-notification-config": "value",
                    "--event-pubsub-topic": "value",
                    "--public-key-path": "value",
                    "--region": "value",
                    "--state-pubsub-topic": "value"
                  }
                },
                "credentials": {
                  "commands": {
                    "clear": {
                      "commands": {},
                      "flags": {
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--path": "value",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--region": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--enable-http-config": "bool",
                    "--enable-mqtt-config": "bool",
                    "--event-notification-config": "value",
                    "--event-pubsub-topic": "value",
                    "--region": "value",
                    "--state-pubsub-topic": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "kms": {
          "commands": {
            "decrypt": {
              "commands": {},
              "flags": {
                "--additional-authenticated-data-file": "value",
                "--ciphertext-file": "value",
                "--key": "dynamic",
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--plaintext-file": "value"
              }
            },
            "encrypt": {
              "commands": {},
              "flags": {
                "--additional-authenticated-data-file": "value",
                "--ciphertext-file": "value",
                "--key": "dynamic",
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--plaintext-file": "value"
              }
            },
            "keyrings": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "keys": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--labels": "value",
                    "--location": "dynamic",
                    "--next-rotation-time": "value",
                    "--purpose": [
                      "encryption"
                    ],
                    "--rotation-period": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--keyring": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--keyring": "dynamic",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "remove-rotation-schedule": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--keyring": "value",
                    "--location": "value"
                  }
                },
                "set-primary-version": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "set-rotation-schedule": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--next-rotation-time": "value",
                    "--rotation-period": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--next-rotation-time": "value",
                    "--primary-version": "dynamic",
                    "--remove-labels": "value",
                    "--remove-rotation-schedule": "bool",
                    "--rotation-period": "value",
                    "--update-labels": "value"
                  }
                },
                "versions": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic",
                        "--primary": "bool"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "destroy": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "disable": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "enable": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--limit": "value",
                        "--location": "dynamic",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "restore": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "locations": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "ml": {
          "commands": {
            "language": {
              "commands": {
                "analyze-entities": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "analyze-entity-sentiment": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "analyze-sentiment": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "analyze-syntax": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "classify-text": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--language": "value"
                  }
                }
              },
              "flags": {}
            },
            "speech": {
              "commands": {
                "operations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "wait": {
                      "commands": {},
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "recognize": {
                  "commands": {},
                  "flags": {
                    "--additional-language-codes": "value",
                    "--diarization-speaker-count": "value",
                    "--enable-speaker-diarization": "bool",
                    "--encoding": [
                      "amr",
                      "amr-wb",
                      "encoding-unspecified",
                      "flac",
                      "linear16",
                      "mulaw",
                      "ogg-opus",
                      "speex-with-header-byte"
                    ],
                    "--filter-profanity": "bool",
                    "--hints": "value",
                    "--include-word-confidence": "bool",
                    "--include-word-time-offsets": "bool",
                    "--language-code": "value",
                    "--max-alternatives": "value",
                    "--sample-rate": "value"
                  }
                },
                "recognize-long-running": {
                  "commands": {},
                  "flags": {
                    "--additional-language-codes": "value",
                    "--async": "bool",
                    "--diarization-speaker-count": "value",
                    "--enable-speaker-diarization": "bool",
                    "--encoding": [
                      "amr",
                      "amr-wb",
                      "encoding-unspecified",
                      "flac",
                      "linear16",
                      "mulaw",
                      "ogg-opus",
                      "speex-with-header-byte"
                    ],
                    "--filter-profanity": "bool",
                    "--hints": "value",
                    "--include-word-confidence": "bool",
                    "--include-word-time-offsets": "bool",
                    "--language-code": "value",
                    "--max-alternatives": "value",
                    "--sample-rate": "value"
                  }
                }
              },
              "flags": {}
            },
            "video": {
              "commands": {
                "detect-explicit-content": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--output-uri": "value",
                    "--region": [
                      "asia-east1",
                      "europe-west1",
                      "us-east1",
                      "us-west1"
                    ],
                    "--segments": "value"
                  }
                },
                "detect-labels": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--detection-mode": [
                      "frame",
                      "shot",
                      "shot-and-frame"
                    ],
                    "--output-uri": "value",
                    "--region": [
                      "asia-east1",
                      "europe-west1",
                      "us-east1",
                      "us-west1"
                    ],
                    "--segments": "value"
                  }
                },
                "detect-shot-changes": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--output-uri": "value",
                    "--region": [
                      "asia-east1",
                      "europe-west1",
                      "us-east1",
                      "us-west1"
                    ],
                    "--segments": "value"
                  }
                },
                "operations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "wait": {
                      "commands": {},
                      "flags": {}
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "vision": {
              "commands": {
                "detect-document": {
                  "commands": {},
                  "flags": {
                    "--language-hints": "value",
                    "--model-version": "value"
                  }
                },
                "detect-faces": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-image-properties": {
                  "commands": {},
                  "flags": {
                    "--model-version": "value"
                  }
                },
                "detect-labels": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-landmarks": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-logos": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-safe-search": {
                  "commands": {},
                  "flags": {
                    "--model-version": "value"
                  }
                },
                "detect-text": {
                  "commands": {},
                  "flags": {
                    "--language-hints": "value",
                    "--model-version": "value"
                  }
                },
                "detect-web": {
                  "commands": {},
                  "flags": {
                    "--include-geo-results": "bool",
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "suggest-crop": {
                  "commands": {},
                  "flags": {
                    "--aspect-ratios": "value",
                    "--model-version": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "ml-engine": {
          "commands": {
            "jobs": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--summarize": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "stream-logs": {
                  "commands": {},
                  "flags": {
                    "--allow-multiline-logs": "bool",
                    "--polling-interval": "value",
                    "--task-name": "value"
                  }
                },
                "submit": {
                  "commands": {
                    "prediction": {
                      "commands": {},
                      "flags": {
                        "--accelerator-count": "value",
                        "--accelerator-type": [
                          "nvidia-tesla-k80",
                          "nvidia-tesla-p100"
                        ],
                        "--batch-size": "value",
                        "--data-format": [
                          "text",
                          "tf-record",
                          "tf-record-gzip"
                        ],
                        "--input-paths": "value",
                        "--labels": "value",
                        "--max-worker-count": "value",
                        "--model": "value",
                        "--model-dir": "value",
                        "--output-path": "value",
                        "--region": "value",
                        "--runtime-version": "value"
                      }
                    },
                    "training": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--config": "value",
                        "--job-dir": "value",
                        "--labels": "value",
                        "--module-name": "value",
                        "--package-path": "value",
                        "--packages": "value",
                        "--python-version": "value",
                        "--region": "dynamic",
                        "--runtime-version": "value",
                        "--scale-tier": [
                          "basic",
                          "basic-gpu",
                          "basic-tpu",
                          "custom",
                          "premium-1",
                          "standard-1"
                        ],
                        "--staging-bucket": "value",
                        "--stream-logs": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "local": {
              "commands": {
                "predict": {
                  "commands": {},
                  "flags": {
                    "--framework": [
                      "scikit-learn",
                      "tensorflow",
                      "xgboost"
                    ],
                    "--json-instances": "value",
                    "--model-dir": "value",
                    "--text-instances": "value"
                  }
                },
                "train": {
                  "commands": {},
                  "flags": {
                    "--distributed": "bool",
                    "--job-dir": "value",
                    "--module-name": "value",
                    "--package-path": "value",
                    "--parameter-server-count": "value",
                    "--start-port": "value",
                    "--worker-count": "value"
                  }
                }
              },
              "flags": {}
            },
            "locations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "models": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-logging": "bool",
                    "--labels": "value",
                    "--regions": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "predict": {
              "commands": {},
              "flags": {
                "--json-instances": "value",
                "--model": "value",
                "--text-instances": "value"
              }
            },
            "versions": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "value",
                    "--description": "value",
                    "--framework": [
                      "scikit-learn",
                      "tensorflow",
                      "xgboost"
                    ],
                    "--labels": "value",
                    "--machine-type": "value",
                    "--model": "value",
                    "--origin": "value",
                    "--python-version": "value",
                    "--runtime-version": "value",
                    "--staging-bucket": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--model": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--model": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--model": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-default": {
                  "commands": {},
                  "flags": {
                    "--model": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--model": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "monitoring": {
          "commands": {
            "channel-descriptors": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "channels": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--channel-content": "value",
                    "--channel-content-from-file": "value",
                    "--channel-labels": "value",
                    "--description": "value",
                    "--display-name": "value",
                    "--enabled": "bool",
                    "--type": "value",
                    "--user-labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--force": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--type": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--channel-content": "value",
                    "--channel-content-from-file": "value",
                    "--clear-channel-labels": "bool",
                    "--clear-user-labels": "bool",
                    "--description": "value",
                    "--display-name": "value",
                    "--enabled": "bool",
                    "--fields": "value",
                    "--remove-channel-labels": "value",
                    "--remove-user-labels": "value",
                    "--type": "value",
                    "--update-channel-labels": "value",
                    "--update-user-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "policies": {
              "commands": {
                "conditions": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--aggregation": "value",
                        "--condition": "value",
                        "--condition-display-name": "value",
                        "--condition-filter": "value",
                        "--condition-from-file": "value",
                        "--duration": "value",
                        "--if": "value",
                        "--trigger-count": "value",
                        "--trigger-percent": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--policy": "value"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--policy": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--display-name": "value",
                        "--if": "value",
                        "--policy": "value",
                        "--trigger-count": "value",
                        "--trigger-percent": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--aggregation": "value",
                    "--condition-display-name": "value",
                    "--condition-filter": "value",
                    "--display-name": "value",
                    "--documentation": "value",
                    "--documentation-format": "value",
                    "--documentation-from-file": "value",
                    "--duration": "value",
                    "--enabled": "bool",
                    "--if": "value",
                    "--notification-channels": "value",
                    "--policy": "value",
                    "--policy-from-file": "value",
                    "--trigger-count": "value",
                    "--trigger-percent": "value",
                    "--user-labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-notification-channels": "value",
                    "--clear-notification-channels": "bool",
                    "--clear-user-labels": "bool",
                    "--display-name": "value",
                    "--documentation": "value",
                    "--documentation-format": "value",
                    "--documentation-from-file": "value",
                    "--enabled": "bool",
                    "--fields": "value",
                    "--policy": "value",
                    "--policy-from-file": "value",
                    "--remove-notification-channels": "value",
                    "--remove-user-labels": "value",
                    "--set-notification-channels": "value",
                    "--update-user-labels": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "organizations": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "projects": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--enable-cloud-apis": "bool",
                "--folder": "value",
                "--labels": "value",
                "--name": "value",
                "--organization": "value",
                "--set-as-default": "bool"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "move": {
              "commands": {},
              "flags": {
                "--folder": "value",
                "--organization": "value"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            },
            "undelete": {
              "commands": {},
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--name": "value",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        },
        "pubsub": {
          "commands": {
            "snapshots": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--labels": "value",
                    "--subscription": "value",
                    "--subscription-project": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "subscriptions": {
              "commands": {
                "ack": {
                  "commands": {},
                  "flags": {
                    "--ack-ids": "value"
                  }
                },
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--labels": "value",
                    "--message-retention-duration": "value",
                    "--push-endpoint": "value",
                    "--retain-acked-messages": "bool",
                    "--topic": "value",
                    "--topic-project": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "modify-ack-deadline": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--ack-ids": "value"
                  }
                },
                "modify-message-ack-deadline": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--ack-ids": "value"
                  }
                },
                "modify-push-config": {
                  "commands": {},
                  "flags": {
                    "--push-endpoint": "value"
                  }
                },
                "pull": {
                  "commands": {},
                  "flags": {
                    "--auto-ack": "bool",
                    "--filter": "value",
                    "--limit": "value",
                    "--max-messages": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--wait": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "seek": {
                  "commands": {},
                  "flags": {
                    "--snapshot": "value",
                    "--snapshot-project": "value",
                    "--time": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--clear-labels": "bool",
                    "--message-retention-duration": "value",
                    "--push-endpoint": "value",
                    "--remove-labels": "value",
                    "--retain-acked-messages": "bool",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "topics": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-snapshots": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-subscriptions": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "publish": {
                  "commands": {},
                  "flags": {
                    "--attribute": "value",
                    "--message": "value"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--recompute-message-storage-policy": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "redis": {
          "commands": {
            "instances": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--alternative-zone": "value",
                    "--async": "bool",
                    "--display-name": "value",
                    "--labels": "value",
                    "--network": "value",
                    "--redis-config": "value",
                    "--redis-version": [
                      "redis_3_2"
                    ],
                    "--region": "dynamic",
                    "--reserved-ip-range": "value",
                    "--size": "value",
                    "--tier": [
                      "basic",
                      "standard"
                    ],
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--clear-labels": "bool",
                    "--display-name": "value",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--remove-redis-config": "value",
                    "--size": "value",
                    "--update-labels": "value",
                    "--update-redis-config": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "zones": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "resource-manager": {
          "commands": {
            "folders": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--display-name": "value",
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--folder": "value",
                    "--limit": "value",
                    "--organization": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "move": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "undelete": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--display-name": "value"
                  }
                }
              },
              "flags": {}
            },
            "liens": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--origin": "value",
                    "--reason": "value",
                    "--restrictions": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "org-policies": {
              "commands": {
                "allow": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "deny": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--effective": "bool",
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "disable-enforce": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "enable-enforce": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--folder": "value",
                    "--limit": "value",
                    "--organization": "value",
                    "--page-size": "value",
                    "--show-unset": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-policy": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "resources": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "scheduler": {
          "commands": {
            "jobs": {
              "commands": {
                "create-app-engine-job": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--header": "value",
                    "--http-method": [
                      "delete",
                      "get",
                      "head",
                      "post",
                      "put"
                    ],
                    "--max-attempts": "value",
                    "--max-backoff": "value",
                    "--max-doublings": "value",
                    "--max-retry-duration": "value",
                    "--message-body": "value",
                    "--message-body-from-file": "value",
                    "--min-backoff": "value",
                    "--relative-url": "value",
                    "--schedule": "value",
                    "--service": "value",
                    "--time-zone": "value"
                  }
                },
                "create-http-job": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--header": "value",
                    "--http-method": [
                      "delete",
                      "get",
                      "head",
                      "post",
                      "put"
                    ],
                    "--max-attempts": "value",
                    "--max-backoff": "value",
                    "--max-doublings": "value",
                    "--max-retry-duration": "value",
                    "--message-body": "value",
                    "--message-body-from-file": "value",
                    "--min-backoff": "value",
                    "--schedule": "value",
                    "--time-zone": "value",
                    "--url": "value"
                  }
                },
                "create-pubsub-job": {
                  "commands": {},
                  "flags": {
                    "--attributes": "value",
                    "--description": "value",
                    "--message-body": "value",
                    "--message-body-from-file": "value",
                    "--schedule": "value",
                    "--time-zone": "value",
                    "--topic": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "run": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "search-help": {
          "commands": {},
          "flags": {}
        },
        "services": {
          "commands": {
            "disable": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "enable": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--available": "bool",
                "--enabled": "bool",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--full": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "vpc-peerings": {
              "commands": {
                "connect": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--network": "value",
                    "--reserved-ranges": "value",
                    "--service": "value"
                  }
                },
                "operations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--name": "value"
                      }
                    },
                    "wait": {
                      "commands": {},
                      "flags": {
                        "--name": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "source": {
          "commands": {
            "project-configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-topic": "value",
                    "--disable-pushblock": "bool",
                    "--enable-pushblock": "bool",
                    "--message-format": [
                      "json",
                      "protobuf"
                    ],
                    "--remove-topic": "value",
                    "--service-account": "value",
                    "--topic-project": "value",
                    "--update-topic": "value"
                  }
                }
              },
              "flags": {}
            },
            "repos": {
              "commands": {
                "clone": {
                  "commands": {},
                  "flags": {
                    "--dry-run": "bool",
                    "--use-full-gcloud-path": "bool"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--force": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-topic": "value",
                    "--message-format": [
                      "json",
                      "protobuf"
                    ],
                    "--remove-topic": "value",
                    "--service-account": "value",
                    "--topic-project": "value",
                    "--update-topic": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "spanner": {
          "commands": {
            "databases": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--instance": "value",
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--ddl": "value",
                    "--instance": "value"
                  }
                },
                "ddl": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--instance": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--ddl": "value",
                        "--instance": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--instance": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "value"
                  }
                },
                "execute-sql": {
                  "commands": {},
                  "flags": {
                    "--instance": "value",
                    "--query-mode": [
                      "NORMAL",
                      "PLAN",
                      "PROFILE"
                    ],
                    "--sql": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--instance": "value",
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "sessions": {
                  "commands": {
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--database": "value",
                        "--instance": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--database": "value",
                        "--filter": "value",
                        "--instance": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--server-filter": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--instance": "value"
                  }
                }
              },
              "flags": {}
            },
            "instance-configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "dynamic",
                    "--description": "value",
                    "--nodes": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--nodes": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--database": "dynamic",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--database": "dynamic",
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--database": "dynamic",
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "rows": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {
                    "--database": "value",
                    "--instance": "value",
                    "--keys": "value",
                    "--table": "value"
                  }
                },
                "insert": {
                  "commands": {},
                  "flags": {
                    "--data": "value",
                    "--database": "value",
                    "--instance": "value",
                    "--table": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--data": "value",
                    "--database": "value",
                    "--instance": "value",
                    "--table": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "sql": {
          "commands": {
            "backups": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "restore": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--backup-instance": "dynamic",
                    "--restore-instance": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "connect": {
              "commands": {},
              "flags": {
                "--database": "value",
                "--user": "value"
              }
            },
            "databases": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--charset": "value",
                    "--collation": "value",
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "patch": {
                  "commands": {},
                  "flags": {
                    "--charset": "value",
                    "--collation": "value",
                    "--diff": "bool",
                    "--instance": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "export": {
              "commands": {
                "csv": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--query": "value"
                  }
                },
                "sql": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--table": "value"
                  }
                }
              },
              "flags": {}
            },
            "flags": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--database-version": [
                      "MYSQL_5_5",
                      "MYSQL_5_6",
                      "MYSQL_5_7",
                      "POSTGRES_9_6"
                    ],
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "import": {
              "commands": {
                "csv": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--columns": "value",
                    "--database": "value",
                    "--table": "value",
                    "--user": "value"
                  }
                },
                "sql": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--user": "value"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "clone": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--bin-log-file-name": "value",
                    "--bin-log-position": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--activation-policy": [
                      "always",
                      "never",
                      "on-demand"
                    ],
                    "--assign-ip": "bool",
                    "--async": "bool",
                    "--authorized-gae-apps": "value",
                    "--authorized-networks": "value",
                    "--availability-type": [
                      "regional",
                      "zonal"
                    ],
                    "--backup": "bool",
                    "--backup-start-time": "value",
                    "--client-certificate-path": "value",
                    "--client-key-path": "value",
                    "--cpu": "value",
                    "--database-flags": "value",
                    "--database-version": [
                      "MYSQL_5_5",
                      "MYSQL_5_6",
                      "MYSQL_5_7",
                      "POSTGRES_9_6"
                    ],
                    "--enable-bin-log": "bool",
                    "--failover-replica-name": "value",
                    "--follow-gae-app": "value",
                    "--gce-zone": "value",
                    "--labels": "value",
                    "--maintenance-release-channel": [
                      "preview",
                      "production"
                    ],
                    "--maintenance-window-day": [
                      "FRI",
                      "MON",
                      "SAT",
                      "SUN",
                      "THU",
                      "TUE",
                      "WED"
                    ],
                    "--maintenance-window-hour": "value",
                    "--main-ca-certificate-path": "value",
                    "--main-dump-file-path": "value",
                    "--main-instance-name": "value",
                    "--main-password": "value",
                    "--main-username": "value",
                    "--memory": "value",
                    "--network": "value",
                    "--pricing-plan": [
                      "PACKAGE",
                      "PER_USE"
                    ],
                    "--prompt-for-main-password": "bool",
                    "--region": "value",
                    "--replica-type": [
                      "FAILOVER",
                      "READ"
                    ],
                    "--replication": [
                      "asynchronous",
                      "synchronous"
                    ],
                    "--require-ssl": "bool",
                    "--source-ip-address": "value",
                    "--source-port": "value",
                    "--storage-auto-increase": "bool",
                    "--storage-auto-increase-limit": "value",
                    "--storage-size": "value",
                    "--storage-type": [
                      "HDD",
                      "SSD"
                    ],
                    "--tier": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--table": "value"
                  }
                },
                "failover": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "patch": {
                  "commands": {},
                  "flags": {
                    "--activation-policy": [
                      "always",
                      "never",
                      "on-demand"
                    ],
                    "--assign-ip": "bool",
                    "--async": "bool",
                    "--authorized-gae-apps": "value",
                    "--authorized-networks": "value",
                    "--availability-type": [
                      "regional",
                      "zonal"
                    ],
                    "--backup-start-time": "value",
                    "--clear-authorized-networks": "bool",
                    "--clear-database-flags": "bool",
                    "--clear-gae-apps": "bool",
                    "--clear-labels": "bool",
                    "--cpu": "value",
                    "--database-flags": "value",
                    "--diff": "bool",
                    "--enable-bin-log": "bool",
                    "--enable-database-replication": "bool",
                    "--follow-gae-app": "value",
                    "--gce-zone": "value",
                    "--maintenance-release-channel": [
                      "preview",
                      "production"
                    ],
                    "--maintenance-window-any": "bool",
                    "--maintenance-window-day": [
                      "FRI",
                      "MON",
                      "SAT",
                      "SUN",
                      "THU",
                      "TUE",
                      "WED"
                    ],
                    "--maintenance-window-hour": "value",
                    "--memory": "value",
                    "--network": "value",
                    "--no-backup": "bool",
                    "--pricing-plan": [
                      "PACKAGE",
                      "PER_USE"
                    ],
                    "--remove-labels": "value",
                    "--replication": [
                      "asynchronous",
                      "synchronous"
                    ],
                    "--require-ssl": "bool",
                    "--storage-auto-increase": "bool",
                    "--storage-auto-increase-limit": "value",
                    "--storage-size": "value",
                    "--tier": "value",
                    "--update-labels": "value"
                  }
                },
                "promote-replica": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "reset-ssl-config": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "restart": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "restore-backup": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--backup-id": "value",
                    "--backup-instance": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "ssl": {
              "commands": {
                "client-certs": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--instance": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--instance": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--instance": "dynamic",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "server-ca-certs": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--instance": "dynamic",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "rollback": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    },
                    "rotate": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "ssl-certs": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "tiers": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "users": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--instance": "dynamic",
                    "--password": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-password": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--instance": "dynamic",
                    "--password": "value",
                    "--prompt-for-password": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "tasks": {
          "commands": {
            "acknowledge": {
              "commands": {},
              "flags": {
                "--queue": "value",
                "--schedule-time": "value"
              }
            },
            "cancel-lease": {
              "commands": {},
              "flags": {
                "--queue": "value",
                "--schedule-time": "value"
              }
            },
            "create-app-engine-task": {
              "commands": {},
              "flags": {
                "--header": "value",
                "--method": "value",
                "--payload-content": "value",
                "--payload-file": "value",
                "--queue": "value",
                "--routing": "value",
                "--schedule-time": "value",
                "--url": "value"
              }
            },
            "create-pull-task": {
              "commands": {},
              "flags": {
                "--payload-content": "value",
                "--payload-file": "value",
                "--queue": "value",
                "--schedule-time": "value",
                "--tag": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--queue": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--queue": "value"
              }
            },
            "lease": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--lease-duration": "value",
                "--limit": "value",
                "--oldest-tag": "bool",
                "--queue": "value",
                "--sort-by": "value",
                "--tag": "value",
                "--uri": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--queue": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "locations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "queues": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create-app-engine-queue": {
                  "commands": {},
                  "flags": {
                    "--max-attempts": "value",
                    "--max-backoff": "value",
                    "--max-concurrent-tasks": "value",
                    "--max-doublings": "value",
                    "--max-retry-duration": "value",
                    "--max-tasks-dispatched-per-second": "value",
                    "--min-backoff": "value",
                    "--routing-override": "value"
                  }
                },
                "create-pull-queue": {
                  "commands": {},
                  "flags": {
                    "--max-attempts": "value",
                    "--max-retry-duration": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "pause": {
                  "commands": {},
                  "flags": {}
                },
                "purge": {
                  "commands": {},
                  "flags": {}
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "resume": {
                  "commands": {},
                  "flags": {}
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "update-app-engine-queue": {
                  "commands": {},
                  "flags": {
                    "--clear-max-attempts": "bool",
                    "--clear-max-backoff": "bool",
                    "--clear-max-concurrent-tasks": "bool",
                    "--clear-max-doublings": "bool",
                    "--clear-max-retry-duration": "bool",
                    "--clear-max-tasks-dispatched-per-second": "bool",
                    "--clear-min-backoff": "bool",
                    "--clear-routing-override": "bool",
                    "--max-attempts": "value",
                    "--max-backoff": "value",
                    "--max-concurrent-tasks": "value",
                    "--max-doublings": "value",
                    "--max-retry-duration": "value",
                    "--max-tasks-dispatched-per-second": "value",
                    "--min-backoff": "value",
                    "--routing-override": "value"
                  }
                },
                "update-pull-queue": {
                  "commands": {},
                  "flags": {
                    "--clear-max-attempts": "bool",
                    "--clear-max-retry-duration": "bool",
                    "--max-attempts": "value",
                    "--max-retry-duration": "value"
                  }
                }
              },
              "flags": {}
            },
            "renew-lease": {
              "commands": {},
              "flags": {
                "--lease-duration": "value",
                "--queue": "value",
                "--schedule-time": "value"
              }
            },
            "run": {
              "commands": {},
              "flags": {
                "--queue": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "app": {
      "commands": {
        "browse": {
          "commands": {},
          "flags": {
            "--launch-browser": "bool",
            "--service": "value"
          }
        },
        "create": {
          "commands": {},
          "flags": {
            "--region": "value"
          }
        },
        "deploy": {
          "commands": {},
          "flags": {
            "--bucket": "value",
            "--image-url": "value",
            "--promote": "bool",
            "--stop-previous-version": "bool"
          }
        },
        "describe": {
          "commands": {},
          "flags": {}
        },
        "domain-mappings": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--certificate-id": "value",
                "--certificate-management": [
                  "automatic",
                  "manual"
                ]
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--certificate-id": "value",
                "--certificate-management": [
                  "automatic",
                  "manual"
                ],
                "--no-certificate-id": "bool"
              }
            }
          },
          "flags": {}
        },
        "firewall-rules": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--action": [
                  "ALLOW",
                  "DENY"
                ],
                "--description": "value",
                "--source-range": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "test-ip": {
              "commands": {},
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--action": [
                  "ALLOW",
                  "DENY"
                ],
                "--description": "value",
                "--source-range": "value"
              }
            }
          },
          "flags": {}
        },
        "instances": {
          "commands": {
            "delete": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "disable-debug": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "enable-debug": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--service": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "scp": {
              "commands": {},
              "flags": {
                "--compress": "bool",
                "--recurse": "bool",
                "--service": "value"
              }
            },
            "ssh": {
              "commands": {},
              "flags": {
                "--container": "value",
                "--service": "value"
              }
            }
          },
          "flags": {}
        },
        "logs": {
          "commands": {
            "read": {
              "commands": {},
              "flags": {
                "--level": [
                  "any",
                  "critical",
                  "debug",
                  "error",
                  "info",
                  "warning"
                ],
                "--limit": "value",
                "--logs": "value",
                "--service": "value"
              }
            },
            "tail": {
              "commands": {},
              "flags": {
                "--level": [
                  "any",
                  "critical",
                  "debug",
                  "error",
                  "info",
                  "warning"
                ],
                "--logs": "value",
                "--service": "value"
              }
            }
          },
          "flags": {}
        },
        "open-console": {
          "commands": {},
          "flags": {
            "--logs": "bool",
            "--service": "value"
          }
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--pending": "bool",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "wait": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "regions": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "services": {
          "commands": {
            "browse": {
              "commands": {},
              "flags": {
                "--launch-browser": "bool"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "set-traffic": {
              "commands": {},
              "flags": {
                "--migrate": "bool",
                "--split-by": [
                  "cookie",
                  "ip",
                  "random"
                ],
                "--splits": "value"
              }
            }
          },
          "flags": {}
        },
        "ssl-certificates": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--certificate": "value",
                "--display-name": "value",
                "--private-key": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--certificate": "value",
                "--display-name": "value",
                "--private-key": "value"
              }
            }
          },
          "flags": {}
        },
        "update": {
          "commands": {},
          "flags": {
            "--split-health-checks": "bool"
          }
        },
        "versions": {
          "commands": {
            "browse": {
              "commands": {},
              "flags": {
                "--launch-browser": "bool",
                "--service": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--hide-no-traffic": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--service": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "migrate": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "start": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            },
            "stop": {
              "commands": {},
              "flags": {
                "--service": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "auth": {
      "commands": {
        "activate-service-account": {
          "commands": {},
          "flags": {
            "--key-file": "value",
            "--password-file": "value",
            "--prompt-for-password": "bool"
          }
        },
        "application-default": {
          "commands": {
            "login": {
              "commands": {},
              "flags": {
                "--client-id-file": "value",
                "--launch-browser": "bool",
                "--scopes": "value"
              }
            },
            "print-access-token": {
              "commands": {},
              "flags": {}
            },
            "revoke": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "configure-docker": {
          "commands": {},
          "flags": {}
        },
        "list": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--filter-account": "value",
            "--limit": "value",
            "--page-size": "value",
            "--sort-by": "value"
          }
        },
        "login": {
          "commands": {},
          "flags": {
            "--activate": "bool",
            "--brief": "bool",
            "--enable-gdrive-access": "bool",
            "--force": "bool",
            "--launch-browser": "bool"
          }
        },
        "revoke": {
          "commands": {},
          "flags": {
            "--all": "bool"
          }
        }
      },
      "flags": {}
    },
    "beta": {
      "commands": {
        "app": {
          "commands": {
            "browse": {
              "commands": {},
              "flags": {
                "--launch-browser": "bool",
                "--service": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "deploy": {
              "commands": {},
              "flags": {
                "--bucket": "value",
                "--image-url": "value",
                "--promote": "bool",
                "--stop-previous-version": "bool"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "domain-mappings": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--certificate-id": "value",
                    "--certificate-management": [
                      "automatic",
                      "manual"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--certificate-id": "value",
                    "--certificate-management": [
                      "automatic",
                      "manual"
                    ],
                    "--no-certificate-id": "bool"
                  }
                }
              },
              "flags": {}
            },
            "firewall-rules": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--action": [
                      "ALLOW",
                      "DENY"
                    ],
                    "--description": "value",
                    "--source-range": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "test-ip": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--action": [
                      "ALLOW",
                      "DENY"
                    ],
                    "--description": "value",
                    "--source-range": "value"
                  }
                }
              },
              "flags": {}
            },
            "gen-config": {
              "commands": {},
              "flags": {
                "--config": "value",
                "--custom": "bool",
                "--runtime": "value"
              }
            },
            "instances": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "disable-debug": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "enable-debug": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "scp": {
                  "commands": {},
                  "flags": {
                    "--compress": "bool",
                    "--recurse": "bool",
                    "--service": "value"
                  }
                },
                "ssh": {
                  "commands": {},
                  "flags": {
                    "--container": "value",
                    "--service": "value"
                  }
                }
              },
              "flags": {}
            },
            "logs": {
              "commands": {
                "read": {
                  "commands": {},
                  "flags": {
                    "--level": [
                      "any",
                      "critical",
                      "debug",
                      "error",
                      "info",
                      "warning"
                    ],
                    "--limit": "value",
                    "--logs": "value",
                    "--service": "value"
                  }
                },
                "tail": {
                  "commands": {},
                  "flags": {
                    "--level": [
                      "any",
                      "critical",
                      "debug",
                      "error",
                      "info",
                      "warning"
                    ],
                    "--logs": "value",
                    "--service": "value"
                  }
                }
              },
              "flags": {}
            },
            "open-console": {
              "commands": {},
              "flags": {
                "--logs": "bool",
                "--service": "value"
              }
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--pending": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "repair": {
              "commands": {},
              "flags": {}
            },
            "services": {
              "commands": {
                "browse": {
                  "commands": {},
                  "flags": {
                    "--launch-browser": "bool"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-traffic": {
                  "commands": {},
                  "flags": {
                    "--migrate": "bool",
                    "--split-by": [
                      "cookie",
                      "ip",
                      "random"
                    ],
                    "--splits": "value"
                  }
                }
              },
              "flags": {}
            },
            "ssl-certificates": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--certificate": "value",
                    "--display-name": "value",
                    "--private-key": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--certificate": "value",
                    "--display-name": "value",
                    "--private-key": "value"
                  }
                }
              },
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--split-health-checks": "bool",
                "--use-container-optimized-os": "bool"
              }
            },
            "versions": {
              "commands": {
                "browse": {
                  "commands": {},
                  "flags": {
                    "--launch-browser": "bool",
                    "--service": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--hide-no-traffic": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "migrate": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--service": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "auth": {
          "commands": {
            "activate-service-account": {
              "commands": {},
              "flags": {
                "--key-file": "value",
                "--password-file": "value",
                "--prompt-for-password": "bool"
              }
            },
            "application-default": {
              "commands": {
                "login": {
                  "commands": {},
                  "flags": {
                    "--client-id-file": "value",
                    "--launch-browser": "bool",
                    "--scopes": "value"
                  }
                },
                "print-access-token": {
                  "commands": {},
                  "flags": {}
                },
                "revoke": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "configure-docker": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--filter-account": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "login": {
              "commands": {},
              "flags": {
                "--activate": "bool",
                "--brief": "bool",
                "--enable-gdrive-access": "bool",
                "--force": "bool",
                "--launch-browser": "bool"
              }
            },
            "revoke": {
              "commands": {},
              "flags": {
                "--all": "bool"
              }
            }
          },
          "flags": {}
        },
        "bigtable": {
          "commands": {
            "app-profiles": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--force": "bool",
                    "--instance": "dynamic",
                    "--route-any": "bool",
                    "--route-to": "dynamic",
                    "--transactional-writes": "bool"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--force": "bool",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--force": "bool",
                    "--instance": "dynamic",
                    "--route-any": "bool",
                    "--route-to": "dynamic",
                    "--transactional-writes": "bool"
                  }
                }
              },
              "flags": {}
            },
            "clusters": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic",
                    "--num-nodes": "value",
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instances": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic",
                    "--num-nodes": "value"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster": "dynamic",
                    "--cluster-num-nodes": "value",
                    "--cluster-storage-type": [
                      "hdd",
                      "ssd"
                    ],
                    "--cluster-zone": "value",
                    "--display-name": "value",
                    "--instance-type": [
                      "DEVELOPMENT",
                      "PRODUCTION"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--display-name": "value"
                  }
                },
                "upgrade": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "billing": {
          "commands": {
            "accounts": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "projects": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "link": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "dynamic",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "unlink": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "builds": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--ongoing": "bool",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "log": {
              "commands": {},
              "flags": {
                "--stream": "bool"
              }
            },
            "submit": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--config": "value",
                "--disk-size": "value",
                "--gcs-log-dir": "value",
                "--gcs-source-staging-dir": "value",
                "--machine-type": [
                  "n1-highcpu-32",
                  "n1-highcpu-8"
                ],
                "--no-source": "bool",
                "--substitutions": "value",
                "--tag": "value",
                "--timeout": "value"
              }
            }
          },
          "flags": {}
        },
        "composer": {
          "commands": {
            "environments": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--airflow-configs": "value",
                    "--async": "bool",
                    "--disk-size": "value",
                    "--env-variables": "value",
                    "--labels": "value",
                    "--location": "value",
                    "--machine-type": "value",
                    "--network": "value",
                    "--node-count": "value",
                    "--oauth-scopes": "value",
                    "--service-account": "value",
                    "--subnetwork": "value",
                    "--tags": "value",
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--location": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--locations": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "run": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "storage": {
                  "commands": {
                    "dags": {
                      "commands": {
                        "delete": {
                          "commands": {},
                          "flags": {
                            "--environment": "value",
                            "--location": "value"
                          }
                        },
                        "export": {
                          "commands": {},
                          "flags": {
                            "--destination": "value",
                            "--environment": "value",
                            "--location": "value",
                            "--source": "value"
                          }
                        },
                        "import": {
                          "commands": {},
                          "flags": {
                            "--destination": "value",
                            "--environment": "value",
                            "--location": "value",
                            "--source": "value"
                          }
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--environment": "value",
                            "--location": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "data": {
                      "commands": {
                        "delete": {
                          "commands": {},
                          "flags": {
                            "--environment": "value",
                            "--location": "value"
                          }
                        },
                        "export": {
                          "commands": {},
                          "flags": {
                            "--destination": "value",
                            "--environment": "value",
                            "--location": "value",
                            "--source": "value"
                          }
                        },
                        "import": {
                          "commands": {},
                          "flags": {
                            "--destination": "value",
                            "--environment": "value",
                            "--location": "value",
                            "--source": "value"
                          }
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--environment": "value",
                            "--location": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "plugins": {
                      "commands": {
                        "delete": {
                          "commands": {},
                          "flags": {
                            "--environment": "value",
                            "--location": "value"
                          }
                        },
                        "export": {
                          "commands": {},
                          "flags": {
                            "--destination": "value",
                            "--environment": "value",
                            "--location": "value",
                            "--source": "value"
                          }
                        },
                        "import": {
                          "commands": {},
                          "flags": {
                            "--destination": "value",
                            "--environment": "value",
                            "--location": "value",
                            "--source": "value"
                          }
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--environment": "value",
                            "--location": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--clear-airflow-configs": "bool",
                    "--clear-env-variables": "bool",
                    "--clear-labels": "bool",
                    "--clear-pypi-packages": "bool",
                    "--location": "value",
                    "--node-count": "value",
                    "--remove-airflow-configs": "value",
                    "--remove-env-variables": "value",
                    "--remove-labels": "value",
                    "--remove-pypi-packages": "value",
                    "--update-airflow-configs": "value",
                    "--update-env-variables": "value",
                    "--update-labels": "value",
                    "--update-pypi-package": "value",
                    "--update-pypi-packages-from-file": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--locations": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "compute": {
          "commands": {
            "accelerator-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "addresses": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--addresses": "value",
                    "--description": "value",
                    "--global": "bool",
                    "--ip-version": [
                      "IPV4",
                      "IPV6"
                    ],
                    "--network-tier": "value",
                    "--region": "dynamic",
                    "--subnet": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--global": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "backend-buckets": {
              "commands": {
                "add-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-file": "value",
                    "--key-name": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-cdn": "bool",
                    "--gcs-bucket-name": "dynamic",
                    "--signed-url-cache-max-age": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "delete-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-name": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-cdn": "bool",
                    "--gcs-bucket-name": "dynamic",
                    "--signed-url-cache-max-age": "value"
                  }
                }
              },
              "flags": {}
            },
            "backend-services": {
              "commands": {
                "add-backend": {
                  "commands": {},
                  "flags": {
                    "--balancing-mode": [
                      "CONNECTION",
                      "RATE",
                      "UTILIZATION"
                    ],
                    "--capacity-scaler": "value",
                    "--description": "value",
                    "--global": "bool",
                    "--instance-group": "dynamic",
                    "--instance-group-region": "dynamic",
                    "--instance-group-zone": "dynamic",
                    "--max-connections": "value",
                    "--max-connections-per-endpoint": "value",
                    "--max-connections-per-instance": "value",
                    "--max-rate": "value",
                    "--max-rate-per-endpoint": "value",
                    "--max-rate-per-instance": "value",
                    "--max-utilization": "value",
                    "--network-endpoint-group": "value",
                    "--network-endpoint-group-zone": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "add-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-file": "value",
                    "--key-name": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--affinity-cookie-ttl": "value",
                    "--cache-key-include-host": "bool",
                    "--cache-key-include-protocol": "bool",
                    "--cache-key-include-query-string": "bool",
                    "--cache-key-query-string-blacklist": "value",
                    "--cache-key-query-string-whitelist": "value",
                    "--connection-draining-timeout": "value",
                    "--custom-request-header": "value",
                    "--description": "value",
                    "--enable-cdn": "bool",
                    "--global": "bool",
                    "--health-checks": "dynamic",
                    "--http-health-checks": "dynamic",
                    "--https-health-checks": "dynamic",
                    "--iap": "value",
                    "--load-balancing-scheme": [
                      "EXTERNAL",
                      "INTERNAL"
                    ],
                    "--port-name": "value",
                    "--protocol": [
                      "HTTP",
                      "HTTP2",
                      "HTTPS",
                      "SSL",
                      "TCP",
                      "UDP"
                    ],
                    "--region": "dynamic",
                    "--session-affinity": [
                      "CLIENT_IP",
                      "CLIENT_IP_PORT_PROTO",
                      "CLIENT_IP_PROTO",
                      "GENERATED_COOKIE",
                      "NONE"
                    ],
                    "--signed-url-cache-max-age": "value",
                    "--timeout": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "delete-signed-url-key": {
                  "commands": {},
                  "flags": {
                    "--key-name": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "edit": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "get-health": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-backend": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--instance-group": "dynamic",
                    "--instance-group-region": "dynamic",
                    "--instance-group-zone": "dynamic",
                    "--network-endpoint-group": "value",
                    "--network-endpoint-group-zone": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--affinity-cookie-ttl": "value",
                    "--cache-key-include-host": "bool",
                    "--cache-key-include-protocol": "bool",
                    "--cache-key-include-query-string": "bool",
                    "--cache-key-query-string-blacklist": "value",
                    "--cache-key-query-string-whitelist": "value",
                    "--connection-draining-timeout": "value",
                    "--custom-request-header": "value",
                    "--description": "value",
                    "--enable-cdn": "bool",
                    "--global": "bool",
                    "--health-checks": "dynamic",
                    "--http-health-checks": "dynamic",
                    "--https-health-checks": "dynamic",
                    "--iap": "value",
                    "--no-custom-request-headers": "bool",
                    "--port-name": "value",
                    "--protocol": [
                      "HTTP",
                      "HTTP2",
                      "HTTPS",
                      "SSL",
                      "TCP",
                      "UDP"
                    ],
                    "--region": "dynamic",
                    "--security-policy": "dynamic",
                    "--session-affinity": [
                      "CLIENT_IP",
                      "CLIENT_IP_PORT_PROTO",
                      "CLIENT_IP_PROTO",
                      "GENERATED_COOKIE",
                      "NONE"
                    ],
                    "--signed-url-cache-max-age": "value",
                    "--timeout": "value"
                  }
                },
                "update-backend": {
                  "commands": {},
                  "flags": {
                    "--balancing-mode": [
                      "CONNECTION",
                      "RATE",
                      "UTILIZATION"
                    ],
                    "--capacity-scaler": "value",
                    "--description": "value",
                    "--global": "bool",
                    "--instance-group": "dynamic",
                    "--instance-group-region": "dynamic",
                    "--instance-group-zone": "dynamic",
                    "--max-connections": "value",
                    "--max-connections-per-endpoint": "value",
                    "--max-connections-per-instance": "value",
                    "--max-rate": "value",
                    "--max-rate-per-endpoint": "value",
                    "--max-rate-per-instance": "value",
                    "--max-utilization": "value",
                    "--network-endpoint-group": "value",
                    "--network-endpoint-group-zone": "dynamic",
                    "--region": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "commitments": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--plan": [
                      "12-month",
                      "36-month"
                    ],
                    "--region": "dynamic",
                    "--resources": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "config-ssh": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--remove": "bool",
                "--ssh-config-file": "value",
                "--ssh-key-file": "value"
              }
            },
            "connect-to-serial-port": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--extra-args": "value",
                "--force-key-file-overwrite": "bool",
                "--port": "value",
                "--ssh-key-file": "value",
                "--zone": "dynamic"
              }
            },
            "copy-files": {
              "commands": {},
              "flags": {
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--plain": "bool",
                "--ssh-key-file": "value",
                "--strict-host-key-checking": [
                  "ask",
                  "no",
                  "yes"
                ],
                "--zone": "value"
              }
            },
            "disk-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                }
              },
              "flags": {}
            },
            "disks": {
              "commands": {
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--csek-key-file": "value",
                    "--description": "value",
                    "--guest-os-features": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--kms-key": "dynamic",
                    "--kms-keyring": "dynamic",
                    "--kms-location": "dynamic",
                    "--kms-project": "dynamic",
                    "--labels": "value",
                    "--licenses": "value",
                    "--region": "dynamic",
                    "--replica-zones": "value",
                    "--require-csek-key-create": "bool",
                    "--size": "value",
                    "--source-snapshot": "dynamic",
                    "--type": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                },
                "move": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--destination-zone": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "resize": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--size": "value",
                    "--zone": "dynamic"
                  }
                },
                "snapshot": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--csek-key-file": "value",
                    "--description": "value",
                    "--guest-flush": "bool",
                    "--labels": "value",
                    "--region": "dynamic",
                    "--snapshot-names": "value",
                    "--zone": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "firewall-rules": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--action": [
                      "ALLOW",
                      "DENY"
                    ],
                    "--allow": "value",
                    "--description": "value",
                    "--destination-ranges": "value",
                    "--direction": [
                      "EGRESS",
                      "IN",
                      "INGRESS",
                      "OUT"
                    ],
                    "--disabled": "bool",
                    "--network": "value",
                    "--priority": "value",
                    "--rules": "value",
                    "--source-ranges": "value",
                    "--source-service-accounts": "value",
                    "--source-tags": "value",
                    "--target-service-accounts": "value",
                    "--target-tags": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--allow": "value",
                    "--description": "value",
                    "--destination-ranges": "value",
                    "--disabled": "bool",
                    "--priority": "value",
                    "--rules": "value",
                    "--source-ranges": "value",
                    "--source-service-accounts": "value",
                    "--source-tags": "value",
                    "--target-service-accounts": "value",
                    "--target-tags": "value"
                  }
                }
              },
              "flags": {}
            },
            "forwarding-rules": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--address": "dynamic",
                    "--address-region": "dynamic",
                    "--backend-service": "value",
                    "--backend-service-region": "dynamic",
                    "--description": "value",
                    "--global": "bool",
                    "--global-address": "bool",
                    "--global-backend-service": "bool",
                    "--ip-protocol": [
                      "AH",
                      "ESP",
                      "ICMP",
                      "SCTP",
                      "TCP",
                      "UDP"
                    ],
                    "--ip-version": [
                      "IPV4",
                      "IPV6"
                    ],
                    "--load-balancing-scheme": [
                      "EXTERNAL",
                      "INTERNAL"
                    ],
                    "--network": "value",
                    "--network-tier": "value",
                    "--port-range": "value",
                    "--ports": "value",
                    "--region": "dynamic",
                    "--service-label": "value",
                    "--subnet": "value",
                    "--subnet-region": "dynamic",
                    "--target-http-proxy": "value",
                    "--target-https-proxy": "value",
                    "--target-instance": "value",
                    "--target-instance-zone": "dynamic",
                    "--target-pool": "value",
                    "--target-pool-region": "dynamic",
                    "--target-ssl-proxy": "value",
                    "--target-tcp-proxy": "value",
                    "--target-vpn-gateway": "value",
                    "--target-vpn-gateway-region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-target": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "value",
                    "--backend-service-region": "dynamic",
                    "--global": "bool",
                    "--global-backend-service": "bool",
                    "--load-balancing-scheme": [
                      "EXTERNAL",
                      "INTERNAL"
                    ],
                    "--network": "value",
                    "--region": "dynamic",
                    "--subnet": "value",
                    "--subnet-region": "dynamic",
                    "--target-http-proxy": "value",
                    "--target-https-proxy": "value",
                    "--target-instance": "value",
                    "--target-instance-zone": "dynamic",
                    "--target-pool": "value",
                    "--target-pool-region": "dynamic",
                    "--target-ssl-proxy": "value",
                    "--target-tcp-proxy": "value",
                    "--target-vpn-gateway": "value",
                    "--target-vpn-gateway-region": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--global": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "health-checks": {
              "commands": {
                "create": {
                  "commands": {
                    "http": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "http2": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "https": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "ssl": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value",
                        "--use-serving-port": "bool"
                      }
                    },
                    "tcp": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--protocol": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {
                    "http": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "http2": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "https": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--host": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request-path": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "ssl": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    },
                    "tcp": {
                      "commands": {},
                      "flags": {
                        "--check-interval": "value",
                        "--description": "value",
                        "--healthy-threshold": "value",
                        "--port": "value",
                        "--port-name": "value",
                        "--proxy-header": [
                          "NONE",
                          "PROXY_V1"
                        ],
                        "--request": "value",
                        "--response": "value",
                        "--timeout": "value",
                        "--unhealthy-threshold": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "http-health-checks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                }
              },
              "flags": {}
            },
            "https-health-checks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                }
              },
              "flags": {}
            },
            "images": {
              "commands": {
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--csek-key-file": "value",
                    "--description": "value",
                    "--family": "value",
                    "--force": "bool",
                    "--force-create": "bool",
                    "--guest-os-features": "value",
                    "--kms-key": "dynamic",
                    "--kms-keyring": "dynamic",
                    "--kms-location": "dynamic",
                    "--kms-project": "dynamic",
                    "--labels": "value",
                    "--licenses": "value",
                    "--require-csek-key-create": "bool",
                    "--source-disk": "dynamic",
                    "--source-disk-zone": "dynamic",
                    "--source-image": "value",
                    "--source-image-family": "value",
                    "--source-image-project": "value",
                    "--source-snapshot": "dynamic",
                    "--source-uri": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "deprecate": {
                  "commands": {},
                  "flags": {
                    "--delete-in": "value",
                    "--delete-on": "value",
                    "--obsolete-in": "value",
                    "--obsolete-on": "value",
                    "--replacement": "dynamic",
                    "--state": [
                      "ACTIVE",
                      "DELETED",
                      "DEPRECATED",
                      "OBSOLETE"
                    ]
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "describe-from-family": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--destination-uri": "value",
                    "--export-format": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--log-location": "value",
                    "--network": "value",
                    "--timeout": "value"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--data-disk": "bool",
                    "--log-location": "value",
                    "--os": [
                      "centos-6",
                      "centos-7",
                      "debian-8",
                      "debian-9",
                      "rhel-6",
                      "rhel-6-byol",
                      "rhel-7",
                      "rhel-7-byol",
                      "ubuntu-1404",
                      "ubuntu-1604",
                      "windows-2008r2",
                      "windows-2012r2",
                      "windows-2016"
                    ],
                    "--source-file": "value",
                    "--source-image": "dynamic",
                    "--timeout": "value",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--preview-images": "bool",
                    "--regexp": "value",
                    "--show-deprecated": "bool",
                    "--sort-by": "value",
                    "--standard-images": "bool",
                    "--uri": "bool"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "instance-groups": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "get-named-ports": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                },
                "list-instances": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "managed": {
                  "commands": {
                    "abandon-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--base-instance-name": "value",
                        "--description": "value",
                        "--health-check": "dynamic",
                        "--http-health-check": "value",
                        "--https-health-check": "value",
                        "--initial-delay": "value",
                        "--region": "dynamic",
                        "--size": "value",
                        "--target-pool": "value",
                        "--template": "value",
                        "--zone": "dynamic",
                        "--zones": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "delete-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "export-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--autoscaling-file": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "get-named-ports": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--regions": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zones": "value"
                      }
                    },
                    "list-instances": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "recreate-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "resize": {
                      "commands": {},
                      "flags": {
                        "--creation-retries": "bool",
                        "--region": "dynamic",
                        "--size": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "rolling-action": {
                      "commands": {
                        "replace": {
                          "commands": {},
                          "flags": {
                            "--max-surge": "value",
                            "--max-unavailable": "value",
                            "--min-ready": "value",
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        },
                        "restart": {
                          "commands": {},
                          "flags": {
                            "--max-unavailable": "value",
                            "--min-ready": "value",
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        },
                        "start-update": {
                          "commands": {},
                          "flags": {
                            "--canary-version": "value",
                            "--force": "bool",
                            "--max-surge": "value",
                            "--max-unavailable": "value",
                            "--min-ready": "value",
                            "--region": "dynamic",
                            "--type": [
                              "opportunistic",
                              "proactive"
                            ],
                            "--zone": "dynamic"
                          }
                        },
                        "stop-proactive-update": {
                          "commands": {},
                          "flags": {
                            "--region": "dynamic",
                            "--zone": "dynamic"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "set-autohealing": {
                      "commands": {},
                      "flags": {
                        "--health-check": "dynamic",
                        "--http-health-check": "value",
                        "--https-health-check": "value",
                        "--initial-delay": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "set-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--autoscaling-file": "value",
                        "--cool-down-period": "value",
                        "--custom-metric-utilization": "value",
                        "--description": "value",
                        "--max-num-replicas": "value",
                        "--min-num-replicas": "value",
                        "--region": "dynamic",
                        "--remove-stackdriver-metric": "value",
                        "--scale-based-on-cpu": "bool",
                        "--scale-based-on-load-balancing": "bool",
                        "--stackdriver-metric-filter": "value",
                        "--stackdriver-metric-single-instance-assignment": "value",
                        "--stackdriver-metric-utilization-target": "value",
                        "--stackdriver-metric-utilization-target-type": [
                          "delta-per-minute",
                          "delta-per-second",
                          "gauge"
                        ],
                        "--target-cpu-utilization": "value",
                        "--target-load-balancing-utilization": "value",
                        "--update-stackdriver-metric": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "set-instance-template": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--template": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "set-named-ports": {
                      "commands": {},
                      "flags": {
                        "--named-ports": "value",
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "set-target-pools": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--target-pools": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "stop-autoscaling": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--zone": "dynamic"
                      }
                    },
                    "wait-until-stable": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic",
                        "--timeout": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "set-named-ports": {
                  "commands": {},
                  "flags": {
                    "--named-ports": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "unmanaged": {
                  "commands": {
                    "add-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "get-named-ports": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zones": "dynamic"
                      }
                    },
                    "list-instances": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "remove-instances": {
                      "commands": {},
                      "flags": {
                        "--instances": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "set-named-ports": {
                      "commands": {},
                      "flags": {
                        "--named-ports": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "instance-templates": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--address": "value",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-kms-key": "dynamic",
                    "--boot-disk-kms-keyring": "dynamic",
                    "--boot-disk-kms-location": "dynamic",
                    "--boot-disk-kms-project": "dynamic",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--configure-disk": "value",
                    "--create-disk": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--node": "value",
                    "--node-affinity-file": "value",
                    "--node-group": "value",
                    "--preemptible": "bool",
                    "--region": "dynamic",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--shielded-vm-integrity-monitoring": "bool",
                    "--shielded-vm-secure-boot": "bool",
                    "--shielded-vm-vtpm": "bool",
                    "--source-instance": "dynamic",
                    "--source-instance-zone": "dynamic",
                    "--subnet": "value",
                    "--tags": "value"
                  }
                },
                "create-with-container": {
                  "commands": {},
                  "flags": {
                    "--address": "value",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--container-arg": "value",
                    "--container-command": "value",
                    "--container-env": "value",
                    "--container-env-file": "value",
                    "--container-image": "value",
                    "--container-mount-host-path": "value",
                    "--container-mount-tmpfs": "value",
                    "--container-privileged": "bool",
                    "--container-restart-policy": [
                      "always",
                      "never",
                      "on-failure"
                    ],
                    "--container-stdin": "bool",
                    "--container-tty": "bool",
                    "--create-disk": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--preemptible": "bool",
                    "--region": "dynamic",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--subnet": "value",
                    "--tags": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "add-access-config": {
                  "commands": {},
                  "flags": {
                    "--access-config-name": "value",
                    "--address": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-metadata": {
                  "commands": {},
                  "flags": {
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "add-tags": {
                  "commands": {},
                  "flags": {
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "attach-disk": {
                  "commands": {},
                  "flags": {
                    "--csek-key-file": "value",
                    "--device-name": "value",
                    "--disk": "value",
                    "--disk-scope": [
                      "regional",
                      "zonal"
                    ],
                    "--force-attach": "bool",
                    "--mode": [
                      "ro",
                      "rw"
                    ],
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--address": "value",
                    "--async": "bool",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-kms-key": "dynamic",
                    "--boot-disk-kms-keyring": "dynamic",
                    "--boot-disk-kms-location": "dynamic",
                    "--boot-disk-kms-project": "dynamic",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--create-disk": "value",
                    "--csek-key-file": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--deletion-protection": "bool",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--node": "value",
                    "--node-affinity-file": "value",
                    "--node-group": "value",
                    "--preemptible": "bool",
                    "--private-network-ip": "value",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--require-csek-key-create": "bool",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--shielded-vm-integrity-monitoring": "bool",
                    "--shielded-vm-secure-boot": "bool",
                    "--shielded-vm-vtpm": "bool",
                    "--source-instance-template": "dynamic",
                    "--subnet": "value",
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "create-with-container": {
                  "commands": {},
                  "flags": {
                    "--address": "value",
                    "--boot-disk-auto-delete": "bool",
                    "--boot-disk-device-name": "value",
                    "--boot-disk-size": "value",
                    "--boot-disk-type": "value",
                    "--can-ip-forward": "bool",
                    "--container-arg": "value",
                    "--container-command": "value",
                    "--container-env": "value",
                    "--container-env-file": "value",
                    "--container-image": "value",
                    "--container-mount-host-path": "value",
                    "--container-mount-tmpfs": "value",
                    "--container-privileged": "bool",
                    "--container-restart-policy": [
                      "always",
                      "never",
                      "on-failure"
                    ],
                    "--container-stdin": "bool",
                    "--container-tty": "bool",
                    "--create-disk": "value",
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--description": "value",
                    "--disk": "value",
                    "--image": "value",
                    "--image-family": "value",
                    "--image-project": "value",
                    "--labels": "value",
                    "--local-ssd": "value",
                    "--machine-type": "dynamic",
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--min-cpu-platform": "value",
                    "--network": "value",
                    "--network-interface": "value",
                    "--network-tier": "value",
                    "--no-address": "bool",
                    "--no-public-dns": "bool",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--preemptible": "bool",
                    "--private-network-ip": "value",
                    "--public-dns": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--restart-on-failure": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--source-instance-template": "dynamic",
                    "--subnet": "value",
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--delete-disks": [
                      "all",
                      "boot",
                      "data"
                    ],
                    "--keep-disks": [
                      "all",
                      "boot",
                      "data"
                    ],
                    "--zone": "dynamic"
                  }
                },
                "delete-access-config": {
                  "commands": {},
                  "flags": {
                    "--access-config-name": "value",
                    "--network-interface": "value",
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "detach-disk": {
                  "commands": {},
                  "flags": {
                    "--device-name": "value",
                    "--disk": "value",
                    "--disk-scope": [
                      "regional",
                      "zonal"
                    ],
                    "--zone": "dynamic"
                  }
                },
                "get-serial-port-output": {
                  "commands": {},
                  "flags": {
                    "--port": "value",
                    "--start": "value",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                },
                "move": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--destination-zone": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "network-interfaces": {
                  "commands": {
                    "update": {
                      "commands": {},
                      "flags": {
                        "--aliases": "value",
                        "--network-interface": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-metadata": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--keys": "value",
                    "--zone": "dynamic"
                  }
                },
                "remove-tags": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--tags": "value",
                    "--zone": "dynamic"
                  }
                },
                "reset": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "set-disk-auto-delete": {
                  "commands": {},
                  "flags": {
                    "--auto-delete": "bool",
                    "--device-name": "value",
                    "--disk": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-machine-type": {
                  "commands": {},
                  "flags": {
                    "--custom-cpu": "value",
                    "--custom-extensions": "bool",
                    "--custom-memory": "value",
                    "--machine-type": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "set-scheduling": {
                  "commands": {},
                  "flags": {
                    "--maintenance-policy": [
                      "MIGRATE",
                      "TERMINATE"
                    ],
                    "--restart-on-failure": "bool",
                    "--zone": "dynamic"
                  }
                },
                "set-scopes": {
                  "commands": {},
                  "flags": {
                    "--no-scopes": "bool",
                    "--no-service-account": "bool",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--zone": "dynamic"
                  }
                },
                "simulate-maintenance-event": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "dynamic"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--csek-key-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "dynamic"
                  }
                },
                "tail-serial-port-output": {
                  "commands": {},
                  "flags": {
                    "--port": "value",
                    "--zone": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--deletion-protection": "bool",
                    "--min-cpu-platform": "value",
                    "--remove-labels": "value",
                    "--shielded-vm-integrity-monitoring": "bool",
                    "--shielded-vm-learn-integrity-policy": "bool",
                    "--shielded-vm-secure-boot": "bool",
                    "--shielded-vm-vtpm": "bool",
                    "--update-labels": "value",
                    "--zone": "dynamic"
                  }
                },
                "update-access-config": {
                  "commands": {},
                  "flags": {
                    "--network-interface": "value",
                    "--no-public-ptr": "bool",
                    "--no-public-ptr-domain": "bool",
                    "--public-ptr": "bool",
                    "--public-ptr-domain": "value",
                    "--zone": "dynamic"
                  }
                },
                "update-container": {
                  "commands": {},
                  "flags": {
                    "--clear-container-args": "bool",
                    "--clear-container-command": "bool",
                    "--container-arg": "value",
                    "--container-command": "value",
                    "--container-env": "value",
                    "--container-env-file": "value",
                    "--container-image": "value",
                    "--container-mount-host-path": "value",
                    "--container-mount-tmpfs": "value",
                    "--container-privileged": "bool",
                    "--container-restart-policy": [
                      "always",
                      "never",
                      "on-failure"
                    ],
                    "--container-stdin": "bool",
                    "--container-tty": "bool",
                    "--remove-container-env": "value",
                    "--remove-container-mounts": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "interconnects": {
              "commands": {
                "attachments": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--interconnect": "dynamic",
                        "--region": "dynamic",
                        "--router": "dynamic"
                      }
                    },
                    "dedicated": {
                      "commands": {
                        "create": {
                          "commands": {},
                          "flags": {
                            "--candidate-subnets": "value",
                            "--description": "value",
                            "--enable-admin": "bool",
                            "--interconnect": "dynamic",
                            "--region": "dynamic",
                            "--router": "dynamic",
                            "--vlan": "value"
                          }
                        },
                        "update": {
                          "commands": {},
                          "flags": {
                            "--clear-labels": "bool",
                            "--description": "value",
                            "--enable-admin": "bool",
                            "--region": "dynamic",
                            "--remove-labels": "value",
                            "--update-labels": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "partner": {
                      "commands": {
                        "create": {
                          "commands": {},
                          "flags": {
                            "--description": "value",
                            "--edge-availability-domain": [
                              "any",
                              "availability-domain-1",
                              "availability-domain-2"
                            ],
                            "--enable-admin": "bool",
                            "--region": "dynamic",
                            "--router": "dynamic"
                          }
                        },
                        "update": {
                          "commands": {},
                          "flags": {
                            "--clear-labels": "bool",
                            "--description": "value",
                            "--enable-admin": "bool",
                            "--region": "dynamic",
                            "--remove-labels": "value",
                            "--update-labels": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--admin-enabled": "bool",
                    "--customer-name": "value",
                    "--description": "value",
                    "--interconnect-type": [
                      "DEDICATED",
                      "IT_PRIVATE",
                      "PARTNER"
                    ],
                    "--link-type": [
                      "LINK_TYPE_ETHERNET_10G_LR"
                    ],
                    "--location": "dynamic",
                    "--noc-contact-email": "value",
                    "--requested-link-count": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "locations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "patch": {
                  "commands": {},
                  "flags": {
                    "--admin-enabled": "bool",
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--noc-contact-email": "value",
                    "--remove-labels": "value",
                    "--requested-link-count": "value",
                    "--update-labels": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--admin-enabled": "bool",
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--noc-contact-email": "value",
                    "--remove-labels": "value",
                    "--requested-link-count": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "machine-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "network-endpoint-groups": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--default-port": "value",
                    "--network": "value",
                    "--subnet": "value",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-network-endpoints": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--zone": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-endpoint": "value",
                    "--remove-endpoint": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "networks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--bgp-routing-mode": [
                      "global",
                      "regional"
                    ],
                    "--description": "value",
                    "--mode": [
                      "auto",
                      "custom",
                      "legacy"
                    ],
                    "--range": "value",
                    "--subnet-mode": [
                      "auto",
                      "custom",
                      "legacy"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "peerings": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--auto-create-routes": "bool",
                        "--network": "value",
                        "--peer-network": "value",
                        "--peer-project": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--network": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--network": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "subnets": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--enable-flow-logs": "bool",
                        "--enable-private-ip-google-access": "bool",
                        "--network": "dynamic",
                        "--range": "value",
                        "--region": "dynamic",
                        "--secondary-range": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "expand-ip-range": {
                      "commands": {},
                      "flags": {
                        "--prefix-length": "value",
                        "--region": "dynamic"
                      }
                    },
                    "get-iam-policy": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--region": "dynamic",
                        "--sort-by": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--network": "value",
                        "--page-size": "value",
                        "--regexp": "value",
                        "--regions": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "list-usable": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "set-iam-policy": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--add-secondary-ranges": "value",
                        "--enable-flow-logs": "bool",
                        "--enable-private-ip-google-access": "bool",
                        "--region": "dynamic",
                        "--remove-secondary-ranges": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--bgp-routing-mode": [
                      "global",
                      "regional"
                    ],
                    "--switch-to-custom-subnet-mode": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--global": "bool",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--global": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                }
              },
              "flags": {}
            },
            "os-login": {
              "commands": {
                "describe-profile": {
                  "commands": {},
                  "flags": {}
                },
                "remove-profile": {
                  "commands": {},
                  "flags": {}
                },
                "ssh-keys": {
                  "commands": {
                    "add": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value",
                        "--ttl": "value"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--key": "value",
                        "--key-file": "value",
                        "--ttl": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "project-info": {
              "commands": {
                "add-metadata": {
                  "commands": {},
                  "flags": {
                    "--metadata": "value",
                    "--metadata-from-file": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "remove-metadata": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--keys": "value"
                  }
                },
                "set-usage-bucket": {
                  "commands": {},
                  "flags": {
                    "--bucket": "value",
                    "--no-bucket": "bool",
                    "--prefix": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--default-network-tier": [
                      "PREMIUM",
                      "STANDARD"
                    ]
                  }
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "reset-windows-password": {
              "commands": {},
              "flags": {
                "--user": "value",
                "--zone": "dynamic"
              }
            },
            "routers": {
              "commands": {
                "add-bgp-peer": {
                  "commands": {},
                  "flags": {
                    "--advertised-route-priority": "value",
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--async": "bool",
                    "--interface": "value",
                    "--peer-asn": "value",
                    "--peer-ip-address": "value",
                    "--peer-name": "value",
                    "--region": "dynamic",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "add-interface": {
                  "commands": {},
                  "flags": {
                    "--interconnect-attachment": "dynamic",
                    "--interconnect-attachment-region": "dynamic",
                    "--interface-name": "value",
                    "--ip-address": "value",
                    "--mask-length": "value",
                    "--region": "dynamic",
                    "--vpn-tunnel": "dynamic",
                    "--vpn-tunnel-region": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--asn": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--network": "dynamic",
                    "--region": "dynamic",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "get-status": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-bgp-peer": {
                  "commands": {},
                  "flags": {
                    "--peer-name": "value",
                    "--region": "dynamic"
                  }
                },
                "remove-interface": {
                  "commands": {},
                  "flags": {
                    "--interface-name": "value",
                    "--region": "dynamic"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-advertisement-groups": "value",
                    "--add-advertisement-ranges": "value",
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--async": "bool",
                    "--region": "dynamic",
                    "--remove-advertisement-groups": "value",
                    "--remove-advertisement-ranges": "value",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "update-bgp-peer": {
                  "commands": {},
                  "flags": {
                    "--add-advertisement-groups": "value",
                    "--add-advertisement-ranges": "value",
                    "--advertised-route-priority": "value",
                    "--advertisement-mode": [
                      "CUSTOM",
                      "DEFAULT"
                    ],
                    "--async": "bool",
                    "--interface": "value",
                    "--ip-address": "value",
                    "--peer-asn": "value",
                    "--peer-ip-address": "value",
                    "--peer-name": "value",
                    "--region": "dynamic",
                    "--remove-advertisement-groups": "value",
                    "--remove-advertisement-ranges": "value",
                    "--set-advertisement-groups": "value",
                    "--set-advertisement-ranges": "value"
                  }
                },
                "update-interface": {
                  "commands": {},
                  "flags": {
                    "--interconnect-attachment": "dynamic",
                    "--interconnect-attachment-region": "dynamic",
                    "--interface-name": "value",
                    "--ip-address": "value",
                    "--mask-length": "value",
                    "--region": "dynamic",
                    "--vpn-tunnel": "dynamic",
                    "--vpn-tunnel-region": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "routes": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--destination-range": "value",
                    "--network": "value",
                    "--next-hop-address": "value",
                    "--next-hop-gateway": "dynamic",
                    "--next-hop-instance": "value",
                    "--next-hop-instance-zone": "value",
                    "--next-hop-vpn-tunnel": "value",
                    "--next-hop-vpn-tunnel-region": "value",
                    "--priority": "value",
                    "--tags": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "scp": {
              "commands": {},
              "flags": {
                "--compress": "bool",
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--plain": "bool",
                "--port": "value",
                "--recurse": "bool",
                "--scp-flag": "value",
                "--ssh-key-file": "value",
                "--strict-host-key-checking": [
                  "ask",
                  "no",
                  "yes"
                ],
                "--zone": "value"
              }
            },
            "security-policies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--file-format": [
                      "json",
                      "yaml"
                    ],
                    "--file-name": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--file-format": [
                      "json",
                      "yaml"
                    ],
                    "--file-name": "value"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--file-format": [
                      "json",
                      "yaml"
                    ],
                    "--file-name": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "rules": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--action": [
                          "allow",
                          "deny-403",
                          "deny-404",
                          "deny-502"
                        ],
                        "--description": "value",
                        "--expression": "value",
                        "--preview": "bool",
                        "--security-policy": "dynamic",
                        "--src-ip-ranges": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--security-policy": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--security-policy": "dynamic"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--action": [
                          "allow",
                          "deny-403",
                          "deny-404",
                          "deny-502"
                        ],
                        "--description": "value",
                        "--expression": "value",
                        "--preview": "bool",
                        "--security-policy": "dynamic",
                        "--src-ip-ranges": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "shared-vpc": {
              "commands": {
                "associated-projects": {
                  "commands": {
                    "add": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "disable": {
                  "commands": {},
                  "flags": {}
                },
                "enable": {
                  "commands": {},
                  "flags": {}
                },
                "get-host-project": {
                  "commands": {},
                  "flags": {}
                },
                "list-associated-resources": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "organizations": {
                  "commands": {
                    "list-host-projects": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "sign-url": {
              "commands": {},
              "flags": {
                "--expires-in": "value",
                "--key-file": "value",
                "--key-name": "value",
                "--validate": "bool"
              }
            },
            "snapshots": {
              "commands": {
                "add-labels": {
                  "commands": {},
                  "flags": {
                    "--labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-labels": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--labels": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "sole-tenancy": {
              "commands": {
                "node-groups": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--node-template": "value",
                        "--target-size": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--add-nodes": "value",
                        "--delete-nodes": "value",
                        "--node-template": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "node-templates": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--node-affinity-labels": "value",
                        "--node-requirements": "value",
                        "--node-type": "value",
                        "--region": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "node-types": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "ssh": {
              "commands": {},
              "flags": {
                "--command": "value",
                "--container": "value",
                "--dry-run": "bool",
                "--force-key-file-overwrite": "bool",
                "--internal-ip": "bool",
                "--plain": "bool",
                "--ssh-flag": "value",
                "--ssh-key-file": "value",
                "--strict-host-key-checking": [
                  "ask",
                  "no",
                  "yes"
                ],
                "--zone": "dynamic"
              }
            },
            "ssl-certificates": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--certificate": "value",
                    "--description": "value",
                    "--private-key": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "ssl-policies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--custom-features": "value",
                    "--description": "value",
                    "--min-tls-version": [
                      "1.0",
                      "1.1",
                      "1.2"
                    ],
                    "--profile": [
                      "COMPATIBLE",
                      "CUSTOM",
                      "MODERN",
                      "RESTRICTED"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-available-features": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--custom-features": "value",
                    "--min-tls-version": [
                      "1.0",
                      "1.1",
                      "1.2"
                    ],
                    "--profile": [
                      "COMPATIBLE",
                      "CUSTOM",
                      "MODERN",
                      "RESTRICTED"
                    ]
                  }
                }
              },
              "flags": {}
            },
            "target-http-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--url-map": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--url-map": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-https-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--quic-override": [
                      "DISABLE",
                      "ENABLE",
                      "NONE"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic",
                    "--url-map": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-ssl-policy": "bool",
                    "--quic-override": [
                      "DISABLE",
                      "ENABLE",
                      "NONE"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic",
                    "--url-map": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-instances": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--instance": "dynamic",
                    "--instance-zone": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-pools": {
              "commands": {
                "add-health-checks": {
                  "commands": {},
                  "flags": {
                    "--http-health-check": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "add-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "dynamic",
                    "--instances-zone": "dynamic",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--backup-pool": "value",
                    "--description": "value",
                    "--failover-ratio": "value",
                    "--health-check": "value",
                    "--http-health-check": "dynamic",
                    "--region": "dynamic",
                    "--session-affinity": [
                      "CLIENT_IP",
                      "CLIENT_IP_PROTO",
                      "GENERATED_COOKIE",
                      "NONE"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "get-health": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-health-checks": {
                  "commands": {},
                  "flags": {
                    "--http-health-check": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "remove-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "dynamic",
                    "--instances-zone": "dynamic",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "set-backup": {
                  "commands": {},
                  "flags": {
                    "--backup-pool": "dynamic",
                    "--failover-ratio": "value",
                    "--no-backup-pool": "bool",
                    "--region": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-ssl-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--description": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--clear-ssl-policy": "bool",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--ssl-certificates": "dynamic",
                    "--ssl-policy": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "target-tcp-proxies": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--description": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--backend-service": "dynamic",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ]
                  }
                }
              },
              "flags": {}
            },
            "target-vpn-gateways": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--network": "dynamic",
                    "--region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "tpus": {
              "commands": {
                "accelerator-types": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator-type": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--network": "value",
                    "--preemptible": "bool",
                    "--range": "value",
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "locations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "reimage": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--zone": "value"
                  }
                },
                "versions": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "url-maps": {
              "commands": {
                "add-host-rule": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--hosts": "value",
                    "--path-matcher-name": "value"
                  }
                },
                "add-path-matcher": {
                  "commands": {},
                  "flags": {
                    "--backend-bucket-path-rules": "value",
                    "--backend-service-path-rules": "value",
                    "--default-backend-bucket": "value",
                    "--default-service": "value",
                    "--delete-orphaned-path-matcher": "bool",
                    "--description": "value",
                    "--existing-host": "value",
                    "--new-hosts": "value",
                    "--path-matcher-name": "value",
                    "--path-rules": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--default-backend-bucket": "value",
                    "--default-service": "value",
                    "--description": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "edit": {
                  "commands": {},
                  "flags": {}
                },
                "invalidate-cdn-cache": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--path": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-cdn-cache-invalidations": {
                  "commands": {},
                  "flags": {
                    "--limit": "value"
                  }
                },
                "remove-host-rule": {
                  "commands": {},
                  "flags": {
                    "--delete-orphaned-path-matcher": "bool",
                    "--host": "value"
                  }
                },
                "remove-path-matcher": {
                  "commands": {},
                  "flags": {
                    "--path-matcher-name": "value"
                  }
                },
                "set-default-service": {
                  "commands": {},
                  "flags": {
                    "--default-backend-bucket": "value",
                    "--default-service": "value"
                  }
                }
              },
              "flags": {}
            },
            "vpn-tunnels": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--ike-version": [
                      1,
                      2
                    ],
                    "--local-traffic-selector": "value",
                    "--peer-address": "value",
                    "--region": "dynamic",
                    "--remote-traffic-selector": "value",
                    "--router": "value",
                    "--shared-secret": "value",
                    "--target-vpn-gateway": "dynamic",
                    "--target-vpn-gateway-region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "xpn": {
              "commands": {
                "associated-projects": {
                  "commands": {
                    "add": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--host-project": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "disable": {
                  "commands": {},
                  "flags": {}
                },
                "enable": {
                  "commands": {},
                  "flags": {}
                },
                "get-host-project": {
                  "commands": {},
                  "flags": {}
                },
                "list-associated-resources": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "organizations": {
                  "commands": {
                    "list-host-projects": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "zones": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "config": {
          "commands": {
            "configurations": {
              "commands": {
                "activate": {
                  "commands": {},
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--activate": "bool"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--all": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "get-value": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            },
            "set": {
              "commands": {},
              "flags": {
                "--installation": "bool"
              }
            },
            "unset": {
              "commands": {},
              "flags": {
                "--installation": "bool"
              }
            }
          },
          "flags": {}
        },
        "container": {
          "commands": {
            "builds": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--ongoing": "bool",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "log": {
                  "commands": {},
                  "flags": {
                    "--stream": "bool"
                  }
                },
                "submit": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "value",
                    "--disk-size": "value",
                    "--gcs-log-dir": "value",
                    "--gcs-source-staging-dir": "value",
                    "--machine-type": [
                      "n1-highcpu-32",
                      "n1-highcpu-8"
                    ],
                    "--no-source": "bool",
                    "--substitutions": "value",
                    "--tag": "value",
                    "--timeout": "value"
                  }
                }
              },
              "flags": {}
            },
            "clusters": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--additional-zones": "value",
                    "--addons": "value",
                    "--allow-route-overlap": "bool",
                    "--async": "bool",
                    "--cluster-ipv4-cidr": "value",
                    "--cluster-secondary-range-name": "value",
                    "--cluster-version": "value",
                    "--create-subnetwork": "value",
                    "--disk-size": "value",
                    "--disk-type": [
                      "pd-ssd",
                      "pd-standard"
                    ],
                    "--enable-autorepair": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-autoupgrade": "bool",
                    "--enable-basic-auth": "bool",
                    "--enable-cloud-endpoints": "bool",
                    "--enable-cloud-logging": "bool",
                    "--enable-cloud-monitoring": "bool",
                    "--enable-ip-alias": "bool",
                    "--enable-kubernetes-alpha": "bool",
                    "--enable-legacy-authorization": "bool",
                    "--enable-main-authorized-networks": "bool",
                    "--enable-network-policy": "bool",
                    "--enable-pod-security-policy": "bool",
                    "--enable-stackdriver-kubernetes": "bool",
                    "--enable-tpu": "bool",
                    "--image-type": "value",
                    "--issue-client-certificate": "bool",
                    "--labels": "value",
                    "--local-ssd-count": "value",
                    "--machine-type": "value",
                    "--maintenance-window": "value",
                    "--main-authorized-networks": "value",
                    "--main-ipv4-cidr": "value",
                    "--max-nodes": "value",
                    "--max-nodes-per-pool": "value",
                    "--min-cpu-platform": "value",
                    "--min-nodes": "value",
                    "--network": "value",
                    "--node-labels": "value",
                    "--node-locations": "value",
                    "--node-taints": "value",
                    "--node-version": "value",
                    "--num-nodes": "value",
                    "--password": "value",
                    "--preemptible": "bool",
                    "--private-cluster": "bool",
                    "--region": "value",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--services-ipv4-cidr": "value",
                    "--services-secondary-range-name": "value",
                    "--subnetwork": "value",
                    "--tags": "value",
                    "--tpu-ipv4-cidr": "value",
                    "--username": "value",
                    "--workload-metadata-from-node": [
                      "EXPOSED",
                      "SECURE",
                      "UNSPECIFIED"
                    ],
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "get-credentials": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "value"
                  }
                },
                "resize": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--node-pool": "value",
                    "--region": "value",
                    "--size": "value",
                    "--zone": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--additional-zones": "value",
                    "--async": "bool",
                    "--complete-credential-rotation": "bool",
                    "--complete-ip-rotation": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-basic-auth": "bool",
                    "--enable-legacy-authorization": "bool",
                    "--enable-main-authorized-networks": "bool",
                    "--enable-network-policy": "bool",
                    "--enable-pod-security-policy": "bool",
                    "--generate-password": "bool",
                    "--logging-service": "value",
                    "--maintenance-window": "value",
                    "--main-authorized-networks": "value",
                    "--max-nodes": "value",
                    "--min-nodes": "value",
                    "--monitoring-service": "value",
                    "--node-locations": "value",
                    "--node-pool": "value",
                    "--password": "value",
                    "--region": "value",
                    "--remove-labels": "value",
                    "--set-password": "bool",
                    "--start-credential-rotation": "bool",
                    "--start-ip-rotation": "bool",
                    "--update-addons": "value",
                    "--update-labels": "value",
                    "--username": "value",
                    "--zone": "value"
                  }
                },
                "upgrade": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster-version": "value",
                    "--image-type": "value",
                    "--main": "bool",
                    "--node-pool": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "get-server-config": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "images": {
              "commands": {
                "add-tag": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--force-delete-tags": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--repository": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-tags": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "untag": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "node-pools": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--accelerator": "value",
                    "--cluster": "value",
                    "--disk-size": "value",
                    "--disk-type": [
                      "pd-ssd",
                      "pd-standard"
                    ],
                    "--enable-autorepair": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-autoupgrade": "bool",
                    "--enable-cloud-endpoints": "bool",
                    "--image-type": "value",
                    "--local-ssd-count": "value",
                    "--machine-type": "value",
                    "--max-nodes": "value",
                    "--min-cpu-platform": "value",
                    "--min-nodes": "value",
                    "--node-labels": "value",
                    "--node-taints": "value",
                    "--node-version": "value",
                    "--num-nodes": "value",
                    "--preemptible": "bool",
                    "--region": "value",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--tags": "value",
                    "--workload-metadata-from-node": [
                      "EXPOSED",
                      "SECURE",
                      "UNSPECIFIED"
                    ],
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "value"
                  }
                },
                "rollback": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--cluster": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--enable-autorepair": "bool",
                    "--enable-autoscaling": "bool",
                    "--enable-autoupgrade": "bool",
                    "--max-nodes": "value",
                    "--min-nodes": "value",
                    "--region": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--zone": "value"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            }
          },
          "flags": {}
        },
        "dataflow": {
          "commands": {
            "jobs": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--full": "bool",
                    "--region": "value"
                  }
                },
                "drain": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "export-steps": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--created-after": "value",
                    "--created-before": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--status": [
                      "active",
                      "all",
                      "terminated"
                    ],
                    "--uri": "bool"
                  }
                },
                "run": {
                  "commands": {},
                  "flags": {
                    "--gcs-location": "value",
                    "--max-workers": "value",
                    "--parameters": "value",
                    "--region": "value",
                    "--service-account-email": "value",
                    "--staging-location": "value",
                    "--zone": "value"
                  }
                },
                "show": {
                  "commands": {},
                  "flags": {
                    "--environment": "bool",
                    "--region": "value",
                    "--steps": "bool"
                  }
                }
              },
              "flags": {}
            },
            "logs": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--after": "value",
                    "--before": "value",
                    "--filter": "value",
                    "--importance": [
                      "debug",
                      "detailed",
                      "error",
                      "warning"
                    ],
                    "--limit": "value",
                    "--region": "value"
                  }
                }
              },
              "flags": {}
            },
            "metrics": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--changed-after": "value",
                    "--filter": "value",
                    "--hide-committed": "bool",
                    "--limit": "value",
                    "--region": "value",
                    "--source": [
                      "all",
                      "service",
                      "user"
                    ],
                    "--tentative": "bool",
                    "--transform": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "dataproc": {
          "commands": {
            "clusters": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--bucket": "value",
                    "--expiration-time": "value",
                    "--gce-pd-kms-key": "dynamic",
                    "--gce-pd-kms-key-keyring": "dynamic",
                    "--gce-pd-kms-key-location": "dynamic",
                    "--gce-pd-kms-key-project": "dynamic",
                    "--image": "value",
                    "--image-version": "value",
                    "--initialization-action-timeout": "value",
                    "--initialization-actions": "value",
                    "--labels": "value",
                    "--main-accelerator": "value",
                    "--main-boot-disk-size": "value",
                    "--main-boot-disk-type": "value",
                    "--main-machine-type": "value",
                    "--main-min-cpu-platform": "value",
                    "--max-age": "value",
                    "--max-idle": "value",
                    "--metadata": "value",
                    "--network": "value",
                    "--no-address": "bool",
                    "--num-main-local-ssds": "value",
                    "--num-mains": "value",
                    "--num-preemptible-workers": "value",
                    "--num-worker-local-ssds": "value",
                    "--num-workers": "value",
                    "--preemptible-worker-boot-disk-size": "value",
                    "--preemptible-worker-boot-disk-type": "value",
                    "--properties": "value",
                    "--region": "value",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--single-node": "bool",
                    "--subnet": "value",
                    "--tags": "value",
                    "--worker-accelerator": "value",
                    "--worker-boot-disk-size": "value",
                    "--worker-boot-disk-type": "value",
                    "--worker-machine-type": "value",
                    "--worker-min-cpu-platform": "value",
                    "--zone": "value"
                  }
                },
                "create-from-file": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--file": "value",
                    "--region": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--region": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "diagnose": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--clear-labels": "bool",
                    "--expiration-time": "value",
                    "--graceful-decommission-timeout": "value",
                    "--max-age": "value",
                    "--max-idle": "value",
                    "--no-max-age": "bool",
                    "--no-max-idle": "bool",
                    "--num-preemptible-workers": "value",
                    "--num-workers": "value",
                    "--region": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {
                "--region": "value"
              }
            },
            "jobs": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "kill": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--state-filter": [
                      "active",
                      "inactive"
                    ]
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "submit": {
                  "commands": {
                    "hadoop": {
                      "commands": {},
                      "flags": {
                        "--archives": "value",
                        "--async": "bool",
                        "--bucket": "value",
                        "--class": "value",
                        "--cluster": "value",
                        "--driver-log-levels": "value",
                        "--files": "value",
                        "--jar": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--max-failures-per-hour": "value",
                        "--properties": "value",
                        "--region": "value"
                      }
                    },
                    "hive": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--bucket": "value",
                        "--cluster": "value",
                        "--continue-on-failure": "bool",
                        "--execute": "value",
                        "--file": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--max-failures-per-hour": "value",
                        "--params": "value",
                        "--properties": "value",
                        "--region": "value"
                      }
                    },
                    "pig": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--bucket": "value",
                        "--cluster": "value",
                        "--continue-on-failure": "bool",
                        "--driver-log-levels": "value",
                        "--execute": "value",
                        "--file": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--max-failures-per-hour": "value",
                        "--params": "value",
                        "--properties": "value",
                        "--region": "value"
                      }
                    },
                    "pyspark": {
                      "commands": {},
                      "flags": {
                        "--archives": "value",
                        "--async": "bool",
                        "--bucket": "value",
                        "--cluster": "value",
                        "--driver-log-levels": "value",
                        "--files": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--max-failures-per-hour": "value",
                        "--properties": "value",
                        "--py-files": "value",
                        "--region": "value"
                      }
                    },
                    "spark": {
                      "commands": {},
                      "flags": {
                        "--archives": "value",
                        "--async": "bool",
                        "--bucket": "value",
                        "--class": "value",
                        "--cluster": "value",
                        "--driver-log-levels": "value",
                        "--files": "value",
                        "--jar": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--max-failures-per-hour": "value",
                        "--properties": "value",
                        "--region": "value"
                      }
                    },
                    "spark-sql": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--bucket": "value",
                        "--cluster": "value",
                        "--driver-log-levels": "value",
                        "--execute": "value",
                        "--file": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--max-failures-per-hour": "value",
                        "--params": "value",
                        "--properties": "value",
                        "--region": "value"
                      }
                    }
                  },
                  "flags": {
                    "--async": "bool",
                    "--bucket": "value",
                    "--region": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--region": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                }
              },
              "flags": {
                "--region": "value"
              }
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--cluster": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--state-filter": [
                      "active",
                      "inactive"
                    ]
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                }
              },
              "flags": {
                "--region": "value"
              }
            },
            "workflow-templates": {
              "commands": {
                "add-job": {
                  "commands": {
                    "hadoop": {
                      "commands": {},
                      "flags": {
                        "--archives": "value",
                        "--class": "value",
                        "--driver-log-levels": "value",
                        "--files": "value",
                        "--jar": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--properties": "value",
                        "--region": "value",
                        "--start-after": "value",
                        "--step-id": "value",
                        "--workflow-template": "value"
                      }
                    },
                    "hive": {
                      "commands": {},
                      "flags": {
                        "--continue-on-failure": "bool",
                        "--execute": "value",
                        "--file": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--params": "value",
                        "--properties": "value",
                        "--region": "value",
                        "--start-after": "value",
                        "--step-id": "value",
                        "--workflow-template": "value"
                      }
                    },
                    "pig": {
                      "commands": {},
                      "flags": {
                        "--continue-on-failure": "bool",
                        "--driver-log-levels": "value",
                        "--execute": "value",
                        "--file": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--params": "value",
                        "--properties": "value",
                        "--region": "value",
                        "--start-after": "value",
                        "--step-id": "value",
                        "--workflow-template": "value"
                      }
                    },
                    "pyspark": {
                      "commands": {},
                      "flags": {
                        "--archives": "value",
                        "--driver-log-levels": "value",
                        "--files": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--properties": "value",
                        "--py-files": "value",
                        "--region": "value",
                        "--start-after": "value",
                        "--step-id": "value",
                        "--workflow-template": "value"
                      }
                    },
                    "spark": {
                      "commands": {},
                      "flags": {
                        "--archives": "value",
                        "--class": "value",
                        "--driver-log-levels": "value",
                        "--files": "value",
                        "--jar": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--properties": "value",
                        "--region": "value",
                        "--start-after": "value",
                        "--step-id": "value",
                        "--workflow-template": "value"
                      }
                    },
                    "spark-sql": {
                      "commands": {},
                      "flags": {
                        "--driver-log-levels": "value",
                        "--execute": "value",
                        "--file": "value",
                        "--jars": "value",
                        "--labels": "value",
                        "--params": "value",
                        "--properties": "value",
                        "--region": "value",
                        "--start-after": "value",
                        "--step-id": "value",
                        "--workflow-template": "value"
                      }
                    }
                  },
                  "flags": {
                    "--region": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--labels": "value",
                    "--region": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value"
                  }
                },
                "instantiate": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--parameters": "value",
                    "--region": "dynamic"
                  }
                },
                "instantiate-from-file": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--file": "value",
                    "--region": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "remove-job": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--step-id": "value"
                  }
                },
                "run": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--region": "dynamic"
                  }
                },
                "set-cluster-selector": {
                  "commands": {},
                  "flags": {
                    "--cluster-labels": "value",
                    "--region": "dynamic",
                    "--zone": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "set-managed-cluster": {
                  "commands": {},
                  "flags": {
                    "--bucket": "value",
                    "--cluster-name": "value",
                    "--expiration-time": "value",
                    "--image": "value",
                    "--image-version": "value",
                    "--initialization-action-timeout": "value",
                    "--initialization-actions": "value",
                    "--labels": "value",
                    "--main-accelerator": "value",
                    "--main-boot-disk-size": "value",
                    "--main-boot-disk-type": "value",
                    "--main-machine-type": "value",
                    "--main-min-cpu-platform": "value",
                    "--max-age": "value",
                    "--max-idle": "value",
                    "--metadata": "value",
                    "--network": "value",
                    "--no-address": "bool",
                    "--num-main-local-ssds": "value",
                    "--num-mains": "value",
                    "--num-preemptible-workers": "value",
                    "--num-worker-local-ssds": "value",
                    "--num-workers": "value",
                    "--preemptible-worker-boot-disk-size": "value",
                    "--preemptible-worker-boot-disk-type": "value",
                    "--properties": "value",
                    "--region": "dynamic",
                    "--scopes": "value",
                    "--service-account": "value",
                    "--single-node": "bool",
                    "--subnet": "value",
                    "--tags": "value",
                    "--worker-accelerator": "value",
                    "--worker-boot-disk-size": "value",
                    "--worker-boot-disk-type": "value",
                    "--worker-machine-type": "value",
                    "--worker-min-cpu-platform": "value",
                    "--zone": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "datastore": {
          "commands": {
            "cleanup-indexes": {
              "commands": {},
              "flags": {}
            },
            "create-indexes": {
              "commands": {},
              "flags": {}
            },
            "export": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--kinds": "value",
                "--namespaces": "value",
                "--operation-labels": "value"
              }
            },
            "import": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--kinds": "value",
                "--namespaces": "value",
                "--operation-labels": "value"
              }
            },
            "indexes": {
              "commands": {
                "cleanup": {
                  "commands": {},
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "debug": {
          "commands": {
            "logpoints": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--condition": "value",
                    "--log-level": [
                      "error",
                      "info",
                      "warning"
                    ],
                    "--target": "value",
                    "--wait": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--all-users": "bool",
                    "--include-inactive": "bool",
                    "--location": "value",
                    "--target": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--all-users": "bool",
                    "--filter": "value",
                    "--include-inactive": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--sort-by": "value",
                    "--target": "value"
                  }
                }
              },
              "flags": {
                "--target": "value"
              }
            },
            "snapshots": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--condition": "value",
                    "--expression": "value",
                    "--target": "value",
                    "--wait": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--all-users": "bool",
                    "--include-inactive": "bool",
                    "--location": "value",
                    "--target": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value",
                    "--target": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--all-users": "bool",
                    "--filter": "value",
                    "--include-inactive": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--sort-by": "value",
                    "--target": "value"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {
                    "--all": "bool",
                    "--all-users": "bool",
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--sort-by": "value",
                    "--target": "value",
                    "--timeout": "value"
                  }
                }
              },
              "flags": {
                "--target": "value"
              }
            },
            "source": {
              "commands": {
                "gen-repo-info-file": {
                  "commands": {},
                  "flags": {
                    "--output-directory": "value",
                    "--source-directory": "value"
                  }
                },
                "upload": {
                  "commands": {},
                  "flags": {
                    "--branch": "value",
                    "--source-context-directory": "value"
                  }
                }
              },
              "flags": {}
            },
            "targets": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--include-inactive": "bool",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "deployment-manager": {
          "commands": {
            "deployments": {
              "commands": {
                "cancel-preview": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--fingerprint": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--automatic-rollback-on-error": "bool",
                    "--composite-type": "value",
                    "--config": "value",
                    "--create-policy": [
                      "acquire",
                      "create",
                      "create-or-acquire"
                    ],
                    "--description": "value",
                    "--labels": "value",
                    "--preview": "bool",
                    "--properties": "value",
                    "--template": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--delete-policy": [
                      "abandon",
                      "delete"
                    ]
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "stop": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--fingerprint": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--composite-type": "value",
                    "--config": "value",
                    "--create-policy": [
                      "acquire",
                      "create",
                      "create-or-acquire"
                    ],
                    "--delete-policy": [
                      "abandon",
                      "delete"
                    ],
                    "--description": "value",
                    "--fingerprint": "value",
                    "--manifest-id": "value",
                    "--preview": "bool",
                    "--properties": "value",
                    "--remove-labels": "value",
                    "--template": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "manifests": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "resources": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--deployment": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--simple-list": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {
                "--deployment": "value"
              }
            },
            "type-providers": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--api-options-file": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--descriptor-url": "value",
                    "--labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--api-options-file": "value",
                    "--async": "bool",
                    "--description": "value",
                    "--descriptor-url": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "types": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--labels": "value",
                    "--status": [
                      "DEPRECATED",
                      "EXPERIMENTAL",
                      "SUPPORTED"
                    ],
                    "--template": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--provider": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--provider": "value",
                    "--provider-project": "value",
                    "--sort-by": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--remove-labels": "value",
                    "--status": [
                      "DEPRECATED",
                      "EXPERIMENTAL",
                      "SUPPORTED"
                    ],
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "dns": {
          "commands": {
            "dns-keys": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "dnskeys": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "managed-zones": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--denial-of-existence": [
                      "nsec",
                      "nsec3"
                    ],
                    "--description": "value",
                    "--dns-name": "value",
                    "--dnssec-state": [
                      "off",
                      "on",
                      "transfer"
                    ],
                    "--ksk-algorithm": "value",
                    "--ksk-key-length": "value",
                    "--labels": "value",
                    "--zsk-algorithm": "value",
                    "--zsk-key-length": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--denial-of-existence": [
                      "nsec",
                      "nsec3"
                    ],
                    "--description": "value",
                    "--dnssec-state": [
                      "off",
                      "on",
                      "transfer"
                    ],
                    "--ksk-algorithm": "value",
                    "--ksk-key-length": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value",
                    "--zsk-algorithm": "value",
                    "--zsk-key-length": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value",
                    "--zones": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "project-info": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "record-sets": {
              "commands": {
                "changes": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--zone": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--sort-order": [
                          "ascending",
                          "descending"
                        ],
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic",
                    "--zone-file-format": "bool"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--delete-all-existing": "bool",
                    "--replace-origin-ns": "bool",
                    "--zone": "dynamic",
                    "--zone-file-format": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--name": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--type": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "transaction": {
                  "commands": {
                    "abort": {
                      "commands": {},
                      "flags": {
                        "--transaction-file": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "add": {
                      "commands": {},
                      "flags": {
                        "--name": "value",
                        "--transaction-file": "value",
                        "--ttl": "value",
                        "--type": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--transaction-file": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "execute": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--transaction-file": "value",
                        "--uri": "bool",
                        "--zone": "dynamic"
                      }
                    },
                    "remove": {
                      "commands": {},
                      "flags": {
                        "--name": "value",
                        "--transaction-file": "value",
                        "--ttl": "value",
                        "--type": "value",
                        "--zone": "dynamic"
                      }
                    },
                    "start": {
                      "commands": {},
                      "flags": {
                        "--transaction-file": "value",
                        "--zone": "dynamic"
                      }
                    }
                  },
                  "flags": {
                    "--transaction-file": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "domains": {
          "commands": {
            "list-user-verified": {
              "commands": {},
              "flags": {}
            },
            "verify": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "emulators": {
          "commands": {
            "bigtable": {
              "commands": {
                "env-init": {
                  "commands": {},
                  "flags": {}
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--host-port": "value"
                  }
                }
              },
              "flags": {}
            },
            "datastore": {
              "commands": {
                "env-init": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value",
                    "--legacy": "bool"
                  }
                },
                "env-unset": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value",
                    "--legacy": "bool"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--consistency": "value",
                    "--data-dir": "value",
                    "--host-port": "value",
                    "--legacy": "bool",
                    "--store-on-disk": "bool"
                  }
                }
              },
              "flags": {
                "--data-dir": "value",
                "--legacy": "bool"
              }
            },
            "pubsub": {
              "commands": {
                "env-init": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--data-dir": "value",
                    "--host-port": "value"
                  }
                }
              },
              "flags": {
                "--data-dir": "value"
              }
            }
          },
          "flags": {}
        },
        "endpoints": {
          "commands": {
            "configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--service": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--full": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "services": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "check-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "deploy": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--force": "bool",
                    "--validate-only": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "undelete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "error-reporting": {
          "commands": {
            "events": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "report": {
                  "commands": {},
                  "flags": {
                    "--message": "value",
                    "--message-file": "value",
                    "--service": "value",
                    "--service-version": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "filestore": {
          "commands": {
            "instances": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--file-share": "value",
                    "--labels": "value",
                    "--location": "value",
                    "--network": "value",
                    "--tier": [
                      "premium",
                      "standard"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--location": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--file-share": "value",
                    "--location": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "locations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "firebase": {
          "commands": {
            "test": {
              "commands": {
                "android": {
                  "commands": {
                    "locales": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "models": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "run": {
                      "commands": {},
                      "flags": {
                        "--additional-apks": "value",
                        "--app": "value",
                        "--app-initial-activity": "value",
                        "--app-package": "value",
                        "--async": "bool",
                        "--auto-google-login": "bool",
                        "--device": "value",
                        "--device-ids": "value",
                        "--directories-to-pull": "value",
                        "--environment-variables": "value",
                        "--filter": "value",
                        "--limit": "value",
                        "--locales": "value",
                        "--max-depth": "value",
                        "--max-steps": "value",
                        "--network-profile": "value",
                        "--obb-files": "value",
                        "--orientations": "dynamic",
                        "--os-version-ids": "value",
                        "--other-files": "value",
                        "--page-size": "value",
                        "--performance-metrics": "bool",
                        "--record-video": "bool",
                        "--results-bucket": "value",
                        "--results-dir": "value",
                        "--results-history-name": "value",
                        "--robo-directives": "value",
                        "--robo-script": "value",
                        "--scenario-labels": "value",
                        "--scenario-numbers": "value",
                        "--sort-by": "value",
                        "--test": "value",
                        "--test-package": "value",
                        "--test-runner-class": "value",
                        "--test-targets": "value",
                        "--timeout": "value",
                        "--type": [
                          "game-loop",
                          "instrumentation",
                          "robo"
                        ],
                        "--use-orchestrator": "bool"
                      }
                    },
                    "versions": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "ios": {
                  "commands": {
                    "models": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    },
                    "versions": {
                      "commands": {
                        "describe": {
                          "commands": {},
                          "flags": {}
                        },
                        "list": {
                          "commands": {},
                          "flags": {
                            "--filter": "value",
                            "--limit": "value",
                            "--page-size": "value",
                            "--sort-by": "value"
                          }
                        }
                      },
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "network-profiles": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "functions": {
          "commands": {
            "call": {
              "commands": {},
              "flags": {
                "--data": "value",
                "--region": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "deploy": {
              "commands": {},
              "flags": {
                "--clear-env-vars": "bool",
                "--clear-labels": "bool",
                "--entry-point": "value",
                "--env-vars-file": "value",
                "--memory": "value",
                "--region": "dynamic",
                "--remove-env-vars": "value",
                "--remove-labels": "value",
                "--retry": "bool",
                "--runtime": "value",
                "--set-env-vars": "value",
                "--source": "value",
                "--stage-bucket": "value",
                "--timeout": "value",
                "--trigger-bucket": "value",
                "--trigger-event": "value",
                "--trigger-http": "bool",
                "--trigger-resource": "value",
                "--trigger-topic": "value",
                "--update-env-vars": "value",
                "--update-labels": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "event-types": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "logs": {
              "commands": {
                "read": {
                  "commands": {},
                  "flags": {
                    "--end-time": "value",
                    "--execution-id": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--min-log-level": [
                      "debug",
                      "error",
                      "info"
                    ],
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--start-time": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "iam": {
          "commands": {
            "list-grantable-roles": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--page-size": "value"
              }
            },
            "list-testable-permissions": {
              "commands": {},
              "flags": {
                "--filter": "value"
              }
            },
            "roles": {
              "commands": {
                "copy": {
                  "commands": {},
                  "flags": {
                    "--dest-organization": "value",
                    "--dest-project": "value",
                    "--destination": "value",
                    "--source": "value",
                    "--source-organization": "value",
                    "--source-project": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--file": "value",
                    "--organization": "value",
                    "--permissions": "value",
                    "--stage": "value",
                    "--title": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--organization": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--organization": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--organization": "value",
                    "--show-deleted": "bool",
                    "--sort-by": "value"
                  }
                },
                "undelete": {
                  "commands": {},
                  "flags": {
                    "--organization": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-permissions": "value",
                    "--description": "value",
                    "--file": "value",
                    "--organization": "value",
                    "--permissions": "value",
                    "--remove-permissions": "value",
                    "--stage": "value",
                    "--title": "value"
                  }
                }
              },
              "flags": {}
            },
            "service-accounts": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--display-name": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "keys": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--iam-account": "value",
                        "--key-file-type": [
                          "json",
                          "p12"
                        ]
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--iam-account": "value"
                      }
                    },
                    "get-public-key": {
                      "commands": {},
                      "flags": {
                        "--iam-account": "value",
                        "--output-file": "value",
                        "--type": [
                          "pem",
                          "raw"
                        ]
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--created-before": "value",
                        "--filter": "value",
                        "--iam-account": "value",
                        "--limit": "value",
                        "--managed-by": [
                          "any",
                          "system",
                          "user"
                        ],
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "sign-blob": {
                  "commands": {},
                  "flags": {
                    "--iam-account": "value"
                  }
                },
                "sign-jwt": {
                  "commands": {},
                  "flags": {
                    "--iam-account": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--display-name": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "init": {
          "commands": {},
          "flags": {
            "--console-only": "bool",
            "--skip-diagnostics": "bool"
          }
        },
        "iot": {
          "commands": {
            "devices": {
              "commands": {
                "configs": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "get-value": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--config-data": "value",
                        "--config-file": "value",
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--version-to-update": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--blocked": "bool",
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--public-key": "value",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "credentials": {
                  "commands": {
                    "clear": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--expiration-time": "value",
                        "--path": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--type": [
                          "es256",
                          "es256-pem",
                          "es256-x509-pem",
                          "rs256",
                          "rsa-pem",
                          "rsa-x509-pem"
                        ]
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--expiration-time": "value",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--device-ids": "value",
                    "--device-num-ids": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "states": {
                  "commands": {
                    "list": {
                      "commands": {},
                      "flags": {
                        "--device": "dynamic",
                        "--filter": "value",
                        "--limit": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--blocked": "bool",
                    "--metadata": "value",
                    "--metadata-from-file": "value",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "registries": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--enable-http-config": "bool",
                    "--enable-mqtt-config": "bool",
                    "--event-notification-config": "value",
                    "--event-pubsub-topic": "value",
                    "--public-key-path": "value",
                    "--region": "value",
                    "--state-pubsub-topic": "value"
                  }
                },
                "credentials": {
                  "commands": {
                    "clear": {
                      "commands": {},
                      "flags": {
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "create": {
                      "commands": {},
                      "flags": {
                        "--path": "value",
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--region": "value",
                        "--registry": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--region": "value",
                        "--registry": "dynamic",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--region": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--enable-http-config": "bool",
                    "--enable-mqtt-config": "bool",
                    "--event-notification-config": "value",
                    "--event-pubsub-topic": "value",
                    "--region": "value",
                    "--state-pubsub-topic": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "kms": {
          "commands": {
            "decrypt": {
              "commands": {},
              "flags": {
                "--additional-authenticated-data-file": "value",
                "--ciphertext-file": "value",
                "--key": "dynamic",
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--plaintext-file": "value"
              }
            },
            "encrypt": {
              "commands": {},
              "flags": {
                "--additional-authenticated-data-file": "value",
                "--ciphertext-file": "value",
                "--key": "dynamic",
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--plaintext-file": "value"
              }
            },
            "keyrings": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--location": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "keys": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--labels": "value",
                    "--location": "dynamic",
                    "--next-rotation-time": "value",
                    "--purpose": [
                      "encryption"
                    ],
                    "--rotation-period": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--keyring": "dynamic",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--keyring": "dynamic",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "remove-rotation-schedule": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "set-primary-version": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "set-rotation-schedule": {
                  "commands": {},
                  "flags": {
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--next-rotation-time": "value",
                    "--rotation-period": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--next-rotation-time": "value",
                    "--primary-version": "dynamic",
                    "--remove-labels": "value",
                    "--remove-rotation-schedule": "bool",
                    "--rotation-period": "value",
                    "--update-labels": "value"
                  }
                },
                "versions": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic",
                        "--primary": "bool"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "destroy": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "disable": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "enable": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--limit": "value",
                        "--location": "dynamic",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "restore": {
                      "commands": {},
                      "flags": {
                        "--key": "dynamic",
                        "--keyring": "dynamic",
                        "--location": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "locations": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "logging": {
          "commands": {
            "logs": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "metrics": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--config-from-file": "value",
                    "--description": "value",
                    "--log-filter": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--config-from-file": "value",
                    "--description": "value",
                    "--log-filter": "value"
                  }
                }
              },
              "flags": {}
            },
            "read": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--folder": "value",
                "--freshness": "value",
                "--limit": "value",
                "--order": [
                  "asc",
                  "desc"
                ],
                "--organization": "dynamic"
              }
            },
            "resource-descriptors": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "sinks": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "value",
                    "--folder": "value",
                    "--include-children": "bool",
                    "--log-filter": "value",
                    "--organization": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "value",
                    "--folder": "value",
                    "--organization": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "value",
                    "--folder": "value",
                    "--organization": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "value",
                    "--filter": "value",
                    "--folder": "value",
                    "--limit": "value",
                    "--organization": "dynamic",
                    "--sort-by": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--billing-account": "value",
                    "--folder": "value",
                    "--log-filter": "value",
                    "--organization": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "write": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--folder": "value",
                "--organization": "dynamic",
                "--payload-type": [
                  "json",
                  "text"
                ],
                "--severity": [
                  "ALERT",
                  "CRITICAL",
                  "DEBUG",
                  "DEFAULT",
                  "EMERGENCY",
                  "ERROR",
                  "INFO",
                  "NOTICE",
                  "WARNING"
                ]
              }
            }
          },
          "flags": {}
        },
        "ml": {
          "commands": {
            "language": {
              "commands": {
                "analyze-entities": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "analyze-entity-sentiment": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "analyze-sentiment": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "analyze-syntax": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--encoding-type": [
                      "none",
                      "utf16",
                      "utf32",
                      "utf8"
                    ],
                    "--language": "value"
                  }
                },
                "classify-text": {
                  "commands": {},
                  "flags": {
                    "--content": "value",
                    "--content-file": "value",
                    "--content-type": [
                      "html",
                      "plain-text"
                    ],
                    "--language": "value"
                  }
                }
              },
              "flags": {}
            },
            "speech": {
              "commands": {
                "operations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "wait": {
                      "commands": {},
                      "flags": {}
                    }
                  },
                  "flags": {}
                },
                "recognize": {
                  "commands": {},
                  "flags": {
                    "--encoding": [
                      "amr",
                      "amr-wb",
                      "encoding-unspecified",
                      "flac",
                      "linear16",
                      "mulaw",
                      "ogg-opus",
                      "speex-with-header-byte"
                    ],
                    "--filter-profanity": "bool",
                    "--hints": "value",
                    "--include-word-time-offsets": "bool",
                    "--language-code": "value",
                    "--max-alternatives": "value",
                    "--sample-rate": "value"
                  }
                },
                "recognize-long-running": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--encoding": [
                      "amr",
                      "amr-wb",
                      "encoding-unspecified",
                      "flac",
                      "linear16",
                      "mulaw",
                      "ogg-opus",
                      "speex-with-header-byte"
                    ],
                    "--filter-profanity": "bool",
                    "--hints": "value",
                    "--include-word-time-offsets": "bool",
                    "--language-code": "value",
                    "--max-alternatives": "value",
                    "--sample-rate": "value"
                  }
                }
              },
              "flags": {}
            },
            "video": {
              "commands": {
                "detect-explicit-content": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--output-uri": "value",
                    "--region": [
                      "asia-east1",
                      "europe-west1",
                      "us-east1",
                      "us-west1"
                    ],
                    "--segments": "value"
                  }
                },
                "detect-labels": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--detection-mode": [
                      "frame",
                      "shot",
                      "shot-and-frame"
                    ],
                    "--output-uri": "value",
                    "--region": [
                      "asia-east1",
                      "europe-west1",
                      "us-east1",
                      "us-west1"
                    ],
                    "--segments": "value"
                  }
                },
                "detect-shot-changes": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--output-uri": "value",
                    "--region": [
                      "asia-east1",
                      "europe-west1",
                      "us-east1",
                      "us-west1"
                    ],
                    "--segments": "value"
                  }
                },
                "operations": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "wait": {
                      "commands": {},
                      "flags": {}
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "vision": {
              "commands": {
                "detect-document": {
                  "commands": {},
                  "flags": {
                    "--language-hints": "value",
                    "--model-version": "value"
                  }
                },
                "detect-faces": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-image-properties": {
                  "commands": {},
                  "flags": {
                    "--model-version": "value"
                  }
                },
                "detect-labels": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-landmarks": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-logos": {
                  "commands": {},
                  "flags": {
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "detect-safe-search": {
                  "commands": {},
                  "flags": {
                    "--model-version": "value"
                  }
                },
                "detect-text": {
                  "commands": {},
                  "flags": {
                    "--language-hints": "value",
                    "--model-version": "value"
                  }
                },
                "detect-web": {
                  "commands": {},
                  "flags": {
                    "--include-geo-results": "bool",
                    "--max-results": "value",
                    "--model-version": "value"
                  }
                },
                "suggest-crop": {
                  "commands": {},
                  "flags": {
                    "--aspect-ratios": "value",
                    "--model-version": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "ml-engine": {
          "commands": {
            "jobs": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--summarize": "bool"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "stream-logs": {
                  "commands": {},
                  "flags": {
                    "--allow-multiline-logs": "bool",
                    "--polling-interval": "value",
                    "--task-name": "value"
                  }
                },
                "submit": {
                  "commands": {
                    "prediction": {
                      "commands": {},
                      "flags": {
                        "--batch-size": "value",
                        "--data-format": [
                          "text",
                          "tf-record",
                          "tf-record-gzip"
                        ],
                        "--input-paths": "value",
                        "--labels": "value",
                        "--max-worker-count": "value",
                        "--model": "value",
                        "--model-dir": "value",
                        "--output-path": "value",
                        "--region": "value",
                        "--runtime-version": "value"
                      }
                    },
                    "training": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--config": "value",
                        "--job-dir": "value",
                        "--labels": "value",
                        "--module-name": "value",
                        "--package-path": "value",
                        "--packages": "value",
                        "--python-version": "value",
                        "--region": "dynamic",
                        "--runtime-version": "value",
                        "--scale-tier": [
                          "basic",
                          "basic-gpu",
                          "basic-tpu",
                          "custom",
                          "premium-1",
                          "standard-1"
                        ],
                        "--staging-bucket": "value",
                        "--stream-logs": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "local": {
              "commands": {
                "predict": {
                  "commands": {},
                  "flags": {
                    "--framework": [
                      "scikit-learn",
                      "tensorflow",
                      "xgboost"
                    ],
                    "--json-instances": "value",
                    "--model-dir": "value",
                    "--text-instances": "value"
                  }
                },
                "train": {
                  "commands": {},
                  "flags": {
                    "--distributed": "bool",
                    "--job-dir": "value",
                    "--module-name": "value",
                    "--package-path": "value",
                    "--parameter-server-count": "value",
                    "--start-port": "value",
                    "--worker-count": "value"
                  }
                }
              },
              "flags": {}
            },
            "models": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-logging": "bool",
                    "--labels": "value",
                    "--regions": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "dynamic"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "predict": {
              "commands": {},
              "flags": {
                "--json-instances": "value",
                "--model": "value",
                "--text-instances": "value"
              }
            },
            "versions": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "value",
                    "--description": "value",
                    "--framework": [
                      "scikit-learn",
                      "tensorflow",
                      "xgboost"
                    ],
                    "--labels": "value",
                    "--machine-type": "value",
                    "--model": "value",
                    "--origin": "value",
                    "--python-version": "value",
                    "--runtime-version": "value",
                    "--staging-bucket": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--model": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--model": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--model": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-default": {
                  "commands": {},
                  "flags": {
                    "--model": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--clear-labels": "bool",
                    "--description": "value",
                    "--model": "value",
                    "--remove-labels": "value",
                    "--update-labels": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "organizations": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "projects": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "move": {
              "commands": {},
              "flags": {
                "--folder": "value",
                "--organization": "value"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            },
            "undelete": {
              "commands": {},
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--name": "value"
              }
            }
          },
          "flags": {}
        },
        "pubsub": {
          "commands": {
            "subscriptions": {
              "commands": {
                "ack": {
                  "commands": {},
                  "flags": {
                    "--ack-ids": "value"
                  }
                },
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--labels": "value",
                    "--push-endpoint": "value",
                    "--topic": "value",
                    "--topic-project": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "modify-ack-deadline": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--ack-ids": "value"
                  }
                },
                "modify-message-ack-deadline": {
                  "commands": {},
                  "flags": {
                    "--ack-deadline": "value",
                    "--ack-ids": "value"
                  }
                },
                "modify-push-config": {
                  "commands": {},
                  "flags": {
                    "--push-endpoint": "value"
                  }
                },
                "pull": {
                  "commands": {},
                  "flags": {
                    "--auto-ack": "bool",
                    "--filter": "value",
                    "--limit": "value",
                    "--max-messages": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--wait": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "topics": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--labels": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "list-subscriptions": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "publish": {
                  "commands": {},
                  "flags": {
                    "--attribute": "value",
                    "--message": "value"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "redis": {
          "commands": {
            "instances": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--alternative-zone": "value",
                    "--async": "bool",
                    "--display-name": "value",
                    "--labels": "value",
                    "--network": "value",
                    "--redis-config": "value",
                    "--redis-version": [
                      "redis_3_2"
                    ],
                    "--region": "dynamic",
                    "--reserved-ip-range": "value",
                    "--size": "value",
                    "--tier": [
                      "basic",
                      "standard"
                    ],
                    "--zone": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--clear-labels": "bool",
                    "--display-name": "value",
                    "--region": "dynamic",
                    "--remove-labels": "value",
                    "--remove-redis-config": "value",
                    "--size": "value",
                    "--update-labels": "value",
                    "--update-redis-config": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "regions": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "zones": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "resource-manager": {
          "commands": {
            "folders": {
              "commands": {
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "org-policies": {
              "commands": {
                "allow": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "deny": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--effective": "bool",
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "disable-enforce": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "enable-enforce": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--folder": "value",
                    "--limit": "value",
                    "--organization": "value",
                    "--page-size": "value",
                    "--show-unset": "bool",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-policy": {
                  "commands": {},
                  "flags": {
                    "--folder": "value",
                    "--organization": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "runtime-config": {
          "commands": {
            "configs": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--description": "value"
                  }
                },
                "variables": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value"
                      }
                    },
                    "get-value": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value",
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool",
                        "--values": "bool"
                      }
                    },
                    "set": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value",
                        "--fail-if-absent": "bool",
                        "--fail-if-present": "bool",
                        "--is-text": "bool"
                      }
                    },
                    "unset": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value",
                        "--fail-if-absent": "bool",
                        "--recursive": "bool"
                      }
                    },
                    "watch": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value",
                        "--max-wait": "value",
                        "--newer-than": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "waiters": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--config-name": "value",
                        "--failure-cardinality-number": "value",
                        "--failure-cardinality-path": "value",
                        "--success-cardinality-number": "value",
                        "--success-cardinality-path": "value",
                        "--timeout": "value"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value",
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "wait": {
                      "commands": {},
                      "flags": {
                        "--config-name": "value",
                        "--max-wait": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "services": {
          "commands": {
            "disable": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "enable": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--available": "bool",
                "--enabled": "bool",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--full": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--service": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "source": {
          "commands": {
            "project-configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-topic": "value",
                    "--disable-pushblock": "bool",
                    "--enable-pushblock": "bool",
                    "--message-format": [
                      "json",
                      "protobuf"
                    ],
                    "--remove-topic": "value",
                    "--service-account": "value",
                    "--topic-project": "value",
                    "--update-topic": "value"
                  }
                }
              },
              "flags": {}
            },
            "repos": {
              "commands": {
                "clone": {
                  "commands": {},
                  "flags": {
                    "--dry-run": "bool",
                    "--use-full-gcloud-path": "bool"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--force": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-topic": "value",
                    "--message-format": [
                      "json",
                      "protobuf"
                    ],
                    "--remove-topic": "value",
                    "--service-account": "value",
                    "--topic-project": "value",
                    "--update-topic": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "spanner": {
          "commands": {
            "databases": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--instance": "value",
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--ddl": "value",
                    "--instance": "value"
                  }
                },
                "ddl": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--instance": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--ddl": "value",
                        "--instance": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--instance": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "value"
                  }
                },
                "execute-sql": {
                  "commands": {},
                  "flags": {
                    "--instance": "value",
                    "--query-mode": [
                      "NORMAL",
                      "PLAN",
                      "PROFILE"
                    ],
                    "--sql": "value"
                  }
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--instance": "value",
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "sessions": {
                  "commands": {
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--database": "value",
                        "--instance": "value"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--database": "value",
                        "--filter": "value",
                        "--instance": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--server-filter": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--instance": "value"
                  }
                }
              },
              "flags": {}
            },
            "instance-configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "add-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "dynamic",
                    "--description": "value",
                    "--nodes": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {}
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove-iam-policy-binding": {
                  "commands": {},
                  "flags": {
                    "--member": "value",
                    "--role": "value"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--nodes": "value"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "cancel": {
                  "commands": {},
                  "flags": {
                    "--database": "dynamic",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--database": "dynamic",
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--database": "dynamic",
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "rows": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {
                    "--database": "value",
                    "--instance": "value",
                    "--keys": "value",
                    "--table": "value"
                  }
                },
                "insert": {
                  "commands": {},
                  "flags": {
                    "--data": "value",
                    "--database": "value",
                    "--instance": "value",
                    "--table": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--data": "value",
                    "--database": "value",
                    "--instance": "value",
                    "--table": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "sql": {
          "commands": {
            "backups": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--description": "value",
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "restore": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--backup-instance": "dynamic",
                    "--restore-instance": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "connect": {
              "commands": {},
              "flags": {
                "--database": "value",
                "--user": "value"
              }
            },
            "databases": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--charset": "value",
                    "--collation": "value",
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "patch": {
                  "commands": {},
                  "flags": {
                    "--charset": "value",
                    "--collation": "value",
                    "--diff": "bool",
                    "--instance": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "export": {
              "commands": {
                "csv": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--query": "value"
                  }
                },
                "sql": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--table": "value"
                  }
                }
              },
              "flags": {}
            },
            "flags": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--database-version": [
                      "MYSQL_5_5",
                      "MYSQL_5_6",
                      "MYSQL_5_7",
                      "POSTGRES_9_6"
                    ],
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "import": {
              "commands": {
                "csv": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--columns": "value",
                    "--database": "value",
                    "--table": "value",
                    "--user": "value"
                  }
                },
                "sql": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--user": "value"
                  }
                }
              },
              "flags": {}
            },
            "instances": {
              "commands": {
                "clone": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--bin-log-file-name": "value",
                    "--bin-log-position": "value"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--activation-policy": [
                      "always",
                      "never",
                      "on-demand"
                    ],
                    "--assign-ip": "bool",
                    "--async": "bool",
                    "--authorized-gae-apps": "value",
                    "--authorized-networks": "value",
                    "--availability-type": [
                      "regional",
                      "zonal"
                    ],
                    "--backup": "bool",
                    "--backup-start-time": "value",
                    "--client-certificate-path": "value",
                    "--client-key-path": "value",
                    "--cpu": "value",
                    "--database-flags": "value",
                    "--database-version": [
                      "MYSQL_5_5",
                      "MYSQL_5_6",
                      "MYSQL_5_7",
                      "POSTGRES_9_6"
                    ],
                    "--enable-bin-log": "bool",
                    "--failover-replica-name": "value",
                    "--follow-gae-app": "value",
                    "--gce-zone": "value",
                    "--labels": "value",
                    "--maintenance-release-channel": [
                      "preview",
                      "production"
                    ],
                    "--maintenance-window-day": [
                      "FRI",
                      "MON",
                      "SAT",
                      "SUN",
                      "THU",
                      "TUE",
                      "WED"
                    ],
                    "--maintenance-window-hour": "value",
                    "--main-ca-certificate-path": "value",
                    "--main-dump-file-path": "value",
                    "--main-instance-name": "value",
                    "--main-password": "value",
                    "--main-username": "value",
                    "--memory": "value",
                    "--pricing-plan": [
                      "PACKAGE",
                      "PER_USE"
                    ],
                    "--prompt-for-main-password": "bool",
                    "--region": "value",
                    "--replica-type": [
                      "FAILOVER",
                      "READ"
                    ],
                    "--replication": [
                      "asynchronous",
                      "synchronous"
                    ],
                    "--require-ssl": "bool",
                    "--source-ip-address": "value",
                    "--source-port": "value",
                    "--storage-auto-increase": "bool",
                    "--storage-auto-increase-limit": "value",
                    "--storage-size": "value",
                    "--storage-type": [
                      "HDD",
                      "SSD"
                    ],
                    "--tier": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "export": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value",
                    "--table": "value"
                  }
                },
                "failover": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "import": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--database": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "patch": {
                  "commands": {},
                  "flags": {
                    "--activation-policy": [
                      "always",
                      "never",
                      "on-demand"
                    ],
                    "--assign-ip": "bool",
                    "--async": "bool",
                    "--authorized-gae-apps": "value",
                    "--authorized-networks": "value",
                    "--availability-type": [
                      "regional",
                      "zonal"
                    ],
                    "--backup-start-time": "value",
                    "--clear-authorized-networks": "bool",
                    "--clear-database-flags": "bool",
                    "--clear-gae-apps": "bool",
                    "--clear-labels": "bool",
                    "--cpu": "value",
                    "--database-flags": "value",
                    "--diff": "bool",
                    "--enable-bin-log": "bool",
                    "--enable-database-replication": "bool",
                    "--follow-gae-app": "value",
                    "--gce-zone": "value",
                    "--maintenance-release-channel": [
                      "preview",
                      "production"
                    ],
                    "--maintenance-window-any": "bool",
                    "--maintenance-window-day": [
                      "FRI",
                      "MON",
                      "SAT",
                      "SUN",
                      "THU",
                      "TUE",
                      "WED"
                    ],
                    "--maintenance-window-hour": "value",
                    "--memory": "value",
                    "--no-backup": "bool",
                    "--pricing-plan": [
                      "PACKAGE",
                      "PER_USE"
                    ],
                    "--remove-labels": "value",
                    "--replication": [
                      "asynchronous",
                      "synchronous"
                    ],
                    "--require-ssl": "bool",
                    "--storage-auto-increase": "bool",
                    "--storage-auto-increase-limit": "value",
                    "--storage-size": "value",
                    "--tier": "value",
                    "--update-labels": "value"
                  }
                },
                "promote-replica": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "reset-ssl-config": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "restart": {
                  "commands": {},
                  "flags": {
                    "--async": "bool"
                  }
                },
                "restore-backup": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--backup-id": "value",
                    "--backup-instance": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "ssl": {
              "commands": {
                "client-certs": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--instance": "dynamic"
                      }
                    },
                    "delete": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    },
                    "describe": {
                      "commands": {},
                      "flags": {
                        "--instance": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--instance": "dynamic",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    }
                  },
                  "flags": {}
                },
                "server-ca-certs": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--instance": "dynamic",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value",
                        "--uri": "bool"
                      }
                    },
                    "rollback": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    },
                    "rotate": {
                      "commands": {},
                      "flags": {
                        "--async": "bool",
                        "--instance": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "ssl-certs": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "tiers": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "users": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--instance": "dynamic",
                    "--password": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-password": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--host": "value",
                    "--instance": "dynamic",
                    "--password": "value",
                    "--prompt-for-password": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "tasks": {
          "commands": {
            "queues": {
              "commands": {
                "get-iam-policy": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "set-iam-policy": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "builds": {
      "commands": {
        "cancel": {
          "commands": {},
          "flags": {}
        },
        "describe": {
          "commands": {},
          "flags": {}
        },
        "list": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--limit": "value",
            "--ongoing": "bool",
            "--page-size": "value",
            "--sort-by": "value",
            "--uri": "bool"
          }
        },
        "log": {
          "commands": {},
          "flags": {
            "--stream": "bool"
          }
        },
        "submit": {
          "commands": {},
          "flags": {
            "--async": "bool",
            "--config": "value",
            "--disk-size": "value",
            "--gcs-log-dir": "value",
            "--gcs-source-staging-dir": "value",
            "--machine-type": [
              "n1-highcpu-32",
              "n1-highcpu-8"
            ],
            "--no-source": "bool",
            "--substitutions": "value",
            "--tag": "value",
            "--timeout": "value"
          }
        }
      },
      "flags": {}
    },
    "components": {
      "commands": {
        "install": {
          "commands": {},
          "flags": {}
        },
        "list": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--limit": "value",
            "--only-local-state": "bool",
            "--show-versions": "bool",
            "--sort-by": "value"
          }
        },
        "reinstall": {
          "commands": {},
          "flags": {}
        },
        "remove": {
          "commands": {},
          "flags": {}
        },
        "repositories": {
          "commands": {
            "add": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            },
            "remove": {
              "commands": {},
              "flags": {
                "--all": "bool"
              }
            }
          },
          "flags": {}
        },
        "restore": {
          "commands": {},
          "flags": {}
        },
        "update": {
          "commands": {},
          "flags": {}
        }
      },
      "flags": {}
    },
    "compute": {
      "commands": {
        "accelerator-types": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "addresses": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--addresses": "value",
                "--description": "value",
                "--global": "bool",
                "--ip-version": [
                  "IPV4",
                  "IPV6"
                ],
                "--region": "dynamic",
                "--subnet": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--global": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "backend-buckets": {
          "commands": {
            "add-signed-url-key": {
              "commands": {},
              "flags": {
                "--key-file": "value",
                "--key-name": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--enable-cdn": "bool",
                "--gcs-bucket-name": "dynamic",
                "--signed-url-cache-max-age": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "delete-signed-url-key": {
              "commands": {},
              "flags": {
                "--key-name": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--enable-cdn": "bool",
                "--gcs-bucket-name": "dynamic",
                "--signed-url-cache-max-age": "value"
              }
            }
          },
          "flags": {}
        },
        "backend-services": {
          "commands": {
            "add-backend": {
              "commands": {},
              "flags": {
                "--balancing-mode": [
                  "CONNECTION",
                  "RATE",
                  "UTILIZATION"
                ],
                "--capacity-scaler": "value",
                "--description": "value",
                "--global": "bool",
                "--instance-group": "dynamic",
                "--instance-group-region": "dynamic",
                "--instance-group-zone": "dynamic",
                "--max-connections": "value",
                "--max-connections-per-instance": "value",
                "--max-rate": "value",
                "--max-rate-per-instance": "value",
                "--max-utilization": "value",
                "--region": "dynamic"
              }
            },
            "add-signed-url-key": {
              "commands": {},
              "flags": {
                "--key-file": "value",
                "--key-name": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--affinity-cookie-ttl": "value",
                "--cache-key-include-host": "bool",
                "--cache-key-include-protocol": "bool",
                "--cache-key-include-query-string": "bool",
                "--cache-key-query-string-blacklist": "value",
                "--cache-key-query-string-whitelist": "value",
                "--connection-draining-timeout": "value",
                "--description": "value",
                "--enable-cdn": "bool",
                "--global": "bool",
                "--health-checks": "dynamic",
                "--http-health-checks": "dynamic",
                "--https-health-checks": "dynamic",
                "--iap": "value",
                "--load-balancing-scheme": [
                  "EXTERNAL",
                  "INTERNAL"
                ],
                "--port-name": "value",
                "--protocol": [
                  "HTTP",
                  "HTTPS",
                  "SSL",
                  "TCP",
                  "UDP"
                ],
                "--region": "dynamic",
                "--session-affinity": [
                  "CLIENT_IP",
                  "GENERATED_COOKIE",
                  "NONE"
                ],
                "--signed-url-cache-max-age": "value",
                "--timeout": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "delete-signed-url-key": {
              "commands": {},
              "flags": {
                "--key-name": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "edit": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "get-health": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--global": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--region": "dynamic",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--global": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-backend": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--instance-group": "dynamic",
                "--instance-group-region": "dynamic",
                "--instance-group-zone": "dynamic",
                "--region": "dynamic"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--affinity-cookie-ttl": "value",
                "--cache-key-include-host": "bool",
                "--cache-key-include-protocol": "bool",
                "--cache-key-include-query-string": "bool",
                "--cache-key-query-string-blacklist": "value",
                "--cache-key-query-string-whitelist": "value",
                "--connection-draining-timeout": "value",
                "--description": "value",
                "--enable-cdn": "bool",
                "--global": "bool",
                "--health-checks": "dynamic",
                "--http-health-checks": "dynamic",
                "--https-health-checks": "dynamic",
                "--iap": "value",
                "--port-name": "value",
                "--protocol": [
                  "HTTP",
                  "HTTPS",
                  "SSL",
                  "TCP",
                  "UDP"
                ],
                "--region": "dynamic",
                "--session-affinity": [
                  "CLIENT_IP",
                  "CLIENT_IP_PORT_PROTO",
                  "CLIENT_IP_PROTO",
                  "GENERATED_COOKIE",
                  "NONE"
                ],
                "--signed-url-cache-max-age": "value",
                "--timeout": "value"
              }
            },
            "update-backend": {
              "commands": {},
              "flags": {
                "--balancing-mode": [
                  "CONNECTION",
                  "RATE",
                  "UTILIZATION"
                ],
                "--capacity-scaler": "value",
                "--description": "value",
                "--global": "bool",
                "--instance-group": "dynamic",
                "--instance-group-region": "dynamic",
                "--instance-group-zone": "dynamic",
                "--max-connections": "value",
                "--max-connections-per-instance": "value",
                "--max-rate": "value",
                "--max-rate-per-instance": "value",
                "--max-utilization": "value",
                "--region": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "commitments": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--plan": [
                  "12-month",
                  "36-month"
                ],
                "--region": "dynamic",
                "--resources": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "config-ssh": {
          "commands": {},
          "flags": {
            "--dry-run": "bool",
            "--force-key-file-overwrite": "bool",
            "--remove": "bool",
            "--ssh-config-file": "value",
            "--ssh-key-file": "value"
          }
        },
        "connect-to-serial-port": {
          "commands": {},
          "flags": {
            "--dry-run": "bool",
            "--extra-args": "value",
            "--force-key-file-overwrite": "bool",
            "--port": "value",
            "--ssh-key-file": "value",
            "--zone": "dynamic"
          }
        },
        "copy-files": {
          "commands": {},
          "flags": {
            "--dry-run": "bool",
            "--force-key-file-overwrite": "bool",
            "--plain": "bool",
            "--ssh-key-file": "value",
            "--strict-host-key-checking": [
              "ask",
              "no",
              "yes"
            ],
            "--zone": "value"
          }
        },
        "disk-types": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "disks": {
          "commands": {
            "add-labels": {
              "commands": {},
              "flags": {
                "--labels": "value",
                "--zone": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--csek-key-file": "value",
                "--description": "value",
                "--guest-os-features": "value",
                "--image": "value",
                "--image-family": "value",
                "--image-project": "value",
                "--labels": "value",
                "--licenses": "value",
                "--require-csek-key-create": "bool",
                "--size": "value",
                "--source-snapshot": "dynamic",
                "--type": "dynamic",
                "--zone": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "dynamic"
              }
            },
            "move": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--destination-zone": "dynamic",
                "--zone": "dynamic"
              }
            },
            "remove-labels": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--labels": "value",
                "--zone": "dynamic"
              }
            },
            "resize": {
              "commands": {},
              "flags": {
                "--size": "value",
                "--zone": "dynamic"
              }
            },
            "snapshot": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--csek-key-file": "value",
                "--description": "value",
                "--guest-flush": "bool",
                "--snapshot-names": "value",
                "--zone": "dynamic"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--remove-labels": "value",
                "--update-labels": "value",
                "--zone": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "firewall-rules": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--action": [
                  "ALLOW",
                  "DENY"
                ],
                "--allow": "value",
                "--description": "value",
                "--destination-ranges": "value",
                "--direction": [
                  "EGRESS",
                  "IN",
                  "INGRESS",
                  "OUT"
                ],
                "--network": "value",
                "--priority": "value",
                "--rules": "value",
                "--source-ranges": "value",
                "--source-service-accounts": "value",
                "--source-tags": "value",
                "--target-service-accounts": "value",
                "--target-tags": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--allow": "value",
                "--description": "value",
                "--destination-ranges": "value",
                "--priority": "value",
                "--rules": "value",
                "--source-ranges": "value",
                "--source-service-accounts": "value",
                "--source-tags": "value",
                "--target-service-accounts": "value",
                "--target-tags": "value"
              }
            }
          },
          "flags": {}
        },
        "forwarding-rules": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--address": "dynamic",
                "--address-region": "dynamic",
                "--backend-service": "value",
                "--backend-service-region": "dynamic",
                "--description": "value",
                "--global": "bool",
                "--global-address": "bool",
                "--global-backend-service": "bool",
                "--ip-protocol": [
                  "AH",
                  "ESP",
                  "ICMP",
                  "SCTP",
                  "TCP",
                  "UDP"
                ],
                "--ip-version": [
                  "IPV4",
                  "IPV6"
                ],
                "--load-balancing-scheme": [
                  "EXTERNAL",
                  "INTERNAL"
                ],
                "--network": "value",
                "--port-range": "value",
                "--ports": "value",
                "--region": "dynamic",
                "--subnet": "value",
                "--subnet-region": "dynamic",
                "--target-http-proxy": "value",
                "--target-https-proxy": "value",
                "--target-instance": "value",
                "--target-instance-zone": "dynamic",
                "--target-pool": "value",
                "--target-pool-region": "dynamic",
                "--target-ssl-proxy": "value",
                "--target-tcp-proxy": "value",
                "--target-vpn-gateway": "value",
                "--target-vpn-gateway-region": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--global": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "set-target": {
              "commands": {},
              "flags": {
                "--backend-service": "value",
                "--backend-service-region": "dynamic",
                "--global": "bool",
                "--global-backend-service": "bool",
                "--load-balancing-scheme": [
                  "EXTERNAL",
                  "INTERNAL"
                ],
                "--network": "value",
                "--region": "dynamic",
                "--subnet": "value",
                "--subnet-region": "dynamic",
                "--target-http-proxy": "value",
                "--target-https-proxy": "value",
                "--target-instance": "value",
                "--target-instance-zone": "dynamic",
                "--target-pool": "value",
                "--target-pool-region": "dynamic",
                "--target-ssl-proxy": "value",
                "--target-tcp-proxy": "value",
                "--target-vpn-gateway": "value",
                "--target-vpn-gateway-region": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "health-checks": {
          "commands": {
            "create": {
              "commands": {
                "http": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "https": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "ssl": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request": "value",
                    "--response": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "tcp": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request": "value",
                    "--response": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                }
              },
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--protocol": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {
                "http": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "https": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--host": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request-path": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "ssl": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request": "value",
                    "--response": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                },
                "tcp": {
                  "commands": {},
                  "flags": {
                    "--check-interval": "value",
                    "--description": "value",
                    "--healthy-threshold": "value",
                    "--port": "value",
                    "--port-name": "value",
                    "--proxy-header": [
                      "NONE",
                      "PROXY_V1"
                    ],
                    "--request": "value",
                    "--response": "value",
                    "--timeout": "value",
                    "--unhealthy-threshold": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "http-health-checks": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--check-interval": "value",
                "--description": "value",
                "--healthy-threshold": "value",
                "--host": "value",
                "--port": "value",
                "--request-path": "value",
                "--timeout": "value",
                "--unhealthy-threshold": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--check-interval": "value",
                "--description": "value",
                "--healthy-threshold": "value",
                "--host": "value",
                "--port": "value",
                "--request-path": "value",
                "--timeout": "value",
                "--unhealthy-threshold": "value"
              }
            }
          },
          "flags": {}
        },
        "https-health-checks": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--check-interval": "value",
                "--description": "value",
                "--healthy-threshold": "value",
                "--host": "value",
                "--port": "value",
                "--request-path": "value",
                "--timeout": "value",
                "--unhealthy-threshold": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--check-interval": "value",
                "--description": "value",
                "--healthy-threshold": "value",
                "--host": "value",
                "--port": "value",
                "--request-path": "value",
                "--timeout": "value",
                "--unhealthy-threshold": "value"
              }
            }
          },
          "flags": {}
        },
        "images": {
          "commands": {
            "add-labels": {
              "commands": {},
              "flags": {
                "--labels": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--csek-key-file": "value",
                "--description": "value",
                "--family": "value",
                "--force": "bool",
                "--guest-os-features": "value",
                "--labels": "value",
                "--licenses": "value",
                "--require-csek-key-create": "bool",
                "--source-disk": "dynamic",
                "--source-disk-zone": "dynamic",
                "--source-image": "value",
                "--source-image-family": "value",
                "--source-image-project": "value",
                "--source-snapshot": "dynamic",
                "--source-uri": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "deprecate": {
              "commands": {},
              "flags": {
                "--delete-in": "value",
                "--delete-on": "value",
                "--obsolete-in": "value",
                "--obsolete-on": "value",
                "--replacement": "dynamic",
                "--state": [
                  "ACTIVE",
                  "DELETED",
                  "DEPRECATED",
                  "OBSOLETE"
                ]
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "describe-from-family": {
              "commands": {},
              "flags": {}
            },
            "export": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--destination-uri": "value",
                "--export-format": "value",
                "--image": "value",
                "--image-family": "value",
                "--image-project": "value",
                "--log-location": "value",
                "--network": "value",
                "--timeout": "value"
              }
            },
            "import": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--data-disk": "bool",
                "--log-location": "value",
                "--os": [
                  "centos-6",
                  "centos-7",
                  "debian-8",
                  "debian-9",
                  "rhel-6",
                  "rhel-6-byol",
                  "rhel-7",
                  "rhel-7-byol",
                  "ubuntu-1404",
                  "ubuntu-1604",
                  "windows-2008r2",
                  "windows-2012r2",
                  "windows-2016"
                ],
                "--source-file": "value",
                "--source-image": "dynamic",
                "--timeout": "value",
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--preview-images": "bool",
                "--regexp": "value",
                "--show-deprecated": "bool",
                "--sort-by": "value",
                "--standard-images": "bool",
                "--uri": "bool"
              }
            },
            "remove-labels": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--labels": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        },
        "instance-groups": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic",
                "--zone": "dynamic"
              }
            },
            "get-named-ports": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "dynamic",
                "--sort-by": "value",
                "--uri": "bool",
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--only-managed": "bool",
                "--only-unmanaged": "bool",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "value"
              }
            },
            "list-instances": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--region": "dynamic",
                "--sort-by": "value",
                "--uri": "bool",
                "--zone": "dynamic"
              }
            },
            "managed": {
              "commands": {
                "abandon-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--base-instance-name": "value",
                    "--description": "value",
                    "--region": "dynamic",
                    "--size": "value",
                    "--target-pool": "value",
                    "--template": "value",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "delete-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "get-named-ports": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "value"
                  }
                },
                "list-instances": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--region": "dynamic",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "recreate-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "resize": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--size": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-autoscaling": {
                  "commands": {},
                  "flags": {
                    "--cool-down-period": "value",
                    "--custom-metric-utilization": "value",
                    "--description": "value",
                    "--max-num-replicas": "value",
                    "--min-num-replicas": "value",
                    "--region": "dynamic",
                    "--scale-based-on-cpu": "bool",
                    "--scale-based-on-load-balancing": "bool",
                    "--target-cpu-utilization": "value",
                    "--target-load-balancing-utilization": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-instance-template": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--template": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-named-ports": {
                  "commands": {},
                  "flags": {
                    "--named-ports": "value",
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "set-target-pools": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--target-pools": "value",
                    "--zone": "dynamic"
                  }
                },
                "stop-autoscaling": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--zone": "dynamic"
                  }
                },
                "wait-until-stable": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic",
                    "--timeout": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "set-named-ports": {
              "commands": {},
              "flags": {
                "--named-ports": "value",
                "--region": "dynamic",
                "--zone": "dynamic"
              }
            },
            "unmanaged": {
              "commands": {
                "add-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "value",
                    "--zone": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--zone": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "get-named-ports": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zones": "dynamic"
                  }
                },
                "list-instances": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--sort-by": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "remove-instances": {
                  "commands": {},
                  "flags": {
                    "--instances": "value",
                    "--zone": "dynamic"
                  }
                },
                "set-named-ports": {
                  "commands": {},
                  "flags": {
                    "--named-ports": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "instance-templates": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--accelerator": "value",
                "--address": "value",
                "--boot-disk-auto-delete": "bool",
                "--boot-disk-device-name": "value",
                "--boot-disk-size": "value",
                "--boot-disk-type": "value",
                "--can-ip-forward": "bool",
                "--configure-disk": "value",
                "--create-disk": "value",
                "--custom-cpu": "value",
                "--custom-extensions": "bool",
                "--custom-memory": "value",
                "--description": "value",
                "--disk": "value",
                "--image": "value",
                "--image-family": "value",
                "--image-project": "value",
                "--labels": "value",
                "--local-ssd": "value",
                "--machine-type": "dynamic",
                "--maintenance-policy": [
                  "MIGRATE",
                  "TERMINATE"
                ],
                "--metadata": "value",
                "--metadata-from-file": "value",
                "--min-cpu-platform": "value",
                "--network": "value",
                "--network-interface": "value",
                "--no-address": "bool",
                "--no-scopes": "bool",
                "--no-service-account": "bool",
                "--preemptible": "bool",
                "--region": "dynamic",
                "--restart-on-failure": "bool",
                "--scopes": "value",
                "--service-account": "value",
                "--source-instance": "dynamic",
                "--source-instance-zone": "dynamic",
                "--subnet": "value",
                "--tags": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "instances": {
          "commands": {
            "add-access-config": {
              "commands": {},
              "flags": {
                "--access-config-name": "value",
                "--address": "value",
                "--network-interface": "value",
                "--no-public-ptr": "bool",
                "--no-public-ptr-domain": "bool",
                "--public-ptr": "bool",
                "--public-ptr-domain": "value",
                "--zone": "dynamic"
              }
            },
            "add-labels": {
              "commands": {},
              "flags": {
                "--labels": "value",
                "--zone": "dynamic"
              }
            },
            "add-metadata": {
              "commands": {},
              "flags": {
                "--metadata": "value",
                "--metadata-from-file": "value",
                "--zone": "dynamic"
              }
            },
            "add-tags": {
              "commands": {},
              "flags": {
                "--tags": "value",
                "--zone": "dynamic"
              }
            },
            "attach-disk": {
              "commands": {},
              "flags": {
                "--csek-key-file": "value",
                "--device-name": "value",
                "--disk": "value",
                "--mode": [
                  "ro",
                  "rw"
                ],
                "--zone": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--accelerator": "value",
                "--address": "value",
                "--async": "bool",
                "--boot-disk-auto-delete": "bool",
                "--boot-disk-device-name": "value",
                "--boot-disk-size": "value",
                "--boot-disk-type": "value",
                "--can-ip-forward": "bool",
                "--create-disk": "value",
                "--csek-key-file": "value",
                "--custom-cpu": "value",
                "--custom-extensions": "bool",
                "--custom-memory": "value",
                "--deletion-protection": "bool",
                "--description": "value",
                "--disk": "value",
                "--image": "value",
                "--image-family": "value",
                "--image-project": "value",
                "--labels": "value",
                "--local-ssd": "value",
                "--machine-type": "dynamic",
                "--maintenance-policy": [
                  "MIGRATE",
                  "TERMINATE"
                ],
                "--metadata": "value",
                "--metadata-from-file": "value",
                "--min-cpu-platform": "value",
                "--network": "value",
                "--network-interface": "value",
                "--no-address": "bool",
                "--no-public-ptr": "bool",
                "--no-public-ptr-domain": "bool",
                "--no-scopes": "bool",
                "--no-service-account": "bool",
                "--preemptible": "bool",
                "--private-network-ip": "value",
                "--public-ptr": "bool",
                "--public-ptr-domain": "value",
                "--require-csek-key-create": "bool",
                "--restart-on-failure": "bool",
                "--scopes": "value",
                "--service-account": "value",
                "--source-instance-template": "dynamic",
                "--subnet": "value",
                "--tags": "value",
                "--zone": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--delete-disks": [
                  "all",
                  "boot",
                  "data"
                ],
                "--keep-disks": [
                  "all",
                  "boot",
                  "data"
                ],
                "--zone": "dynamic"
              }
            },
            "delete-access-config": {
              "commands": {},
              "flags": {
                "--access-config-name": "value",
                "--network-interface": "value",
                "--zone": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "detach-disk": {
              "commands": {},
              "flags": {
                "--device-name": "value",
                "--disk": "value",
                "--zone": "dynamic"
              }
            },
            "get-serial-port-output": {
              "commands": {},
              "flags": {
                "--port": "value",
                "--start": "value",
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "dynamic"
              }
            },
            "move": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--destination-zone": "dynamic",
                "--zone": "dynamic"
              }
            },
            "network-interfaces": {
              "commands": {
                "update": {
                  "commands": {},
                  "flags": {
                    "--aliases": "value",
                    "--network-interface": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "remove-labels": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--labels": "value",
                "--zone": "dynamic"
              }
            },
            "remove-metadata": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--keys": "value",
                "--zone": "dynamic"
              }
            },
            "remove-tags": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--tags": "value",
                "--zone": "dynamic"
              }
            },
            "reset": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "set-disk-auto-delete": {
              "commands": {},
              "flags": {
                "--auto-delete": "bool",
                "--device-name": "value",
                "--disk": "value",
                "--zone": "dynamic"
              }
            },
            "set-machine-type": {
              "commands": {},
              "flags": {
                "--custom-cpu": "value",
                "--custom-extensions": "bool",
                "--custom-memory": "value",
                "--machine-type": "dynamic",
                "--zone": "dynamic"
              }
            },
            "set-scheduling": {
              "commands": {},
              "flags": {
                "--maintenance-policy": [
                  "MIGRATE",
                  "TERMINATE"
                ],
                "--restart-on-failure": "bool",
                "--zone": "dynamic"
              }
            },
            "set-service-account": {
              "commands": {},
              "flags": {
                "--no-scopes": "bool",
                "--no-service-account": "bool",
                "--scopes": "value",
                "--service-account": "value",
                "--zone": "dynamic"
              }
            },
            "start": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--csek-key-file": "value",
                "--zone": "dynamic"
              }
            },
            "stop": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--zone": "dynamic"
              }
            },
            "tail-serial-port-output": {
              "commands": {},
              "flags": {
                "--port": "value",
                "--zone": "dynamic"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--deletion-protection": "bool",
                "--min-cpu-platform": "value",
                "--remove-labels": "value",
                "--update-labels": "value",
                "--zone": "dynamic"
              }
            },
            "update-access-config": {
              "commands": {},
              "flags": {
                "--network-interface": "value",
                "--no-public-ptr": "bool",
                "--no-public-ptr-domain": "bool",
                "--public-ptr": "bool",
                "--public-ptr-domain": "value",
                "--zone": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "interconnects": {
          "commands": {
            "attachments": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--interconnect": "dynamic",
                    "--region": "dynamic",
                    "--router": "dynamic"
                  }
                },
                "dedicated": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--candidate-subnets": "value",
                        "--description": "value",
                        "--enable-admin": "bool",
                        "--interconnect": "dynamic",
                        "--region": "dynamic",
                        "--router": "dynamic",
                        "--vlan": "value"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--enable-admin": "bool",
                        "--region": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "partner": {
                  "commands": {
                    "create": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--edge-availability-domain": [
                          "any",
                          "availability-domain-1",
                          "availability-domain-2"
                        ],
                        "--enable-admin": "bool",
                        "--region": "dynamic",
                        "--router": "dynamic"
                      }
                    },
                    "update": {
                      "commands": {},
                      "flags": {
                        "--description": "value",
                        "--enable-admin": "bool",
                        "--region": "dynamic"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "create": {
              "commands": {},
              "flags": {
                "--admin-enabled": "bool",
                "--customer-name": "value",
                "--description": "value",
                "--interconnect-type": [
                  "DEDICATED"
                ],
                "--link-type": [
                  "LINK_TYPE_ETHERNET_10G_LR"
                ],
                "--location": "dynamic",
                "--noc-contact-email": "value",
                "--requested-link-count": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "locations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "patch": {
              "commands": {},
              "flags": {
                "--admin-enabled": "bool",
                "--description": "value",
                "--noc-contact-email": "value",
                "--requested-link-count": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--admin-enabled": "bool",
                "--description": "value",
                "--noc-contact-email": "value",
                "--requested-link-count": "value"
              }
            }
          },
          "flags": {}
        },
        "machine-types": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "networks": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--bgp-routing-mode": [
                  "global",
                  "regional"
                ],
                "--description": "value",
                "--mode": [
                  "auto",
                  "custom",
                  "legacy"
                ],
                "--range": "value",
                "--subnet-mode": [
                  "auto",
                  "custom",
                  "legacy"
                ]
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "peerings": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--auto-create-routes": "bool",
                    "--network": "value",
                    "--peer-network": "value",
                    "--peer-project": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--network": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--network": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "subnets": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--description": "value",
                    "--enable-flow-logs": "bool",
                    "--enable-private-ip-google-access": "bool",
                    "--network": "dynamic",
                    "--range": "value",
                    "--region": "dynamic",
                    "--secondary-range": "value"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "dynamic"
                  }
                },
                "expand-ip-range": {
                  "commands": {},
                  "flags": {
                    "--prefix-length": "value",
                    "--region": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--network": "value",
                    "--page-size": "value",
                    "--regexp": "value",
                    "--regions": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--add-secondary-ranges": "value",
                    "--enable-flow-logs": "bool",
                    "--enable-private-ip-google-access": "bool",
                    "--region": "dynamic",
                    "--remove-secondary-ranges": "value"
                  }
                }
              },
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--bgp-routing-mode": [
                  "global",
                  "regional"
                ],
                "--switch-to-custom-subnet-mode": "bool"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--global": "bool",
                "--region": "dynamic",
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--global": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "value"
              }
            }
          },
          "flags": {}
        },
        "os-login": {
          "commands": {
            "describe-profile": {
              "commands": {},
              "flags": {}
            },
            "remove-profile": {
              "commands": {},
              "flags": {}
            },
            "ssh-keys": {
              "commands": {
                "add": {
                  "commands": {},
                  "flags": {
                    "--key": "value",
                    "--key-file": "value",
                    "--ttl": "value"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--key": "value",
                    "--key-file": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                },
                "remove": {
                  "commands": {},
                  "flags": {
                    "--key": "value",
                    "--key-file": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--key": "value",
                    "--key-file": "value",
                    "--ttl": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "project-info": {
          "commands": {
            "add-metadata": {
              "commands": {},
              "flags": {
                "--metadata": "value",
                "--metadata-from-file": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "remove-metadata": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--keys": "value"
              }
            },
            "set-usage-bucket": {
              "commands": {},
              "flags": {
                "--bucket": "value",
                "--no-bucket": "bool",
                "--prefix": "value"
              }
            }
          },
          "flags": {}
        },
        "regions": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "reset-windows-password": {
          "commands": {},
          "flags": {
            "--user": "value",
            "--zone": "dynamic"
          }
        },
        "routers": {
          "commands": {
            "add-bgp-peer": {
              "commands": {},
              "flags": {
                "--advertised-route-priority": "value",
                "--advertisement-mode": [
                  "CUSTOM",
                  "DEFAULT"
                ],
                "--async": "bool",
                "--interface": "value",
                "--peer-asn": "value",
                "--peer-ip-address": "value",
                "--peer-name": "value",
                "--region": "dynamic",
                "--set-advertisement-groups": "value",
                "--set-advertisement-ranges": "value"
              }
            },
            "add-interface": {
              "commands": {},
              "flags": {
                "--interconnect-attachment": "dynamic",
                "--interconnect-attachment-region": "dynamic",
                "--interface-name": "value",
                "--ip-address": "value",
                "--mask-length": "value",
                "--region": "dynamic",
                "--vpn-tunnel": "dynamic",
                "--vpn-tunnel-region": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--advertisement-mode": [
                  "CUSTOM",
                  "DEFAULT"
                ],
                "--asn": "value",
                "--async": "bool",
                "--description": "value",
                "--network": "dynamic",
                "--region": "dynamic",
                "--set-advertisement-groups": "value",
                "--set-advertisement-ranges": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "get-status": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-bgp-peer": {
              "commands": {},
              "flags": {
                "--peer-name": "value",
                "--region": "dynamic"
              }
            },
            "remove-interface": {
              "commands": {},
              "flags": {
                "--interface-name": "value",
                "--region": "dynamic"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--add-advertisement-groups": "value",
                "--add-advertisement-ranges": "value",
                "--advertisement-mode": [
                  "CUSTOM",
                  "DEFAULT"
                ],
                "--async": "bool",
                "--region": "dynamic",
                "--remove-advertisement-groups": "value",
                "--remove-advertisement-ranges": "value",
                "--set-advertisement-groups": "value",
                "--set-advertisement-ranges": "value"
              }
            },
            "update-bgp-peer": {
              "commands": {},
              "flags": {
                "--add-advertisement-groups": "value",
                "--add-advertisement-ranges": "value",
                "--advertised-route-priority": "value",
                "--advertisement-mode": [
                  "CUSTOM",
                  "DEFAULT"
                ],
                "--async": "bool",
                "--interface": "value",
                "--ip-address": "value",
                "--peer-asn": "value",
                "--peer-ip-address": "value",
                "--peer-name": "value",
                "--region": "dynamic",
                "--remove-advertisement-groups": "value",
                "--remove-advertisement-ranges": "value",
                "--set-advertisement-groups": "value",
                "--set-advertisement-ranges": "value"
              }
            },
            "update-interface": {
              "commands": {},
              "flags": {
                "--interconnect-attachment": "dynamic",
                "--interconnect-attachment-region": "dynamic",
                "--interface-name": "value",
                "--ip-address": "value",
                "--mask-length": "value",
                "--region": "dynamic",
                "--vpn-tunnel": "dynamic",
                "--vpn-tunnel-region": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "routes": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--destination-range": "value",
                "--network": "value",
                "--next-hop-address": "value",
                "--next-hop-gateway": "dynamic",
                "--next-hop-instance": "value",
                "--next-hop-instance-zone": "value",
                "--next-hop-vpn-tunnel": "value",
                "--next-hop-vpn-tunnel-region": "value",
                "--priority": "value",
                "--tags": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "scp": {
          "commands": {},
          "flags": {
            "--compress": "bool",
            "--dry-run": "bool",
            "--force-key-file-overwrite": "bool",
            "--plain": "bool",
            "--port": "value",
            "--recurse": "bool",
            "--scp-flag": "value",
            "--ssh-key-file": "value",
            "--strict-host-key-checking": [
              "ask",
              "no",
              "yes"
            ],
            "--zone": "value"
          }
        },
        "shared-vpc": {
          "commands": {
            "associated-projects": {
              "commands": {
                "add": {
                  "commands": {},
                  "flags": {
                    "--host-project": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove": {
                  "commands": {},
                  "flags": {
                    "--host-project": "value"
                  }
                }
              },
              "flags": {}
            },
            "disable": {
              "commands": {},
              "flags": {}
            },
            "enable": {
              "commands": {},
              "flags": {}
            },
            "get-host-project": {
              "commands": {},
              "flags": {}
            },
            "list-associated-resources": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "organizations": {
              "commands": {
                "list-host-projects": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "sign-url": {
          "commands": {},
          "flags": {
            "--expires-in": "value",
            "--key-file": "value",
            "--key-name": "value",
            "--validate": "bool"
          }
        },
        "snapshots": {
          "commands": {
            "add-labels": {
              "commands": {},
              "flags": {
                "--labels": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-labels": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--labels": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        },
        "ssh": {
          "commands": {},
          "flags": {
            "--command": "value",
            "--container": "value",
            "--dry-run": "bool",
            "--force-key-file-overwrite": "bool",
            "--plain": "bool",
            "--ssh-flag": "value",
            "--ssh-key-file": "value",
            "--strict-host-key-checking": [
              "ask",
              "no",
              "yes"
            ],
            "--zone": "dynamic"
          }
        },
        "ssl-certificates": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--certificate": "value",
                "--description": "value",
                "--private-key": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "ssl-policies": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--custom-features": "value",
                "--description": "value",
                "--min-tls-version": [
                  "1.0",
                  "1.1",
                  "1.2"
                ],
                "--profile": [
                  "COMPATIBLE",
                  "CUSTOM",
                  "MODERN",
                  "RESTRICTED"
                ]
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "list-available-features": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--custom-features": "value",
                "--min-tls-version": [
                  "1.0",
                  "1.1",
                  "1.2"
                ],
                "--profile": [
                  "COMPATIBLE",
                  "CUSTOM",
                  "MODERN",
                  "RESTRICTED"
                ]
              }
            }
          },
          "flags": {}
        },
        "target-http-proxies": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--url-map": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--url-map": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "target-https-proxies": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--quic-override": [
                  "DISABLE",
                  "ENABLE",
                  "NONE"
                ],
                "--ssl-certificates": "dynamic",
                "--ssl-policy": "dynamic",
                "--url-map": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-ssl-policy": "bool",
                "--quic-override": [
                  "DISABLE",
                  "ENABLE",
                  "NONE"
                ],
                "--ssl-certificates": "dynamic",
                "--ssl-policy": "dynamic",
                "--url-map": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "target-instances": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--instance": "dynamic",
                "--instance-zone": "dynamic",
                "--zone": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zones": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "target-pools": {
          "commands": {
            "add-health-checks": {
              "commands": {},
              "flags": {
                "--http-health-check": "dynamic",
                "--region": "dynamic"
              }
            },
            "add-instances": {
              "commands": {},
              "flags": {
                "--instances": "dynamic",
                "--instances-zone": "dynamic",
                "--region": "dynamic",
                "--zone": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--backup-pool": "value",
                "--description": "value",
                "--failover-ratio": "value",
                "--health-check": "value",
                "--http-health-check": "dynamic",
                "--region": "dynamic",
                "--session-affinity": [
                  "CLIENT_IP",
                  "CLIENT_IP_PROTO",
                  "GENERATED_COOKIE",
                  "NONE"
                ]
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "get-health": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-health-checks": {
              "commands": {},
              "flags": {
                "--http-health-check": "dynamic",
                "--region": "dynamic"
              }
            },
            "remove-instances": {
              "commands": {},
              "flags": {
                "--instances": "dynamic",
                "--instances-zone": "dynamic",
                "--region": "dynamic",
                "--zone": "dynamic"
              }
            },
            "set-backup": {
              "commands": {},
              "flags": {
                "--backup-pool": "dynamic",
                "--failover-ratio": "value",
                "--no-backup-pool": "bool",
                "--region": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "target-ssl-proxies": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--backend-service": "dynamic",
                "--description": "value",
                "--proxy-header": [
                  "NONE",
                  "PROXY_V1"
                ],
                "--ssl-certificates": "dynamic",
                "--ssl-policy": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--backend-service": "dynamic",
                "--clear-ssl-policy": "bool",
                "--proxy-header": [
                  "NONE",
                  "PROXY_V1"
                ],
                "--ssl-certificates": "dynamic",
                "--ssl-policy": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "target-tcp-proxies": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--backend-service": "dynamic",
                "--description": "value",
                "--proxy-header": [
                  "NONE",
                  "PROXY_V1"
                ]
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--backend-service": "dynamic",
                "--proxy-header": [
                  "NONE",
                  "PROXY_V1"
                ]
              }
            }
          },
          "flags": {}
        },
        "target-vpn-gateways": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--network": "dynamic",
                "--region": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "tpus": {
          "commands": {
            "accelerator-types": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "create": {
              "commands": {},
              "flags": {
                "--accelerator-type": "value",
                "--async": "bool",
                "--description": "value",
                "--network": "value",
                "--preemptible": "bool",
                "--range": "value",
                "--zone": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--zone": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zone": "dynamic"
              }
            },
            "locations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "reimage": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--zone": "value"
              }
            },
            "start": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--zone": "value"
              }
            },
            "stop": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--zone": "value"
              }
            },
            "versions": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "url-maps": {
          "commands": {
            "add-host-rule": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--hosts": "value",
                "--path-matcher-name": "value"
              }
            },
            "add-path-matcher": {
              "commands": {},
              "flags": {
                "--backend-bucket-path-rules": "value",
                "--backend-service-path-rules": "value",
                "--default-backend-bucket": "value",
                "--default-service": "value",
                "--delete-orphaned-path-matcher": "bool",
                "--description": "value",
                "--existing-host": "value",
                "--new-hosts": "value",
                "--path-matcher-name": "value",
                "--path-rules": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--default-backend-bucket": "value",
                "--default-service": "value",
                "--description": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "edit": {
              "commands": {},
              "flags": {}
            },
            "invalidate-cdn-cache": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--host": "value",
                "--path": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "list-cdn-cache-invalidations": {
              "commands": {},
              "flags": {
                "--limit": "value"
              }
            },
            "remove-host-rule": {
              "commands": {},
              "flags": {
                "--delete-orphaned-path-matcher": "bool",
                "--host": "value"
              }
            },
            "remove-path-matcher": {
              "commands": {},
              "flags": {
                "--path-matcher-name": "value"
              }
            },
            "set-default-service": {
              "commands": {},
              "flags": {
                "--default-backend-bucket": "value",
                "--default-service": "value"
              }
            }
          },
          "flags": {}
        },
        "vpn-tunnels": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--ike-version": [
                  1,
                  2
                ],
                "--local-traffic-selector": "value",
                "--peer-address": "value",
                "--region": "dynamic",
                "--remote-traffic-selector": "value",
                "--router": "value",
                "--shared-secret": "value",
                "--target-vpn-gateway": "dynamic",
                "--target-vpn-gateway-region": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--regions": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "xpn": {
          "commands": {
            "associated-projects": {
              "commands": {
                "add": {
                  "commands": {},
                  "flags": {
                    "--host-project": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "remove": {
                  "commands": {},
                  "flags": {
                    "--host-project": "value"
                  }
                }
              },
              "flags": {}
            },
            "disable": {
              "commands": {},
              "flags": {}
            },
            "enable": {
              "commands": {},
              "flags": {}
            },
            "get-host-project": {
              "commands": {},
              "flags": {}
            },
            "list-associated-resources": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "organizations": {
              "commands": {
                "list-host-projects": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "zones": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--regexp": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "config": {
      "commands": {
        "configurations": {
          "commands": {
            "activate": {
              "commands": {},
              "flags": {}
            },
            "create": {
              "commands": {},
              "flags": {
                "--activate": "bool"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {
                "--all": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            }
          },
          "flags": {}
        },
        "get-value": {
          "commands": {},
          "flags": {}
        },
        "list": {
          "commands": {},
          "flags": {
            "--all": "bool",
            "--filter": "value",
            "--limit": "value",
            "--sort-by": "value"
          }
        },
        "set": {
          "commands": {},
          "flags": {
            "--installation": "bool"
          }
        },
        "unset": {
          "commands": {},
          "flags": {
            "--installation": "bool"
          }
        }
      },
      "flags": {}
    },
    "container": {
      "commands": {
        "builds": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--ongoing": "bool",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "log": {
              "commands": {},
              "flags": {
                "--stream": "bool"
              }
            },
            "submit": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--config": "value",
                "--disk-size": "value",
                "--gcs-log-dir": "value",
                "--gcs-source-staging-dir": "value",
                "--machine-type": [
                  "n1-highcpu-32",
                  "n1-highcpu-8"
                ],
                "--no-source": "bool",
                "--substitutions": "value",
                "--tag": "value",
                "--timeout": "value"
              }
            }
          },
          "flags": {}
        },
        "clusters": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--accelerator": "value",
                "--additional-zones": "value",
                "--addons": "value",
                "--async": "bool",
                "--cluster-ipv4-cidr": "value",
                "--cluster-secondary-range-name": "value",
                "--cluster-version": "value",
                "--create-subnetwork": "value",
                "--disk-size": "value",
                "--enable-autorepair": "bool",
                "--enable-autoscaling": "bool",
                "--enable-autoupgrade": "bool",
                "--enable-basic-auth": "bool",
                "--enable-cloud-endpoints": "bool",
                "--enable-cloud-logging": "bool",
                "--enable-cloud-monitoring": "bool",
                "--enable-ip-alias": "bool",
                "--enable-kubernetes-alpha": "bool",
                "--enable-legacy-authorization": "bool",
                "--enable-main-authorized-networks": "bool",
                "--enable-network-policy": "bool",
                "--image-type": "value",
                "--issue-client-certificate": "bool",
                "--labels": "value",
                "--local-ssd-count": "value",
                "--machine-type": "value",
                "--maintenance-window": "value",
                "--main-authorized-networks": "value",
                "--max-nodes": "value",
                "--max-nodes-per-pool": "value",
                "--min-cpu-platform": "value",
                "--min-nodes": "value",
                "--network": "value",
                "--node-labels": "value",
                "--node-locations": "value",
                "--node-taints": "value",
                "--node-version": "value",
                "--num-nodes": "value",
                "--password": "value",
                "--preemptible": "bool",
                "--region": "value",
                "--scopes": "value",
                "--service-account": "value",
                "--services-ipv4-cidr": "value",
                "--services-secondary-range-name": "value",
                "--subnetwork": "value",
                "--tags": "value",
                "--username": "value",
                "--zone": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--region": "value",
                "--zone": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "get-credentials": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zone": "value"
              }
            },
            "resize": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--node-pool": "value",
                "--region": "value",
                "--size": "value",
                "--zone": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--complete-credential-rotation": "bool",
                "--complete-ip-rotation": "bool",
                "--enable-autoscaling": "bool",
                "--enable-basic-auth": "bool",
                "--enable-legacy-authorization": "bool",
                "--enable-main-authorized-networks": "bool",
                "--enable-network-policy": "bool",
                "--generate-password": "bool",
                "--logging-service": "value",
                "--maintenance-window": "value",
                "--main-authorized-networks": "value",
                "--max-nodes": "value",
                "--min-nodes": "value",
                "--monitoring-service": "value",
                "--node-locations": "value",
                "--node-pool": "value",
                "--password": "value",
                "--region": "value",
                "--remove-labels": "value",
                "--set-password": "bool",
                "--start-credential-rotation": "bool",
                "--start-ip-rotation": "bool",
                "--update-addons": "value",
                "--update-labels": "value",
                "--username": "value",
                "--zone": "value"
              }
            },
            "upgrade": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--cluster-version": "value",
                "--image-type": "value",
                "--main": "bool",
                "--node-pool": "value",
                "--region": "value",
                "--zone": "value"
              }
            }
          },
          "flags": {
            "--region": "value",
            "--zone": "value"
          }
        },
        "get-server-config": {
          "commands": {},
          "flags": {
            "--region": "value",
            "--zone": "value"
          }
        },
        "images": {
          "commands": {
            "add-tag": {
              "commands": {},
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {
                "--force-delete-tags": "bool"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--repository": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "list-tags": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "untag": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "node-pools": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--accelerator": "value",
                "--cluster": "value",
                "--disk-size": "value",
                "--enable-autorepair": "bool",
                "--enable-autoscaling": "bool",
                "--enable-autoupgrade": "bool",
                "--enable-cloud-endpoints": "bool",
                "--image-type": "value",
                "--local-ssd-count": "value",
                "--machine-type": "value",
                "--max-nodes": "value",
                "--min-cpu-platform": "value",
                "--min-nodes": "value",
                "--node-labels": "value",
                "--node-taints": "value",
                "--node-version": "value",
                "--num-nodes": "value",
                "--preemptible": "bool",
                "--region": "value",
                "--scopes": "value",
                "--service-account": "value",
                "--tags": "value",
                "--zone": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--cluster": "value",
                "--region": "value",
                "--zone": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--cluster": "value",
                "--region": "value",
                "--zone": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--cluster": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--uri": "bool",
                "--zone": "value"
              }
            },
            "rollback": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--cluster": "value",
                "--region": "value",
                "--zone": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--cluster": "value",
                "--enable-autorepair": "bool",
                "--enable-autoupgrade": "bool",
                "--region": "value",
                "--zone": "value"
              }
            }
          },
          "flags": {
            "--region": "value",
            "--zone": "value"
          }
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--zone": "value"
              }
            },
            "wait": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--zone": "value"
              }
            }
          },
          "flags": {
            "--region": "value",
            "--zone": "value"
          }
        }
      },
      "flags": {}
    },
    "dataflow": {
      "commands": {
        "jobs": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--full": "bool",
                "--region": "value"
              }
            },
            "drain": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--created-after": "value",
                "--created-before": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--status": [
                  "active",
                  "all",
                  "terminated"
                ],
                "--uri": "bool"
              }
            },
            "run": {
              "commands": {},
              "flags": {
                "--gcs-location": "value",
                "--max-workers": "value",
                "--parameters": "value",
                "--region": "value",
                "--service-account-email": "value",
                "--staging-location": "value",
                "--zone": "value"
              }
            },
            "show": {
              "commands": {},
              "flags": {
                "--environment": "bool",
                "--region": "value",
                "--steps": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "dataproc": {
      "commands": {
        "clusters": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--bucket": "value",
                "--image": "value",
                "--image-version": "value",
                "--initialization-action-timeout": "value",
                "--initialization-actions": "value",
                "--labels": "value",
                "--main-boot-disk-size": "value",
                "--main-boot-disk-type": "value",
                "--main-machine-type": "value",
                "--metadata": "value",
                "--network": "value",
                "--num-main-local-ssds": "value",
                "--num-mains": "value",
                "--num-preemptible-workers": "value",
                "--num-worker-local-ssds": "value",
                "--num-workers": "value",
                "--preemptible-worker-boot-disk-size": "value",
                "--preemptible-worker-boot-disk-type": "value",
                "--properties": "value",
                "--region": "value",
                "--scopes": "value",
                "--service-account": "value",
                "--single-node": "bool",
                "--subnet": "value",
                "--tags": "value",
                "--worker-boot-disk-size": "value",
                "--worker-boot-disk-type": "value",
                "--worker-machine-type": "value",
                "--zone": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--region": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "diagnose": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--clear-labels": "bool",
                "--graceful-decommission-timeout": "value",
                "--num-preemptible-workers": "value",
                "--num-workers": "value",
                "--region": "value",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {
            "--region": "value"
          }
        },
        "jobs": {
          "commands": {
            "delete": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "kill": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--cluster": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--state-filter": [
                  "active",
                  "inactive"
                ]
              }
            },
            "submit": {
              "commands": {
                "hadoop": {
                  "commands": {},
                  "flags": {
                    "--archives": "value",
                    "--async": "bool",
                    "--bucket": "value",
                    "--class": "value",
                    "--cluster": "value",
                    "--driver-log-levels": "value",
                    "--files": "value",
                    "--jar": "value",
                    "--jars": "value",
                    "--labels": "value",
                    "--max-failures-per-hour": "value",
                    "--properties": "value",
                    "--region": "value"
                  }
                },
                "hive": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--bucket": "value",
                    "--cluster": "value",
                    "--continue-on-failure": "bool",
                    "--execute": "value",
                    "--file": "value",
                    "--jars": "value",
                    "--labels": "value",
                    "--max-failures-per-hour": "value",
                    "--params": "value",
                    "--properties": "value",
                    "--region": "value"
                  }
                },
                "pig": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--bucket": "value",
                    "--cluster": "value",
                    "--continue-on-failure": "bool",
                    "--driver-log-levels": "value",
                    "--execute": "value",
                    "--file": "value",
                    "--jars": "value",
                    "--labels": "value",
                    "--max-failures-per-hour": "value",
                    "--params": "value",
                    "--properties": "value",
                    "--region": "value"
                  }
                },
                "pyspark": {
                  "commands": {},
                  "flags": {
                    "--archives": "value",
                    "--async": "bool",
                    "--bucket": "value",
                    "--cluster": "value",
                    "--driver-log-levels": "value",
                    "--files": "value",
                    "--jars": "value",
                    "--labels": "value",
                    "--max-failures-per-hour": "value",
                    "--properties": "value",
                    "--py-files": "value",
                    "--region": "value"
                  }
                },
                "spark": {
                  "commands": {},
                  "flags": {
                    "--archives": "value",
                    "--async": "bool",
                    "--bucket": "value",
                    "--class": "value",
                    "--cluster": "value",
                    "--driver-log-levels": "value",
                    "--files": "value",
                    "--jar": "value",
                    "--jars": "value",
                    "--labels": "value",
                    "--max-failures-per-hour": "value",
                    "--properties": "value",
                    "--region": "value"
                  }
                },
                "spark-sql": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--bucket": "value",
                    "--cluster": "value",
                    "--driver-log-levels": "value",
                    "--execute": "value",
                    "--file": "value",
                    "--jars": "value",
                    "--labels": "value",
                    "--max-failures-per-hour": "value",
                    "--params": "value",
                    "--properties": "value",
                    "--region": "value"
                  }
                }
              },
              "flags": {
                "--async": "bool",
                "--bucket": "value",
                "--region": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--region": "value",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            },
            "wait": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            }
          },
          "flags": {
            "--region": "value"
          }
        },
        "operations": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--cluster": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--state-filter": [
                  "active",
                  "inactive"
                ]
              }
            }
          },
          "flags": {
            "--region": "value"
          }
        }
      },
      "flags": {
        "--region": "value"
      }
    },
    "datastore": {
      "commands": {
        "cleanup-indexes": {
          "commands": {},
          "flags": {}
        },
        "create-indexes": {
          "commands": {},
          "flags": {}
        },
        "export": {
          "commands": {},
          "flags": {
            "--async": "bool",
            "--kinds": "value",
            "--namespaces": "value",
            "--operation-labels": "value"
          }
        },
        "import": {
          "commands": {},
          "flags": {
            "--async": "bool",
            "--kinds": "value",
            "--namespaces": "value",
            "--operation-labels": "value"
          }
        },
        "operations": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "debug": {
      "commands": {
        "logpoints": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--condition": "value",
                "--log-level": [
                  "error",
                  "info",
                  "warning"
                ],
                "--target": "value",
                "--wait": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--all-users": "bool",
                "--include-inactive": "bool",
                "--location": "value",
                "--target": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--all-users": "bool",
                "--filter": "value",
                "--include-inactive": "value",
                "--limit": "value",
                "--location": "value",
                "--sort-by": "value",
                "--target": "value"
              }
            }
          },
          "flags": {
            "--target": "value"
          }
        },
        "snapshots": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--condition": "value",
                "--expression": "value",
                "--target": "value",
                "--wait": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--all-users": "bool",
                "--include-inactive": "bool",
                "--location": "value",
                "--target": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--location": "value",
                "--target": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--all-users": "bool",
                "--filter": "value",
                "--include-inactive": "value",
                "--limit": "value",
                "--location": "value",
                "--sort-by": "value",
                "--target": "value"
              }
            },
            "wait": {
              "commands": {},
              "flags": {
                "--all": "bool",
                "--all-users": "bool",
                "--filter": "value",
                "--limit": "value",
                "--location": "value",
                "--sort-by": "value",
                "--target": "value",
                "--timeout": "value"
              }
            }
          },
          "flags": {
            "--target": "value"
          }
        },
        "source": {
          "commands": {
            "gen-repo-info-file": {
              "commands": {},
              "flags": {
                "--output-directory": "value",
                "--source-directory": "value"
              }
            }
          },
          "flags": {}
        },
        "targets": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--include-inactive": "bool",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "deployment-manager": {
      "commands": {
        "deployments": {
          "commands": {
            "cancel-preview": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--fingerprint": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--automatic-rollback-on-error": "bool",
                "--composite-type": "value",
                "--config": "value",
                "--description": "value",
                "--labels": "value",
                "--preview": "bool",
                "--properties": "value",
                "--template": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--delete-policy": [
                  "abandon",
                  "delete"
                ]
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--simple-list": "bool",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "stop": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--fingerprint": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--composite-type": "value",
                "--config": "value",
                "--create-policy": [
                  "acquire",
                  "create-or-acquire"
                ],
                "--delete-policy": [
                  "abandon",
                  "delete"
                ],
                "--description": "value",
                "--fingerprint": "value",
                "--preview": "bool",
                "--properties": "value",
                "--remove-labels": "value",
                "--template": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        },
        "manifests": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--deployment": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--deployment": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--simple-list": "bool",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--simple-list": "bool",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "wait": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "resources": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--deployment": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--deployment": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--simple-list": "bool",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {
            "--deployment": "value"
          }
        },
        "types": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "dns": {
      "commands": {
        "dns-keys": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value",
                "--zone": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "managed-zones": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--denial-of-existence": [
                  "nsec",
                  "nsec3"
                ],
                "--description": "value",
                "--dns-name": "value",
                "--dnssec-state": [
                  "off",
                  "on",
                  "transfer"
                ],
                "--ksk-algorithm": "value",
                "--ksk-key-length": "value",
                "--labels": "value",
                "--zsk-algorithm": "value",
                "--zsk-key-length": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--denial-of-existence": [
                  "nsec",
                  "nsec3"
                ],
                "--description": "value",
                "--dnssec-state": [
                  "off",
                  "on",
                  "transfer"
                ],
                "--ksk-algorithm": "value",
                "--ksk-key-length": "value",
                "--remove-labels": "value",
                "--update-labels": "value",
                "--zsk-algorithm": "value",
                "--zsk-key-length": "value"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--zone": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value",
                "--zones": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "project-info": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "record-sets": {
          "commands": {
            "changes": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--zone": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--sort-order": [
                      "ascending",
                      "descending"
                    ],
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "export": {
              "commands": {},
              "flags": {
                "--zone": "dynamic",
                "--zone-file-format": "bool"
              }
            },
            "import": {
              "commands": {},
              "flags": {
                "--delete-all-existing": "bool",
                "--replace-origin-ns": "bool",
                "--zone": "dynamic",
                "--zone-file-format": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--name": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--type": "value",
                "--uri": "bool",
                "--zone": "dynamic"
              }
            },
            "transaction": {
              "commands": {
                "abort": {
                  "commands": {},
                  "flags": {
                    "--transaction-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "add": {
                  "commands": {},
                  "flags": {
                    "--name": "value",
                    "--transaction-file": "value",
                    "--ttl": "value",
                    "--type": "value",
                    "--zone": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--transaction-file": "value",
                    "--zone": "dynamic"
                  }
                },
                "execute": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--transaction-file": "value",
                    "--uri": "bool",
                    "--zone": "dynamic"
                  }
                },
                "remove": {
                  "commands": {},
                  "flags": {
                    "--name": "value",
                    "--transaction-file": "value",
                    "--ttl": "value",
                    "--type": "value",
                    "--zone": "dynamic"
                  }
                },
                "start": {
                  "commands": {},
                  "flags": {
                    "--transaction-file": "value",
                    "--zone": "dynamic"
                  }
                }
              },
              "flags": {
                "--transaction-file": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "docker": {
      "commands": {},
      "flags": {
        "--authorize-only": "bool",
        "--docker-host": "value",
        "--server": "value"
      }
    },
    "domains": {
      "commands": {
        "list-user-verified": {
          "commands": {},
          "flags": {}
        },
        "verify": {
          "commands": {},
          "flags": {}
        }
      },
      "flags": {}
    },
    "endpoints": {
      "commands": {
        "configs": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--service": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--service": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--full": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--service": "dynamic",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "wait": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "services": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "check-iam-policy": {
              "commands": {},
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "deploy": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--force": "bool",
                "--validate-only": "bool"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "undelete": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "feedback": {
      "commands": {},
      "flags": {
        "--log-file": "value"
      }
    },
    "firebase": {
      "commands": {
        "test": {
          "commands": {
            "android": {
              "commands": {
                "locales": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "models": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                },
                "run": {
                  "commands": {},
                  "flags": {
                    "--app": "value",
                    "--app-initial-activity": "value",
                    "--app-package": "value",
                    "--async": "bool",
                    "--auto-google-login": "bool",
                    "--device": "value",
                    "--device-ids": "value",
                    "--directories-to-pull": "value",
                    "--environment-variables": "value",
                    "--filter": "value",
                    "--limit": "value",
                    "--locales": "value",
                    "--max-depth": "value",
                    "--max-steps": "value",
                    "--obb-files": "value",
                    "--orientations": "dynamic",
                    "--os-version-ids": "value",
                    "--page-size": "value",
                    "--performance-metrics": "bool",
                    "--record-video": "bool",
                    "--results-bucket": "value",
                    "--results-dir": "value",
                    "--results-history-name": "value",
                    "--robo-directives": "value",
                    "--scenario-labels": "value",
                    "--scenario-numbers": "value",
                    "--sort-by": "value",
                    "--test": "value",
                    "--test-package": "value",
                    "--test-runner-class": "value",
                    "--test-targets": "value",
                    "--timeout": "value",
                    "--type": [
                      "game-loop",
                      "instrumentation",
                      "robo"
                    ],
                    "--use-orchestrator": "bool"
                  }
                },
                "versions": {
                  "commands": {
                    "describe": {
                      "commands": {},
                      "flags": {}
                    },
                    "list": {
                      "commands": {},
                      "flags": {
                        "--filter": "value",
                        "--limit": "value",
                        "--page-size": "value",
                        "--sort-by": "value"
                      }
                    }
                  },
                  "flags": {}
                }
              },
              "flags": {}
            },
            "network-profiles": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "help": {
      "commands": {},
      "flags": {}
    },
    "iam": {
      "commands": {
        "list-grantable-roles": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--page-size": "value"
          }
        },
        "list-testable-permissions": {
          "commands": {},
          "flags": {
            "--filter": "value"
          }
        },
        "roles": {
          "commands": {
            "copy": {
              "commands": {},
              "flags": {
                "--dest-organization": "value",
                "--dest-project": "value",
                "--destination": "value",
                "--source": "value",
                "--source-organization": "value",
                "--source-project": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--file": "value",
                "--organization": "value",
                "--permissions": "value",
                "--stage": "value",
                "--title": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--organization": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--organization": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--organization": "value",
                "--show-deleted": "bool",
                "--sort-by": "value"
              }
            },
            "undelete": {
              "commands": {},
              "flags": {
                "--organization": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--add-permissions": "value",
                "--description": "value",
                "--file": "value",
                "--organization": "value",
                "--permissions": "value",
                "--remove-permissions": "value",
                "--stage": "value",
                "--title": "value"
              }
            }
          },
          "flags": {}
        },
        "service-accounts": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--display-name": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "keys": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--iam-account": "value",
                    "--key-file-type": [
                      "json",
                      "p12"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--iam-account": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--created-before": "value",
                    "--filter": "value",
                    "--iam-account": "value",
                    "--limit": "value",
                    "--managed-by": [
                      "any",
                      "system",
                      "user"
                    ],
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            },
            "sign-blob": {
              "commands": {},
              "flags": {
                "--iam-account": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--display-name": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "info": {
      "commands": {},
      "flags": {
        "--anonymize": "bool",
        "--run-diagnostics": "bool",
        "--show-log": "bool"
      }
    },
    "init": {
      "commands": {},
      "flags": {
        "--console-only": "bool",
        "--skip-diagnostics": "bool"
      }
    },
    "iot": {
      "commands": {
        "devices": {
          "commands": {
            "configs": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "get-value": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--filter": "value",
                    "--limit": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--sort-by": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--config-data": "value",
                    "--config-file": "value",
                    "--device": "dynamic",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--version-to-update": "value"
                  }
                }
              },
              "flags": {}
            },
            "create": {
              "commands": {},
              "flags": {
                "--blocked": "bool",
                "--metadata": "value",
                "--metadata-from-file": "value",
                "--public-key": "value",
                "--region": "value",
                "--registry": "dynamic"
              }
            },
            "credentials": {
              "commands": {
                "clear": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--expiration-time": "value",
                    "--path": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--type": [
                      "es256",
                      "es256-pem",
                      "es256-x509-pem",
                      "rs256",
                      "rsa-pem",
                      "rsa-x509-pem"
                    ]
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--filter": "value",
                    "--limit": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--sort-by": "value"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--expiration-time": "value",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                }
              },
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--registry": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value",
                "--registry": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--device-ids": "value",
                "--device-num-ids": "value",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--registry": "dynamic",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "states": {
              "commands": {
                "list": {
                  "commands": {},
                  "flags": {
                    "--device": "dynamic",
                    "--filter": "value",
                    "--limit": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--blocked": "bool",
                "--metadata": "value",
                "--metadata-from-file": "value",
                "--region": "value",
                "--registry": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "registries": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--enable-http-config": "bool",
                "--enable-mqtt-config": "bool",
                "--event-notification-config": "value",
                "--public-key-path": "value",
                "--region": "value",
                "--state-pubsub-topic": "value"
              }
            },
            "credentials": {
              "commands": {
                "clear": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "create": {
                  "commands": {},
                  "flags": {
                    "--path": "value",
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--region": "value",
                    "--registry": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--limit": "value",
                    "--region": "value",
                    "--registry": "dynamic",
                    "--sort-by": "value"
                  }
                }
              },
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--region": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {
                "--region": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--enable-http-config": "bool",
                "--enable-mqtt-config": "bool",
                "--event-notification-config": "value",
                "--region": "value",
                "--state-pubsub-topic": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "kms": {
      "commands": {
        "decrypt": {
          "commands": {},
          "flags": {
            "--additional-authenticated-data-file": "value",
            "--ciphertext-file": "value",
            "--key": "dynamic",
            "--keyring": "dynamic",
            "--location": "dynamic",
            "--plaintext-file": "value"
          }
        },
        "encrypt": {
          "commands": {},
          "flags": {
            "--additional-authenticated-data-file": "value",
            "--ciphertext-file": "value",
            "--key": "dynamic",
            "--keyring": "dynamic",
            "--location": "dynamic",
            "--plaintext-file": "value"
          }
        },
        "keyrings": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--location": "dynamic",
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--location": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--location": "dynamic"
              }
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--location": "dynamic",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--location": "dynamic",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--location": "dynamic",
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {
                "--location": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "keys": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--labels": "value",
                "--location": "dynamic",
                "--next-rotation-time": "value",
                "--purpose": [
                  "encryption"
                ],
                "--rotation-period": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic"
              }
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--keyring": "dynamic",
                "--limit": "value",
                "--location": "dynamic",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--keyring": "dynamic",
                "--limit": "value",
                "--location": "dynamic",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "remove-rotation-schedule": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic"
              }
            },
            "set-primary-version": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic"
              }
            },
            "set-rotation-schedule": {
              "commands": {},
              "flags": {
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--next-rotation-time": "value",
                "--rotation-period": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--keyring": "dynamic",
                "--location": "dynamic",
                "--next-rotation-time": "value",
                "--primary-version": "dynamic",
                "--remove-labels": "value",
                "--remove-rotation-schedule": "bool",
                "--rotation-period": "value",
                "--update-labels": "value"
              }
            },
            "versions": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--location": "dynamic",
                    "--primary": "bool"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "destroy": {
                  "commands": {},
                  "flags": {
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "disable": {
                  "commands": {},
                  "flags": {
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "enable": {
                  "commands": {},
                  "flags": {
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--limit": "value",
                    "--location": "dynamic",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "restore": {
                  "commands": {},
                  "flags": {
                    "--key": "dynamic",
                    "--keyring": "dynamic",
                    "--location": "dynamic"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "locations": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "logging": {
      "commands": {
        "logs": {
          "commands": {
            "delete": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            }
          },
          "flags": {}
        },
        "metrics": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--log-filter": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--log-filter": "value"
              }
            }
          },
          "flags": {}
        },
        "read": {
          "commands": {},
          "flags": {
            "--billing-account": "value",
            "--folder": "value",
            "--freshness": "value",
            "--limit": "value",
            "--order": [
              "asc",
              "desc"
            ],
            "--organization": "dynamic"
          }
        },
        "resource-descriptors": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--sort-by": "value"
              }
            }
          },
          "flags": {}
        },
        "sinks": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--folder": "value",
                "--include-children": "bool",
                "--log-filter": "value",
                "--organization": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--folder": "value",
                "--organization": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--folder": "value",
                "--organization": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--filter": "value",
                "--folder": "value",
                "--limit": "value",
                "--organization": "dynamic",
                "--sort-by": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--billing-account": "value",
                "--folder": "value",
                "--log-filter": "value",
                "--organization": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "write": {
          "commands": {},
          "flags": {
            "--billing-account": "value",
            "--folder": "value",
            "--organization": "dynamic",
            "--payload-type": [
              "json",
              "text"
            ],
            "--severity": [
              "ALERT",
              "CRITICAL",
              "DEBUG",
              "DEFAULT",
              "EMERGENCY",
              "ERROR",
              "INFO",
              "NOTICE",
              "WARNING"
            ]
          }
        }
      },
      "flags": {}
    },
    "ml": {
      "commands": {
        "language": {
          "commands": {
            "analyze-entities": {
              "commands": {},
              "flags": {
                "--content": "value",
                "--content-file": "value",
                "--content-type": [
                  "html",
                  "plain-text"
                ],
                "--encoding-type": [
                  "none",
                  "utf16",
                  "utf32",
                  "utf8"
                ],
                "--language": "value"
              }
            },
            "analyze-entity-sentiment": {
              "commands": {},
              "flags": {
                "--content": "value",
                "--content-file": "value",
                "--content-type": [
                  "html",
                  "plain-text"
                ],
                "--encoding-type": [
                  "none",
                  "utf16",
                  "utf32",
                  "utf8"
                ],
                "--language": "value"
              }
            },
            "analyze-sentiment": {
              "commands": {},
              "flags": {
                "--content": "value",
                "--content-file": "value",
                "--content-type": [
                  "html",
                  "plain-text"
                ],
                "--encoding-type": [
                  "none",
                  "utf16",
                  "utf32",
                  "utf8"
                ],
                "--language": "value"
              }
            },
            "analyze-syntax": {
              "commands": {},
              "flags": {
                "--content": "value",
                "--content-file": "value",
                "--content-type": [
                  "html",
                  "plain-text"
                ],
                "--encoding-type": [
                  "none",
                  "utf16",
                  "utf32",
                  "utf8"
                ],
                "--language": "value"
              }
            },
            "classify-text": {
              "commands": {},
              "flags": {
                "--content": "value",
                "--content-file": "value",
                "--content-type": [
                  "html",
                  "plain-text"
                ],
                "--language": "value"
              }
            }
          },
          "flags": {}
        },
        "speech": {
          "commands": {
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            },
            "recognize": {
              "commands": {},
              "flags": {
                "--encoding": [
                  "amr",
                  "amr-wb",
                  "encoding-unspecified",
                  "flac",
                  "linear16",
                  "mulaw",
                  "ogg-opus",
                  "speex-with-header-byte"
                ],
                "--filter-profanity": "bool",
                "--hints": "value",
                "--include-word-time-offsets": "bool",
                "--language-code": "value",
                "--max-alternatives": "value",
                "--sample-rate": "value"
              }
            },
            "recognize-long-running": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--encoding": [
                  "amr",
                  "amr-wb",
                  "encoding-unspecified",
                  "flac",
                  "linear16",
                  "mulaw",
                  "ogg-opus",
                  "speex-with-header-byte"
                ],
                "--filter-profanity": "bool",
                "--hints": "value",
                "--include-word-time-offsets": "bool",
                "--language-code": "value",
                "--max-alternatives": "value",
                "--sample-rate": "value"
              }
            }
          },
          "flags": {}
        },
        "video": {
          "commands": {
            "detect-explicit-content": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--output-uri": "value",
                "--region": [
                  "asia-east1",
                  "europe-west1",
                  "us-east1",
                  "us-west1"
                ],
                "--segments": "value"
              }
            },
            "detect-labels": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--detection-mode": [
                  "frame",
                  "shot",
                  "shot-and-frame"
                ],
                "--output-uri": "value",
                "--region": [
                  "asia-east1",
                  "europe-west1",
                  "us-east1",
                  "us-west1"
                ],
                "--segments": "value"
              }
            },
            "detect-shot-changes": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--output-uri": "value",
                "--region": [
                  "asia-east1",
                  "europe-west1",
                  "us-east1",
                  "us-west1"
                ],
                "--segments": "value"
              }
            },
            "operations": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {}
                },
                "wait": {
                  "commands": {},
                  "flags": {}
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "vision": {
          "commands": {
            "detect-document": {
              "commands": {},
              "flags": {
                "--language-hints": "value"
              }
            },
            "detect-faces": {
              "commands": {},
              "flags": {
                "--max-results": "value"
              }
            },
            "detect-image-properties": {
              "commands": {},
              "flags": {}
            },
            "detect-labels": {
              "commands": {},
              "flags": {
                "--max-results": "value"
              }
            },
            "detect-landmarks": {
              "commands": {},
              "flags": {
                "--max-results": "value"
              }
            },
            "detect-logos": {
              "commands": {},
              "flags": {
                "--max-results": "value"
              }
            },
            "detect-safe-search": {
              "commands": {},
              "flags": {}
            },
            "detect-text": {
              "commands": {},
              "flags": {
                "--language-hints": "value"
              }
            },
            "detect-web": {
              "commands": {},
              "flags": {
                "--max-results": "value"
              }
            },
            "suggest-crop": {
              "commands": {},
              "flags": {
                "--aspect-ratios": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "ml-engine": {
      "commands": {
        "jobs": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {
                "--summarize": "bool"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "stream-logs": {
              "commands": {},
              "flags": {
                "--allow-multiline-logs": "bool",
                "--polling-interval": "value",
                "--task-name": "value"
              }
            },
            "submit": {
              "commands": {
                "prediction": {
                  "commands": {},
                  "flags": {
                    "--batch-size": "value",
                    "--data-format": [
                      "text",
                      "tf-record",
                      "tf-record-gzip"
                    ],
                    "--input-paths": "value",
                    "--labels": "value",
                    "--max-worker-count": "value",
                    "--model": "value",
                    "--model-dir": "value",
                    "--output-path": "value",
                    "--region": "value",
                    "--runtime-version": "value"
                  }
                },
                "training": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--config": "value",
                    "--job-dir": "value",
                    "--labels": "value",
                    "--module-name": "value",
                    "--package-path": "value",
                    "--packages": "value",
                    "--python-version": "value",
                    "--region": "dynamic",
                    "--runtime-version": "value",
                    "--scale-tier": [
                      "basic",
                      "basic-gpu",
                      "basic-tpu",
                      "custom",
                      "premium-1",
                      "standard-1"
                    ],
                    "--staging-bucket": "value",
                    "--stream-logs": "bool"
                  }
                }
              },
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        },
        "local": {
          "commands": {
            "predict": {
              "commands": {},
              "flags": {
                "--framework": [
                  "scikit-learn",
                  "tensorflow",
                  "xgboost"
                ],
                "--json-instances": "value",
                "--model-dir": "value",
                "--text-instances": "value"
              }
            },
            "train": {
              "commands": {},
              "flags": {
                "--distributed": "bool",
                "--job-dir": "value",
                "--module-name": "value",
                "--package-path": "value",
                "--parameter-server-count": "value",
                "--start-port": "value",
                "--worker-count": "value"
              }
            }
          },
          "flags": {}
        },
        "models": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--description": "value",
                "--enable-logging": "bool",
                "--labels": "value",
                "--regions": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "dynamic"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--description": "value",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "wait": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "predict": {
          "commands": {},
          "flags": {
            "--json-instances": "value",
            "--model": "value",
            "--text-instances": "value"
          }
        },
        "versions": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--config": "value",
                "--description": "value",
                "--framework": [
                  "scikit-learn",
                  "tensorflow",
                  "xgboost"
                ],
                "--labels": "value",
                "--model": "value",
                "--origin": "value",
                "--python-version": "value",
                "--runtime-version": "value",
                "--staging-bucket": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--model": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--model": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--model": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "set-default": {
              "commands": {},
              "flags": {
                "--model": "value"
              }
            },
            "update": {
              "commands": {},
              "flags": {
                "--clear-labels": "bool",
                "--description": "value",
                "--model": "value",
                "--remove-labels": "value",
                "--update-labels": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "organizations": {
      "commands": {
        "add-iam-policy-binding": {
          "commands": {},
          "flags": {
            "--member": "value",
            "--role": "dynamic"
          }
        },
        "describe": {
          "commands": {},
          "flags": {}
        },
        "get-iam-policy": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--limit": "value",
            "--page-size": "value",
            "--sort-by": "value"
          }
        },
        "list": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--limit": "value",
            "--page-size": "value",
            "--sort-by": "value",
            "--uri": "bool"
          }
        },
        "remove-iam-policy-binding": {
          "commands": {},
          "flags": {
            "--member": "value",
            "--role": "value"
          }
        },
        "set-iam-policy": {
          "commands": {},
          "flags": {}
        }
      },
      "flags": {}
    },
    "projects": {
      "commands": {
        "add-iam-policy-binding": {
          "commands": {},
          "flags": {
            "--member": "value",
            "--role": "dynamic"
          }
        },
        "create": {
          "commands": {},
          "flags": {
            "--enable-cloud-apis": "bool",
            "--folder": "value",
            "--labels": "value",
            "--name": "value",
            "--organization": "value",
            "--set-as-default": "bool"
          }
        },
        "delete": {
          "commands": {},
          "flags": {}
        },
        "describe": {
          "commands": {},
          "flags": {}
        },
        "get-iam-policy": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--limit": "value",
            "--page-size": "value",
            "--sort-by": "value"
          }
        },
        "list": {
          "commands": {},
          "flags": {
            "--filter": "value",
            "--limit": "value",
            "--page-size": "value",
            "--sort-by": "value",
            "--uri": "bool"
          }
        },
        "remove-iam-policy-binding": {
          "commands": {},
          "flags": {
            "--member": "value",
            "--role": "dynamic"
          }
        },
        "set-iam-policy": {
          "commands": {},
          "flags": {}
        },
        "undelete": {
          "commands": {},
          "flags": {}
        },
        "update": {
          "commands": {},
          "flags": {
            "--name": "value"
          }
        }
      },
      "flags": {}
    },
    "pubsub": {
      "commands": {
        "subscriptions": {
          "commands": {
            "ack": {
              "commands": {},
              "flags": {
                "--ack-ids": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--ack-deadline": "value",
                "--push-endpoint": "value",
                "--topic": "value",
                "--topic-project": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "modify-message-ack-deadline": {
              "commands": {},
              "flags": {
                "--ack-deadline": "value",
                "--ack-ids": "value"
              }
            },
            "modify-push-config": {
              "commands": {},
              "flags": {
                "--push-endpoint": "value"
              }
            },
            "pull": {
              "commands": {},
              "flags": {
                "--auto-ack": "bool",
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "topics": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "list-subscriptions": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "publish": {
              "commands": {},
              "flags": {
                "--attribute": "value",
                "--message": "value"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "services": {
      "commands": {
        "disable": {
          "commands": {},
          "flags": {
            "--async": "bool"
          }
        },
        "enable": {
          "commands": {},
          "flags": {
            "--async": "bool"
          }
        },
        "list": {
          "commands": {},
          "flags": {
            "--available": "bool",
            "--enabled": "bool",
            "--filter": "value",
            "--limit": "value",
            "--page-size": "value",
            "--sort-by": "value"
          }
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {
                "--full": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--service": "dynamic",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "wait": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "source": {
      "commands": {
        "repos": {
          "commands": {
            "clone": {
              "commands": {},
              "flags": {
                "--dry-run": "bool"
              }
            },
            "create": {
              "commands": {},
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {
                "--force": "bool"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "spanner": {
      "commands": {
        "databases": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--instance": "value",
                "--member": "value",
                "--role": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--ddl": "value",
                "--instance": "value"
              }
            },
            "ddl": {
              "commands": {
                "describe": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                },
                "update": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--ddl": "value",
                    "--instance": "value"
                  }
                }
              },
              "flags": {}
            },
            "delete": {
              "commands": {},
              "flags": {
                "--instance": "value"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--instance": "value"
              }
            },
            "execute-sql": {
              "commands": {},
              "flags": {
                "--instance": "value",
                "--query-mode": [
                  "NORMAL",
                  "PLAN",
                  "PROFILE"
                ],
                "--sql": "value"
              }
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--instance": "value",
                "--member": "value",
                "--role": "value"
              }
            },
            "sessions": {
              "commands": {
                "delete": {
                  "commands": {},
                  "flags": {
                    "--database": "value",
                    "--instance": "value"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--database": "value",
                    "--filter": "value",
                    "--instance": "value",
                    "--limit": "value",
                    "--page-size": "value",
                    "--server-filter": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {
                "--instance": "value"
              }
            }
          },
          "flags": {}
        },
        "instance-configs": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "instances": {
          "commands": {
            "add-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--config": "dynamic",
                "--description": "value",
                "--nodes": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {}
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "get-iam-policy": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "remove-iam-policy-binding": {
              "commands": {},
              "flags": {
                "--member": "value",
                "--role": "value"
              }
            },
            "set-iam-policy": {
              "commands": {},
              "flags": {}
            },
            "update": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--description": "value",
                "--nodes": "value"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "cancel": {
              "commands": {},
              "flags": {
                "--database": "dynamic",
                "--instance": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--database": "dynamic",
                "--instance": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--database": "dynamic",
                "--filter": "value",
                "--instance": "dynamic",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "sql": {
      "commands": {
        "backups": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--description": "value",
                "--instance": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--instance": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--instance": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "dynamic",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "restore": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--backup-instance": "dynamic",
                "--restore-instance": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "connect": {
          "commands": {},
          "flags": {
            "--user": "value"
          }
        },
        "databases": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--charset": "value",
                "--collation": "value",
                "--instance": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--instance": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--instance": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "dynamic",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "patch": {
              "commands": {},
              "flags": {
                "--charset": "value",
                "--collation": "value",
                "--diff": "bool",
                "--instance": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "export": {
          "commands": {
            "csv": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--database": "value",
                "--query": "value"
              }
            },
            "sql": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--database": "value",
                "--table": "value"
              }
            }
          },
          "flags": {}
        },
        "flags": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--database-version": [
                  "MYSQL_5_5",
                  "MYSQL_5_6",
                  "MYSQL_5_7",
                  "POSTGRES_9_6"
                ],
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "import": {
          "commands": {
            "csv": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--columns": "value",
                "--database": "value",
                "--table": "value",
                "--user": "value"
              }
            },
            "sql": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--database": "value",
                "--user": "value"
              }
            }
          },
          "flags": {}
        },
        "instances": {
          "commands": {
            "clone": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--bin-log-file-name": "value",
                "--bin-log-position": "value"
              }
            },
            "create": {
              "commands": {},
              "flags": {
                "--activation-policy": [
                  "always",
                  "never",
                  "on-demand"
                ],
                "--assign-ip": "bool",
                "--async": "bool",
                "--authorized-gae-apps": "value",
                "--authorized-networks": "value",
                "--availability-type": [
                  "regional",
                  "zonal"
                ],
                "--backup": "bool",
                "--backup-start-time": "value",
                "--cpu": "value",
                "--database-flags": "value",
                "--database-version": [
                  "MYSQL_5_5",
                  "MYSQL_5_6",
                  "MYSQL_5_7",
                  "POSTGRES_9_6"
                ],
                "--enable-bin-log": "bool",
                "--failover-replica-name": "value",
                "--follow-gae-app": "value",
                "--gce-zone": "value",
                "--maintenance-release-channel": [
                  "preview",
                  "production"
                ],
                "--maintenance-window-day": [
                  "FRI",
                  "MON",
                  "SAT",
                  "SUN",
                  "THU",
                  "TUE",
                  "WED"
                ],
                "--maintenance-window-hour": "value",
                "--main-instance-name": "value",
                "--memory": "value",
                "--pricing-plan": [
                  "PACKAGE",
                  "PER_USE"
                ],
                "--region": "value",
                "--replica-type": [
                  "FAILOVER",
                  "READ"
                ],
                "--replication": [
                  "asynchronous",
                  "synchronous"
                ],
                "--require-ssl": "bool",
                "--storage-auto-increase": "bool",
                "--storage-size": "value",
                "--storage-type": [
                  "HDD",
                  "SSD"
                ],
                "--tier": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "describe": {
              "commands": {},
              "flags": {}
            },
            "export": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--database": "value",
                "--table": "value"
              }
            },
            "failover": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "import": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--database": "value"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "patch": {
              "commands": {},
              "flags": {
                "--activation-policy": [
                  "always",
                  "never",
                  "on-demand"
                ],
                "--assign-ip": "bool",
                "--async": "bool",
                "--authorized-gae-apps": "value",
                "--authorized-networks": "value",
                "--availability-type": [
                  "regional",
                  "zonal"
                ],
                "--backup-start-time": "value",
                "--clear-authorized-networks": "bool",
                "--clear-database-flags": "bool",
                "--clear-gae-apps": "bool",
                "--cpu": "value",
                "--database-flags": "value",
                "--diff": "bool",
                "--enable-bin-log": "bool",
                "--enable-database-replication": "bool",
                "--follow-gae-app": "value",
                "--gce-zone": "value",
                "--maintenance-release-channel": [
                  "preview",
                  "production"
                ],
                "--maintenance-window-any": "bool",
                "--maintenance-window-day": [
                  "FRI",
                  "MON",
                  "SAT",
                  "SUN",
                  "THU",
                  "TUE",
                  "WED"
                ],
                "--maintenance-window-hour": "value",
                "--memory": "value",
                "--no-backup": "bool",
                "--pricing-plan": [
                  "PACKAGE",
                  "PER_USE"
                ],
                "--replication": [
                  "asynchronous",
                  "synchronous"
                ],
                "--require-ssl": "bool",
                "--storage-auto-increase": "bool",
                "--storage-size": "value",
                "--tier": "value"
              }
            },
            "promote-replica": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "reset-ssl-config": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "restart": {
              "commands": {},
              "flags": {
                "--async": "bool"
              }
            },
            "restore-backup": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--backup-id": "value",
                "--backup-instance": "dynamic"
              }
            }
          },
          "flags": {}
        },
        "operations": {
          "commands": {
            "describe": {
              "commands": {},
              "flags": {}
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "dynamic",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "wait": {
              "commands": {},
              "flags": {}
            }
          },
          "flags": {}
        },
        "ssl": {
          "commands": {
            "client-certs": {
              "commands": {
                "create": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "delete": {
                  "commands": {},
                  "flags": {
                    "--async": "bool",
                    "--instance": "dynamic"
                  }
                },
                "describe": {
                  "commands": {},
                  "flags": {
                    "--instance": "dynamic"
                  }
                },
                "list": {
                  "commands": {},
                  "flags": {
                    "--filter": "value",
                    "--instance": "dynamic",
                    "--limit": "value",
                    "--page-size": "value",
                    "--sort-by": "value",
                    "--uri": "bool"
                  }
                }
              },
              "flags": {}
            }
          },
          "flags": {}
        },
        "ssl-certs": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--instance": "dynamic"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--instance": "dynamic"
              }
            },
            "describe": {
              "commands": {},
              "flags": {
                "--instance": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "dynamic",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "tiers": {
          "commands": {
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            }
          },
          "flags": {}
        },
        "users": {
          "commands": {
            "create": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--host": "value",
                "--instance": "dynamic",
                "--password": "value"
              }
            },
            "delete": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--host": "value",
                "--instance": "dynamic"
              }
            },
            "list": {
              "commands": {},
              "flags": {
                "--filter": "value",
                "--instance": "dynamic",
                "--limit": "value",
                "--page-size": "value",
                "--sort-by": "value",
                "--uri": "bool"
              }
            },
            "set-password": {
              "commands": {},
              "flags": {
                "--async": "bool",
                "--host": "value",
                "--instance": "dynamic",
                "--password": "value",
                "--prompt-for-password": "bool"
              }
            }
          },
          "flags": {}
        }
      },
      "flags": {}
    },
    "topic": {
      "commands": {
        "arg-files": {
          "commands": {},
          "flags": {}
        },
        "cli-trees": {
          "commands": {},
          "flags": {}
        },
        "command-conventions": {
          "commands": {},
          "flags": {}
        },
        "configurations": {
          "commands": {},
          "flags": {}
        },
        "datetimes": {
          "commands": {},
          "flags": {}
        },
        "escaping": {
          "commands": {},
          "flags": {}
        },
        "filters": {
          "commands": {},
          "flags": {}
        },
        "formats": {
          "commands": {},
          "flags": {}
        },
        "gcloudignore": {
          "commands": {},
          "flags": {}
        },
        "projections": {
          "commands": {},
          "flags": {}
        },
        "resource-keys": {
          "commands": {},
          "flags": {}
        },
        "startup": {
          "commands": {},
          "flags": {}
        }
      },
      "flags": {}
    },
    "version": {
      "commands": {},
      "flags": {}
    }
  },
  "flags": {
    "--account": "value",
    "--configuration": "value",
    "--flatten": "value",
    "--format": "value",
    "--help": "bool",
    "--log-http": "bool",
    "--project": "dynamic",
    "--quiet": "bool",
    "--trace-token": "value",
    "--user-output-enabled": "bool",
    "--verbosity": [
      "critical",
      "debug",
      "error",
      "info",
      "none",
      "warning"
    ],
    "--version": "bool"
  }
}
