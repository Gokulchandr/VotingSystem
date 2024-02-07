nominee1=input("Enter the name of 1st nominee: ")
nominee2=input("Enter the name of 2st nominee: ")
n1_votes=0
n2_votes=0
voter_id=list(map(int,input("Enter eligible voters: ").split()))
no_of_voter=len(voter_id)
while True:
    if voter_id==[]:
        print("Voting session is over !!!")
        if n1_votes>n2_votes:
            percent=(n1_votes/no_of_voter)*100
            print()
            print(nominee1,"has won the election with ","{:.2f}".format(percent),"% of votes")
            print()
            break
        elif n2_votes>n1_votes:
            percent=(n2_votes/no_of_voter)*100
            print()
            print(nominee2,"has won the vote with","{:.2f}".format(percent),"% of votes")
            print()
            break
        else:
            print()
            print("Both of them have equal number of votes !!!!")
            print()
            break
    voter = int(input("Enter your voter id : "))
    if not voter in voter_id:
        print("You are not a valid User")
        voter = int(input("Enter your valid voter id : "))
    elif voter in voter_id:
        print("You are a voter ")
        voter_id.remove(voter)
        print("----------------------------------")
        print("To give vote to",nominee1,"Press 1")
        print("To give vote to",nominee2,"Press 2")
        print("----------------------------------")
        vote=int(input("Enter your precious vote : "))
        
        if vote==1:
            n1_votes+=1
            print(nominee1,"Thank you to give your important vote to them !!")
        elif vote==2:
            n2_votes+=1
            print(nominee2,"Thank you to give your important vote to them !!")
        elif vote>2:
            print("Please Check your pressed key !!")
        else:
            print("You are not voter or You are already voted")

