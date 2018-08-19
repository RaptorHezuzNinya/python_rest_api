from realestateapi import db
from sqlalchemy import event, DDL


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    account_holder = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(35))
    iban = db.Column(db.String(35), nullable=False)
    rent = db.Column(db.Float)
    phone = db.Column(db.String(12))

    def __repr__(self):
        return f"Tenant('{self.id}','{self.first_name}','{self.last_name}','{self.iban}','{self.rent}','{self.phone}')"


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iban = db.Column(db.String(40), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    account_holder = db.Column(db.String(150), nullable=False)
    payment_json = db.Column(db.JSON, nullable=False)
    date = db.Column(db.Date, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey(
        'tenant.id'), nullable=False)

    def __repr__(self):
        return f"Payment('{self.id}', '{self.iban}, '{self.rent}','{self.account_holder}')"


class Upload(db.Model):
    __tablename__ = "json_upload"
    id = db.Column(db.Integer, primary_key=True)
    json_file = db.Column(db.JSON)
    uploaded_at = db.Column(db.Date)

    def __init__(self, json_file, uploaded_at):
        self.json_file = json_file
        self.uploaded_at = uploaded_at

    def __repr__(self):
        return f"Upload('{self.id}', '{self.json_file}')"


event.listen(Tenant.__table__,
             'after_create',
             DDL(""" INSERT INTO tenant (email, account_holder, first_name, last_name, iban, rent, phone) VALUES                                         
                    ('malou_proper@hotmail.com', 'Mw M Proper', 'Malou', 'Proper', 'NL08INGB0001193558', 747.16, '0612345678'),
                    ('bienbeijderwellen@gmail.com', 'BIEN BEIJDERWELLEN', 'Bien', 'Beijderwellen', 'NL58ABNA0535684053', 728.18, '0612345678'),
                    ('matine_eising@outlook.com', 'M. Eising eo', 'Matine', 'Eising', 'NL40RABO0184147433', 752.76, '0612345678'),
                    ('ninakatherinadejong@gmail.com', 'K.S.A. de Jong', 'Nina', 'de Jong', 'NL94RABO0354260308', 799.05, '0612345678'),
                    ('kris.stroeken@hotmail.com', 'Hr G L M Stroeken en?Mw A J M J Stroeken-Smeets', 'Kris', 'Stroeken', 'NL79INGB0003694783', 715.33, '0612345678'),
                    ('fennascharloo@outlook.com', 'F. Scharloo', 'Fenna', 'ScharLoo', 'NL08RABO0133380343', 588.37, '0612345678'),
                    ('daphnevanede@hotmail.com', 'D D F VAN EDE', 'Daphne', 'van Ede', 'NL15ABNA0490096379', 720.64, '0612345678'),
                    ('stijn_bronzwaer@hotmail.com', 'M.E.S. Bronzwaer-Timmerm', 'Stijn', 'Bronzwaer', 'NL75RABO0140989757', 824.65, '0612345678'),
                    ('mathijs.mulder@live.nl', 'HR M Mulder', 'Mathijs', 'Mulder', 'NL39INGB0008753374', 599.97, '0612345678'),
                    ('mshinta_moes@hotmail.com', 'MW S L Moes ', 'Shinta', 'Moes', 'NL84INGB0008756347', 703.88, '0612345678')
                """))
