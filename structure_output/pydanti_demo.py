from pydantic import BaseModel , EmailStr ,field
from typing import Optional


class Student(BaseModel):
    name: str 
    age: Optional[int] = None  # use of optional type hint
    email: Optional[EmailStr] = None  # use of emailstr
    cgpa: Optional[float] = field(default=None, ge=0.0, le=4.0)  # use of field with constraints

new_student = {"name":"Saurav kumar",
"age": 21,
"email": "saurav.kumar@example.com",
"cgpa": 3.5
}

student  = Student(**new_student)

print((student))

student_dict =dict(["name", "email"])  # convert to dict with only name and email fields
student_json = student.model_dump_json()  # convert to json string

# pydantic is a data validation and settings management library for 
# Python, based on Python type annotations. 
# It allows you to define data models with type hints and automatically validates the input data against those models.
#  In this example, we define a `Student` model with a single field `name` of type `str`. We then create a new student dictionary and 
# use it to instantiate a `Student` object, which is validated against the defined model.
#  Finally, we print the type of the created `student` object, which will be `<class '__main__.Student'>`.