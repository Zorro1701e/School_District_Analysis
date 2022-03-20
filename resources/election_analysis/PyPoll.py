# The DATA we need to retrieve.
    # 1. The total number of votes cast. (369,711)
    # 2. A complete lists of Candidates who recieved votes.
    # 3. Percentage of votes each candidate won.
    # 4. Total number of votes each candidate won. 
    # 5. Winner of election based on popular vote.


# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join(".", "election_results.csv")
file_to_save = os.path.join('.', 'election_analysis.txt')

# 1. Inititalize counter to Zero
total_votes = 0

#Candidate options 
candidate_options = []
# I DECLARE AN EMPTY DICTIONARY!
candidate_votes = {}

#open election results & read file
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        #Read the Header row
        headers = next(file_reader)

    #Print each row in the CSV file.
        for row in file_reader:
            # 2. add to the total vote count..
            total_votes += 1

        #print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate THEN...
        if candidate_name not in candidate_options:
            # ADD it to the list of candidates.
            candidate_options.append(candidate_name)

            # begin tracking THAT candidates vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# print the candidate vote dictionary
print(candidate_votes)
   