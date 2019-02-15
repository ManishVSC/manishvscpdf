import pdfkit
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template 
from django.template import Context
import datetime
import os
import subprocess
import pydf
westerncount = 0
loantaxcount = 0
moneygramcount = 0
outstandingcount = 0
remainoutstandingcount = 0
filechargescount = 0
agreementcount = 0
if 'DYNO' in os.environ:
    print ('loading wkhtmltopdf path on heroku')
    WKHTMLTOPDF_CMD = subprocess.Popen(
        ['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], # Note we default to 'wkhtmltopdf' as the binary name
        stdout=subprocess.PIPE).communicate()[0].strip()
else:
    print ('loading wkhtmltopdf path on localhost')
    MYDIR = os.path.dirname(__file__)    
    WKHTMLTOPDF_CMD = os.path.join(MYDIR + "/static/executables/bin/", "wkhtmltopdf.exe")

def western(request):
	global westerncount

	Full_Name = request.GET['NAME']
	Loan_Amount = request.GET['LOAN AMOUNT']
	Fees = request.GET['FEES']
	Total_Amount = int(Loan_Amount) + int(Fees)
	Date_Time = datetime.datetime.today()

	template = get_template("homenew.html")

	Context = {
	"Full_Name": Full_Name,
	"Loan_Amount": Loan_Amount,
	"Fees": Fees,
	"Total_Amount": Total_Amount,
	"Date_Time": Date_Time.strftime('%m-%d-%Y'),
	"westerncount": westerncount,

	}  # data is the context data that is sent to the html file to render the output.
	file_name = Full_Name 
	html = template.render(Context)  # Renders the template with the context data.
	pdfkit.from_string(html, 'out.pdf')
	pdf = open("out.pdf", 'rb')
	response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
	response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
	pdf.close()
	os.remove("out.pdf")  # remove the locally created pdf file.
	westerncount +=1
	print(westerncount)
	return response  # returns the response.





def agreement(request):
	global agreementcount
	name = request.GET['NAME']
	verification_amount = request.GET['VERIFICATION AMOUNT']
	payment_date = request.GET['PAYMENT DATE']
	address = request.GET['FULL ADDRESS']
	extra_lines = request.GET['EXTRA LINES']
	loan_amount = request.GET['LOAN AMOUNT']
	date_today = datetime.datetime.today()

	if loan_amount == '1000':
		template = get_template("1000.html")
	elif loan_amount == '1500':
		template = get_template('1500.html')
	elif loan_amount == '2000':
		template = get_template('2000.html')
	elif loan_amount == '3000':
		template = get_template('3000.html')
	elif loan_amount == '4000':
		template = get_template('4000.html')
	elif loan_amount == '4500':
		template = get_template('4500.html')
	elif loan_amount == '5000':
		template = get_template('5000.html')
	elif loan_amount == '5500':
		template = get_template('5500.html')
	elif loan_amount == '6000':
		template = get_template('6000.html')
	elif loan_amount == '6500':
		template = get_template('6500.html')
	elif loan_amount == '7000':
		template = get_template('7000.html')
	elif loan_amount == '7500':
		template = get_template('7500.html')
	elif loan_amount == '8000':
		template = get_template('8000.html')
	elif loan_amount == '2500':
		template = get_template('2500.html')
	elif loan_amount == '3500':
		template = get_template('3500.html')
	else:
		return HttpResponse('<h1> SEEMS LIKE YOUR AMOUNT DOES NOT MATCH WITH THE STORED TEMPLATES </h1>')




	Context = {
		"Full_Name": name,
		"Verification_Amount": verification_amount,
		"Full_Address": address,
		"Payment_Date": payment_date,
		"Extra_Line": extra_lines,
	 	"date_time": date_today.strftime('%m-%d-%Y'),


	}

	file_name = name
	html = template.render(Context)  # Renders the template with the context data.
	pdfkit.from_string(html, 'out.pdf')
	pdf = open("out.pdf", 'rb')
	agreementcount+=1
	response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
	response['Content-Disposition'] = 'attachment; filename=""' + name + '.pdf'
	pdf.close()
	os.remove("out.pdf")  # remove the locally created pdf file.
	return response  # returns the response.


def home(request):
	return render(request, 'home.html')

def welcome(request):
	global westerncount
	return render(request, 'welcome.html', {"westerncount":westerncount})


def moneygram(request):
	return render(request, 'moneygram.html')



def agreementform(request):
	return render(request, 'agreementform.html')


def westernform(request):
	return render(request, 'westernform.html')

def outstanding(request):
	global outstandingcount
	date_today = datetime.datetime.today()

	template = get_template("outstanding.html")
	Full_Name = request.GET['NAME']
	outstanding_balance = request.GET['outstanding_balance']
	half_outstanding = int(outstanding_balance) / 2
	total_refund = request.GET['TOTAL REFUND']
	loan_amount = request.GET['LOAN AMOUNT']

	Context = {
	"date_today": date_today.strftime('%m-%d-%Y'),
	"full_name": Full_Name,
	"outstanding_balance": outstanding_balance,
	"half_outstanding": half_outstanding,
	"total_refund": total_refund,
	"loan_amount": loan_amount, }

	  # data is the context data that is sent to the html file to render the output.
	file_name = Full_Name
	outstandingcount+=1 
	html = template.render(Context)  # Renders the template with the context data.
	pdfkit.from_string(html, 'out.pdf')
	pdf = open("out.pdf", 'rb')
	response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
	response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
	pdf.close()
	os.remove("out.pdf")  # remove the locally created pdf file.

	return response  # returns the response.


def outstandingform(request):
	return render(request, 'outstandingform.html')


def counter(request):
	global westerncount 
	global loantaxcount 
	global moneygramcount 
	global outstandingcount 
	global remainoutstandingcount 
	global filechargescount 
	global agreementcount
	return render(request, 'counter.html', {"westerncount": westerncount, "loantaxcount": loantaxcount, "moneygramcount": moneygramcount, "outstandingcount":outstandingcount, "remainoutstandingcount": remainoutstandingcount, "filechargescount": filechargescount, "agreementcount": agreementcount,})



def loantaxform(request):
	return render(request, 'loantaxform.html')


def loantax(request):
	global loantaxcount
	date_today = datetime.datetime.today()
	Full_Name = request.GET['FULL NAME']
	loan_amount = request.GET['LOAN AMOUNT']
	loan_tax = request.GET['LOAN TAX']


	template = get_template("loantax.html")

	Context = {"full_name": Full_Name,
	"loan_amount": loan_amount,
	"loan_tax": loan_tax,
	"date_today":date_today.strftime('%m-%d-%Y'),
	 }

	  # data is the context data that is sent to the html file to render the output.
	file_name = Full_Name
	loantaxcount+=1 
	html = template.render(Context)  # Renders the template with the context data.
	pdfkit.from_string(html, 'out.pdf')
	pdf = open("out.pdf", 'rb')
	response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
	response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
	pdf.close()
	os.remove("out.pdf")  # remove the locally created pdf file.

	return response  # returns the response.
	


def remainoutstandingform(request):
	return render(request, 'remainoutstandingform.html')



def remainoutstanding(request):
	global remainoutstandingcount
	date_today = datetime.datetime.today()

	template = get_template("remainoutstanding.html")
	Full_Name = request.GET['NAME']
	loan_amount = request.GET['LOAN AMOUNT']
	total_refund = request.GET['TOTAL REFUND']
	remainoutstanding = request.GET['remainoutstanding']
	Context = {
	"date_today": date_today.strftime('%m-%d-%Y'),
	"full_name": Full_Name,
	"total_refund": total_refund,
	"loan_amount": loan_amount,
	"remain_outstanding": remainoutstanding, }

	  # data is the context data that is sent to the html file to render the output.
	file_name = Full_Name
	remainoutstandingcount+=1 
	html = template.render(Context)  # Renders the template with the context data.
	pdfkit.from_string(html, 'out.pdf')
	pdf = open("out.pdf", 'rb')
	response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
	response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
	pdf.close()
	os.remove("out.pdf")  # remove the locally created pdf file.

	return response  # returns the response.


def filechargesform(request):
	return render(request, 'filechargesform.html')

def filecharges(request):
	global filechargescount
	date_today = datetime.datetime.today()

	template = get_template("filecharges.html")
	Full_Name = request.GET['NAME']
	loan_amount = request.GET['LOAN AMOUNT']
	total_refund = request.GET['TOTAL REFUND']
	file_charges = request.GET['FILE CHARGES']
	Context = {
	"date_today": date_today.strftime('%m-%d-%Y'),
	"full_name": Full_Name,
	"total_refund": total_refund,
	"loan_amount": loan_amount,
	"file_charges": file_charges, }

	  # data is the context data that is sent to the html file to render the output.
	file_name = Full_Name
	filechargescount+=1 
	html = template.render(Context)  # Renders the template with the context data.
	pdfkit.from_string(html, 'out.pdf')
	pdf = open("out.pdf", 'rb')
	response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
	response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
	pdf.close()
	os.remove("out.pdf")  # remove the locally created pdf file.

	return response  # returns the response.


def login(request):
	return render(request, 'login.html')