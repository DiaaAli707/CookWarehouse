from chalice import Chalice
import pymysql
import logging
import traceback
from os import environ

app = Chalice(app_name='')
# Enable DEBUG logs.
app.log.setLevel(logging.DEBUG)


endpoint=""
port=""
dbuser=""
password=""
database=""


get_ingredients_query="SELECT Ingredient_Name, Ingredient_Image FROM ingredients"
get_recipes_query="""
SELECT Recipe, Image from recipes r
INNER JOIN recipe_ingredients ri on r.ID=ri.Recipe_ID
INNER JOIN ingredients i on i.ID=ri.ingredients_ID
GROUP BY r.ID
"""

logger=logging.getLogger()
logger.setLevel(logging.INFO)


def make_connection():
    return pymysql.connect(host=endpoint, user=dbuser, passwd=password,
        port=int(port), db=database, autocommit=True)

def log_err(errmsg):
    logger.error(errmsg)
    return {"body": errmsg , "headers": {}, "statusCode": 400,
        "isBase64Encoded":"false"}

app.log.debug("Cold start complete.")


def build_recipe_query(ingredient_list):
    number_of_ingredients = len(ingredient_list)
    ingredient_list_tuple = str(ingredient_list).replace("[", "(").replace("]",")")

    intermediate_query = f"""
    HAVING COUNT(DISTINCT i.Ingredient_Name)={number_of_ingredients} AND
       COUNT(DISTINCT case when i.Ingredient_Name IN {ingredient_list_tuple} then i.ID end)={number_of_ingredients}
    """
    app.log.debug(number_of_ingredients)
    final_query = get_recipes_query + intermediate_query
    app.log.debug(final_query)
    return final_query
    

def execute_query_and_return_results(query):
    app.log.debug("execute query function")
    app.log.debug(query)
    try:
        cnx = make_connection()
        cursor=cnx.cursor()
        try:
            cursor.execute(query)
        except:
            return log_err ("ERROR: Cannot execute cursor.\n{}".format(
                traceback.format_exc()) )

        try:
            results_list=[]
            for result in cursor: 
                results_list.append(result)
            cursor.close()
            app.log.debug(results_list)

        except:
            return log_err ("ERROR: Cannot retrieve query data.\n{}".format(
                traceback.format_exc()))

        return {"body": results_list, "headers": {}, "statusCode": 200,
        "isBase64Encoded":"false"}

    except:
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(
            traceback.format_exc()))

    finally:
        try:
            cnx.close()
        except:
            pass


@app.route('/ingredients')
def get_ingredients():
        return execute_query_and_return_results(get_ingredients_query)


@app.route('/recipes', methods=['POST'])
def get_recipes():
        request_body = app.current_request
        app.log.debug(request_body)
        if request_body:
            request_body_json = request_body.json_body
            app.log.debug(request_body_json)
            ingredients = request_body_json["ingredients"]
            app.log.debug(ingredients)
            query = build_recipe_query(ingredients)
            return execute_query_and_return_results(query)


@app.route('/recipes/{recipe}')
def get_recipe(recipe):
    str_recipe = str(recipe).replace("_", " ")
    query = f"""
                SELECT * from recipes
                WHERE Recipe=\"{str_recipe}\""""
    return execute_query_and_return_results(query)

@app.route('/recipes/search/{recipe}')
def search_for_recipe(recipe):
    str_recipe = str(recipe).replace("_", " ")
    query = f"SELECT * FROM recipes WHERE Recipe like '%{str_recipe}%'"
    return execute_query_and_return_results(query)