AddIngr = "INSERT INTO ingredients ( ingr_group_id, calories, provider_id, ingredient_name ) " \
          "VALUES ( %s, %s, %s, %s )"
EditIngr = "UPDATE ingredients " \
           "SET ingr_group_id = %s, calories = %s, provider_id = %s, ingredient_name = %s WHERE ingredient_name = %s"
DeleteIngr = "DELETE FROM ingredients " \
           "WHERE ingredient_name = %s"

AddRecipe = "INSERT INTO recipe ( recipe_id, recipe_name, description, author_id ) " \
            "VALUES ( %s, %s, %s, %s )"
EditRecipe = "UPDATE recipe " \
             "SET recipe_id = %s, recipe_name = %s, description = %s, author_id = %s WHERE recipe_name = %s"
DeleteRecipe = "DELETE FROM recipe " \
               "WHERE recipe_name = %s"

AddSupplier = "INSERT INTO suppliers ( supplier_id, supplier_name, address, phone ) " \
               "VALUES ( %s, %s, %s, %d )"
EditSupplier = "UPDATE suppliers " \
               "SET supplier_id = %s, supplier_name = %s, address = %s, phone = %s WHERE supplier_name = %s"
DeleteSupplier = "DELETE FROM suppliers " \
                 "WHERE supplier_name = %s"
