AddIngr = "INSERT INTO ingredients ( ingr_group_id, calories, provider_id, ingredient_name ) " \
          "VALUES ( %s, %s, %s, %s )"
EditIngr = "UPDATE ingredients " \
           "SET ingr_group_id = %s, calories = %s, provider_id = %s, ingredient_name = %s WHERE ingredient_name = %s"
DeleteIngr = "DELETE FROM ingredients " \
           "WHERE ingredient_name = '%s'"

AddRecipt = "INSERT INTO recipt ( recipt_id, recipt_name, description, author_id ) " \
            "VALUES ( %s, %s, %s, %s )"
EditRecipt = "UPDATE recipt " \
             "SET recipt_id = %s, recipt_name = %s, description = %s, author_id = %s WHERE recipt_name = %s"
DeleteRecipt = "DELETE FROM recipt " \
               "WHERE recipt_name = '%s'"

AddSupplier = "INSERT INTO providers ( provider_id, provider_name, address, phone ) " \
               "VALUES ( %s, %s, %s, %s )"
EditSupplier = "UPDATE providers " \
               "SET provider_id = %s, provider_name = %s, address = %s, phone = %s WHERE provider_name = %s"
DeleteSupplier = "DELETE FROM providers " \
                 "WHERE provider_name = '%s'"