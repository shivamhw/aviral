# Aviral API Wrapper

Use aviral in your python application with ease, check marks, get details or make a sign in with aviral option in your application.
This bypasses the static content calls so response is much faster then aviral website. Get your marks in less then 1 second even during when the main site is running slow. 


# Requirements
- Python 3.x
- requests module
# Install

`pip install aviral`

# Examples

To use any api endpoint, Initialization is required. for full api documentation [Click HERE.](https://shivamhw.github.io/aviral)

## Initialize

```python
from  aviral_api  import  AviralAPI

avi = AviralAPI()
```
## Get sessions
For using multiple functions, you need to specify a session. this call returns available valid sessions for a user as a list of json.
```python
from  aviral_api  import  AviralAPI

avi = AviralAPI()
print(avi.get_sessions())
```
Sample Response :
<details>

```json
[
   {
      "current":true,
      "name":"July-Dec 2020",
      "session_id":"JUL-20"
   },
   {
      "current":false,
      "name":"July-Dec 2018",
      "session_id":"JUL-18"
   },
   {
      "current":false,
      "name":"Jan-June 2019",
      "session_id":"JAN-19"
   },
   {
      "current":false,
      "name":"SUMMER 2019",
      "session_id":"SUM-19"
   },
   {
      "current":false,
      "name":"July-Dec 2019",
      "session_id":"JUL-19"
   },
   {
      "current":false,
      "name":"SUMMER 2020",
      "session_id":"SUM-20"
   },
   {
      "current":true,
      "name":"Jan-June 2021",
      "session_id":"JAN-21"
   },
   {
      "current":true,
      "name":"SUMMER 2021",
      "session_id":"SUM-21"
   },
   {
      "current":true,
      "name":"July-Dec 2021",
      "session_id":"JUL-21"
   },
   {
      "current":true,
      "name":"Jan-June 2020",
      "session_id":"JAN-20"
   }
]
```
</details>

## Get details about user

Returns details about user based on session. if session is not specified, default session is used.

```python
from  aviral_api  import  AviralAPI


avi = AviralAPI()
user = avi.login("##ROLLNM##", "##PASS##")
print(avi.get_userdata(user))
```

<details>
  <summary>Sample Response:</summary>

```json
{
   "completed_elective":4,
   "enrolled_courses_core":1,
   "enrolled_courses":4,
   "cgpi":8.95,
   "completed_core":32,
   "total_elective_credits":16,
   "last_name":"",
   "semester":"Third",
   "admission_year":2020,
   "enrolled_courses_elective":3,
   "duration":2,
   "student_id":"MIT2020122",
   "total_core_credits":48,
   "section":"",
   "total_credits":64,
   "first_name":"Shivam Mishra",
   "program":"M.Tech. IT (CLIS)",
   "completed_total":36,
   "enrolled_courses_addon":0,
   "middle_name":"",
   "phone":"##"
}
```

</details>

---

## Get subject wise marks

Returns list of json of subject wise marks for the session specified. If no session is specified, then current session is used.

```python
from  aviral_api  import  AviralAPI


avi = AviralAPI()
user = avi.login("##ROLLNM##", "##PASS##")
print(avi.get_subjectwise_marks(user))

```

<details>
  <summary>Sample Response:</summary>

```json
[
   {
      "course_id":"MITD",
      "c1_marks":"29.00",
      "credits":4,
      "total":"80.00",
      "c3_marks":"28.00",
      "gpa":"9.64",
      "name":"Intrusion Detection System",
      "c2_marks":"23.00"
   },
   {
      "course_id":"MDAS",
      "c1_marks":"21.60",
      "credits":4,
      "total":"71.81",
      "c3_marks":"33.06",
      "gpa":"8.26",
      "name":"Database Security",
      "c2_marks":"17.15"
   },
   {
      "course_id":"MINP",
      "c1_marks":"19.00",
      "credits":4,
      "total":"N/A",
      "c3_marks":"N/A",
      "gpa":"N/A",
      "name":"Internet Protocols",
      "c2_marks":"21.00"
   },
   {
      "course_id":"MTHE",
      "c1_marks":"N/A",
      "credits":6,
      "total":"N/A",
      "c3_marks":"N/A",
      "gpa":"N/A",
      "name":"Thesis - I",
      "c2_marks":"N/A"
   }
]
```

</details>

---

## Get semester wise result

Returns a json which includes semester wise result in data key.
```python
from  aviral_api  import  AviralAPI


avi = AviralAPI()
user = avi.login("##ROLLNM##", "##PASS##")
print(avi.get_semesterwise_marks(user))
```
Sample Response :
<details>

```json
{
   "data":[
      {
         "sgpi":"8.76",
         "semester":1
      },
      {
         "sgpi":"9.10",
         "semester":2
      }
   ]
}
```
</details>

# Credits

To those who developed Aviral portal. Really setting cookie value to "haha" does made my day. JK ;)
