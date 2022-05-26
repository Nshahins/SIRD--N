from typing import TYPE_CHECKING, List

from sqlmodel import Field, SQLModel, Relationship

from .patientmetadata_join import PatientMetadata

if TYPE_CHECKING:  # pragma: no cover
    from .project import Project
    from .sample import Sample
    from .metadatavalue import MetadataValue
----------------------------



class Patient(SQLModel, table=True):
    """Patient Model"""

    # Primary Key
    patient_id: int | None = Field(primary_key=True, default=None)

    # Foreign Key
    project_id: int = Field(foreign_key="project.project_id")

    # Attributes
    external_patient_id: str
    updated_by: int | None

    # Generated Attributes
    sidr_patient_id: str | None = Field(default=None)

    # Many-to-One Relationships
    project: "Project" = Relationship(back_populates="patients")

    # One-to-Many Relationships
    samples: List["Sample"] = Relationship(back_populates="patients")

    # Many-to-Many Relationships
    metadata_values: List["MetadataValue"] = Relationship(link_model=PatientMetadata)
