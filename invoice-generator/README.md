# Invoice Generator
This is a project that receives the invoice details as an input
from the user, and generates a PDF invoice and emails it to the
respective recipients.

- weasyprint
Is used to convert HTML documents to PDF

- jinja 
Is a templating engine for embedding Python into HTML and rendering
it in the server.

- We create a basic API to collect the input with the invoice details
from the user. The app receives JSON and returns PDF.

NOTE:
Rendering and sending the file directly without saving it to the 
disk can become a bottleneck in bigger applications. In such a case,
using a task scheduler (e.g. Celery) to render the PDF in the 
background and then send it to the client is recommended.
