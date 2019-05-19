# CookWarehouse
Serverless Cooking Web-Application that reverses the process of looking up recipes, it provides users recipes that only include the ingredients they select rather than finding a recipe and afterwards determine if the ingredients are available. Other ways of obtaining recipes have also been implemented. 

![HomePage3](https://user-images.githubusercontent.com/42480955/57983179-c62f7400-7a03-11e9-9465-b985879b3ada.PNG)

![ingredients page](https://user-images.githubusercontent.com/42480955/57983180-c62f7400-7a03-11e9-98d4-ddae462fcdaa.PNG)

![search ingredients](https://user-images.githubusercontent.com/42480955/57983183-c6c80a80-7a03-11e9-9124-819e6f3d89f4.PNG)

![recipe displayed](https://user-images.githubusercontent.com/42480955/57983181-c6c80a80-7a03-11e9-94d9-7645a1aea88a.PNG)

![recipe search](https://user-images.githubusercontent.com/42480955/57983182-c6c80a80-7a03-11e9-9e95-0e194d99f821.PNG)

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
  
  4. Run the command 'Chalice deploy'
  
# Note
  - The whole provided file is the Lambda function
  - Within the file there are multiple API routes that are the children of the parent API that is created for you once you create a chalice project. The parent API will have the same name as your chalice project name.
  - This is not a tutorial on how use chalice but rather showing how chalice was used to simplify the process of creating a lambda function and an API 
  - Make sure your crednetials are configured prior to deploying, otherwise it will not work.

