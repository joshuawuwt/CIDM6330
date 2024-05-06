1- Test
The test code is moved to a seperated folder. It makes sense the test folder is parallel with the app folder. With adding pytest.ini in the root directory, we can run "py manage.py test" directly. Otherwise we can run "py manage.py test -k barkytest".
When run pytest, it didn't discover or execute any tets cases. After change the file name from "tests.py" to "test_.py", it works. But the test result has some error.

2- Model
Move model file to subfolder \domain.

3- Others
Create subfolders such as \service and \adapters but only copy these files to those subfolders.