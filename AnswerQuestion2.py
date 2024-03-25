def register_party(party_name, reg_number,member_count):
    register.append({'party_name': input("Enter Party name"),
                     'reg_number': int(input("Enter Registration number :")),
                     'member_count': int(input("Enter Number of Members"))})

def register_party(parties):
    for party in parties:
        if party["member_count"] >= 5000:
            print(f"Party {party['party_name']} meets the criteria for registration.")
        else:
            print(f"Party {party['party_name']} does not meet the criteria for registration.")



last_registration_number = 10003318
new_party = {
    "party_name": "MK party",
    "reg_number": last_registration_number + 1,
    "member_count": 5300
}
register_party([new_party])

# 2.3
def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    if voter_id in voter_info:
        voter_info[voter_id].update({"name": name, "voting_district": voting_district})
        if not voter_info[voter_id]["has_voted"]:
            voter_info[voter_id]["has_voted"] = has_voted
    else:
        voter_info[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}


voter_info = {}
update_voter_info(voter_info, "ID123", "John Doe", "District A", False)
update_voter_info(voter_info, "ID456", "Jane Smith", "District B", True)


parties_on_ballot = ["ANC", "DA", "EFF", "IFP", "ACDP", "COPE"]
filtered_parties = [party for party in parties_on_ballot if len(party) >= 1000]
print(filtered_parties)


filtered_parties_list = list(filter(lambda party: len(party) >= 1000, parties_on_ballot))
print(filtered_parties_list)
voters = [
    {"name": "Nkoinamandla", "registered": True},
    {"name": "Thandeka", "registered": False},
    {"name": "Luthando", "registered": True}
]

registered_voters = list(filter(lambda voter: voter["registered"], voters))
print(registered_voters)
