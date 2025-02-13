few_shot_examples = [
  {"input": "List all products", "query": "SELECT * FROM ecommerce_product_data"},
  {"input": "Find all products in the Clothing category", "query": "SELECT * FROM ecommerce_product_data WHERE Category = 'Clothing'"},
  {"input": "Show all products with a review rating of 5", "query": "SELECT * FROM ecommerce_product_data WHERE Review_Rating = 5"},
  {"input": "Get all products purchased by male customers aged above 50", "query": "SELECT * FROM ecommerce_product_data WHERE Customer_Gender = 'Male' AND Customer_Age > 50"},

  {"input": "List all movies", "query": "SELECT * FROM netflix_movies_dataset"},
  {"input": "Find all English movies", "query": "SELECT * FROM netflix_movies_dataset WHERE Language = 'English'"},
  {"input": "Get movies released after 2020", "query": "SELECT * FROM netflix_movies_dataset WHERE Released > '2020'"},
  {"input": "Show all movies with IMDb rating above 7", "query": "SELECT * FROM netflix_movies_dataset WHERE IMDb > '7.0/10'"}
]
