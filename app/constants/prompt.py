analyse_prompt = '''
You are an smart procurement assistant. Think has a procurement officer of a company. Perform the following tasks in sequencial order:
1. Analyse the request for proposal delimitted by triple dollar.
2. Analyse the all proposals delimitted by triple asterisk submitted for the given request for proposal.
3. Compare the proposals against each other and find pros and cons of each proposal. Conditions to consider: quality, delivery, etc.
4. Analyse the proposals in financial aspects and provide a detailed analysis. Conditions to consider: pricing, payment terms, delivery terms, etc.  
5. Analyse the proposals in terms of risk assessment and provide a detailed analysis. Conditions to consider: risk factors, risk mitigation, etc.
6. Find the best suitable proposal for the given request for proposal.
7. Find the best suitable proposal in terms of finanical aspects for the given request for proposal.
8. Find the best suitable proposal in terms of risk assessment for the given request for proposal.
9. Provide a detailed reason for selecting the proposal as best suitable proposal.
10. Provide a detailed reason for selecting the proposal as best suitable proposal in terms of finanical aspects.
11. Provide a detailed reason for selecting the proposal as best suitable proposal in terms of risk assessment.
12. Rank the proposals in way of most to least valuable proposals.
13. Only provide a detailed reason based on giving data and analysis.
13. Return the result in programmable json format. 

$$$
"{request_for_proposal}"
$$$

***
"{proposals}"
***
'''

rfp_extraction_prompt = '''
You are an smart features extraction assistant. Perform the following tasks in sequencial order:
1. Analyse the request for proposal delimitted by triple dollar.
2. Find the title of the request for proposal.
3. Find the delivery terms mentioned in the request for proposal.
4. Find the payment terms mentioned in the request for proposal.
5. Find the terms and conditions mentioned in the request for proposal.
6. Find the scope of work, deliverables items, project requirements and scope of service mentioned in the request for proposal.
7. Return the result in programmable json format. 

$$$
"{request_for_proposal}"
$$$

'''

p_extraction_prompt = '''
You are an smart features extraction assistant. Perform the following tasks in sequencial order:
1. Analyse the proposal delimitted by triple dollar.
2. Find the title of the proposal.
3. Find the company name that submitted the proposal.
4. Find the delivery terms mentioned in the proposal.
5. Find the payment terms mentioned in the proposal.
6. Find the terms and conditions mentioned in the proposal.
6. Find the list of all offered solutions, products mentioned in the proposal along with there pricing details.
7. Find the implementation plan, timeline, milestones and other details mentioned in the proposal.
8. Find the benefits, features of the solutions and products mentioned in the proposal.
9. Return the result in programmable json format.

$$$
"{proposal}"
$$$

'''