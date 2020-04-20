'''
pro rata calculator 
'''

from pro_rata_class import Policy

if __name__ == "__main__":
    
    while True:
        print("please enter your name")
        user_name = (input())
        if user_name.isalpha() == True:
            break
        else:
            print("Please enter letters only")
            
    user_policy = Policy(user_name)
    
    #gets limits from user
    while True:
        print("Enter policy limits")
        try:
            policy_limit = int(input())
            break
        except ValueError:
            print("value must be a whole number")
            
    #sets policy limits 
    user_policy.set_pd_limits(policy_limit)
    
    #gets number of claimants 
    while True:
        print("Enter number of claimants")
        try:
            total_claiamnts = int(input())
            break
        except ValueError:
            print("value must be a whole number")
    
    #inititalizes list of damages 
    damage_list = []
    
    #gets each claimant damage amount
    for num in range(total_claiamnts):
        while True:
            print("Enter claimant {} damage".format(num+1))
            try:
                damages = float(input())
                if total_claiamnts < 0:
                    raise ValueError
                damage_list.append(damages)
                break
            except ValueError:
                print("value must be a numeric and must be positive")
    pro_rata_amounts = []
    for claimant in damage_list:
        pro_rata_amounts.append(claimant/sum(damage_list)*policy_limit)
    for num in range(total_claiamnts):
        print("claimant {} amount: ${:,.2f}".format((num+1), pro_rata_amounts[num]))
              
          
    


    
    