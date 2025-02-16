#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        # Initialize the parent class User with first and last name
        super().__init__(first_name, last_name)
        # Initialize knowledge with some default topics
        self.knowledge = ["Math", "Science", "History", "Literature"]
    
    def teach(self):
        # Return a random topic from the knowledge list
        return random.choice(self.knowledge)
