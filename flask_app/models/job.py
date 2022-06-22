from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Job:
    db_name ="chores"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO job (title,description,location,created_at,user_id) VALUES (%(title)s,%(description)s,%(location)s,%(created_at)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM job LEFT JOIN user on user.id = job.user_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_jobs = []
        for job in results:
            print(job['created_at'])
            all_jobs.append( cls(job) )
        return all_jobs


    @classmethod
    def get_job_user(cls,data):
        query = "SELECT * FROM job LEFT JOIN user on user.id = job.user_id where user.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        all_jobs = []
        for job in results:
            all_jobs.append( cls(job) )
        return all_jobs


    @classmethod
    def update(cls,data):
        query = "UPDATE job SET title=%(title)s, description=%(description)s, location=%(location)s, created_at=%(created_at)s, updated_at=%(updated_at)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM job where id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)




    @staticmethod
    def validate_job(job):
        is_valid = True
        if len(job['title']) < 1:
            is_valid = False
            flash("Name must be at least 5 characters")
        if len(job['description']) <1:
            is_valid = False
            flash("Name must be at least 5 characters")
        if len(job['location']) < 1:
            flash("Reason must be less than 50 characters")
            is_valid = False
        return is_valid

"""
    @staticmethod
    def validate_product(product):
        is_valid = True
        if len(product['product']) < 1:
            is_valid = False
            flash("Please enter a product")
        if len(product['sku']) < 1:
            is_valid = False
            flash("Please enter sku")
        if len(product['product_cost']) < 1:
            flash("Please enter cost")
            is_valid = False
        if len(product['quantity']) < 1:
            is_valid = False
            flash("Please enter quantity of product")
        if len(product['reason']) < 1:
            is_valid = False
            flash("Please enter a reason for purchase")
        return is_valid
"""