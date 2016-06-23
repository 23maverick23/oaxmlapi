# -*- coding: utf-8

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

try:
    import simplejson as json
except ImportError:
    import json


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
    'Envelope', 'Error', 'Estimate', 'Estimateadjustment',
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
    'RateCardItem', 'Reimbursement', 'Repeat', 'Report', 'Request_item',
    'Resourceprofile', 'Resourceprofile_type', 'RevenueContainer',
    'Revenue_recognition_rule', 'Revenue_recognition_rule_amount',
    'Revenue_recognition_transaction', 'RevenueStage', 'Role',
    'Schedulebyday', 'Scheduleexception', 'Schedulerequest',
    'Schedulerequest_item', 'Slip', 'SlipProjection', 'Slipstage', 'TagGroup',
    'TagGroupAttribute', 'TargetUtilization', 'Task', 'TaskTimecard',
    'TaxLocation', 'TaxRate', 'Term', 'Ticket', 'Timecard', 'Timesheet',
    'Timetype', 'Todo', 'Uprate', 'User', 'UserWorkschedule', 'Vendor',
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


def elem2dict(elem, strip=True):
    """
    Convert an ElementTree() object into a Python dictionary.

    Arguments:
        elem (obj): a valid ElementTree() object
        strip (bool): a boolean value for striping whitespace (optional)

    Credit: Hay Kranen (https://github.com/hay/xml2json)

    """
    d = {}
    for key, value in elem.attrib.items():
        d['@'+key] = value

    # loop over subelements to merge them
    for subelem in elem:
        v = elem2dict(subelem, strip=strip)
        tag = subelem.tag
        value = v[tag]
        try:
            # add to existing list for this tag
            d[tag].append(value)
        except AttributeError:
            # turn existing entry into a list
            d[tag] = [d[tag], value]
        except KeyError:
            # add a new non-list entry
            d[tag] = value
    text = elem.text
    tail = elem.tail
    if strip:
        # ignore leading and trailing whitespace
        if text:
            text = text.strip()
        if tail:
            tail = tail.strip()

    if tail:
        d['#tail'] = tail

    if d:
        # use #text element if other attributes exist
        if text:
            d["#text"] = text
    else:
        # text is the value if no attributes
        d = text or None

    return {elem.tag: d}


def xml2json(xmlstring, strip=True):
    """
    Convert an XML string into a JSON string.

    Arguments:
        xmlstring (str): a valid XML string
        strip (bool): a boolean value for striping whitespace (optional)

    Credit: Hay Kranen (https://github.com/hay/xml2json)

    """
    elem = ET.fromstring(xmlstring)
    return json.dumps(elem2dict(elem, strip=strip))
