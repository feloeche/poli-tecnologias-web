from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Office(models.Model):
    code = models.CharField(max_length=20, unique=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='offices')

    def __str__(self) -> str:
        return f"Office {self.code}"


class Classroom(models.Model):
    code = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return f"Classroom {self.code}"


class Employee(models.Model):
    class Role(models.TextChoices):
        PROFESSOR = 'PROFESSOR', 'Professor'
        ADMINISTRATIVE = 'ADMINISTRATIVE', 'Administrative'

    class ProfessorType(models.TextChoices):
        NONE = 'NONE', 'None'  # for non-professors
        PERMANENT = 'PERMANENT', 'Permanent'
        CONTRACTOR = 'CONTRACTOR', 'Contractor'

    document_id = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=120)
    role = models.CharField(max_length=20, choices=Role.choices)
    professor_type = models.CharField(max_length=20, choices=ProfessorType.choices, default=ProfessorType.NONE)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name='employees')
    office = models.ForeignKey(Office, on_delete=models.PROTECT, related_name='employees')

    def __str__(self) -> str:
        return f"{self.full_name} ({self.document_id})"

    def clean(self) -> None:
        # Ensure professor_type only applies to professors
        from django.core.exceptions import ValidationError

        if self.role != Employee.Role.PROFESSOR and self.professor_type != Employee.ProfessorType.NONE:
            raise ValidationError('professor_type must be NONE when role is not PROFESSOR')
        if self.role == Employee.Role.PROFESSOR and self.professor_type == Employee.ProfessorType.NONE:
            raise ValidationError('professor_type is required for PROFESSOR')
