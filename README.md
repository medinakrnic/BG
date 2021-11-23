# BG

1. Navigate to web directory 
2. Build the images and run the containers: ```docker-compose up -d --build```
3. Create database tables: ```docker-compose exec web python manage.py create_db```
4. Populate tables with data: ```docker-compose exec web python manage.py seed_db```


# Users
Returns json data listing all users in database.

URL

/users

Method:

GET

# Discount Codes
Returns json data listing all discount codes in database.

URL

/discount-codes

Method:

GET

# Generate Discount Codes
Returns json data listing all discount codes generated and then stored in database.

URL

/generate-discount-codes

Method:

POST

Data Params:

discount-codes

discount-value

# Redeem Discount code
Returns json data listing an available and unredeemed discount code from the database.

URL

/user/discount-code

Method:

GET

URL Params:

user-id

# Check Claimed Discount codes
Returns json data listing users that have redeemed discount codes (mailing list).

URL

/check-claimed-discount-codes

Method:

GET
