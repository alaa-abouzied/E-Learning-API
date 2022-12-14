from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_instructor=models.CharField(max_length=100)
    course_description=models.TextField()
    course_image=models.ImageField(upload_to="courses/images", null=True)
    course_rate=models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    #course_category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="track_courses" )
    course_created_at=models.DateTimeField(auto_now_add=True)
    student_course_name = models.ManyToManyField(User, related_name="student_course")
    student_course_instructor = models.ForeignKey(User, on_delete=models.CASCADE,related_name="instructor_course")
    def __str__(self):
        return self.course_name