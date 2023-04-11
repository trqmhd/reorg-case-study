import io
import xlsxwriter
from flask import make_response
from flask_restful import Resource
from model import PaymentInformation
from flask_cors import cross_origin

class ExportResult(Resource):
    """
    Routes for Export
    """
    @cross_origin()
    def get(self, profile_id):
        # Create a new workbook and add a worksheet
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        # Set column headings
        headings = ['Physcian First Name', 'Physcian Last Name', 'Recipient Id', \
                'Payment Country', 'Payment Id', 'Payment Name','Payment State', \
                'Physcian License State', 'Physcian Npi', 'Physcian Specialty', \
                'Physcian Type', 'Form Of Payment', 'Payment Publication Date', \
                'Record Id', 'Total Amount Of Payment', 'Date Of Payment']

        for i, heading in enumerate(headings):
            worksheet.write(0, i, heading)

        results = PaymentInformation.query.filter_by(Covered_Recipient_Profile_ID=profile_id).all()
        print (PaymentInformation.query.filter_by(Covered_Recipient_Profile_ID=profile_id).count())
        serialized_results = [result.serialize() for result in results]
        data = []
        for serialized_result in serialized_results:
            result_values = list(serialized_result.values())
            data.append(result_values)

        for row_num, row_data in enumerate(data, start=1):
            try:
                for col_num, cell_data in enumerate(row_data):
                    worksheet.write(row_num, col_num, cell_data)
            except Exception as e:
                # Close the workbook and re-raise the exception
                workbook.close()
                raise e

        # Close the workbook
        workbook.close()

        # Set the file name and content type
        filename = 'data.xlsx'
        output.seek(0)
        response = make_response(output.read())
        response.headers.set('Content-Disposition', 'attachment', filename=filename)
        response.headers.set('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        return response