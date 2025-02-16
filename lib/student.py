#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        # Initialize the parent class User with first and last name
        super().__init__(first_name, last_name)
        # Initialize knowledge with an empty list
        self.knowledge = []
    
    def learn(self, info):
        # Add learned information to the knowledge list
        self.knowledge.append(info)
