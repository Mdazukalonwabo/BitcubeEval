from django.db import models


# Lecturer can tech multiple Degrees
class Lecturer(models.Model):
    forenames = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    DOB = models.DateField(blank=False)    # Date of Birth

    def first_name(self):
        # should return the first given name even if multiple names are given
        first_name = self.forenames
        return first_name

    def full_name(self):
        # joins the forenames and surname to return the full name of the student
        # e.g forenames: Lonwabo Sipho, Surname: Mdazuka
        # return Lonwabo Sipho Mdazuka
        return f"{self.forenames} {self.surname}"

    def __str__(self):
        return self.full_name()


# One Degree can have multiple courses under it
class Degree(models.Model):
    degree_name = models.CharField(max_length=30)
    years = models.IntegerField(blank=False)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.degree_name} taught by {self.lecturer.full_name()}"


# multiple courses can be under one degree
class Courses(models.Model):
    course_name = models.CharField(max_length=30)
    duration_in_months = models.IntegerField(blank=False)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_name} in the {self.degree.degree_name}"


# students that can only be enrolled into one Degree only
class Student(models.Model):
    forenames = models.CharField(max_length=30)     # first_name(s)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    DOB = models.DateField(blank=False)     # Date of Birth
    degree = models.OneToOneField(Degree, models.SET_NULL, blank=True, null=True,)

    def first_name(self):
        # should return the first given name even if multiple names are given
        first_name = self.forenames.split(" ")
        return first_name

    def full_name(self):
        # joins the forenames and surname to return the full name of the student
        # e.g forenames: Lonwabo Sipho, Surname: Mdazuka
        # return Lonwabo Sipho Mdazuka
        return f"{self.forenames} {self.surname}"

    def __str__(self):
        return self.full_name()
