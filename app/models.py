from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
)
from sqlalchemy.dialects.postgresql import (
    CHAR,
    NUMERIC
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True)
    product_desc = Column(String(50), nullable=False)
    product_usage_type = Column(CHAR(1), nullable=True)
    product_min_weight = Column(NUMERIC(18,2), nullable=False)
    product_max_weight = Column(NUMERIC(18,2), nullable=True)
    product_group = Column(CHAR(10), nullable=True)
    product_type = Column(CHAR(10), nullable=True)


class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    customer_priority = Column(Integer, nullable=False)
    customer_name = Column(String(50), nullable=False)
    customer_group_id = Column(Integer, nullable=False)


class Product_Link(Base):
    __tablename__ = 'product_link'
    product_link_id = Column(Integer, primary_key=True)
    owner_pruduct = Column(CHAR(12), nullable=False)
    component_product = Column(Integer, nullable=False)
    product_link_ty_id = Column(CHAR(1), nullable=False, default='L')


class Resource(Base):
    __tablename__ = 'resource'
    resource_id = Column(Integer, primary_key=True)
    resource_desc = Column(String(30), nullable=False)
    wearout_factor = Column(NUMERIC(18,2), nullable=False)
    start_maintenance = Column(Integer, nullable=False)
    end_maintenance = Column(Integer, nullable=False)
    status = Column(CHAR(1), nullable=False)


class Standard_Operation(Base):
    __tablename__ = 'standard_operation'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'), nullable=False)
    resource_id = Column(Integer, ForeignKey('resource.resource.id'), nullable=False)
    alternative_pref = Column(Integer, primary_key=True)
    standard_op_no = Column(Integer, primary_key=True)
    operation_type = Column(CHAR(1), nullable=False)
    standard_time = Column(NUMERIC(18,2), nullable=False)
    yield_percent = Column(NUMERIC(18,2), nullable=False)


class Sales_Orders(Base):
    __tablename__ = 'sales_orders'
    sales_order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.product_id'), nullable=False)
    so_quantity = Column(NUMERIC(18, 2), nullable=False)
    so_tolerance = Column(NUMERIC(18, 2), nullable=False)
    shipped_quantity = Column(NUMERIC(18, 2), nullable=False)
    so_status = Column(Integer, nullable=False)
    orig_due_date = Column(Date, nullable=False)
    so_due_date = Column(Date, nullable=False)
    release_date = Column(Date, nullable=False)
    ship_to_location = Column(String(50), nullable=True)
    original_from_date = Column(Date, nullable=True)