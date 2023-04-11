import pytest
from flask import json
from flask_restful import Api
from flask_testing import TestCase
from app import app as flask_app, db
from model import PaymentInformation
from route.typeahead import TypeAheadResult


class TestTypeAheadResult(TestCase):

    def create_app(self):
        app = flask_app
        api = Api(app)
        api.add_resource(TypeAheadResult, '/typeahead')
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        db.create_all()

        # Add test data
        payment_information = [
            PaymentInformation(Covered_Recipient_First_Name='John', Covered_Recipient_Last_Name='Doe', Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name='Company A', Date_of_Payment='2022-01-01', Covered_Recipient_Profile_ID='12345'),
            PaymentInformation(Covered_Recipient_First_Name='Jane', Covered_Recipient_Last_Name='Smith', Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name='Company B', Date_of_Payment='2022-01-02', Covered_Recipient_Profile_ID='67890')
        ]

        db.session.add_all(payment_information)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_empty_query(self):
        response = self.app.get('/typeahead?query=')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert len(data['items']) == 2

    def test_search_query(self):
        response = self.app.get('/typeahead?query=John')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert len(data['items']) == 1
        assert data['items'][0]['Covered_Recipient_First_Name'] == 'John'

    def test_pagination(self):
        response = self.app.get('/typeahead?query=&per_page=1&page=2')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert len(data['items']) == 1
        assert data['items'][0]['Covered_Recipient_First_Name'] == 'Jane'

    def test_server_error(self):
        with pytest.raises(Exception):
            self.app.get('/typeahead?query=')
            PaymentInformation.query.paginate = MagicMock(side_effect=Exception('Test exception'))


if __name__ == '__main__':
    pytest.main()
