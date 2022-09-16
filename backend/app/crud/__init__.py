from .crud_item import item
from .crud_user import user
from .crud_joke import joke

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)