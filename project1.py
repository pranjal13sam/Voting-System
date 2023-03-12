
print("------------------WELCOME----------------")
print("\n\n")
print("Your vote matters a Lot so Please vote Accordingly")


nominee1=input("Enter the name of 1st nominee: ")
nominee2=input("Enter the name of 2nd nominee: ")


#initially vote count of both the candidates should be 0
nm1_votes=0
nm2_votes=0

voter_id=[1,2,3,4,5]

no_of_voter=len(voter_id)

while True:
    if voter_id==[]:#to check when voter list is completed
        print("Voting session is over!!!")
        if nm1_votes>nm2_votes:
            percent=(nm1_votes/no_of_voter)*100
            print(nominee1,"has won the Elections with ",percent,"% of votes")
            break
        elif nm2_votes>nm1_votes:
            percent=(nm2_votes/no_of_voter)*100
            print(nominee2,"has won the Elections with ",percent,"% of votes")
            break
        else:
            print("Votes of both the nominees are equal so let the present Government decide who will Rule!!!")
            break
    
    voter=int(input("Enter your voter Id: "))
    if voter in voter_id:
        print("You are a voter ")
        voter_id.remove(voter)#removing voter so that he is not allowed to vote again
        print("-----------------------------------")
        print("To give vote to ",nominee1,"Press 1")
        print("To give vote to ",nominee2,"press 2")
        print("-----------------------------------")
        vote=int(input("Enter Your Vote: "))
        if vote==1:
            nm1_votes+=1
            print("Your voted",nominee1,"Thankyou for your precious vote!!")
        elif vote==2:
            nm2_votes+=2
            print("you voted",nominee2,"Thanks for your precious vote!!")
        elif vote>3:
            print("Check your pressed key!!")
        else:
            print("You are not a voter anymore OR you have already voted")


            
