# import csv file
import os
import csv

# set the path for the budget data csv file
election_csv = os.path.join("Resources", "election_data.csv")

# read in csv file
with open(election_csv, 'r') as csvfile:

    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # set variables
    Votes = []
    Candidates = []
    # create empty list for each candidate
    K = []
    C = []
    L = []
    O = []

    # find total votes
    for row in csvreader:
        Votes.append(row[0]) 
        Candidates.append(row[2])

        VoteCount = len(Votes)
        
    # separate candidates and add up how many votes each received
    for i in Candidates:
        if i == "Khan":
            K.append(i)
            Kvotes = len(K)
        elif i == "Correy":
            C.append(i)
            Cvotes = len(C)
        elif i == "Li":
            L.append(i)
            Lvotes = len(L)
        else:
            O.append(i)
            Ovotes = len(O)
    
    # find percentage of votes each candidate won
    KPercent = round((Kvotes / VoteCount)*100, 3)
    CPercent = round((Cvotes / VoteCount)*100, 3)
    LPercent = round((Lvotes / VoteCount)*100, 3)
    OPercent = round((Ovotes / VoteCount)*100, 3)

    # compare percentages against each other to determine winner
    if OPercent > max(KPercent, CPercent, LPercent):
        Winner = "O'Tooley"
    elif LPercent > max(KPercent, CPercent, OPercent):
        Winner = "Li"
    elif CPercent > max(KPercent, LPercent, OPercent):
        Winner = "Correy"
    else:
        Winner = "Khan"
    
    # print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {VoteCount}")
    print("-------------------------")
    print(f"Khan: {KPercent:.3f}% ({Kvotes})")
    print(f"Correy: {CPercent:.3f}% ({Cvotes})")
    print(f"Li: {LPercent:.3f}% ({Lvotes})")
    print(f"O'Tooley: {OPercent:.3f}% ({Ovotes})")
    print("-------------------------")
    print(f"Winner: {Winner}")
    print("-------------------------")

# set path for txt file
txtpath = os.path.join("analysis", "results.txt")

# send results to a txt file
with open(txtpath, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {VoteCount}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {KPercent:.3f}% ({Kvotes})\n")
    txtfile.write(f"Correy: {CPercent:.3f}% ({Cvotes})\n")
    txtfile.write(f"Li: {LPercent:.3f}% ({Lvotes})\n")
    txtfile.write(f"O'Tooley: {OPercent:.3f}% ({Ovotes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {Winner}\n")
    txtfile.write("-------------------------\n")