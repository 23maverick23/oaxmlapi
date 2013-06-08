# -*- coding: utf-8

ADDRESS_FIELDS = (
    'first', 'middle', 'last', 'salutation', 'email', 'phone',
    'fax', 'mobile', 'addr1', 'addr2', 'addr3', 'addr4',
    'city', 'state', 'zip', 'country'
)

XML_DATATYPES = (
    'Actualcost', 'Address', 'Agreement', 'Agreement_to_project', 'Approval',
    'Attachment', 'Booking', 'BookingType', 'Budget', 'BudgetAllocation',
    'Category', 'Category_1', 'Category_2', 'Category_3', 'Category_4',
    'Category_5', 'Ccrate', 'Company', 'Contact', 'Costcategory',
    'Costcenter', 'Costtype', 'Currency', 'Currencyrate', 'CustField',
    'Customer', 'Customerpo', 'Customerpo_to_project', 'CustomerProspect',
    'Date', 'Deal', 'Dealcontact', 'Dealschedule', 'Department', 'Entitytag',
    'Envelope', 'Error', 'Estimate', 'Estimatedadjustment',
    'Estimateexpense', 'Estimatelabor', 'Estimatemarkup', 'Estimatephase',
    'Event', 'Filter', 'Filterset', 'Flag', 'ForexInput', 'Fulfillment',
    'Hierarchy', 'HierarchyNode', 'History', 'ImportExport', 'Invoice',
    'Issue', 'IssueCategory', 'IssueSeverity', 'IssueSource', 'IssueStage',
    'IssueStatus', 'Item', 'Jobcode', 'Leave_accrual_rule',
    'Leave_accrual_rule_to_user', 'Leave_accrual_transaction', 'LoadedCost',
    'Login', 'Module', 'Notes', 'Payment', 'Paymentterms', 'Paymenttype',
    'Payrolltype', 'Preference', 'Product', 'Project', 'Projectassign',
    'Projectbillingrule', 'Projectbillingtransaction', 'Projectgroup',
    'Projectlocation', 'Projectstage', 'Projecttask', 'Projecttask_type',
    'Projecttaskassign', 'Proposal', 'Proposalblock', 'Purchase_item',
    'Purchaseorder', 'Purchaser', 'Purchaserequest', 'Ratecard',
    'RatecardItem', 'Reimbursement', 'Repeat', 'Report', 'Request_item',
    'Resourceprofile', 'Resourceprofile_type', 'RevenueContainer',
    'Revenue_recognition_rule', 'Revenue_recognition_rule_amount',
    'Revenue_recognition_transaction', 'RevenueStage', 'Role',
    'Schedulebyday', 'Scheduleexception', 'Schedulerequest',
    'Schedulerequest_item', 'Slip', 'SlipProjection', 'Slipstage', 'TagGroup',
    'TagGroupAttribute', 'TargetUtilization', 'Task', 'TaskTimecard',
    'TaxLocation', 'TaxRate', 'Term', 'Ticket', 'Timecard', 'Timesheet',
    'Timetype', 'Todo', 'Uprate', 'User', 'UserWorkSchedule', 'Vendor',
    'Viewfilter', 'Viewfilterrule', 'Workspacelink', 'Workspaceuser',
)

READ_METHODS = (
    'all', 'equal to', 'not equal to', 'user', 'project', 'not exported',
)

READ_ATTRIBUTES = (
    'limit', 'deleted', 'include_flags', 'include_nondeleted',
    'with_project_only', 'base_currency', 'generic', 'enable_custom',
    'filter', 'field',
)
