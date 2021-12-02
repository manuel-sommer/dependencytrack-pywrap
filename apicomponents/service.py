import json
class DependencyTrackService(object):

    def list_services(self, uuid, pageSize=100):
        """Returns a list of all services for a given project

        Args:
            uuid (string): The UUID of the project.
            pageSize (int, optional): page size. Defaults to 100.

        Returns:
            List: list of all services for a given service
        """
        servicelist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/service/project/{uuid}", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        try:
            for service in range(0, len(response.json())):
                servicelist.append(response.json()[service-1])
            while len(response.json()) == pageSize:
                pageNumber += 1
                response = self.session.get(self.apicall + f"/v1/service/project/{uuid}", params={'pageSize': pageSize, 'pageNumber': pageNumber})
                for service in range(0, len(response.json())):
                    servicelist.append(response.json()[service-1])
            if response.status_code == 200:
                return servicelist
        except :
            if response.status_code == 404:
                return (f"The project could not be found, {response.status_code}")
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden, {response.status_code}")
            elif response.status_code == 401:
                return (f"Unauthorized, {response.status_code}")
            else:
                return ((response.content).decode("utf-8"), response.status_code)
            
    def get_service(self,uuid):
        """Returns a specific service.

        Args:
            uuid (string): The UUID of the project.

        Returns:
            dict: Returns a specific service.
        """
        response = self.session.get(self.apicall + f"/v1/service/{uuid}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The service could not be found, {response.status_code}")
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
        
    def delete_service(self, uuid):
        """Deletes a service

        Args:
            uuid (string): The UUID of the project. 
        """
        response = self.session.delete(self.apicall + f"/v1/service/{uuid}")
        if response.status_code == 200:
            return (f"Successful operation")
        elif response.status_code == 403:
            return (f"Access to the specified service is forbidden, {response.status_code}")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The UUID of the service could not be found, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
        
    def create_service(self, uuid, providerName=None, providerURL=None, contactName=None, contactEmail=None, contactPhone=None):
        """
        Model:
        {
        "provider": {
            "name": "string",
            "urls": [
            "string"
            ],
            "contacts": [
            {
                "name": "string",
                "email": "string",
                "phone": "string"
            }
            ]
        },
        "group": "string",
        "name": "string",
        "version": "string",
        "description": "string",
        "endpoints": [
            "string"
        ],
        "authenticated": true,
        "crossesTrustBoundary": true,
        "data": [
            {
            "direction": "INBOUND",
            "name": "string"
            }
        ],
        "externalReferences": [
            {
            "type": "vcs",
            "url": "string",
            "comment": "string"
            }
        ],
        "children": [
            null
        ],
        "vulnerabilities": [
            {
            "vulnId": "string",
            "source": "string",
            "friendlyVulnId": "string",
            "title": "string",
            "subTitle": "string",
            "description": "string",
            "recommendation": "string",
            "references": "string",
            "credits": "string",
            "created": "2021-12-02T12:27:25.400Z",
            "published": "2021-12-02T12:27:25.400Z",
            "updated": "2021-12-02T12:27:25.400Z",
            "cwe": {
                "cweId": 0,
                "name": "string"
            },
            "cvssV2BaseScore": 0,
            "cvssV2ImpactSubScore": 0,
            "cvssV2ExploitabilitySubScore": 0,
            "cvssV2Vector": "string",
            "cvssV3BaseScore": 0,
            "cvssV3ImpactSubScore": 0,
            "cvssV3ExploitabilitySubScore": 0,
            "cvssV3Vector": "string",
            "severity": "CRITICAL",
            "vulnerableVersions": "string",
            "patchedVersions": "string",
            "vulnerableSoftware": [
                {
                "purl": "string",
                "purlType": "string",
                "purlNamespace": "string",
                "purlName": "string",
                "purlVersion": "string",
                "purlQualifiers": "string",
                "purlSubpath": "string",
                "cpe22": "string",
                "cpe23": "string",
                "part": "string",
                "vendor": "string",
                "product": "string",
                "version": "string",
                "update": "string",
                "edition": "string",
                "language": "string",
                "swEdition": "string",
                "targetSw": "string",
                "targetHw": "string",
                "other": "string",
                "versionEndExcluding": "string",
                "versionEndIncluding": "string",
                "versionStartExcluding": "string",
                "versionStartIncluding": "string",
                "vulnerabilities": [
                    null
                ],
                "uuid": "string",
                "isVulnerable": true
                }
            ],
            "components": [
                {
                "author": "string",
                "publisher": "string",
                "group": "string",
                "name": "string",
                "version": "string",
                "classifier": "APPLICATION",
                "filename": "string",
                "extension": "string",
                "md5": "string",
                "sha1": "string",
                "sha256": "string",
                "sha384": "string",
                "sha512": "string",
                "sha3_256": "string",
                "sha3_384": "string",
                "sha3_512": "string",
                "blake2b_256": "string",
                "blake2b_384": "string",
                "blake2b_512": "string",
                "blake3": "string",
                "cpe": "string",
                "purl": {
                    "scheme": "string",
                    "type": "string",
                    "namespace": "string",
                    "name": "string",
                    "version": "string",
                    "qualifiers": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                    },
                    "subpath": "string",
                    "coordinates": "string"
                },
                "purlCoordinates": {
                    "scheme": "string",
                    "type": "string",
                    "namespace": "string",
                    "name": "string",
                    "version": "string",
                    "qualifiers": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                    },
                    "subpath": "string",
                    "coordinates": "string"
                },
                "swidTagId": "string",
                "description": "string",
                "copyright": "string",
                "license": "string",
                "resolvedLicense": {
                    "licenseGroups": [
                    {
                        "name": "string",
                        "licenses": [
                        null
                        ],
                        "riskWeight": 0,
                        "uuid": "string"
                    }
                    ],
                    "uuid": "string",
                    "name": "string",
                    "licenseText": "string",
                    "standardLicenseTemplate": "string",
                    "standardLicenseHeader": "string",
                    "licenseComments": "string",
                    "licenseId": "string",
                    "isOsiApproved": true,
                    "isFsfLibre": true,
                    "isDeprecatedLicenseId": true,
                    "seeAlso": [
                    "string"
                    ]
                },
                "directDependencies": "string",
                "children": [
                    null
                ],
                "vulnerabilities": [
                    null
                ],
                "project": {
                    "author": "string",
                    "publisher": "string",
                    "group": "string",
                    "name": "string",
                    "description": "string",
                    "version": "string",
                    "classifier": "APPLICATION",
                    "cpe": "string",
                    "purl": {
                    "scheme": "string",
                    "type": "string",
                    "namespace": "string",
                    "name": "string",
                    "version": "string",
                    "qualifiers": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    },
                    "subpath": "string",
                    "coordinates": "string"
                    },
                    "swidTagId": "string",
                    "directDependencies": "string",
                    "uuid": "string",
                    "children": [
                    null
                    ],
                    "properties": [
                    {
                        "groupName": "string",
                        "propertyName": "string",
                        "propertyValue": "string",
                        "propertyType": "BOOLEAN",
                        "description": "string"
                    }
                    ],
                    "tags": [
                    {
                        "name": "string",
                        "projects": [
                        null
                        ]
                    }
                    ],
                    "lastBomImport": "2021-12-02T12:27:25.400Z",
                    "lastBomImportFormat": "string",
                    "lastInheritedRiskScore": 0,
                    "active": true,
                    "metrics": {
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "unassigned": 0,
                    "vulnerabilities": 0,
                    "vulnerableComponents": 0,
                    "components": 0,
                    "suppressed": 0,
                    "findingsTotal": 0,
                    "findingsAudited": 0,
                    "findingsUnaudited": 0,
                    "inheritedRiskScore": 0,
                    "policyViolationsFail": 0,
                    "policyViolationsWarn": 0,
                    "policyViolationsInfo": 0,
                    "policyViolationsTotal": 0,
                    "policyViolationsAudited": 0,
                    "policyViolationsUnaudited": 0,
                    "policyViolationsSecurityTotal": 0,
                    "policyViolationsSecurityAudited": 0,
                    "policyViolationsSecurityUnaudited": 0,
                    "policyViolationsLicenseTotal": 0,
                    "policyViolationsLicenseAudited": 0,
                    "policyViolationsLicenseUnaudited": 0,
                    "policyViolationsOperationalTotal": 0,
                    "policyViolationsOperationalAudited": 0,
                    "policyViolationsOperationalUnaudited": 0,
                    "firstOccurrence": "2021-12-02T12:27:25.400Z",
                    "lastOccurrence": "2021-12-02T12:27:25.400Z"
                    }
                },
                "lastInheritedRiskScore": 0,
                "notes": "string",
                "uuid": "string",
                "bomRef": "string",
                "metrics": {
                    "project": {
                    "author": "string",
                    "publisher": "string",
                    "group": "string",
                    "name": "string",
                    "description": "string",
                    "version": "string",
                    "classifier": "APPLICATION",
                    "cpe": "string",
                    "purl": {
                        "scheme": "string",
                        "type": "string",
                        "namespace": "string",
                        "name": "string",
                        "version": "string",
                        "qualifiers": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                        },
                        "subpath": "string",
                        "coordinates": "string"
                    },
                    "swidTagId": "string",
                    "directDependencies": "string",
                    "uuid": "string",
                    "children": [
                        null
                    ],
                    "properties": [
                        {
                        "groupName": "string",
                        "propertyName": "string",
                        "propertyValue": "string",
                        "propertyType": "BOOLEAN",
                        "description": "string"
                        }
                    ],
                    "tags": [
                        {
                        "name": "string",
                        "projects": [
                            null
                        ]
                        }
                    ],
                    "lastBomImport": "2021-12-02T12:27:25.400Z",
                    "lastBomImportFormat": "string",
                    "lastInheritedRiskScore": 0,
                    "active": true,
                    "metrics": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unassigned": 0,
                        "vulnerabilities": 0,
                        "vulnerableComponents": 0,
                        "components": 0,
                        "suppressed": 0,
                        "findingsTotal": 0,
                        "findingsAudited": 0,
                        "findingsUnaudited": 0,
                        "inheritedRiskScore": 0,
                        "policyViolationsFail": 0,
                        "policyViolationsWarn": 0,
                        "policyViolationsInfo": 0,
                        "policyViolationsTotal": 0,
                        "policyViolationsAudited": 0,
                        "policyViolationsUnaudited": 0,
                        "policyViolationsSecurityTotal": 0,
                        "policyViolationsSecurityAudited": 0,
                        "policyViolationsSecurityUnaudited": 0,
                        "policyViolationsLicenseTotal": 0,
                        "policyViolationsLicenseAudited": 0,
                        "policyViolationsLicenseUnaudited": 0,
                        "policyViolationsOperationalTotal": 0,
                        "policyViolationsOperationalAudited": 0,
                        "policyViolationsOperationalUnaudited": 0,
                        "firstOccurrence": "2021-12-02T12:27:25.400Z",
                        "lastOccurrence": "2021-12-02T12:27:25.400Z"
                    }
                    },
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "unassigned": 0,
                    "vulnerabilities": 0,
                    "suppressed": 0,
                    "findingsTotal": 0,
                    "findingsAudited": 0,
                    "findingsUnaudited": 0,
                    "inheritedRiskScore": 0,
                    "policyViolationsFail": 0,
                    "policyViolationsWarn": 0,
                    "policyViolationsInfo": 0,
                    "policyViolationsTotal": 0,
                    "policyViolationsAudited": 0,
                    "policyViolationsUnaudited": 0,
                    "policyViolationsSecurityTotal": 0,
                    "policyViolationsSecurityAudited": 0,
                    "policyViolationsSecurityUnaudited": 0,
                    "policyViolationsLicenseTotal": 0,
                    "policyViolationsLicenseAudited": 0,
                    "policyViolationsLicenseUnaudited": 0,
                    "policyViolationsOperationalTotal": 0,
                    "policyViolationsOperationalAudited": 0,
                    "policyViolationsOperationalUnaudited": 0,
                    "firstOccurrence": "2021-12-02T12:27:25.400Z",
                    "lastOccurrence": "2021-12-02T12:27:25.400Z"
                },
                "repositoryMeta": {
                    "repositoryType": "MAVEN",
                    "namespace": "string",
                    "name": "string",
                    "latestVersion": "string",
                    "published": "2021-12-02T12:27:25.400Z",
                    "lastCheck": "2021-12-02T12:27:25.400Z"
                },
                "usedBy": 0,
                "isInternal": true
                }
            ],
            "serviceComponents": [
                null
            ],
            "uuid": "string",
            "affectedProjectCount": 0,
            "findingAttribution": {
                "attributedOn": "2021-12-02T12:27:25.400Z",
                "analyzerIdentity": "INTERNAL_ANALYZER",
                "component": {
                "author": "string",
                "publisher": "string",
                "group": "string",
                "name": "string",
                "version": "string",
                "classifier": "APPLICATION",
                "filename": "string",
                "extension": "string",
                "md5": "string",
                "sha1": "string",
                "sha256": "string",
                "sha384": "string",
                "sha512": "string",
                "sha3_256": "string",
                "sha3_384": "string",
                "sha3_512": "string",
                "blake2b_256": "string",
                "blake2b_384": "string",
                "blake2b_512": "string",
                "blake3": "string",
                "cpe": "string",
                "purl": {
                    "scheme": "string",
                    "type": "string",
                    "namespace": "string",
                    "name": "string",
                    "version": "string",
                    "qualifiers": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                    },
                    "subpath": "string",
                    "coordinates": "string"
                },
                "purlCoordinates": {
                    "scheme": "string",
                    "type": "string",
                    "namespace": "string",
                    "name": "string",
                    "version": "string",
                    "qualifiers": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                    },
                    "subpath": "string",
                    "coordinates": "string"
                },
                "swidTagId": "string",
                "description": "string",
                "copyright": "string",
                "license": "string",
                "resolvedLicense": {
                    "licenseGroups": [
                    {
                        "name": "string",
                        "licenses": [
                        null
                        ],
                        "riskWeight": 0,
                        "uuid": "string"
                    }
                    ],
                    "uuid": "string",
                    "name": "string",
                    "licenseText": "string",
                    "standardLicenseTemplate": "string",
                    "standardLicenseHeader": "string",
                    "licenseComments": "string",
                    "licenseId": "string",
                    "isOsiApproved": true,
                    "isFsfLibre": true,
                    "isDeprecatedLicenseId": true,
                    "seeAlso": [
                    "string"
                    ]
                },
                "directDependencies": "string",
                "children": [
                    null
                ],
                "vulnerabilities": [
                    null
                ],
                "project": {
                    "author": "string",
                    "publisher": "string",
                    "group": "string",
                    "name": "string",
                    "description": "string",
                    "version": "string",
                    "classifier": "APPLICATION",
                    "cpe": "string",
                    "purl": {
                    "scheme": "string",
                    "type": "string",
                    "namespace": "string",
                    "name": "string",
                    "version": "string",
                    "qualifiers": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    },
                    "subpath": "string",
                    "coordinates": "string"
                    },
                    "swidTagId": "string",
                    "directDependencies": "string",
                    "uuid": "string",
                    "children": [
                    null
                    ],
                    "properties": [
                    {
                        "groupName": "string",
                        "propertyName": "string",
                        "propertyValue": "string",
                        "propertyType": "BOOLEAN",
                        "description": "string"
                    }
                    ],
                    "tags": [
                    {
                        "name": "string",
                        "projects": [
                        null
                        ]
                    }
                    ],
                    "lastBomImport": "2021-12-02T12:27:25.400Z",
                    "lastBomImportFormat": "string",
                    "lastInheritedRiskScore": 0,
                    "active": true,
                    "metrics": {
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "unassigned": 0,
                    "vulnerabilities": 0,
                    "vulnerableComponents": 0,
                    "components": 0,
                    "suppressed": 0,
                    "findingsTotal": 0,
                    "findingsAudited": 0,
                    "findingsUnaudited": 0,
                    "inheritedRiskScore": 0,
                    "policyViolationsFail": 0,
                    "policyViolationsWarn": 0,
                    "policyViolationsInfo": 0,
                    "policyViolationsTotal": 0,
                    "policyViolationsAudited": 0,
                    "policyViolationsUnaudited": 0,
                    "policyViolationsSecurityTotal": 0,
                    "policyViolationsSecurityAudited": 0,
                    "policyViolationsSecurityUnaudited": 0,
                    "policyViolationsLicenseTotal": 0,
                    "policyViolationsLicenseAudited": 0,
                    "policyViolationsLicenseUnaudited": 0,
                    "policyViolationsOperationalTotal": 0,
                    "policyViolationsOperationalAudited": 0,
                    "policyViolationsOperationalUnaudited": 0,
                    "firstOccurrence": "2021-12-02T12:27:25.400Z",
                    "lastOccurrence": "2021-12-02T12:27:25.400Z"
                    }
                },
                "lastInheritedRiskScore": 0,
                "notes": "string",
                "uuid": "string",
                "bomRef": "string",
                "metrics": {
                    "project": {
                    "author": "string",
                    "publisher": "string",
                    "group": "string",
                    "name": "string",
                    "description": "string",
                    "version": "string",
                    "classifier": "APPLICATION",
                    "cpe": "string",
                    "purl": {
                        "scheme": "string",
                        "type": "string",
                        "namespace": "string",
                        "name": "string",
                        "version": "string",
                        "qualifiers": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                        },
                        "subpath": "string",
                        "coordinates": "string"
                    },
                    "swidTagId": "string",
                    "directDependencies": "string",
                    "uuid": "string",
                    "children": [
                        null
                    ],
                    "properties": [
                        {
                        "groupName": "string",
                        "propertyName": "string",
                        "propertyValue": "string",
                        "propertyType": "BOOLEAN",
                        "description": "string"
                        }
                    ],
                    "tags": [
                        {
                        "name": "string",
                        "projects": [
                            null
                        ]
                        }
                    ],
                    "lastBomImport": "2021-12-02T12:27:25.400Z",
                    "lastBomImportFormat": "string",
                    "lastInheritedRiskScore": 0,
                    "active": true,
                    "metrics": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unassigned": 0,
                        "vulnerabilities": 0,
                        "vulnerableComponents": 0,
                        "components": 0,
                        "suppressed": 0,
                        "findingsTotal": 0,
                        "findingsAudited": 0,
                        "findingsUnaudited": 0,
                        "inheritedRiskScore": 0,
                        "policyViolationsFail": 0,
                        "policyViolationsWarn": 0,
                        "policyViolationsInfo": 0,
                        "policyViolationsTotal": 0,
                        "policyViolationsAudited": 0,
                        "policyViolationsUnaudited": 0,
                        "policyViolationsSecurityTotal": 0,
                        "policyViolationsSecurityAudited": 0,
                        "policyViolationsSecurityUnaudited": 0,
                        "policyViolationsLicenseTotal": 0,
                        "policyViolationsLicenseAudited": 0,
                        "policyViolationsLicenseUnaudited": 0,
                        "policyViolationsOperationalTotal": 0,
                        "policyViolationsOperationalAudited": 0,
                        "policyViolationsOperationalUnaudited": 0,
                        "firstOccurrence": "2021-12-02T12:27:25.400Z",
                        "lastOccurrence": "2021-12-02T12:27:25.400Z"
                    }
                    },
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "unassigned": 0,
                    "vulnerabilities": 0,
                    "suppressed": 0,
                    "findingsTotal": 0,
                    "findingsAudited": 0,
                    "findingsUnaudited": 0,
                    "inheritedRiskScore": 0,
                    "policyViolationsFail": 0,
                    "policyViolationsWarn": 0,
                    "policyViolationsInfo": 0,
                    "policyViolationsTotal": 0,
                    "policyViolationsAudited": 0,
                    "policyViolationsUnaudited": 0,
                    "policyViolationsSecurityTotal": 0,
                    "policyViolationsSecurityAudited": 0,
                    "policyViolationsSecurityUnaudited": 0,
                    "policyViolationsLicenseTotal": 0,
                    "policyViolationsLicenseAudited": 0,
                    "policyViolationsLicenseUnaudited": 0,
                    "policyViolationsOperationalTotal": 0,
                    "policyViolationsOperationalAudited": 0,
                    "policyViolationsOperationalUnaudited": 0,
                    "firstOccurrence": "2021-12-02T12:27:25.400Z",
                    "lastOccurrence": "2021-12-02T12:27:25.400Z"
                },
                "repositoryMeta": {
                    "repositoryType": "MAVEN",
                    "namespace": "string",
                    "name": "string",
                    "latestVersion": "string",
                    "published": "2021-12-02T12:27:25.400Z",
                    "lastCheck": "2021-12-02T12:27:25.400Z"
                },
                "usedBy": 0,
                "isInternal": true
                },
                "alternateIdentifier": "string",
                "referenceUrl": "string",
                "uuid": "string"
            }
            }
        ],
        "project": {
            "author": "string",
            "publisher": "string",
            "group": "string",
            "name": "string",
            "description": "string",
            "version": "string",
            "classifier": "APPLICATION",
            "cpe": "string",
            "purl": {
            "scheme": "string",
            "type": "string",
            "namespace": "string",
            "name": "string",
            "version": "string",
            "qualifiers": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
            },
            "subpath": "string",
            "coordinates": "string"
            },
            "swidTagId": "string",
            "directDependencies": "string",
            "uuid": "string",
            "children": [
            null
            ],
            "properties": [
            {
                "groupName": "string",
                "propertyName": "string",
                "propertyValue": "string",
                "propertyType": "BOOLEAN",
                "description": "string"
            }
            ],
            "tags": [
            {
                "name": "string",
                "projects": [
                null
                ]
            }
            ],
            "lastBomImport": "2021-12-02T12:27:25.400Z",
            "lastBomImportFormat": "string",
            "lastInheritedRiskScore": 0,
            "active": true,
            "metrics": {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "unassigned": 0,
            "vulnerabilities": 0,
            "vulnerableComponents": 0,
            "components": 0,
            "suppressed": 0,
            "findingsTotal": 0,
            "findingsAudited": 0,
            "findingsUnaudited": 0,
            "inheritedRiskScore": 0,
            "policyViolationsFail": 0,
            "policyViolationsWarn": 0,
            "policyViolationsInfo": 0,
            "policyViolationsTotal": 0,
            "policyViolationsAudited": 0,
            "policyViolationsUnaudited": 0,
            "policyViolationsSecurityTotal": 0,
            "policyViolationsSecurityAudited": 0,
            "policyViolationsSecurityUnaudited": 0,
            "policyViolationsLicenseTotal": 0,
            "policyViolationsLicenseAudited": 0,
            "policyViolationsLicenseUnaudited": 0,
            "policyViolationsOperationalTotal": 0,
            "policyViolationsOperationalAudited": 0,
            "policyViolationsOperationalUnaudited": 0,
            "firstOccurrence": "2021-12-02T12:27:25.401Z",
            "lastOccurrence": "2021-12-02T12:27:25.401Z"
            }
        },
        "lastInheritedRiskScore": 0,
        "notes": "string",
        "uuid": "string",
        "bomRef": "string"
        }"""
        data={}
        contact={}
        if providerName:
            data['provider'] = {"name": providerName}
        if providerURL:
            data['provider'] = {"url": providerURL}
        if contactName:
            contact['name'] = contactName
        if contactEmail:
            contact['email'] = contactEmail
        if contactPhone:
            contact['phone']= contactPhone
        if not bool(contact):
            data['contact'] =[contact]
        #TODO: add more option
        response = self.session.put(self.apicall +f"/v1/service/project/{uuid}",data=json.dumps(data))
        if response.status_code == 201:
            return ("Successful operation")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The team could not be found, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)

def update_service(self,**args):
    data={}
    # TODO: improve the input parameters
    #? this wont return anything for now.
    response = self.session.post(self.apicall + "/v1/service", data=json.dumps(data))
    if response.status_code == 200:
        return ("Successful operation")
    else:
        return ((response.content).decode("utf-8"), response.status_code)