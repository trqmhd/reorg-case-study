from flask_restful import Resource
from sqlalchemy import or_
from flask import request, jsonify
from flask_cors import cross_origin
from model import PaymentInformation
from utils import serialize_results


class TypeAheadResult(Resource):
    """
    Routes for TypeAhead
    """

    @cross_origin()
    def get(self,):
        try:
            query = request.args.get('query')
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))

            # if the 'query' parameter is empty, return all results with pagination
            if query == '':
                results = PaymentInformation.query.paginate(page=page, per_page=per_page, error_out=False)
            
            # otherwise, search for results that match the query and return them with pagination
            else:
                results = PaymentInformation.query.filter(
                    or_(
                        PaymentInformation.Covered_Recipient_First_Name.like(f'%{query}%'),
                        PaymentInformation.Covered_Recipient_Last_Name.like(f'%{query}%'),
                        PaymentInformation.Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name.like(f'%{query}%'),
                        PaymentInformation.Date_of_Payment.like(f'%{query}%'),
                        PaymentInformation.Covered_Recipient_Profile_ID.like(f'%{query}%'),
                    )
                ).paginate(page=page, per_page=per_page, error_out=False)

            return jsonify(serialize_results(results))
        except Exception as e:
            # handle the exception here
            return jsonify({'message': f'Error occurred: {e}'}), 500