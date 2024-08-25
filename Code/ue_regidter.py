import time
import requests
import json


def ue_register(imsi, permanentKeyValue):
    url = f"http://19xxx9:5000/api/subscriber/{imsi}/20893"

    payload = json.dumps({
        "plmnID": "20893",
        "ueId": imsi,
        "AuthenticationSubscription": {
            "authenticationManagementField": "8000",
            "authenticationMethod": "5G_AKA",
            "milenage": {
                "op": {
                    "encryptionAlgorithm": 0,
                    "encryptionKey": 0,
                    "opValue": ""
                }
            },
            "opc": {
                "encryptionAlgorithm": 0,
                "encryptionKey": 0,
                "opcValue": "8e27xxxxxxxxxxxxxxxx605d"
            },
            "permanentKey": {
                "encryptionAlgorithm": 0,
                "encryptionKey": 0,
                "permanentKeyValue": permanentKeyValue
            },
            "sequenceNumber": "16xxxxxxxxxxx2"
        },
        "AccessAndMobilitySubscriptionData": {
            "gpsis": [
                "msisdn-0900000000"
            ],
            "nssai": {
                "defaultSingleNssais": [
                    {
                        "sst": 1,
                        "sd": "010203",
                        "isDefault": True
                    },
                    {
                        "sst": 1,
                        "sd": "112233",
                        "isDefault": True
                    }
                ],
                "singleNssais": []
            },
            "subscribedUeAmbr": {
                "downlink": "2 Gbps",
                "uplink": "1 Gbps"
            }
        },
        "SessionManagementSubscriptionData": [
            {
                "singleNssai": {
                    "sst": 1,
                    "sd": "010203"
                },
                "dnnConfigurations": {
                    "internet": {
                        "pduSessionTypes": {
                            "defaultSessionType": "IPV4",
                            "allowedSessionTypes": [
                                "IPV4"
                            ]
                        },
                        "sessionAmbr": {
                            "uplink": "200 Mbps",
                            "downlink": "100 Mbps"
                        },
                        "5gQosProfile": {
                            "5qi": 9,
                            "arp": {
                                "priorityLevel": 8
                            },
                            "priorityLevel": 8
                        }
                    },
                    "internet2": {
                        "pduSessionTypes": {
                            "defaultSessionType": "IPV4",
                            "allowedSessionTypes": [
                                "IPV4"
                            ]
                        },
                        "sessionAmbr": {
                            "uplink": "200 Mbps",
                            "downlink": "100 Mbps"
                        },
                        "5gQosProfile": {
                            "5qi": 9,
                            "arp": {
                                "priorityLevel": 8
                            },
                            "priorityLevel": 8
                        }
                    }
                }
            },
            {
                "singleNssai": {
                    "sst": 1,
                    "sd": "112233"
                },
                "dnnConfigurations": {
                    "internet": {
                        "pduSessionTypes": {
                            "defaultSessionType": "IPV4",
                            "allowedSessionTypes": [
                                "IPV4"
                            ]
                        },
                        "sessionAmbr": {
                            "uplink": "200 Mbps",
                            "downlink": "100 Mbps"
                        },
                        "5gQosProfile": {
                            "5qi": 9,
                            "arp": {
                                "priorityLevel": 8
                            },
                            "priorityLevel": 8
                        }
                    },
                    "internet2": {
                        "pduSessionTypes": {
                            "defaultSessionType": "IPV4",
                            "allowedSessionTypes": [
                                "IPV4"
                            ]
                        },
                        "sessionAmbr": {
                            "uplink": "200 Mbps",
                            "downlink": "100 Mbps"
                        },
                        "5gQosProfile": {
                            "5qi": 9,
                            "arp": {
                                "priorityLevel": 8
                            },
                            "priorityLevel": 8
                        }
                    }
                }
            }
        ],
        "SmfSelectionSubscriptionData": {
            "subscribedSnssaiInfos": {
                "01010203": {
                    "dnnInfos": [
                        {
                            "dnn": "internet"
                        },
                        {
                            "dnn": "internet2"
                        }
                    ]
                },
                "01112233": {
                    "dnnInfos": [
                        {
                            "dnn": "internet"
                        },
                        {
                            "dnn": "internet2"
                        }
                    ]
                }
            }
        },
        "AmPolicyData": {
            "subscCats": [
                "free5gc"
            ]
        },
        "SmPolicyData": {
            "smPolicySnssaiData": {
                "01010203": {
                    "snssai": {
                        "sst": 1,
                        "sd": "010203"
                    },
                    "smPolicyDnnData": {
                        "internet": {
                            "dnn": "internet"
                        },
                        "internet2": {
                            "dnn": "internet2"
                        }
                    }
                },
                "01112233": {
                    "snssai": {
                        "sst": 1,
                        "sd": "112233"
                    },
                    "smPolicyDnnData": {
                        "internet": {
                            "dnn": "internet"
                        },
                        "internet2": {
                            "dnn": "internet2"
                        }
                    }
                }
            }
        },
        "FlowRules": []
    })
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': '19xxxxx1:5000',
        'Referer': 'http://19xxxx.31:5000/',
        'Token': 'admin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def api_request():
    count = 1000
    suffix_width = len(str(count))

    for i in range(0, count):
        sufix = str(i).rjust(suffix_width, "0")
        imsi = f"imsi-208xxxx000{sufix}"
        permanentKeyValue = f"8xxxxxxxxxxxx7c{sufix}"
        res = ue_register(imsi, permanentKeyValue)
        print(res)
        time.sleep(1)


if __name__ == '__main__':
    api_request()
