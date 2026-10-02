class Service:
 def run(self,value):
  x=value.lower(); s='critical' if any(k in x for k in ('outage','down','data loss')) else 'warning'
  return {'incident':value,'severity':s,'proposed_actions':['validate alert','correlate signals','retrieve runbook','request approval'],'auto_remediation':False}