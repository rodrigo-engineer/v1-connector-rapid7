# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get Incident by Incident Number"


class Input:
    INCIDENT_NUMBER = "incident_number"
    

class Output:
    INCIDENT = "incident"
    

class GetIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_number": {
      "type": "integer",
      "title": "Incident Number",
      "description": "Incident Number of Incident to get",
      "order": 1
    }
  },
  "required": [
    "incident_number"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident": {
      "$ref": "#/definitions/incident",
      "title": "Incident",
      "description": "Incident requested",
      "order": 1
    }
  },
  "required": [
    "incident"
  ],
  "definitions": {
    "incident": {
      "type": "object",
      "title": "incident",
      "properties": {
        "Accuracy": {
          "type": "string",
          "title": "Accuracy",
          "description": "Accuracy",
          "order": 162
        },
        "ActualCategory": {
          "type": "string",
          "title": "Actual Category",
          "description": "Actual category",
          "order": 2
        },
        "ActualCategory_Valid": {
          "type": "string",
          "title": "Actual Category Valid",
          "description": "Actual category valid",
          "order": 1
        },
        "ActualService": {
          "type": "string",
          "title": "Actual Service",
          "description": "Actual service",
          "order": 89
        },
        "ActualService_Valid": {
          "type": "string",
          "title": "Actual Service Valid",
          "description": "Actual service valid",
          "order": 88
        },
        "AddChatconversationtoActivityHistory": {
          "type": "boolean",
          "title": "Add Chat Conversation To Activity History",
          "description": "Add chat conversation to activity history",
          "order": 154
        },
        "AlternateContactEmail": {
          "type": "string",
          "title": "Alternate Contact Email",
          "description": "Alternate Contact Email",
          "order": 77
        },
        "AlternateContactLink": {
          "type": "string",
          "title": "Alternate Contact Link",
          "description": "Alternate contact link",
          "order": 54
        },
        "AlternateContactLink_Category": {
          "type": "string",
          "title": "Alternate Contact Link Category",
          "description": "Alternate contact link category",
          "order": 52
        },
        "AlternateContactLink_RecID": {
          "type": "string",
          "title": "Alternate Contact Link Rec ID",
          "description": "Alternate contact link rec ID",
          "order": 53
        },
        "AlternateContactPhone": {
          "type": "string",
          "title": "Alternate Contact Phone",
          "description": "Altername contact phone number",
          "order": 82
        },
        "ApprovalStatus": {
          "type": "string",
          "title": "Approval Status",
          "description": "Approval Status",
          "order": 127
        },
        "Approver": {
          "type": "string",
          "title": "Approver",
          "description": "Approver",
          "order": 125
        },
        "Approver_Valid": {
          "type": "string",
          "title": "Approver Valid",
          "description": "Approver valid",
          "order": 124
        },
        "Category": {
          "type": "string",
          "title": "Category",
          "description": "Category",
          "order": 4
        },
        "Category_Valid": {
          "type": "string",
          "title": "Category Valid",
          "description": "Category valid",
          "order": 3
        },
        "CauseCode": {
          "type": "string",
          "title": "Cause Code",
          "description": "Cause code",
          "order": 6
        },
        "CauseCode_Valid": {
          "type": "string",
          "title": "Cause Code Valid",
          "description": "Cause code valid",
          "order": 5
        },
        "ClosedBy": {
          "type": "string",
          "title": "Closed By",
          "description": "Closed by",
          "order": 7
        },
        "ClosedDateTime": {
          "type": "string",
          "title": "Closed Date Time",
          "description": "Closed date and time",
          "order": 8
        },
        "ClosedDuration": {
          "type": "integer",
          "title": "Closed Duration",
          "description": "Closed duration",
          "order": 9
        },
        "ClosingEscLink": {
          "type": "string",
          "title": "ClosingEscLink",
          "description": "ClosingEscLink",
          "order": 76
        },
        "ClosingEscLink_Category": {
          "type": "string",
          "title": "ClosingEscLink Category",
          "description": "ClosingEscLink",
          "order": 74
        },
        "ClosingEscLink_RecID": {
          "type": "string",
          "title": "ClosingEscLink RecID",
          "description": "ClosingEscLink RecID",
          "order": 75
        },
        "Cost": {
          "type": "string",
          "title": "Cost",
          "description": "Cost",
          "order": 120
        },
        "CostPerMinute": {
          "type": "string",
          "title": "Cost Per Minute",
          "description": "Cost per minute",
          "order": 92
        },
        "CostPerMinute_Currency": {
          "type": "string",
          "title": "Cost Per Minute Currency",
          "description": "Cost per minute currency",
          "order": 90
        },
        "CostPerMinute_CurrencyValid": {
          "type": "string",
          "title": "Cost Per Minute Currency Valid",
          "description": "Cost per minute currency valid",
          "order": 91
        },
        "Cost_Currency": {
          "type": "string",
          "title": "Cost Currency",
          "description": "Cost currency",
          "order": 118
        },
        "Cost_CurrencyValid": {
          "type": "string",
          "title": "Cost Currency Valid",
          "description": "Cost currency valid",
          "order": 119
        },
        "CreatedBy": {
          "type": "string",
          "title": "Created By",
          "description": "Created by",
          "order": 10
        },
        "CreatedByType": {
          "type": "string",
          "title": "Created By Type",
          "description": "Created by type",
          "order": 112
        },
        "CreatedDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date and time",
          "order": 11
        },
        "CustomerDepartment": {
          "type": "string",
          "title": "Customer Department",
          "description": "Customer department",
          "order": 87
        },
        "CustomerLocation": {
          "type": "string",
          "title": "Customer Location",
          "description": "Customer location",
          "order": 63
        },
        "CustomerLocation_Valid": {
          "type": "string",
          "title": "Customer Location Valid",
          "description": "Customer location valid",
          "order": 62
        },
        "Email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 12
        },
        "EntityLink": {
          "type": "string",
          "title": "Entity Link",
          "description": "Entity link",
          "order": 138
        },
        "EntityLink_Category": {
          "type": "string",
          "title": "Entity Link Category",
          "description": "Entity link category",
          "order": 136
        },
        "EntityLink_RecID": {
          "type": "string",
          "title": "Entity Link Rec ID",
          "description": "Entity link rec ID",
          "order": 137
        },
        "EventCIRecId": {
          "type": "string",
          "title": "Event CI RecId",
          "description": "Event CI RecId",
          "order": 139
        },
        "FirstCallResolution": {
          "type": "boolean",
          "title": "First Call Resolution",
          "description": "First call resolution",
          "order": 13
        },
        "HRCaseLink": {
          "type": "string",
          "title": "HR Case Link",
          "description": "HR case link",
          "order": 151
        },
        "HRCaseLink_Category": {
          "type": "string",
          "title": "HR Case Link Category",
          "description": "HR case link category",
          "order": 149
        },
        "HRCaseLink_RecID": {
          "type": "string",
          "title": "HR Case Link RecID",
          "description": "HR case link recID",
          "order": 150
        },
        "HoursOfOperation": {
          "type": "string",
          "title": "Hours Of Operation",
          "description": "Created by",
          "order": 58
        },
        "HoursOfOperation_Valid": {
          "type": "string",
          "title": "Hours Of Operation Valid",
          "description": "Hours of operation valid",
          "order": 57
        },
        "Impact": {
          "type": "string",
          "title": "Impact",
          "description": "Impact",
          "order": 15
        },
        "Impact_Valid": {
          "type": "string",
          "title": "Impact Valid",
          "description": "Impact valid",
          "order": 14
        },
        "IncidentDetailSummary": {
          "type": "string",
          "title": "Incident Detail Summary",
          "description": "Incident detail summary",
          "order": 122
        },
        "IncidentDetailWorkflowTag": {
          "type": "string",
          "title": "Incident Detail Workflow Tag",
          "description": "Incident Detail Workflow Tag",
          "order": 121
        },
        "IncidentNetworkUserName": {
          "type": "string",
          "title": "Incident Network User Name",
          "description": "Incident network user name",
          "order": 134
        },
        "IncidentNumber": {
          "type": "integer",
          "title": "IncidentNumber",
          "description": "Incident number",
          "order": 16
        },
        "IsApprovalNeeded": {
          "type": "boolean",
          "title": "Is Approval Needed",
          "description": "Is approval needed",
          "order": 123
        },
        "IsDSMTaskExisted": {
          "type": "boolean",
          "title": "Is DSM Task Existed By",
          "description": "Is DSM task existed",
          "order": 126
        },
        "IsInFinalState": {
          "type": "boolean",
          "title": "Is In Final State",
          "description": "Is the incident in its final state",
          "order": 93
        },
        "IsMasterIncident": {
          "type": "boolean",
          "title": "Is Master Incident",
          "description": "Is master incidint",
          "order": 140
        },
        "IsNewRecord": {
          "type": "boolean",
          "title": "Is New Record",
          "description": "Is new record",
          "order": 51
        },
        "IsNotification": {
          "type": "boolean",
          "title": "Is Notification",
          "description": "Is notification",
          "order": 17
        },
        "IsReclassifiedForResolution": {
          "type": "boolean",
          "title": "Is Reclassified For Resolution",
          "description": "Is reclassified for resolution",
          "order": 94
        },
        "IsRecommended": {
          "type": "boolean",
          "title": "Is Recommended",
          "description": "Is recommended",
          "order": 163
        },
        "IsRelatedIncidentResolutionUpdate": {
          "type": "boolean",
          "title": "Is Related Incident Resolution Update",
          "description": "Is related incident resolution update",
          "order": 147
        },
        "IsRelatedIncidentUpdate": {
          "type": "boolean",
          "title": "Is Related Incident Update",
          "description": "Is related incident update",
          "order": 146
        },
        "IsReportedByAlternateContact": {
          "type": "boolean",
          "title": "Is Reported By Alternate Contact",
          "description": "Is reported by alternate contact",
          "order": 64
        },
        "IsResolvedByMaster": {
          "type": "boolean",
          "title": "Is Resolved By Master",
          "description": "Is resolved by master",
          "order": 141
        },
        "IsRunTicketClassification": {
          "type": "boolean",
          "title": "Is Run Ticket Classification",
          "description": "Is run ticket classification",
          "order": 167
        },
        "IsUnRead": {
          "type": "boolean",
          "title": "Is Unread",
          "description": "Is unread",
          "order": 148
        },
        "IsVIP": {
          "type": "boolean",
          "title": "Is VIP",
          "description": "Is the ticket raised by VIP",
          "order": 18
        },
        "IsWorkAround": {
          "type": "boolean",
          "title": "Is Work Around",
          "description": "Is there a workaround available",
          "order": 19
        },
        "KnowledgeLink": {
          "type": "string",
          "title": "Knowledge Link",
          "description": "Knowledge link",
          "order": 97
        },
        "KnowledgeLink_Category": {
          "type": "string",
          "title": "Knowledge Link Category",
          "description": "Knowledge Link category",
          "order": 95
        },
        "KnowledgeLink_RecID": {
          "type": "string",
          "title": "Knowledge Link Rec ID",
          "description": "Knowledge link rec ID",
          "order": 96
        },
        "LastModBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "Last modified by",
          "order": 20
        },
        "LastModDateTime": {
          "type": "string",
          "title": "Last Modified Date Time",
          "description": "Last modified date and time",
          "order": 21
        },
        "LoginId": {
          "type": "string",
          "title": "Login ID",
          "description": "Login ID",
          "order": 45
        },
        "MasterIncidentLink": {
          "type": "string",
          "title": "Master Incident Link",
          "description": "Master Incident Link",
          "order": 144
        },
        "MasterIncidentLink_Category": {
          "type": "string",
          "title": "Master Incident Link Category",
          "description": "Master Incident Link Category",
          "order": 142
        },
        "MasterIncidentLink_RecID": {
          "type": "string",
          "title": "Master Incident Link RecID",
          "description": "Master Incident Link RecID",
          "order": 143
        },
        "NewNotes": {
          "type": "string",
          "title": "New Notes",
          "description": "New notes",
          "order": 111
        },
        "OrgUnitLink": {
          "type": "string",
          "title": "Org Unit Link",
          "description": "Organization unit link",
          "order": 105
        },
        "OrgUnitLink_Category": {
          "type": "string",
          "title": "Org Unit Link Category",
          "description": "Organization unit link category",
          "order": 103
        },
        "OrgUnitLink_RecID": {
          "type": "string",
          "title": "Org Unit Link Rec ID",
          "description": "Organization unit link rec ID",
          "order": 104
        },
        "OrganizationUnitID": {
          "type": "string",
          "title": "Organization Unit ID",
          "description": "Organization unit ID",
          "order": 78
        },
        "Owner": {
          "type": "string",
          "title": "Owner",
          "description": "Owner",
          "order": 47
        },
        "OwnerEmail": {
          "type": "string",
          "title": "Owner Email",
          "description": "Owner email",
          "order": 59
        },
        "OwnerTeam": {
          "type": "string",
          "title": "Owner Team",
          "description": "Owner team",
          "order": 49
        },
        "OwnerTeamEmail": {
          "type": "string",
          "title": "Owner Team Email",
          "description": "Owner team email",
          "order": 60
        },
        "OwnerTeam_Valid": {
          "type": "string",
          "title": "Owner Team Valid",
          "description": "Owner team valid",
          "order": 48
        },
        "OwnerType": {
          "type": "string",
          "title": "Owner Type",
          "description": "Owner type",
          "order": 50
        },
        "Owner_Valid": {
          "type": "string",
          "title": "Owner Valid",
          "description": "Owner valid",
          "order": 46
        },
        "OwnershipAssignmentEmail": {
          "type": "string",
          "title": "Ownership Assignment Email",
          "description": "Ownership assignment email",
          "order": 61
        },
        "OwningOrgUnitId": {
          "type": "string",
          "title": "Owning Org Unit ID",
          "description": "Owning org unit ID",
          "order": 107
        },
        "OwningOrgUnitId Valid": {
          "type": "string",
          "title": "Owning Org Unit ID Valid",
          "description": "Owning org unit ID valid",
          "order": 106
        },
        "Phone": {
          "type": "string",
          "title": "Phone",
          "description": "Phone",
          "order": 22
        },
        "PreviousState": {
          "type": "string",
          "title": "Previous State",
          "description": "Previous State",
          "order": 98
        },
        "Priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority",
          "order": 24
        },
        "Priority_Valid": {
          "type": "string",
          "title": "Priority Valid By",
          "description": "Priority valid by",
          "order": 23
        },
        "ProblemLink": {
          "type": "string",
          "title": "Problem Link",
          "description": "Problem Link",
          "order": 86
        },
        "ProblemLink_Category": {
          "type": "string",
          "title": "Problem Link Category",
          "description": "Problem Link Category",
          "order": 84
        },
        "ProblemLink_RecID": {
          "type": "string",
          "title": "Problem Link RecID",
          "description": "Problem Link RecID",
          "order": 85
        },
        "ProfileFullName": {
          "type": "string",
          "title": "Profile Full Name",
          "description": "Full name of who raised the incident",
          "order": 25
        },
        "ProfileLink": {
          "type": "string",
          "title": "Profile Link",
          "description": "Profile link",
          "order": 28
        },
        "ProfileLink_Category": {
          "type": "string",
          "title": "Profile Link Category",
          "description": "Profile link category",
          "order": 26
        },
        "ProfileLink_RecID": {
          "type": "string",
          "title": "Profile Link Rec ID",
          "description": "Profile link Rec ID",
          "order": 27
        },
        "Progress Bar Position": {
          "type": "string",
          "title": "Progress Bar Position",
          "description": "Progress bar position",
          "order": 108
        },
        "ReadOnly": {
          "type": "boolean",
          "title": "Read Only",
          "description": "Read only",
          "order": 117
        },
        "RecId": {
          "type": "string",
          "title": "Rec ID",
          "description": "Rec ID",
          "order": 29
        },
        "RecomCategory": {
          "type": "string",
          "title": "Recom Category",
          "description": "Recom category",
          "order": 165
        },
        "RecomService": {
          "type": "string",
          "title": "Recom Service",
          "description": "Recom service",
          "order": 164
        },
        "RecomSubCategory": {
          "type": "string",
          "title": "Recom SubCategory",
          "description": "Recom SubCategory",
          "order": 166
        },
        "RecommendedCategory": {
          "type": "string",
          "title": "Recommended Category",
          "description": "Recommended category",
          "order": 159
        },
        "RecommendedService": {
          "type": "string",
          "title": "Recommended Service",
          "description": "Recommended service",
          "order": 160
        },
        "RecommendedSubCategory": {
          "type": "string",
          "title": "Recommended SubCategory",
          "description": "Recommended subcategory",
          "order": 161
        },
        "ReportedBy": {
          "type": "string",
          "title": "Reported By",
          "description": "Reported by",
          "order": 110
        },
        "ReportingOrgUnitID": {
          "type": "string",
          "title": "Reporting Org Unit ID",
          "description": "Reporting organization unit ID",
          "order": 80
        },
        "ReportingOrgUnitID_Valid": {
          "type": "string",
          "title": "Reporting Org Unit ID Valid",
          "description": "Reporting organization unit ID valid",
          "order": 79
        },
        "Resolution": {
          "type": "string",
          "title": "Resolution",
          "description": "Resolution",
          "order": 30
        },
        "ResolutionEscLink": {
          "type": "string",
          "title": "ResolutionEscLink",
          "description": "ResolutionEscLink",
          "order": 67
        },
        "ResolutionEscLink_Category": {
          "type": "string",
          "title": "ResolutionEscLink Category",
          "description": "ResolutionEscLink Category",
          "order": 65
        },
        "ResolutionEscLink_RecID": {
          "type": "string",
          "title": "ResolutionEscLink Rec ID",
          "description": "ResolutionEscLink Rec ID",
          "order": 66
        },
        "ResolvedBy": {
          "type": "string",
          "title": "Resolved By",
          "description": "Resolved by",
          "order": 56
        },
        "ResolvedByIncidentNumber": {
          "type": "string",
          "title": "Resolved By Incident Number",
          "description": "Resolved By Incident Number",
          "order": 99
        },
        "ResolvedByType": {
          "type": "string",
          "title": "Resolved by Type",
          "description": "Resolved by type",
          "order": 109
        },
        "ResolvedDateTime": {
          "type": "string",
          "title": "Resolved Date Time",
          "description": "Resolved date and time",
          "order": 55
        },
        "RespondedBy": {
          "type": "string",
          "title": "Responded By",
          "description": "Responded By",
          "order": 101
        },
        "RespondedDateTime": {
          "type": "string",
          "title": "Responded Date Time",
          "description": "Responded date time",
          "order": 102
        },
        "ResponseEscLink": {
          "type": "string",
          "title": "ResponseEscLink",
          "description": "ResponseEscLink",
          "order": 70
        },
        "ResponseEscLink_RecID": {
          "type": "string",
          "title": "ResponseEscLink RecID",
          "description": "ResponseEscLink RecID",
          "order": 69
        },
        "ResponseEscLink_category": {
          "type": "string",
          "title": "ResponseEscLink Category",
          "description": "ResponseEscLink Category",
          "order": 68
        },
        "SLA": {
          "type": "string",
          "title": "SLA",
          "description": "SLA",
          "order": 33
        },
        "SLADisplayText": {
          "type": "string",
          "title": "SLA Display Text",
          "description": "SLA display text",
          "order": 113
        },
        "SLALink": {
          "type": "string",
          "title": "SLA Link",
          "description": "SLA link",
          "order": 36
        },
        "SLALink_Category": {
          "type": "string",
          "title": "SLA Link Category",
          "description": "SLA link Category",
          "order": 34
        },
        "SLALink_RecID": {
          "type": "string",
          "title": "SLA Link Rec ID",
          "description": "SLA link rec ID",
          "order": 35
        },
        "SendSurveyNotification": {
          "type": "boolean",
          "title": "Send Survey Notification",
          "description": "Send survey notification",
          "order": 135
        },
        "Service": {
          "type": "string",
          "title": "Service",
          "description": "Service",
          "order": 32
        },
        "ServiceOwnerEmail": {
          "type": "string",
          "title": "Service Owner Email",
          "description": "Service owner email",
          "order": 145
        },
        "ServiceReqLink": {
          "type": "string",
          "title": "Service ReqLink",
          "description": "Service ReqLink",
          "order": 116
        },
        "ServiceReqLink_Category": {
          "type": "string",
          "title": "Service ReqLink Category",
          "description": "Service ReqLink category",
          "order": 114
        },
        "ServiceReqLink_RecID": {
          "type": "string",
          "title": "Service ReqLink RecID",
          "description": "Service ReqLink ReqID",
          "order": 115
        },
        "Service_Valid": {
          "type": "string",
          "title": "Service Valid",
          "description": "Service valid",
          "order": 31
        },
        "SocialTextHeader": {
          "type": "string",
          "title": "Social Text Header",
          "description": "Social text header",
          "order": 128
        },
        "Source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 38
        },
        "Source_Valid": {
          "type": "string",
          "title": "Source Valid",
          "description": "Source valid",
          "order": 37
        },
        "Status": {
          "type": "string",
          "title": "Status",
          "description": "Created by",
          "order": 40
        },
        "Status_Valid": {
          "type": "string",
          "title": "Status Valid",
          "description": "Status valid",
          "order": 39
        },
        "SubCategory": {
          "type": "string",
          "title": "SubCategory",
          "description": "SubCategory",
          "order": 130
        },
        "SubCategory_Valid": {
          "type": "string",
          "title": "SubCategory Valid",
          "description": "SubCategory Valid",
          "order": 129
        },
        "Subject": {
          "type": "string",
          "title": "Subject",
          "description": "Incident subject",
          "order": 41
        },
        "Symptom": {
          "type": "string",
          "title": "Symptom",
          "description": "Symptoms of the indident",
          "order": 42
        },
        "TeamManagerEmail": {
          "type": "string",
          "title": "Team Manager Email",
          "description": "Team manager email",
          "order": 83
        },
        "TotalTimeSpent": {
          "type": "integer",
          "title": "Total Time Spent",
          "description": "Total time spent",
          "order": 100
        },
        "TypeOfIncident": {
          "type": "string",
          "title": "Type Of Incident",
          "description": "Type of incident",
          "order": 81
        },
        "Urgency": {
          "type": "string",
          "title": "Urgency",
          "description": "Urgency",
          "order": 44
        },
        "Urgency_Valid": {
          "type": "string",
          "title": "Urgency Valid",
          "description": "Urgency valid",
          "order": 43
        },
        "ViewType": {
          "type": "string",
          "title": "View Type",
          "description": "View Type",
          "order": 133
        },
        "VirimaAssetID": {
          "type": "string",
          "title": "Virima Asset ID",
          "description": "Virima asset ID",
          "order": 158
        },
        "WaitingEscLink": {
          "type": "string",
          "title": "WaitingEscLink",
          "description": "WaitingEscLink",
          "order": 73
        },
        "WaitingEscLink_Category": {
          "type": "string",
          "title": "WaitingEscLink Category",
          "description": "WaitingEscLink Category",
          "order": 71
        },
        "WaitingEscLink_RecID": {
          "type": "string",
          "title": "WaitingEscLink RecID",
          "description": "WaitingEscLink RecID",
          "order": 72
        },
        "helpdesk_Priority": {
          "type": "string",
          "title": "Helpdesk Priority",
          "description": "Helpdesk priority",
          "order": 132
        },
        "helpdesk_Priority_Valid": {
          "type": "string",
          "title": "Helpdesk Priority Valid",
          "description": "Helpdesk priority valid",
          "order": 131
        },
        "ivnt_RequestforInformationorData": {
          "type": "boolean",
          "title": "Ivnt Request For Information Or Data",
          "description": "Ivnt request for information or data",
          "order": 152
        },
        "ivnt_TeamsUserDetailsLink": {
          "type": "string",
          "title": "Ivnt Teams User Details Link",
          "description": "Ivnt teams user details link",
          "order": 157
        },
        "ivnt_TeamsUserDetailsLink_Category": {
          "type": "string",
          "title": "Ivnt Teams User Details Link Category",
          "description": "Ivnt teams user details link category",
          "order": 155
        },
        "ivnt_TeamsUserDetailsLink_RecID": {
          "type": "string",
          "title": "Ivnt Teams User Details Link RecID",
          "description": "Ivnt teams user details link RecID",
          "order": 156
        },
        "ivnt_UpdateRFI": {
          "type": "string",
          "title": "Ivnt Update RFI",
          "description": "Ivnt update RFI",
          "order": 153
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
