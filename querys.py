AddIngr = "INSERT INTO ingredients ( ingr_group_id, calories, supplier_id, ingredient_name ) " \
          "VALUES ( %s, %s, %s, %s )"
EditIngr = "UPDATE ingredients " \
           "SET ingr_group_id = %s, calories = %s, supplier_id = %s, ingredient_name = %s WHERE ingredient_name = %s"
DeleteIngr = "DELETE FROM ingredients " \
             "WHERE ingredient_name = %s"

AddRecipe = "INSERT INTO recipe ( recipe_id, recipe_name, description, author_id ) " \
            "VALUES ( %s, %s, %s, %s )"
EditRecipe = "UPDATE recipe " \
             "SET recipe_id = %s, recipe_name = %s, description = %s, author_id = %s WHERE recipe_name = %s"
DeleteRecipe = "DELETE FROM recipe " \
               "WHERE recipe_name = %s"

AddSupplier = "INSERT INTO suppliers ( supplier_id, supplier_name, address, phone ) " \
              "VALUES ( %s, %s, %s, %s )"
EditSupplier = "UPDATE suppliers " \
               "SET supplier_id = %s, supplier_name = %s, address = %s, phone = %s WHERE supplier_name = %s"
DeleteSupplier = "DELETE FROM suppliers " \
                 "WHERE supplier_name = %s"

PriceList = "SELECT date, i.supplier_id, supplier_name, address, phone, waybill.ingredient_name, ingr_price " \
            "FROM waybill " \
            "INNER JOIN ingredients i on waybill.ingredient_name = i.ingredient_name " \
            "INNER JOIN suppliers s on i.supplier_id = s.supplier_id " \
            "WHERE  i.supplier_id= %s AND date = %s"

Food_RecipeList = "SELECT food_name, recipe_name " \
           "FROM food " \
           "INNER JOIN recipe r on food.recipe_id = r.recipe_id"

Low_calorie_dish = "SELECT food_name "\
                   "FROM food "\
                   "WHERE recipe_id = (SELECT recipe_id "\
                   "FROM(SELECT recipe_id, SUM(calories * gramme) as sum "\
                   "FROM ingredients "\
                   "INNER JOIN layout_of_ingredients loi on ingredients.ingredient_name = loi.ingredient_name "\
                   "GROUP BY recipe_id) as ris "\
                   "ORDER BY sum LIMIT 1)"

