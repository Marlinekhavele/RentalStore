# RentalStore
It is a program to calculate and print a statement of a customer's charges at a book rental store

# Running the project locally
Clone the project using git clone
Enter the project directory i.e cd store
### create virtual environment
- virtualenv env -p python3.6
### activate
- source env/bin/activate

install deps
- pip install -r requirements.txt
- python manage.py createsuperuser
- python manage.py makemigrations
- python manage.py migrate
### Start the project with the command python manage.py runserver
### Visit http://localhost:8000/api/v1/docs to get started with the browsable api

![alt text](BookApp.jpg "ERD diagram")
MIT License

Copyright (c) 2020 CodeBeast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
