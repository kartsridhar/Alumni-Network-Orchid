-All files in "bin" folder are created as microservices
-"server.py" is the starting point so just execute it
-I used "Talend API Tester" to test the functionalities
-As we are going to use axios and JSON objects all routes have only POST methoda to prevent data leakage
-Session Management is done by JWTtokens which will be made during login/signup(for first time)
-Mostly the jwt token will be stored as a cookie on frontend and for every request data will be decoded from this token
-below i have specified routes and the json objects that they need to return results
-chat functionality is remaining

"signup.py"
/signup:
{
    "email" : "",
    "password" : "",
    "full_name" : "",
    "user_name" : ""
}

"login.py"
/login:
{
    "email" : "",
    "password" : ""
}

"verification.py"
/verify:
{
    "email" : "",
    "confirmation_code" : ""
}

"selectcategory.py"
/selectcategory:
{
    "email" : "",
    "category_1" : "",
    "category_2" : "",
    "category_3" : ""
}

"createpost.py"
/createpost:
{
    "email" : "",
    "title" : "",
    "content" : "",
    "category" : ""
}

"deletepost.py"
/deletepost:
{
    "email" : "",
    "title" : ""
}

"getpost.py"
/getpost:
{
    "email" : ""
}

"bookmarkpost.py"
/addbookmark , /removebookmark
{
    "email" : "",
    "post_id" : ""   
}

"comments.py"
/addcomment
{
    "email" : "",
    "post_id" : "",
    "body" : "",
}
/deletecomment
{
    "comment_id" : ""
}
/updatecomment
{
    "comment_id" : "",
    "body" : ""
}
/getcomments
{
    "post_id" : ""
}

"getuser.py"
/getuser
{
    "user_email" : ""
}

-discover page route is remaining