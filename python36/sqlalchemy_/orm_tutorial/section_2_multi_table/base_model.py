from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

from .user import User
from .address import Address

# Build Relationships
# User.addresses = relationship("Address", order_by=Address.id, back_populates="user")
# Address.user = relationship("User", back_populates="addresses")
