"""
Generate sample Parquet datasets for Databricks course exercises.
This script creates realistic sample data in Parquet format for optimal performance.
"""

import pandas as pd
from datetime import datetime, timedelta

def create_customers_parquet():
    """Generate customers dataset"""
    customers_data = {
        'customer_id': list(range(1, 21)),
        'first_name': ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Lisa', 'James', 'Patricia',
                       'Christopher', 'Jennifer', 'Daniel', 'Nancy', 'Matthew', 'Barbara', 'Joseph', 'Susan', 'Charles', 'Jessica'],
        'last_name': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                      'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson'],
        'email': ['john.doe@email.com', 'jane.smith@email.com', 'm.johnson@email.com', 'emily.w@email.com', 'david.b@email.com',
                  'sarah.d@email.com', 'r.miller@email.com', 'lisa.w@email.com', 'james.m@email.com', 'patricia.t@email.com',
                  'c.anderson@email.com', 'j.thomas@email.com', 'd.jackson@email.com', 'nancy.w@email.com', 'm.harris@email.com',
                  'b.martin@email.com', 'j.thompson@email.com', 'susan.g@email.com', 'c.martinez@email.com', 'j.robinson@email.com'],
        'phone': [f'555-{str(i).zfill(4)}' for i in range(101, 121)],
        'address': ['123 Main St', '456 Oak Ave', '789 Pine Rd', '321 Elm St', '654 Maple Dr', '987 Cedar Ln',
                    '147 Birch Ct', '258 Spruce St', '369 Ash Ave', '741 Walnut Rd', '852 Cherry Ln', '963 Poplar Dr',
                    '159 Hickory St', '357 Redwood Ave', '486 Sycamore Rd', '753 Magnolia Ct', '951 Willow Ln',
                    '246 Beech St', '135 Fir Ave', '789 Oak St'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
                 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco',
                 'Indianapolis', 'Seattle', 'Denver', 'Boston'],
        'state': ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA', 'TX', 'FL', 'TX', 'OH', 'NC', 'CA', 'IN', 'WA', 'CO', 'MA'],
        'zip_code': ['10001', '90001', '60601', '77001', '85001', '19019', '78201', '92101', '75201', '95101',
                     '78701', '32099', '76101', '43004', '28201', '94101', '46201', '98101', '80201', '02101'],
        'country': ['USA'] * 20,
        'registration_date': pd.date_range(start='2023-01-01', periods=20, freq='5D')
    }
    df = pd.DataFrame(customers_data)
    df.to_parquet('customers.parquet', index=False, compression='snappy')
    print(f"✓ Created customers.parquet ({len(df)} records)")

def create_products_parquet():
    """Generate products dataset"""
    products_data = {
        'product_id': list(range(1, 21)),
        'product_name': ['Wireless Mouse', 'USB Keyboard', '27-inch Monitor', 'Laptop Bag', 'Office Chair',
                         'Desk Lamp', 'Notebook Pack', 'Ballpoint Pens', 'Coffee Mug', 'Water Bottle',
                         'Headphones', 'Smartphone Case', 'Backpack', 'Running Shoes', 'T-Shirt',
                         'Yoga Mat', 'Protein Powder', 'Multivitamin', 'Desk Organizer', 'Plant Pot'],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture',
                     'Furniture', 'Stationery', 'Stationery', 'Kitchen', 'Kitchen',
                     'Electronics', 'Electronics', 'Bags', 'Apparel', 'Apparel',
                     'Sports', 'Health', 'Health', 'Office', 'Home'],
        'subcategory': ['Computer Accessories', 'Computer Accessories', 'Displays', 'Accessories', 'Office',
                        'Lighting', 'Paper Products', 'Writing Tools', 'Drinkware', 'Drinkware',
                        'Audio', 'Mobile Accessories', 'Travel', 'Footwear', 'Clothing',
                        'Fitness', 'Supplements', 'Supplements', 'Storage', 'Decor'],
        'price': [29.99, 49.99, 299.99, 39.99, 199.99, 34.99, 12.99, 8.99, 14.99, 19.99,
                  79.99, 24.99, 59.99, 89.99, 19.99, 34.99, 49.99, 29.99, 24.99, 16.99],
        'cost': [15.00, 25.00, 180.00, 20.00, 100.00, 18.00, 6.00, 4.00, 7.00, 10.00,
                 40.00, 12.00, 30.00, 45.00, 8.00, 18.00, 25.00, 15.00, 12.00, 8.00],
        'brand': ['TechPro', 'KeyMaster', 'ViewTech', 'CarryAll', 'ComfortSeat',
                  'BrightLight', 'WritePro', 'InkFlow', 'MugLife', 'HydroPlus',
                  'SoundWave', 'PhoneGuard', 'TravelPro', 'RunFast', 'BasicWear',
                  'FlexMat', 'NutriFit', 'VitaBoost', 'TidyDesk', 'GreenThumb'],
        'description': ['Ergonomic wireless mouse with 3 buttons', 'Mechanical keyboard with RGB lighting', '4K UHD monitor with HDR support',
                        'Padded laptop bag fits up to 15 inch', 'Ergonomic office chair with lumbar support', 'LED desk lamp with adjustable brightness',
                        'Pack of 3 college-ruled notebooks', 'Pack of 12 blue ballpoint pens', 'Ceramic coffee mug 12 oz', 'Stainless steel insulated bottle 24 oz',
                        'Wireless over-ear headphones with ANC', 'Protective case with shock absorption', '30L backpack with multiple compartments',
                        'Lightweight running shoes with cushioning', '100% cotton crew neck t-shirt', 'Non-slip yoga mat 6mm thickness',
                        'Whey protein isolate 2 lbs', 'Daily multivitamin 90 tablets', 'Wooden desk organizer with compartments', 'Ceramic plant pot with drainage hole']
    }
    df = pd.DataFrame(products_data)
    df.to_parquet('products.parquet', index=False, compression='snappy')
    print(f"✓ Created products.parquet ({len(df)} records)")

def create_orders_parquet():
    """Generate orders dataset"""
    orders_data = {
        'order_id': list(range(1, 31)),
        'customer_id': [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        'product_id': [3,11,5,14,1,7,10,16,2,13,6,8,9,12,15,17,18,19,20,4,3,11,5,14,1,7,10,16,2,13],
        'order_date': pd.date_range(start='2023-06-01', periods=30, freq='D'),
        'quantity': [1,1,1,2,3,5,2,1,1,1,2,10,4,1,3,2,1,1,3,1,1,1,2,1,1,2,1,1,2,1],
        'amount': [299.99,79.99,199.99,179.98,89.97,64.95,39.98,34.99,49.99,59.99,
                   69.98,89.90,59.96,24.99,59.97,99.98,29.99,24.99,50.97,39.99,
                   299.99,79.99,399.98,89.99,29.99,25.98,19.99,34.99,99.98,59.99],
        'status': ['completed','completed','completed','completed','completed','completed','completed','pending','completed','completed',
                   'completed','completed','completed','completed','cancelled','completed','completed','completed','completed','pending',
                   'completed','completed','completed','completed','completed','completed','completed','completed','pending','completed'],
        'shipping_address': [
            '123 Main St New York NY 10001', '456 Oak Ave Los Angeles CA 90001', '789 Pine Rd Chicago IL 60601',
            '321 Elm St Houston TX 77001', '654 Maple Dr Phoenix AZ 85001', '987 Cedar Ln Philadelphia PA 19019',
            '147 Birch Ct San Antonio TX 78201', '258 Spruce St San Diego CA 92101', '369 Ash Ave Dallas TX 75201',
            '741 Walnut Rd San Jose CA 95101', '123 Main St New York NY 10001', '456 Oak Ave Los Angeles CA 90001',
            '789 Pine Rd Chicago IL 60601', '321 Elm St Houston TX 77001', '654 Maple Dr Phoenix AZ 85001',
            '987 Cedar Ln Philadelphia PA 19019', '147 Birch Ct San Antonio TX 78201', '258 Spruce St San Diego CA 92101',
            '369 Ash Ave Dallas TX 75201', '741 Walnut Rd San Jose CA 95101', '852 Cherry Ln Austin TX 78701',
            '963 Poplar Dr Jacksonville FL 32099', '159 Hickory St Fort Worth TX 76101', '357 Redwood Ave Columbus OH 43004',
            '486 Sycamore Rd Charlotte NC 28201', '753 Magnolia Ct San Francisco CA 94101', '951 Willow Ln Indianapolis IN 46201',
            '246 Beech St Seattle WA 98101', '135 Fir Ave Denver CO 80201', '789 Oak St Boston MA 02101'
        ],
        'payment_method': ['credit_card','paypal','credit_card','debit_card','credit_card','paypal','credit_card','credit_card','debit_card','paypal',
                           'credit_card','credit_card','paypal','credit_card','credit_card','debit_card','paypal','credit_card','credit_card','paypal',
                           'credit_card','debit_card','credit_card','paypal','credit_card','credit_card','paypal','debit_card','credit_card','paypal']
    }
    df = pd.DataFrame(orders_data)
    df.to_parquet('orders.parquet', index=False, compression='snappy')
    print(f"✓ Created orders.parquet ({len(df)} records)")

def create_sales_parquet():
    """Generate sales dataset"""
    sales_data = {
        'sale_id': list(range(1, 31)),
        'order_id': list(range(1, 31)),
        'product_id': [3,11,5,14,1,7,10,16,2,13,6,8,9,12,15,17,18,19,20,4,3,11,5,14,1,7,10,16,2,13],
        'customer_id': [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        'sale_date': pd.date_range(start='2023-06-01 10:00:00', periods=30, freq='6H'),
        'quantity': [1,1,1,2,3,5,2,1,1,1,2,10,4,1,3,2,1,1,3,1,1,1,2,1,1,2,1,1,2,1],
        'unit_price': [299.99,79.99,199.99,89.99,29.99,12.99,19.99,34.99,49.99,59.99,
                       34.99,8.99,14.99,24.99,19.99,49.99,29.99,24.99,16.99,39.99,
                       299.99,79.99,199.99,89.99,29.99,12.99,19.99,34.99,49.99,59.99],
        'total_amount': [299.99,79.99,199.99,179.98,89.97,64.95,39.98,34.99,49.99,59.99,
                         69.98,89.90,59.96,24.99,59.97,99.98,29.99,24.99,50.97,39.99,
                         299.99,79.99,399.98,89.99,29.99,25.98,19.99,34.99,99.98,59.99],
        'discount': [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,
                     0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,
                     10.00,0.00,20.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
        'region': ['Northeast','West','Midwest','South','West','Northeast','South','West','South','West',
                   'Northeast','West','Midwest','South','West','Northeast','South','West','South','West',
                   'South','South','South','Midwest','South','West','Midwest','West','West','Northeast']
    }
    df = pd.DataFrame(sales_data)
    df.to_parquet('sales.parquet', index=False, compression='snappy')
    print(f"✓ Created sales.parquet ({len(df)} records)")

def create_employees_parquet():
    """Generate employees dataset"""
    employees_data = {
        'employee_id': list(range(1, 21)),
        'first_name': ['Alice','Bob','Carol','David','Emma','Frank','Grace','Henry','Ivy','Jack',
                       'Karen','Leo','Mary','Nathan','Olivia','Paul','Quinn','Rachel','Sam','Tina'],
        'last_name': ['Johnson','Smith','Williams','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson',
                      'Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson','Clark'],
        'email': ['alice.j@company.com','bob.s@company.com','carol.w@company.com','david.b@company.com','emma.d@company.com',
                  'frank.m@company.com','grace.w@company.com','henry.m@company.com','ivy.t@company.com','jack.a@company.com',
                  'karen.t@company.com','leo.j@company.com','mary.w@company.com','nathan.h@company.com','olivia.m@company.com',
                  'paul.t@company.com','quinn.g@company.com','rachel.m@company.com','sam.r@company.com','tina.c@company.com'],
        'department': ['Engineering','Engineering','Engineering','Sales','Sales','Sales','Marketing','Marketing','Marketing','Engineering',
                       'Sales','Marketing','HR','HR','Finance','Finance','Operations','Operations','IT','IT'],
        'position': ['Senior Engineer','Software Engineer','Junior Engineer','Sales Manager','Account Executive','Sales Representative',
                     'Marketing Manager','Content Specialist','Social Media Manager','VP of Engineering',
                     'VP of Sales','VP of Marketing','HR Manager','VP of HR','Accountant','CFO',
                     'Operations Manager','VP of Operations','IT Manager','CTO'],
        'hire_date': pd.to_datetime(['2020-01-15','2021-03-20','2022-06-01','2019-05-10','2021-08-15',
                                     '2022-02-20','2020-04-05','2021-11-10','2022-01-25','2018-03-01',
                                     '2019-07-15','2019-09-20','2020-02-10','2018-11-05','2021-05-15',
                                     '2018-06-20','2020-08-01','2019-10-15','2020-06-25','2018-04-10']),
        'salary': [95000,75000,60000,85000,65000,55000,80000,60000,58000,130000,
                   125000,120000,75000,115000,65000,140000,82000,118000,80000,145000],
        'manager_id': [10,10,10,11,4,4,12,7,7,None,None,None,14,None,16,None,18,None,20,None]
    }
    df = pd.DataFrame(employees_data)
    df.to_parquet('employees.parquet', index=False, compression='snappy')
    print(f"✓ Created employees.parquet ({len(df)} records)")

if __name__ == "__main__":
    print("Generating Parquet datasets for Databricks course...\n")
    
    create_customers_parquet()
    create_products_parquet()
    create_orders_parquet()
    create_sales_parquet()
    create_employees_parquet()
    
    print("\n✅ All Parquet datasets created successfully!")
    print("\nDatasets created:")
    print("  • customers.parquet (20 records)")
    print("  • products.parquet (20 records)")
    print("  • orders.parquet (30 records)")
    print("  • sales.parquet (30 records)")
    print("  • employees.parquet (20 records)")
    print("\nThese datasets use Snappy compression for optimal performance in Databricks.")
