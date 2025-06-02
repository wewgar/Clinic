from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"