"""
Module représentant les modèles de données pour une application de formation de Pokémon.

Ce module définit trois modèles SQLAlchemy : Trainer, Pokemon et Item.
Ces modèles sont utilisés pour stocker des informations sur les dresseurs, leurs Pokémon et
les objets qu'ils possèdent.

Classes :
    - Trainer : Représente un dresseur de Pokémon.
    - Pokemon : Représente un Pokémon associé à un dresseur.
    - Item : Représente un objet dans l'inventaire d'un dresseur.
"""

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .sqlite import Base


class Trainer(Base):
    """
        Class representing a Pokémon trainer
    """
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date)

    inventory = relationship("Item", back_populates="trainer")
    pokemons = relationship("Pokemon", back_populates="trainer")

    def __str__(self):
        return f"Trainer(id={self.id}, name={self.name}, birthdate={self.birthdate})"

    def get_pokemon_count(self):
        """
        Get the count of Pokémon associated with the trainer.
        """
        return len(self.pokemons)


class Pokemon(Base):
    """
    Class representing a Pokémon
    Parameters:
        api_id (int): ID from the PokéAPI
        name (str): Populated with the PokéAPI data
    """

    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, index=True)
    name = Column(String, index=True)
    custom_name = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="pokemons")

    def __str__(self):
        """
        Returns a string representation of the Pokémon.
        """
        return f"Pokemon(id={self.id}, name={self.name}, custom_name={self.custom_name})"

    def to_dict(self):
        """
        Converts the Pokémon instance to a dictionary.
        Returns:
            dict: A dictionary representation of the Pokémon.
        """
        return {
            "id": self.id,
            "api_id": self.api_id,
            "name": self.name,
            "custom_name": self.custom_name,
            "trainer_id": self.trainer_id
        }


class Item(Base):
    """
        Class representing a Pokémon trainer
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="inventory")

    def __str__(self):
        """
        Returns a string representation of the Item.
        """
        return f"Item(id={self.id}, name={self.name})"

    def to_dict(self):
        """
        Converts the Pokémon instance to a dictionary.
        Returns:
            dict: A dictionary representation of the Item.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "trainer_id": self.trainer_id
        }
