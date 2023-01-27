import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker


Base = declarative_base()


class Organization(Base):
	__tablename__ = "Organizations"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	oib = db.Column(db.Integer(), nullable=False, unique=True)
	address = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False, unique=True)
	phone = db.Column(db.String(50), nullable=False)
	
	employees = relationship("Employee", backref=backref("Organizations"))
	customers = relationship("Customer", backref=backref("Organizations"))
	
	def print_org_info(self):
		print(f"ID={self.id}, "
		      f"Name={self.name}, "
		      f"OIB={self.oib}, "
		      f"Address={self.address}, "
		      f"Email={self.email}, "
		      f"Phone={self.phone}")


class Employee(Base):
	__tablename__ = "Employees"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	surname = db.Column(db.String(50), nullable=False)
	oib = db.Column(db.Integer(), nullable=False, unique=True)
	function = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(100), nullable=False, unique=True)
	phone = db.Column(db.String(50), nullable=False)
	
	organization_id = db.Column(db.Integer, db.ForeignKey("Organizations.id"))
	# Organization = relationship("Organization")
	
	def print_employee_info(self):
		print(f"ID={self.id}, "
		      f"Name={self.name} {self.surname}, "
		      f"OIB={self.oib}, "
		      f"Function={self.function}, "
		      f"Email={self.email}, "
		      f"Phone={self.phone}")


class Customer(Base):
	__tablename__ = "Customers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	surname = db.Column(db.String(50), nullable=False)
	oib = db.Column(db.Integer(), nullable=False, unique=True)
	email = db.Column(db.String(100), nullable=False, unique=True)
	phone = db.Column(db.String(50), nullable=False)
	organization_id = db.Column(db.Integer, db.ForeignKey("Organizations.id"))
	
	def print_customer_info(self):
		print(f"ID={self.id}, "
		      f"Name={self.name} {self.surname}, "
		      f"OIB={self.oib}, "
		      f"Email={self.email}, "
		      f"Phone={self.phone}")
		
		
def connect_to_db(db_name):
	db_engine = db.create_engine(f"sqlite:///{db_name}")
	Base.metadata.create_all(db_engine)
	Session = sessionmaker()
	Session.configure(bind=db_engine) # zasto bind?
	session = Session()
	return session


class SQLAlchemyRepo:
	def __init__(self, session):
		self.session = session
		
	def create_organization(self, organization):
		self.session.add(organization)
		self.session.commit()
		return organization
	
	def create_employee(self, employee):
		self.session.add(employee)
		self.session.commit()
		return employee
	
	def create_customer(self, customer):
		self.session.add(customer)
		self.session.commit()
		return customer
	
	def get_org_by_id(self, org_id):
		return self.session.query(Organization).filter_by(id=org_id).one_or_none()
	
	def get_org_by_oib(self, org_oib):
		return self.session.query(Organization).filter_by(oib=org_oib).one_or_none()
	
	def get_all_organizations(self):
		return self.session.query(Organization).all()
	
	def get_all_employees_in_organization(self, org_id):
		return self.session.query(Employee).filter(Employee.organization_id==org_id).all()
	
	def get_all_customers_in_organization(self, org_id):
		return self.session.query(Customer).filter(Customer.organization_id==org_id).all()
	
	def get_employee_by_id(self, employee_id):
		return self.session.query(Employee).filter_by(id=employee_id).one_or_none()
	
	def get_customer_by_id(self, customer_id):
		return self.session.query(Customer).filter_by(id=customer_id).one_or_none()
	
