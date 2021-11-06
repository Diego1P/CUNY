# CUNY
## rough draft of tasks
- [ ] The front-end GUI is going to be handled with html/CSS + Bootstrap.
- [ ] Forms will be handled through Django with crispy forms, a popular method of form handling. 
- [ ] Applying to become a student will happen with user registration, by default the student user will start off with a default gpa of 4.0, gaining admission to the school as a freshman. Django comes with an admin site allowing further actions, such as giving someone admin privileges. The admin site will act as registrar which can choose to drop a student if they choose to. 
- [ ] The class/course model will be handled with date-time, the challenge being that for demonstration purposes all courses will still be available when we run the website from the local server. We can have the model with a time field that expires representing the period.
- [ ] An alert message will be sustained on the student user’s registration page as long as the number of courses is below 2. Similarly for cancelled courses we can have an alert message saying that the course is no longer available from the student registration page. 
-[ ] Will need to create a review model, that will store the number of stars for a course (foreign key) and will contain a comment field that will filter for words to remove foul language (library)
- [ ] The graduation application can be a message from the student user model to the admin page where, after viewing the transcript of the student (8 classes) there can be an evaluation.
- [ ] Complaints will also go to the admin page as a message
- [ ] Dropping a class will be handled with CRUD user model with Django
- [ ] he creative feature for that project is that it is web based
