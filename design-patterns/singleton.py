"""
Example:
1. Logger Class
2. Shared Class for accessing resources
3. Configuration Class

How to Use and Benefits:
1. Thread safe implementation.
"""
from typing import Optional
import threading

class ExternalAuthroizationPool:
    instance : Optional['ExternalAuthroizationPool']= None
    lock = threading.Lock()

    def __new__(cls, username, password):
        if cls.instance is None:
            with cls.lock:
                if cls.instance is None:
                    cls.instance = super().__new__(cls)

        return cls.instance
    
    def __init__(self, username, password):
        if not hasattr(self, 'initialized'):
            self.username = username
            self.password = password
            self.initialized = True
    
if __name__ == "__main__":
    eap1 = ExternalAuthroizationPool("dummy1", "dummy1")
    print(eap1.username)
    eap2 = ExternalAuthroizationPool("dummy2", "dummy2") # This wont be setting
    print(eap1 is eap2) # True
    print(eap2.username) # No changes, becuase the instance is already initialized.