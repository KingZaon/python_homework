import csv

voter_id = []
candidate = []
with open("election_data.csv.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        voter_id.append(row[0])
        candidate.append(row[2])
#Write "Election Results" with total votes done
print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(voter_id)}")
print("---------------------------")

# Get list of candidates values of specific candidates
cands = list(set(candidate))
cands.sort()
# Get a vote count of candidates
vote_candidates = []
for cand in cands:
    vote_candidates.append(candidate.count(cand))
# Write code to list out pertectange and totals of votes with the winner of candidates
for i in range(len(cands)):
    print(f"{cands[i]}: {'{:.2%}'.format(vote_candidates[i]/len(candidate))} ({vote_candidates[i]})")
print("--------------------")
print(f"Winner: {cands[vote_candidates.index(max(vote_candidates))]}")
print("-------------------\n")



# 