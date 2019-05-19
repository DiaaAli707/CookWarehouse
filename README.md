# CookWarehouse
Serverless Cooking Web-Application that reverses the process of looking up recipes, it provides users recipes that only include the ingredients they select rather than finding a recipe and afterwards determine if the ingredients are available. Other ways of obtaining recipes have also been implemented. 

# Developed Using:
  - AWS (S3, Lambda, API Gateway, RDS, Elastic BeanStalk)
  - Chalice
  - PHP
  - HTML5
  - JAVASCRIPT
  
# Using chalice to create a Lambda Function and an API: 
  1. Create MySQL DB instance on Amazon RDS with the following schema with 3 main tables: Ingredients, Recipe_ingredients, and Recipes
  
  ![db-ingredients table](https://user-images.githubusercontent.com/42480955/57982799-cbd68b00-79fe-11e9-9102-6f3d1576d104.PNG)
  ![db-Recipe_ingredients table](https://user-images.githubusercontent.com/42480955/57982800-cc6f2180-79fe-11e9-87b1-be8ee1132b44.PNG)
  ![db-Recipes_table](https://user-images.githubusercontent.com/42480955/57982801-cc6f2180-79fe-11e9-9ee6-d4f429dfae0b.PNG)

  2. Install Chalice by following this link (https://chalice.readthedocs.io/en/latest/) and create a new project
  
  3. Copy the code provided into your chalice file while making sure to add your DB instance information 

