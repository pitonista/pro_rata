class Policy:
    
    
    
    def __init__(self, policy_holder, pd_limits = 5000):
        '''creates claimant class object'''
        self.__pd_limits = pd_limits 
        self.policy_holder = policy_holder
        
    
    def get_pd_limits(self):
        return self.__pd_limits
    
    def set_pd_limits(self, pd_limits):
        self.__pd_limits = pd_limits
        
        
        
        
    
        
        
        
        
        