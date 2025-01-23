from weasyprint import HTML
from flask import Flask, render_template, send_file, request
import os
import io
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    input_data = request.get_json() or {}
    today = datetime.today().strftime("%d/%m/%Y")
    default_data =  {
        'duedate': '23/03/2025',
        'from_details': {
            'company_name': 'Canalside.io',
            'add1': 'Grachtenweg 17, 1017VX',
            'add2': 'Amsterdam, Noord-Holland, Netherlands'
        },
        'invoice_number': 123,
        'items': [
            {
                'title': 'Website ontwerp',
                'price': 300.00
            },
            {
                'title': 'Hosting (3 maanden',
                'price': 75.00
            },
            {
                'title': 'Domainnaam (1 jaar',
                'price': 20.00
            }
        ],
        'to_details': {
            'company_name': 'Herengracht House',
            'contact_person': 'Joroen van Dijk',
            'contact_email': 'joroen@example.nl'
        }
    }

    duedate = input_data.get('duedate', default_data['duedate'])
    from_details = input_data.get('from_details', default_data['from_details'])
    to_details = input_data.get('to_details', default_data['to_details'])
    invoice_number = input_data.get('invoice_number', default_data['invoice_number'])
    items = input_data.get('items', default_data['items'])

    total = sum([i['price'] for i in items])
    rendered = render_template('invoice.html', 
                           date = today,
                           from_details = from_details,
                           to_details = to_details,
                           items = items,
                           total = total,
                           invoice_number = invoice_number,
                           duedate = duedate)
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf()
    return send_file(
            io.BytesIO(rendered_pdf),
            download_name='invoice.pdf'
        )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

