# data2410-oblig

Rules and prerequisites
This mandatory assignment must be completed individually. Your submission must be approved prior
to submission of the portfolio 1. To pass the submission you must meet the requirements that are
documented here, and be able to explain every single module.
Should you be missing lectures and lab sessions, it is your own responsibility to catch up to the
competence level that you are supposed to get it from the lectures and lab sessions. Make good use of
the lectures and lab sessions because we will cover important concepts there.

Task 1: Making a simple webserver
You will develop a web server that handles one HTTP request at a time. Your web server should
accept and parse the HTTP request, get the requested file from the server’s file system, create an
HTTP response message consisting of the requested file preceded by header lines, and then send the
response directly to the client. If the requested file is not present in the server, the server should send
an HTTP “404 Not Found” message back to the client.

Running the server
Put an HTML file (e.g., index.html) in the same directory that the server is in. Run the server program.
Open a browser and provide the corresponding URL. For example: http://127.0.0.1:6789/index.html
‘index.html’ is the name of the file you placed in the server directory. Note also the use of the port
number after the colon. You need to replace this port number with whatever port you have used in
the server code. In the above example, we have used the port number 6789. The browser should then
display the contents of index.html. If you omit ”:6789”, the browser will assume port 80 and you will
get the web page from the server only if your server is listening at port 80. Then try to get a file that
is not present at the server. You should get a “404 Not Found” message.

Task 2: Making a web client
Instead of using a browser, write your own HTTP client to test your server. Your client will connect
to the server using a TCP connection, send an HTTP request to the server, and display the server
response as an output. You can assume that the HTTP request sent is a GET method. The client
should take command line arguments specifying the server IP address or host name, the port at which
the server is listening, and the path at which the requested object is stored at the server. The following
is an input command format to run the client. client.py server host server port filename

Task 3: Making a multi-threaded web server
Currently, your web server handles only one HTTP request at a time. You should implement a
multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first
create a main thread in which your modified server listens for clients at a fixed port. When it receives
a TCP connection request from a client, it will set up the TCP connection through another port and
1services the client request in a separate thread. There will be a separate TCP connection in a separate
thread for each request/response pair.

Submission
You must submit:
1. You must submit the a complete simple server code where the code is well commented. Also,
provide screenshots of the client browser, verifying that you receive the contents of the HTML
(task 1).
2. the complete web client code where the code is well commented (task 2).
3. the complete multi-threaded server code where the code is well commented (task 3).
4. document all the variables and definitions.
5. document the following for each function:
• what the function does.
• what input and output parameters mean and how they are used.
• what the function returns.
• how do you handle exceptions
DEADLINE to hand in oblig: Wednesday March 1, 23:59
