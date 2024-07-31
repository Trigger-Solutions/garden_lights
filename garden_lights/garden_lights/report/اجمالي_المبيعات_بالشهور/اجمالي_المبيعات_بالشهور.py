# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import json

import frappe
from frappe import _
from frappe.utils import get_url_to_list
from datetime import datetime
import calendar


def execute(filters=None):
	columns = columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"fieldname": "month",
			"label": _("الشهر"),
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"fieldname": "title",
			"label": _("الصافي قبل الضريبة"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 200,
		},
		{
			"fieldname": "amount",
			"label": _("قيمة الضريبة"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 200,
		},
		{
			"fieldname": "adjustment_amount",
			"label": _("الصافي بعد الضريبة"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 200,
		},
		{
			"fieldname": "vat_amount",
			"label": _("نقدي"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 200,
		},
		{
			"fieldname": "visa",
			"label": _("شبكة"),
			"fieldtype": "Currency",
			"options": "currency",
			"width": 200,
		},
		
	]


def get_data(filters):
	data = []
	year = int(filters.get("year"))
	jan = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-01-01", f"{year}-01-31"]]], fields={"total"}, pluck="total")
	feb = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-02-01", f"{year}-02-{calendar.monthrange(year, 2)[1]}"]]], fields={"total"}, pluck="total")
	mar = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-03-01", f"{year}-03-31"]]], fields={"total"}, pluck="total")
	apr = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-04-01", f"{year}-04-30"]]], fields={"total"}, pluck="total")
	may = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-05-01", f"{year}-05-31"]]], fields={"total"}, pluck="total")
	jun = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-06-01", f"{year}-06-30"]]], fields={"total"}, pluck="total")
	jul = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-07-01", f"{year}-07-31"]]], fields={"total"}, pluck="total")
	aug = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-08-01", f"{year}-08-31"]]], fields={"total"}, pluck="total")
	sep = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-09-01", f"{year}-09-30"]]], fields={"total"}, pluck="total")
	oct = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-10-01", f"{year}-10-31"]]], fields={"total"}, pluck="total")
	nov = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-11-01", f"{year}-11-30"]]], fields={"total"}, pluck="total")
	dec = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-12-01", f"{year}-12-31"]]], fields={"total"}, pluck="total")
	
	jan1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-01-01", f"{year}-01-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	feb1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-02-01", f"{year}-02-{calendar.monthrange(year, 2)[1]}"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	mar1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-03-01", f"{year}-03-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	apr1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-04-01", f"{year}-04-30"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	may1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-05-01", f"{year}-05-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	jun1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-06-01", f"{year}-06-30"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	jul1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-07-01", f"{year}-07-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	aug1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-08-01", f"{year}-08-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	sep1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-09-01", f"{year}-09-30"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	oct1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-10-01", f"{year}-10-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	nov1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-11-01", f"{year}-11-30"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")
	dec1 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-12-01", f"{year}-12-31"]]], fields={"total_taxes_and_charges"}, pluck="total_taxes_and_charges")

	jan2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-01-01", f"{year}-01-31"]]], fields={"grand_total"}, pluck="grand_total")
	feb2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-02-01", f"{year}-02-{calendar.monthrange(year, 2)[1]}"]]], fields={"grand_total"}, pluck="grand_total")
	mar2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-03-01", f"{year}-03-31"]]], fields={"grand_total"}, pluck="grand_total")
	apr2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-04-01", f"{year}-04-30"]]], fields={"grand_total"}, pluck="grand_total")
	may2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-05-01", f"{year}-05-31"]]], fields={"grand_total"}, pluck="grand_total")
	jun2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-06-01", f"{year}-06-30"]]], fields={"grand_total"}, pluck="grand_total")
	jul2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-07-01", f"{year}-07-31"]]], fields={"grand_total"}, pluck="grand_total")
	aug2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-08-01", f"{year}-08-31"]]], fields={"grand_total"}, pluck="grand_total")
	sep2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-09-01", f"{year}-09-30"]]], fields={"grand_total"}, pluck="grand_total")
	oct2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-10-01", f"{year}-10-31"]]], fields={"grand_total"}, pluck="grand_total")
	nov2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-11-01", f"{year}-11-30"]]], fields={"grand_total"}, pluck="grand_total")
	dec2 = frappe.get_all("Sales Invoice", filters=[["posting_date", "between", [f"{year}-12-01", f"{year}-12-31"]]], fields={"grand_total"}, pluck="grand_total")

	cash1 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-01-01", f"{year}-01-31"]]], fields={"grand_total"}, pluck="grand_total")
	cash2 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-02-01", f"{year}-02-{calendar.monthrange(year, 2)[1]}"]]], fields={"grand_total"}, pluck="grand_total")
	cash3 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-03-01", f"{year}-03-31"]]], fields={"grand_total"}, pluck="grand_total")
	cash4 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-04-01", f"{year}-04-30"]]], fields={"grand_total"}, pluck="grand_total")
	cash5 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-05-01", f"{year}-05-31"]]], fields={"grand_total"}, pluck="grand_total")
	cash6 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-06-01", f"{year}-06-30"]]], fields={"grand_total"}, pluck="grand_total")
	cash7 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-07-01", f"{year}-07-31"]]], fields={"grand_total"}, pluck="grand_total")
	cash8 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-08-01", f"{year}-08-31"]]], fields={"grand_total"}, pluck="grand_total")
	cash9 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-09-01", f"{year}-09-30"]]], fields={"grand_total"}, pluck="grand_total")
	cash10 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-10-01", f"{year}-10-31"]]], fields={"grand_total"}, pluck="grand_total")
	cash11 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-11-01", f"{year}-11-30"]]], fields={"grand_total"}, pluck="grand_total")
	cash12 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "نقد"}, ["posting_date", "between", [f"{year}-12-01", f"{year}-12-31"]]], fields={"grand_total"}, pluck="grand_total")

	visa1 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-01-01", f"{year}-01-31"]]], fields={"grand_total"}, pluck="grand_total")
	visa2 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-02-01", f"{year}-02-{calendar.monthrange(year, 2)[1]}"]]], fields={"grand_total"}, pluck="grand_total")
	visa3 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-03-01", f"{year}-03-31"]]], fields={"grand_total"}, pluck="grand_total")
	visa4 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-04-01", f"{year}-04-30"]]], fields={"grand_total"}, pluck="grand_total")
	visa5 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-05-01", f"{year}-05-31"]]], fields={"grand_total"}, pluck="grand_total")
	visa6 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-06-01", f"{year}-06-30"]]], fields={"grand_total"}, pluck="grand_total")
	visa7 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-07-01", f"{year}-07-31"]]], fields={"grand_total"}, pluck="grand_total")
	visa8 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-08-01", f"{year}-08-31"]]], fields={"grand_total"}, pluck="grand_total")
	visa9 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-09-01", f"{year}-09-30"]]], fields={"grand_total"}, pluck="grand_total")
	visa10 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-10-01", f"{year}-10-31"]]], fields={"grand_total"}, pluck="grand_total")
	visa11 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-11-01", f"{year}-11-30"]]], fields={"grand_total"}, pluck="grand_total")
	visa12 = frappe.get_all("Sales Invoice", filters=[{"mode_of_payment": "بطاقة ائتمان"}, ["posting_date", "between", [f"{year}-12-01", f"{year}-12-31"]]], fields={"grand_total"}, pluck="grand_total")

	company = filters.get("company")
	company_currency = frappe.get_cached_value("Company", company, "default_currency")
	append_data(data, "يناير", round(sum(jan),2), round(sum(jan1),2), round(sum(jan2),2), round(sum(cash1),2), round(sum(visa1),2), company_currency)
	append_data(data, "فبراير", round(sum(feb),2), round(sum(feb1),2), round(sum(feb2),2), round(sum(cash2),2), round(sum(visa2),2), company_currency)
	append_data(data, "مارس", round(sum(mar),2), round(sum(mar1),2), round(sum(mar2),2), round(sum(cash3),2), round(sum(visa3),2), company_currency)
	append_data(data, "ابريل", round(sum(apr),2), round(sum(apr1),2), round(sum(apr2),2), round(sum(cash4),2), round(sum(visa4),2), company_currency)
	append_data(data, "مايو", round(sum(may),2), round(sum(may1),2), round(sum(may2),2), round(sum(cash5),2), round(sum(visa5),2), company_currency)
	append_data(data, "يونيو", round(sum(jun),2), round(sum(jun1),2), round(sum(jun2),2), round(sum(cash6),2), round(sum(visa6),2), company_currency)
	append_data(data, "يوليو", round(sum(jul),2), round(sum(jul1),2), round(sum(jul2),2), round(sum(cash7),2), round(sum(visa7),2), company_currency)
	append_data(data, "اغسطس", round(sum(aug),2), round(sum(aug1),2), round(sum(aug2),2), round(sum(cash8),2), round(sum(visa8),2), company_currency)
	append_data(data, "سبتمبر", round(sum(sep),2), round(sum(sep1),2), round(sum(sep2),2), round(sum(cash9),2), round(sum(visa9),2), company_currency)
	append_data(data, "اكتوبر", round(sum(oct),2), round(sum(oct1),2), round(sum(oct2),2), round(sum(cash10),2), round(sum(visa10),2), company_currency)
	append_data(data, "نوفمبر", round(sum(nov),2), round(sum(nov1),2), round(sum(nov2),2), round(sum(cash11),2), round(sum(visa11),2), company_currency)
	append_data(data, "ديسمبر", round(sum(dec),2), round(sum(dec1),2), round(sum(dec2),2), round(sum(cash12),2), round(sum(visa12),2), company_currency)
	return data

def append_data(data, month, title, amount, adjustment_amount, vat_amount, visa, company_currency):
	"""Returns data with appended value."""
	data.append(
		{
			"month": month,
			"title": title,
			"amount": amount,
			"adjustment_amount": adjustment_amount,
			"vat_amount": vat_amount,
			"visa": visa,
			"currency": company_currency,
		}
	)