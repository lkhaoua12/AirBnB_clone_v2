#!/usr/bin/python3
"""
    This module defines the Review class representing reviews in the database.
"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

# Define a base class for declarative models
Base = declarative_base()


class Review(BaseModel, Base):
    """
    Attributes:
    - id (int): The unique identifier for the review.
    - created_at (datetime): The timestamp when the review was created.
    - updated_at (datetime): The timestamp when the review was last updated.
    - text (str): The text content of the review (up to 1024 characters).
    - place_id (str): The ID of the place associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    """
    __tablename__ = "reviews"
    # Define columns for the Review table
    # The text content of the review
    text = Column(String(1024), nullable=False)

    # ID of the associated place
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    # ID of the user who wrote the review

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
