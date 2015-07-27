from .manager import Manager

class LiquidPlanner(object):
    """An ORM-like interface to the LiquidPlanner API"""

    # (name, url, options)
    MANAGERS = (
            # The special two that don't require a workspace id
            ('account', '/account', {}),
            ('workspaces', '/workspaces', {}),

            # The rest in the same order as listed at
            # https://app.liquidplanner.com/api/help/types
            ('activities', '/workspaces/{workspace_id}/activities', {}),
            #('alerts', '/workspaces/{workspace_id}/alerts', {}),
            ('members', '/workspaces/{workspace_id}/members', {}),
            #('assignments', '/workspaces/{workspace_id}/assignments', {}), 
            #('changes', '/workspaces/{workspace_id}/changes', {}), 
            ('checklist_items', '/workspaces/{workspace_id}/checklist_items', {}), 
            ('clients', '/workspaces/{workspace_id}/clients', {}),
            ('comments', '/workspaces/{workspace_id}/comments', {}), 
            ('custom_fields', '/workspaces/{workspace_id}/custom_fields', {}), 
            #('custom_field_values', '/workspaces/{workspace_id}/custom_field_values', {}), 
            #('dependencies', '/workspaces/{workspace_id}/dependency', {}), 
            ('documents', '/workspaces/{workspace_id}/documents', {}), 
            #('estimates', '/workspaces/{workspace_id}/estimates', {}), 
            ('events', '/workspaces/{workspace_id}/events', {}), 
            ('folders', '/workspaces/{workspace_id}/folders', {}), 
            #('inbox', '/workspaces/{workspace_id}/inbox', {}), 
            ('links', '/workspaces/{workspace_id}/links', {}), 
            ('milestones', '/workspaces/{workspace_id}/milestones', {}), 
            #('notes', '/workspaces/{workspace_id}/notes', {}), 
            ('packages', '/workspaces/{workspace_id}/packages', {}), 
            ('partial_day_events', '/workspaces/{workspace_id}/partial_day_events', {}), 
            ('projects', '/workspaces/{workspace_id}/projects', {}),
            #('recurrence_pattern', '/workspaces/{workspace_id}/reccurence_patterns', {}),
            #('root', '/workspaces/{workspace_id}/root', {}),
            #('occurrences', '/workspaces/{workspace_id}/occurrences', {}),
            ('tags', '/workspaces/{workspace_id}/tags', {}),
            ('tasks', '/workspaces/{workspace_id}/tasks', {}),
            ('teams', '/workspaces/{workspace_id}/teams', {}),
            #('timers', '/workspaces/{workspace_id}/timers', {}),
            ('timesheet_entries', '/workspaces/{workspace_id}/timesheet_entries', {}),
            ('timesheets', '/workspaces/{workspace_id}/timesheets', {}),
            #('snapshots', '/workspaces/{workspace_id}/snapshots', {}),
            ('webhooks', '/workspaces/{workspace_id}/webhooks', {}),
    )

    def __init__(self, credentials, use_first_workspace=True):
        self.workspace_id = None
        self.credentials = credentials

        for manager in self.MANAGERS:
            setattr(self, manager[0], Manager(self, *manager))

        if use_first_workspace:
            self.workspace_id = self.workspaces.all()[0]['id']

