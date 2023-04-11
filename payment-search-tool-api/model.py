from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PaymentInformation(db.Model):
    __tablename__ = 'payment'

    Change_Type = db.Column(db.String(), nullable=True)
    Covered_Recipient_Type = db.Column(db.String(), nullable=True)
    Teaching_Hospital_CCN = db.Column(db.String(), nullable=True)
    Teaching_Hospital_ID = db.Column(db.String(), nullable=True)
    Teaching_Hospital_Name = db.Column(db.String(), nullable=True)
    Covered_Recipient_Profile_ID = db.Column(db.String(), nullable=True)
    Covered_Recipient_NPI = db.Column(db.String(), nullable=True)
    Covered_Recipient_First_Name = db.Column(db.String(), nullable=True)
    Covered_Recipient_Middle_Name = db.Column(db.String(), nullable=True)
    Covered_Recipient_Last_Name = db.Column(db.String(), nullable=True)
    Covered_Recipient_Name_Suffix = db.Column(db.String(), nullable=True)
    Recipient_Primary_Business_Street_Address_Line1 = db.Column(db.String(), nullable=True)
    Recipient_Primary_Business_Street_Address_Line2 = db.Column(db.String(), nullable=True)
    Recipient_City = db.Column(db.String(), nullable=True)
    Recipient_State = db.Column(db.String(), nullable=True)
    Recipient_Zip_Code = db.Column(db.String(), nullable=True)
    Recipient_Country = db.Column(db.String(), nullable=True)
    Recipient_Province = db.Column(db.String(), nullable=True)
    Recipient_Postal_Code = db.Column(db.String(), nullable=True)
    Covered_Recipient_Primary_Type_1 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Primary_Type_2 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Primary_Type_3 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Primary_Type_4 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Primary_Type_5 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Primary_Type_6 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Specialty_1 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Specialty_2 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Specialty_3 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Specialty_4 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Specialty_5 = db.Column(db.String(), nullable=True)
    Covered_Recipient_Specialty_6 = db.Column(db.String(), nullable=True)
    Covered_Recipient_License_State_code1 = db.Column(db.String(), nullable=True)
    Covered_Recipient_License_State_code2 = db.Column(db.String(), nullable=True)
    Covered_Recipient_License_State_code3 = db.Column(db.String(), nullable=True)
    Covered_Recipient_License_State_code4 = db.Column(db.String(), nullable=True)
    Covered_Recipient_License_State_code5 = db.Column(db.String(), nullable=True)
    Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name = db.Column(db.String(), nullable=True)
    Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID = db.Column(db.String(), nullable=True)
    Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name = db.Column(db.String(), nullable=True)
    Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State = db.Column(db.String(), nullable=True)
    Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country = db.Column(db.String(), nullable=True)
    Total_Amount_of_Payment_USDollars = db.Column(db.String(), nullable=True)
    Date_of_Payment = db.Column(db.String(), nullable=True)
    Number_of_Payments_Included_in_Total_Amount = db.Column(db.BigInteger, nullable=True)
    Form_of_Payment_or_Transfer_of_Value = db.Column(db.String(), nullable=True)
    Nature_of_Payment_or_Transfer_of_Value = db.Column(db.String(), nullable=True)
    City_of_Travel = db.Column(db.String(), nullable=True)
    State_of_Travel = db.Column(db.String(), nullable=True)
    Country_of_Travel = db.Column(db.String(), nullable=True)
    Physician_Ownership_Indicator = db.Column(db.String(), nullable=True)
    Third_Party_Payment_Recipient_Indicator = db.Column(db.String(), nullable=True)
    Name_of_Third_Party_Entity_Receiving_Payment_or_Transfer_of_Valu = db.Column(db.String(), nullable=True)
    Charity_Indicator = db.Column(db.String(), nullable=True)
    Third_Party_Equals_Covered_Recipient_Indicator = db.Column(db.String(), nullable=True)
    Contextual_Information = db.Column(db.String(), nullable=True)
    Delay_in_Publication_Indicator = db.Column(db.String(), nullable=True)
    Record_ID = db.Column(db.Integer(), nullable=True, primary_key=True)
    Dispute_Status_for_Publication = db.Column(db.String(), nullable=True)
    Related_Product_Indicator = db.Column(db.String(), nullable=True)
    Covered_or_Noncovered_Indicator_1 = db.Column(db.String(), nullable=True)
    Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1 = db.Column(db.String(), nullable=True)
    Product_Category_or_Therapeutic_Area_1 = db.Column(db.String(), nullable=True)
    Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1 = db.Column(db.String(), nullable=True)
    Associated_Drug_or_Biological_NDC_1 = db.Column(db.String(), nullable=True)
    Associated_Device_or_Medical_Supply_PDI_1 = db.Column(db.String(), nullable=True)
    Covered_or_Noncovered_Indicator_2 = db.Column(db.String(), nullable=True)
    Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2 = db.Column(db.String(), nullable=True)
    Product_Category_or_Therapeutic_Area_2 = db.Column(db.String(), nullable=True)
    Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2 = db.Column(db.String(), nullable=True)
    Associated_Drug_or_Biological_NDC_2 = db.Column(db.String(), nullable=True)
    Associated_Device_or_Medical_Supply_PDI_2 = db.Column(db.String(), nullable=True)
    Covered_or_Noncovered_Indicator_3 = db.Column(db.String(), nullable=True)
    Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3 = db.Column(db.String(), nullable=True)
    Product_Category_or_Therapeutic_Area_3 = db.Column(db.String(), nullable=True)
    Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3 = db.Column(db.String(), nullable=True)
    Associated_Drug_or_Biological_NDC_3 = db.Column(db.String(), nullable=True)
    Associated_Device_or_Medical_Supply_PDI_3 = db.Column(db.String(), nullable=True)
    Covered_or_Noncovered_Indicator_4 = db.Column(db.String(), nullable=True)
    Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4 = db.Column(db.String(), nullable=True)
    Product_Category_or_Therapeutic_Area_4 = db.Column(db.String(), nullable=True)
    Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4 = db.Column(db.String(), nullable=True)
    Associated_Drug_or_Biological_NDC_4 = db.Column(db.String(), nullable=True)
    Associated_Device_or_Medical_Supply_PDI_4 = db.Column(db.String, nullable=True)
    Covered_or_Noncovered_Indicator_5 = db.Column(db.String, nullable=True)
    Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5 = db.Column(db.String, nullable=True)
    Product_Category_or_Therapeutic_Area_5 = db.Column(db.String, nullable=True)
    Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5 = db.Column(db.String, nullable=True)
    Associated_Drug_or_Biological_NDC_5 = db.Column(db.String, nullable=True)
    Associated_Device_or_Medical_Supply_PDI_5 = db.Column(db.String, nullable=True)
    Program_Year = db.Column(db.String, nullable=True)
    Payment_Publication_Date = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<PaymentInformation {self.Covered_Recipient_First_Name} {self.Covered_Recipient_Last_Name}>'
    
    def serialize(self):
        return {
            'physcian_first_name': self.Covered_Recipient_First_Name,
            'physcian_last_name': self.Covered_Recipient_Last_Name,
            # 'physcian_name': f"{self.Covered_Recipient_First_Name} - {self.Covered_Recipient_Last_Name}",
            'recipient_id': self.Covered_Recipient_Profile_ID,
            'payment_country': self.Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country,
            'payment_id': self.Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,
            'payment_name': self.Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name,
            'payment_state': self.Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,
            'physcian_license_state': self.Covered_Recipient_License_State_code1,
            'physcian_npi': self.Covered_Recipient_NPI,
            'physcian_specialty': self.Covered_Recipient_Specialty_1,
            'physcian_type': self.Covered_Recipient_Type,
            'form_of_payment': self.Form_of_Payment_or_Transfer_of_Value,
            'payment_publication_date': self.Payment_Publication_Date,
            'record_id': self.Record_ID,
            'total_amount_of_Payment': self.Total_Amount_of_Payment_USDollars,
            'date_of_payment': self.Date_of_Payment

        }
    def serialize_all(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}