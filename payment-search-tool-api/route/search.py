from flask_restful import Resource
from flask import request, jsonify, abort
from model import PaymentInformation
from utils import serialize_results
from flask_cors import cross_origin


class SearchResult(Resource):
    """
    Routes for Search
    """
    @cross_origin()
    def get(self, profile_id):
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))

             # search for results that match the provided 'profile_id' and return them with pagination
            results = PaymentInformation.query.filter(PaymentInformation.Covered_Recipient_Profile_ID==profile_id)\
                .paginate(page=page, per_page=per_page, error_out=False)
            
            if results is None:
                abort(404)

            return jsonify(serialize_results(results))
        except Exception as e:
            return jsonify({'message': f'Error occurred: {e}'}), 500