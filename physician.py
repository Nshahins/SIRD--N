from typing import TYPE_CHECKING, List

from sqlmodel import SQLModel, Field, Relationship

from .orderphysician_join import OrderPhysician
from .physicianmetadata_join import PhysicianMetadata

if TYPE_CHECKING:  # pragma: no cover
    from .order import Order
    from .metadatavalue import MetadataValue


class Physician(SQLModel, table=True):
    """Physician Model"""

    # Primary Key
    physician_id: int | None = Field(primary_key=True, default=None)

    # Attributes
    physician_name: str
    physician_npi: str
    updated_by: int | None

    # Many-to-Many Relationships
    orders: List["Order"] = Relationship(
        link_model=OrderPhysician, back_populates="physicians"
    )

    metadata_values: List["MetadataValue"] = Relationship(link_model=PhysicianMetadata)


