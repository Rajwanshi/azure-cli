from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

# TODO: Change 1.summary of command groups 3.Add description for alert list-summary

helps['alertsmanagement'] = """
type: group
short-summary: Manage alerts, smart-groups and action-rules for Azure Monitor.
"""

helps['alertsmanagement alert'] = """
type: group
short-summary: Manage Azure alerts
"""

helps['alertsmanagement alert list'] = """
type: command
short-summary: Get alerts list
long-summary: >
    Get list of alerts with optional filters as parameters.
parameters:
  - name: --target-resource
    type: string
    short-summary: Filter by target resource id.
  - name: --target-resource-type
    type: string
    short-summary: Filter by target resource type
  - name: --target-resource-group
    type: string
    short-summary: Filter by resource group.
  - name: --monitor-service
    type: string
    short-summary: Filter on monitor service.
  - name: --severity
    type: string
    short-summary: Filter by severity. Supported values : Sev0, Sev1, Sev2, Sev3, Sev4
  - name: --state
    type: string
    short-summary: Filter by alert state. Supported values - New, Acknowledged, Closed.
  - name: --alert-rule
    type: string
    short-summary: Filter by alert rule Id.
  - name: --smart-group-id
    type: string
    short-summary: Filter by smart group Id.
  - name: --include-context
    type: boolean
    short-summary: Include Context in response. Supported values : true, false.
  - name: --include-egress-config
    type: boolean
    short-summary: Include Egress config in response. Supported values : true, false.
  - name: --page-count
    type: string
    short-summary: Number of alerts returned at once..
  - name: --sort-by
    type: string
    short-summary: Sort the results by parameter. Supported values : name, severity, alertState, monitorCondition, targetResource, targetResourceName, targetResourceGroup, targetResourceType, startDateTime, lastModifiedDateTime.
  - name: --sort-order
    type: string
    short-summary: Sorting order. Supported values : asc, desc.
  - name: --time-range
    type: string
    short-summary: Supported time range values : 1h, 1d, 7d, 30d (Default is 1d).
  - name: --custom-time-range
    type: string
    short-summary: Supported format - <start-time>/<end-time> where time is in ISO-8601 format.
  - name: --select
    type: string
    short-summary: Project the required fields out of essentials. Expected input is comma-separated.
  - name: --monitor-condition
    type: string
    short-summary: Filter by monitor condition. Supported values : Fired, Resolved.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement alert list --severity "Sev2" --monitor-condition "Fired" --include-context true
"""

helps['alertsmanagement alert show'] = """
type: command
short-summary: Get alert for an alert Id
long-summary: >
    Get alert for an alert Id.
parameters:
  - name: --alert-id
    type: string
    short-summary: Alert Id to be fetched.
  examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement alert show --alert-id "afbf1b3a-0a6c-4f19-9c9b-644ccd7b1529"
"""
# TODO: Add examples
helps['alertsmanagement alert list-summary'] = """
type: command
short-summary: Get alerts list
long-summary: >
    Get list of alerts with optional filters as parameters.
parameters:
  - name: --group-by
    type: string
    short-summary: Supported values : severity, alertState, monitorCondition, monitorService, signalType, alertRule.
  - name: --include-smart-groups-count
    type: string
    short-summary: Supported values - true or false
  - name: --target-resource
    type: string
    short-summary: Filter by target resource id.
  - name: --target-resource-type
    type: string
    short-summary: Filter by target resource type.
  - name: --target-resource-group
    type: string
    short-summary: Filter by resource group.
  - name: --monitor-service
    type: string
    short-summary: Filter on monitor service.
  - name: --severity
    type: string
    short-summary: Filter by severity. Supported values : Sev0, Sev1, Sev2, Sev3, Sev4
  - name: --state
    type: string
    short-summary: Filter by alert state. Supported values - New, Acknowledged, Closed.
  - name: --alert-rule
    type: string
    short-summary: Filter by alert rule Id.
  - name: --time-range
    type: string
    short-summary: Supported time range values : 1h, 1d, 7d, 30d (Default is 1d).
  - name: --custom-time-range
    type: string
    short-summary: Supported format - <start-time>/<end-time> where time is in ISO-8601 format.
  - name: --monitor-condition
    type: string
    short-summary: Filter by monitor condition. Supported values : Fired, Resolved.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az cdn custom-domain create -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name --hostname www.example.com
"""

helps['alertsmanagement alert show-history'] = """
type: command
short-summary: Gets Alert History information
long-summary: >
    Gets Alert History information
parameters:
  - name: --alert-id
    type: string
    short-summary: Unique identifier of Alert.
  examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement alert show-history --alert-id "afbf1b3a-0a6c-4f19-9c9b-644ccd7b1529"
"""

helps['alertsmanagement alert update-state'] = """
type: command
short-summary: Updates alert state
long-summary: >
    Updates alert state
parameters:
  - name: --alert-id
    type: string
    short-summary: Id of alert to be updated.
  - name: --state
    type: string
    short-summary: Filter by alert state. Supported values - New, Acknowledged, Closed.
  examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement alert update-state --alert-id "afbf1b3a-0a6c-4f19-9c9b-644ccd7b1529" --state "Closed"
"""

helps['alertsmanagement smart-group'] = """
type: group
short-summary: Manage smart groups
"""

helps['alertsmanagement smart-group list'] = """
type: command
short-summary: Gets Smart Groups list
long-summary: >
    Gets Smart Groups list based on filters passed as parameters
parameters:
  - name: --time-range
    type: string
    short-summary: Supported time range values : 1h, 1d, 7d, 30d (Default is 1d).
  - name: --sort-by
    type: string
    short-summary: Sort the results by parameter. Supported values : name, severity, alertState, monitorCondition, targetResource, targetResourceName, targetResourceGroup, targetResourceType, startDateTime, lastModifiedDateTime.
  - name: --sort-order
    type: string
    short-summary: Sorting order. Supported values : asc, desc.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
         az alertsmanagement smart-group list --time-range "1h"
"""

helps['alertsmanagement smart-group show'] = """
type: command
short-summary: Gets Smart Group for a smart-group Id
long-summary: >
    Gets Smart Group for a smart-group Id
parameters:
  - name: --smart-group-id
    type: string
    short-summary: Id of the smart group to be fetched.
  examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement smart-group show --smart-group-id "afbf1b3a-0a6c-4f19-9c9b-644ccd7b1529"
"""

helps['az alertsmanagement  smart-group show-history'] = """
type: command
short-summary: Gets smart group history
long-summary: >
    Get alert based in alert Id.
parameters:
  - name: --smart-group-id
    type: string
    short-summary: Id of the smart group to be fetched.
  examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement smart-group show-history --smart-group-id "afbf1b3a-0a6c-4f19-9c9b-644ccd7b1529"
"""

helps['alertsmanagement smart-group update-state'] = """
type: command
short-summary: Updates smart group state
long-summary: >
    Get alert based in alert Id.
parameters:
  - name: --smart-group-id
    type: string
    short-summary: Id of smart group to be updated.
  - name: --state
    type: string
    short-summary: Filter by alert state. Supported values - New, Acknowledged, Closed.
  examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement smart-group update-state --smart-group-id "afbf1b3a-0a6c-4f19-9c9b-644ccd7b1529" --state "Acknowledged"
"""

helps['alertsmanagement action-rule'] = """
type: group
short-summary: Create, update or ge information an action rule.
"""

helps['alertsmanagement action-rule list'] = """
type: command
short-summary: Get Action Rules Information
long-summary: >
    Get Action Rules Information.
parameters:
  - name: --resource-group-name
    type: string
    short-summary: Resource group in which action rule reside.
  - name: --target-resource
    type: string
    short-summary: Filter by target resource id.
  - name: --target-resource-type
    type: string
    short-summary: Filter by target resource type
  - name: --target-resource-group
    type: string
    short-summary: Filter by resource group.
  - name: --monitor-service
    type: string
    short-summary: Filter on monitor service.
  - name: --severity
    type: string
    short-summary: Filter by severity. Supported values : Sev0, Sev1, Sev2, Sev3, Sev4
  - name: --alert-rule
    type: string
    short-summary: Filter by alert rule Id.
  - name: --impacted-scope
    type: string
    short-summary: Filter by alert rule Id.
  - name: --description
    type: string
    short-summary: Gets all actions rules in a subscription filter by description.
  - name: --action-group
    type: string
    short-summary: Gets all actions rules in a subscription filter by action group.
  - name: --name
    type: string
    short-summary: Gets all actions rules in a subscription filter by action rule name.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement action-rule list --resource-group-name "test-rg" --severity "Sev2" --monitor-service "Platform"
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement action-rule list --resource-group-name "test-rg" --name "Test-Action-Rule"
"""
# TODO: Add examples
helps['alertsmanagement action-rule show'] = """
type: command
short-summary: Get alerts list
long-summary: >
    Get list of alerts with optional filters as parameters.
parameters:
  - name: --resource-group-name
    type: string
    short-summary: Resource group in which action rule reside.
  - name: --name
    type: string
    short-summary: Gets all actions rules in a subscription filter by action rule name.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az cdn custom-domain create -g group --endpoint-name endpoint --profile-name profile \\
            -n domain-name --hostname www.example.com
"""
# TODO: Command example mismatch
helps['alertsmanagement action-rule set'] = """
type: command
short-summary: Create or update an action rule.
long-summary: >
    Create or update an action rule.
parameters:
  - name: --resource-group-name
    type: string
    short-summary: Resource group in which action rule reside.
  - name: --name
    type: string
    short-summary: Gets all actions rules in a subscription filter by action rule name.
  - name: --alert-rule
    type: string
    short-summary: Filter by alert rule Id.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement action-rule set --resource-group-name "test-rg" --name "Test-AR" -Scope "/subscriptions/dd91de05-d791-4ceb-b6dc-988682dc7d72/resourceGroups/alertslab","/subscriptions/dd91de05-d791-4ceb-b6dc-988682dc7d72/resourceGroups/Test-VMs" -SeverityCondition "Equals:Sev0,Sev1" -MonitorCondition "NotEquals:Resolved" -Description "Test description" -Status "Enabled" -ActionRuleType "Suppression" -ReccurenceType "Weekly" -SuppressionStartTime "06/26/2018 06:00:00" -SuppressionEndTime "07/27/2018 06:00:00" -ReccurentValue 1,4,6
"""
# TODO: Add patch parameter to the example
helps['alertsmanagement action-rule update'] = """
type: command
short-summary: Updates action rule properties.
long-summary: >
    Updates action rule properties.
parameters:
  - name: --resource-group-name
    type: string
    short-summary: Resource group in which action rule reside.
  - name: --name
    type: string
    short-summary: Gets all actions rules in a subscription filter by action rule name.
  - name: --patch
    type: string
    short-summary: changes to be made in rule.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        az alertsmanagement action-rule update --resource-group-name "test-rg" --name "Test-ActionRule" -Status "Disabled"
"""

helps['alertsmanagement action-rule delete'] = """
type: command
short-summary: Deletes a action group
long-summary: >
    Deletes a action group based on parameters
parameters:
  - name: --resource-group-name
    type: string
    short-summary: Resource group in which action rule reside.
  - name: --name
    type: string
    short-summary: Gets all actions rules in a subscription filter by action rule name.
examples:
  - name: Create a custom domain within an endpoint and profile.
    text: >
        alertsmanagement action-rule delete --resource-group-name "test-rg" -Name --name
"""
